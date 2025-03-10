---
title: Aspose.PDF for .NET 8をDockerで実行する方法
linktitle: DockerでのAspose.PDF for .NET 8の使用
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/docker/dotnet8/
description: Docker LinuxまたはWindowsコンテナを使用して、.NET 8アプリケーションにAspose.PDF機能を統合する
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
    "abstract": "LinuxまたはWindowsコンテナを使用して、アプリケーションにAspose.PDF for .NET 8をシームレスに統合する方法を発見してください。この機能により、ASP.NET Coreアプリケーション内で効率的なPDFドキュメントの生成と操作が可能になり、開発者はコンテナ化された環境で強力なPDF機能を活用できます。この簡単なセットアップガイドを利用して.NETプロジェクトを最適化し、Aspose.PDF for .NETの堅牢な機能で開発ワークフローを向上させましょう。",
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
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 前提条件

以下の例は、次の環境でテストされました：

* Docker v.25.0.2およびDocker Desktop 4.27.1。
* Visual Studio 2022 Community Edition v.17.0.5。
* 以下の例で使用される.NET 8 SDK。
* Aspose.PDF.Drawing v.24.01。

## Docker Linuxコンテナ用のサンプルアプリケーションを作成する

1. Visual Studio 2022を起動し、**ASP.NET Core Web App (Model-View-Controller)** テンプレートを選択して**次へ**を押します。
1. **新しいプロジェクトの構成**ウィンドウで、希望するプロジェクト名と場所を設定し、**次へ**を押します。
1. **追加情報**ウィンドウで、**.NET 6.0 (長期サポート)**を選択し、Dockerサポートを有効にします。必要に応じて**Docker OS**をLinuxに設定することもできます。
1. **作成**を押します。
1. **ツール->Nugetパッケージマネージャ->パッケージマネージャコンソール**を選択し、**Aspose.PDF for .NET**をインストールします（コマンド `Install-Package Aspose.PDF` を使用）。

### Linuxコンテナ内のASP.NET Core Web Appを使用してPDFドキュメントを生成する

このアプリでは、**複雑な例**のコードを使用します。詳細な説明については[こちらのリンク](/pdf/net/complex-pdf-example/)を参照してください。

1. `wwwroot`フォルダ内に`images`フォルダを作成し、画像`logo.png`を置きます。この画像は[こちら](/pdf/net/docker/logo.png)からダウンロードできます。
1. `wwwroot`フォルダ内に`fonts`フォルダを作成し、[Roboto](https://fonts.google.com/specimen/Roboto)フォントをそこに置きます。
1. `wwwroot`フォルダ内に`samples`フォルダを作成し、サンプルデータをそこに置きます。
1. `HomeController.cs`内のコードを以下のスニペットに置き換えます（別の名前空間を持つことができますのでご注意ください）：

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

1. `Dockerfile`内の内容を以下の内容に置き換えます：

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