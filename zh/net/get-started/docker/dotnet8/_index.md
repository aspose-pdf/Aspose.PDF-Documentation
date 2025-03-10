---
title: 如何在 Docker 中运行 Aspose.PDF for .NET 8
linktitle: 在 Docker 中使用 Aspose.PDF for .NET 8
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/docker/dotnet8/
description: 使用 Docker Linux 或 Windows 容器将 Aspose.PDF 功能集成到 .NET 8 应用程序中
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to run Aspose.PDF for .NET 8 in Docker",
    "alternativeHeadline": "Integrate Aspose.PDF with .NET 8 in Docker",
    "abstract": "了解如何在 Linux 或 Windows 容器中使用 Docker 无缝集成 Aspose.PDF for .NET 8 到您的应用程序中。此功能使得在 ASP.NET Core 应用程序中高效生成和处理 PDF 文档成为可能，允许开发人员在容器化环境中利用强大的 PDF 功能。通过利用此简单的设置指南优化您的 .NET 项目，并通过 Aspose.PDF for .NET 强大的功能增强您的开发工作流程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/docker/dotnet8/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/docker/dotnet8/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 先决条件

以下示例经过测试：

* Docker v.25.0.2 和 Docker Desktop 4.27.1。
* Visual Studio 2022 Community Edition v.17.0.5。
* 示例中使用 .NET 8 SDK。
* Aspose.PDF.Drawing v.24.01。

## 为 Docker Linux 容器创建示例应用程序

1. 启动 Visual Studio 2022，选择 **ASP.NET Core Web App (Model-View-Controller)** 模板，然后按 **Next**。
1. 在 **配置您的新项目** 窗口中设置所需的项目名称和位置，然后按 **Next**。
1. 在 **附加信息** 窗口中选择 **.NET 6.0 (长期支持)** 并启用 Docker 支持。如果需要，您还可以将 **Docker OS** 设置为 Linux。
1. 按 **Create**。
1. 选择 **Tools->Nuget Package Manager->Package Manager Console** 并安装 **Aspose.PDF for .NET**（使用命令 `Install-Package Aspose.PDF`）。

### 在 Linux 容器中使用 ASP.NET Core Web App 生成 PDF 文档

我们将在此应用程序中使用 **复杂示例** 的代码。请按照 [此链接](/pdf/net/complex-pdf-example/) 获取更详细的说明。

1. 在 `wwwroot` 文件夹中创建 `images` 文件夹并放入图像 `logo.png`。您可以从 [这里](/pdf/net/docker/logo.png) 下载此图像。
1. 在 `wwwroot` 文件夹中创建 `fonts` 文件夹并将 [Roboto](https://fonts.google.com/specimen/Roboto) 字体放入其中。
1. 在 `wwwroot` 文件夹中创建 `samples` 文件夹并将示例数据放入其中。
1. 用以下代码替换 `HomeController.cs` 中的代码（请注意，您可以有其他命名空间）：

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
    // Represents a controller for the home page and PDF generation in a Linux demo application.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // Displays the index view.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // Generates a PDF document and returns it as a file.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("PDF Generation: Start ");
            // Create PDF document
            using (var document = new Aspose.Pdf.Document())
            {
                // Add page
                var page = document.Pages.Add();

                // Add image
                var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
                page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

                // Add Header
                var header = new TextFragment("New ferry routes in Fall 2020");
                header.TextState.Font = FontRepository.FindFont("Roboto");
                header.TextState.FontSize = 24;
                header.HorizontalAlignment = HorizontalAlignment.Center;
                header.Position = new Position(130, 720);
                page.Paragraphs.Add(header);

                // Add description
                var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
                var description = new TextFragment(descriptionText);
                description.TextState.Font = FontRepository.FindFont("Helvetica");
                description.TextState.FontSize = 14;
                description.HorizontalAlignment = HorizontalAlignment.Left;
                page.Paragraphs.Add(description);

                // Add table
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
                headerRow.Cells.Add("Departs City");
                headerRow.Cells.Add("Departs Island");
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
            }
            _logger.LogInformation("PDF Generation: Finish");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Converts a file to a different format based on the provided id.
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
        // Converts a PDF file to JPEG format and returns it as a file.
        // </summary>
        private FileStreamResult ConvertPdfToJpeg()
        {
            const string fileType = "image/jpeg";
            const string fileName = "sample.jpeg";

            var memoryStream = new MemoryStream();
            var pdfFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.pdf");

            // Open PDF document
            using (var document = new Aspose.Pdf.Document(pdfFileName))
            {
                var resolution = new Resolution(300);
                var renderer = new JpegDevice(resolution, 90);
                renderer.Process(document.Pages[1], memoryStream);
                memoryStream.Seek(0, SeekOrigin.Begin);
                return File(memoryStream, fileType, fileName);
            }
        }

        // <summary>
        // Converts an XPS file to PDF format and returns it as a file.
        // </summary>
        private FileStreamResult ConvertXpsToPdf()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";

            var memoryStream = new MemoryStream();
            var xpsFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.oxps");

            // Open XPS document
            using (var document = new Aspose.Pdf.Document(xpsFileName, new Aspose.Pdf.XpsLoadOptions()))
            {
                document.Save(memoryStream);
            }

            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Displays the privacy view.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // Displays the error view.
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```

1. 用以下内容替换 `Dockerfile` 中的内容：

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