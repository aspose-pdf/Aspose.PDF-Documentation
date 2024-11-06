---
title: 如何在 Docker 中运行 Aspose.PDF for .NET 6
linktitle: 在 Docker 中使用 Aspose.PDF for .NET 6
type: docs
weight: 10
url: zh/net/docker/dotnet6/
description: 使用 Docker Linux 或 Windows 容器将 Aspose.PDF 功能集成到您的应用程序中
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 先决条件

以下示例已测试：

* Docker v.20.10.11 和 Docker Desktop 4.3.2
* Visual Studio 2022 社区版 v.17.0.5
* 下面提供的示例中使用了 .NET 6 SDK。
* Aspose.PDF for .NET v.22.01

## 为 Docker Linux 容器创建示例应用程序

1. 启动 Visual Studio 2022 并选择 **ASP.NET Core Web 应用程序（模型-视图-控制器）** 模板，然后按 **下一步**
1. 在 **配置新项目** 窗口中设置所需的项目名称和位置，然后按 **下一步**
1. 在 **附加信息** 窗口中选择 **.NET 6.0（长期支持）** 并启用 Docker 支持。如果需要，您还可以设置 **Docker OS** 为 Linux。
1. 选择 **工具->Nuget 包管理器->包管理器控制台** 并安装 **Aspose.PDF for .NET**（使用命令 `Install-Package Aspose.PDF`）

### 使用 ASP.NET Core Web 应用在 Linux 容器中生成 PDF 文档

我们将在此应用中使用**复杂示例**的代码。请访问[此链接](/pdf/net/complex-pdf-example/)获取更详细的说明。

1. 在 `wwwroot` 文件夹中创建一个 `images` 文件夹，并放入图片 `logo.png`。您可以从[这里](/pdf/net/docker/logo.png)下载这张图片
1. 用以下代码片段替换 `HomeController.cs` 中的代码（请注意，您可能有另一个命名空间）：

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```cs
using Aspose.Pdf;
using Aspose.Pdf.Text;
using Docker.Linux.Demo01.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Docker.Linux.Demo01.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IWebHostEnvironment _appEnvironment;

        public HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment)
        {
            _logger = logger;
            _appEnvironment = appEnvironment;
        }

        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Generate()
        {
            const string file_type = "application/pdf";
            const string file_name = "sample.pdf";
            var memoryStream = new System.IO.MemoryStream();

            _logger.LogInformation("开始");
            // 初始化文档对象
            var document = new Document();
            // 添加页面
            var page = document.Pages.Add();

            // 添加图片
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // 添加标题
            var header = new TextFragment("2020年秋季新渡轮路线");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 添加描述
            var descriptionText = "游客必须在线购票，每天的票务限量为5000张。渡轮服务以半容量运作，并采取减少班次的时间表。请预计排队。";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);

            // 添加表格
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.Black),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Gray),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Top = 10,
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("出发城市");
            headerRow.Cells.Add("出发岛屿");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.LightGray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.FromRgb(0.1, 0.1, 0.1);
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time = time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(memoryStream);
            _logger.LogInformation("完成");
            return File(memoryStream, file_type, file_name);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```
1. 将 `Dockerfile` 中的内容替换为以下内容：

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
RUN apt-get update && apt-get install -y libgdiplus
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
RUN apt-get update; apt-get install -y ttf-mscorefonts-installer fontconfig

WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Docker.Linux.Demo01/Docker.Linux.Demo01.csproj", "Docker.Linux.Demo01/"]
RUN dotnet restore "Docker.Linux.Demo01/Docker.Linux.Demo01.csproj"
COPY . .
WORKDIR "/src/Docker.Linux.Demo01"
RUN dotnet build "Docker.Linux.Demo01.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Docker.Linux.Demo01.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.Linux.Demo01.dll"]
```

## 为 Docker Windows 容器创建示例应用

1.
1. 在**配置新项目**窗口中设置所需的项目名称和位置，然后按**下一步**
1. 在**附加信息**窗口中选择 **.NET 6.0 (长期支持)** 并启用 Docker 支持。如果需要，您还可以将 **Docker OS** 设置为 `Windows`。
1. 按**创建**
1. 选择 **工具->Nuget 包管理器->包管理器控制台** 并安装 **Aspose.PDF for .NET**（使用命令 `Install-Package Aspose.PDF`）

### 使用 ASP.NET Core Web 应用在 Windows 容器中生成 PDF 文档

我们将使用与上一个示例相同的代码。

1. 在 `wwwroot` 文件夹中创建一个 `images` 文件夹并放入图片 `logo.png`。您可以从[这里](/pdf/net/docker/logo.png)下载此图片
1. 用上面的代码片段替换 `HomeController.cs` 中的代码。

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0.101-nanoserver-ltsc2022 AS build
WORKDIR /src
COPY ["Docker.Windows.Demo01/Docker.Windows.Demo01.csproj", "Docker.Windows.Demo01/"]
RUN dotnet restore "Docker.Windows.Demo01/Docker.Windows.Demo01.csproj"
COPY . .
WORKDIR "/src/Docker.Windows.Demo01"
RUN dotnet build "Docker.Windows.Demo01.csproj" -c Release -o /app/build -r win-x64 --self-contained true

FROM build AS publish
RUN dotnet publish "Docker.Windows.Demo01.csproj" -c Release -o /app/publish -r win-x64 --self-contained true

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.Windows.Demo01.dll"]
```

