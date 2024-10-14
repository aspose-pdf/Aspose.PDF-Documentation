---
title: 如何在 Docker 中运行 Aspose.PDF
linktitle: 使用 Docker
type: docs
weight: 20
url: /net/docker/dotnet8/
description: 将 Aspose.PDF 功能集成到使用 Docker Linux 容器的应用程序中
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 先决条件

以下示例已测试：

* Docker v.25.0.2 和 Docker Desktop 4.27.1
* Visual Studio 2022 社区版 v.17.0.5
* 下面提供的示例中使用了 .NET 8 SDK。
* Aspose.PDF.Drawing v.24.01

## 为 Docker Linux 容器创建示例应用程序

1. 启动 Visual Studio 2022 并选择 **ASP.NET Core Web App (Model-View-Controller)** 模板，然后按 **下一步**
1. 在 **配置新项目** 窗口中设置所需的项目名称和位置，然后按 **下一步**
1. 在 **附加信息** 窗口选择 **.NET 6.0 (长期支持)** 并启用 Docker 支持。如果需要，还可以设置 **Docker OS** 为 Linux。
1. 按 **创建**
### 在 Linux 容器中使用 ASP.NET Core Web 应用生成 PDF 文档

我们将在此应用中使用**复杂示例**中的代码。请跟随[此链接](/pdf/net/complex-pdf-example/)了解更多详细说明。

1. 在 `wwwroot` 文件夹中创建 `images` 文件夹并放入图片 `logo.png`。您可以从[这里](/pdf/net/docker/logo.png)下载此图片
1. 在 `wwwroot` 文件夹中创建 `fonts` 文件夹并放入 [Roboto](https://fonts.google.com/specimen/Roboto) 字体。
1. 在 `wwwroot` 文件夹中创建 `samples` 文件夹并放入示例数据。
1. 用以下代码片段替换 `HomeController.cs` 中的代码（请注意，您可能有另一个命名空间）：

```cs
using Aspose.Pdf;
using Aspose.Pdf.Devices;
using Aspose.Pdf.Text;
using Docker.LinuxDemo.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Docker.LinuxDemo.Controllers
{
    // <summary>
    // 代表 Linux 演示应用中首页和 PDF 生成的控制器。
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // 显示索引视图。
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // 生成 PDF 文档并以文件形式返回。
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("PDF Generation: Start ");
            // 初始化文档对象
            var document = new Document();
            // 添加页面
            var page = document.Pages.Add();

            // 添加图片
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // 添加标题
            var header = new TextFragment("2020年秋季新的渡轮路线");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 添加描述
            var descriptionText = "游客必须在线购买票，每天的票数限制为5000张。渡轮服务以半载量和缩减的时间表运营。预计会有排队现象。";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
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
            _logger.LogInformation("PDF Generation: Finish");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // 根据提供的 id 将文件转换为不同格式。
        // </summary>
        public FileStreamResult Convert(string id)
        {
            return id switch
            {
                "xps-to-pdf" => ConvertXpsToPdf(),
                "pdf-to-jpeg" => ConvertPdfToJpeg(),
                _ => throw new NotImplementedException(),
            };
        }

        // <summary>
        // 将 PDF 文件转换为 JPEG 格式并以文件形式返回。
        // </summary>
        private FileStreamResult ConvertPdfToJpeg()
        {
            const string fileType = "image/jpeg";
            const string fileName = "sample.jpeg";

            var memoryStream = new MemoryStream();
            var pdfFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.pdf");

            var document = new Document(pdfFileName);
            var resolution = new Resolution(300);
            var renderer = new JpegDevice(resolution, 90);
            renderer.Process(document.Pages[1], memoryStream);
            memoryStream.Seek(0, SeekOrigin.Begin);
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // 将 XPS 文件转换为 PDF 格式并以文件形式返回。
        // </summary>
        private FileStreamResult ConvertXpsToPdf()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";

            var memoryStream = new MemoryStream();
            var xpsFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.oxps");

            var document = new Document(xpsFileName, new XpsLoadOptions());
            document.Save(memoryStream);

            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // 显示隐私视图。
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // 显示错误视图。
        // </summary>
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
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base

RUN apt-get update && apt-get install -y libgdiplus
RUN apt install software-properties-common -y
RUN echo "deb http://deb.debian.org/debian bookworm contrib non-free" > /etc/apt/sources.list.d/contrib.list
RUN apt update && apt upgrade
RUN apt install ttf-mscorefonts-installer -y


USER app
WORKDIR /app
EXPOSE 8080
EXPOSE 8081

FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG BUILD_CONFIGURATION=Release
WORKDIR /src
COPY ["Docker.Demo/Docker.LinuxDemo.csproj", "Docker.Demo/"]
RUN dotnet restore "./Docker.Demo/./Docker.LinuxDemo.csproj"
COPY . .
WORKDIR "/src/Docker.Demo"
RUN dotnet build "./Docker.LinuxDemo.csproj" -c $BUILD_CONFIGURATION -o /app/build

FROM build AS publish
ARG BUILD_CONFIGURATION=Release
RUN dotnet publish "./Docker.LinuxDemo.csproj" -c $BUILD_CONFIGURATION -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.LinuxDemo.dll"]
```

