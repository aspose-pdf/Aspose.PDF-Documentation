---
title: DockerでAspose.PDF for .NET 6を実行する方法
linktitle: DockerでのAspose.PDF for .NET 6の使用
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/docker/dotnet6/
description: Docker LinuxまたはWindowsコンテナを使用して、.NET 6アプリケーションにAspose.PDF機能を統合する
lastmod: "2024-08-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to run Aspose.PDF for .NET 6 in Docker",
    "alternativeHeadline": "Run Aspose.PDF in .NET 6 with Docker Support",
    "abstract": "この機能により、開発者はDocker LinuxまたはWindowsコンテナを利用して、.NET 6アプリケーション内にAspose.PDF機能をシームレスに統合できます。この機能は、ASP.NET Coreアプリケーションから直接PDFドキュメントを生成するプロセスを簡素化し、クラウドベースの環境におけるドキュメント管理の効率を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1067",
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
    "url": "/net/docker/dotnet6/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/docker/dotnet6/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## 前提条件

以下の例は次の環境でテストされました：

* Docker v.20.10.11およびDocker Desktop 4.3.2。
* Visual Studio 2022 Community Edition v.17.0.5。
* 以下の例で使用される.NET 6 SDK。
* Aspose.PDF for .NET v.22.01。

## Docker Linuxコンテナ用のサンプルアプリケーションを作成する

1. Visual Studio 2022を起動し、**ASP.NET Core Web App (Model-View-Controller)** テンプレートを選択して**次へ**を押します。
1. **新しいプロジェクトの構成**ウィンドウで、希望するプロジェクト名と場所を設定し、**次へ**を押します。
1. **追加情報**ウィンドウで、**.NET 6.0 (長期サポート)**を選択し、Dockerサポートを有効にします。必要に応じて、**Docker OS**をLinuxに設定することもできます。
1. **作成**を押します。
1. **ツール->Nugetパッケージマネージャ->パッケージマネージャコンソール**を選択し、**Aspose.PDF for .NET**をインストールします（コマンド `Install-Package Aspose.PDF` を使用）。

### Linuxコンテナ内のASP.NET Core Web Appを使用してPDFドキュメントを生成する

このアプリでは**複雑な例**のコードを使用します。詳細な説明については[こちらのリンク](/pdf/ja/net/complex-pdf-example/)を参照してください。

1. `wwwroot`フォルダ内に`images`フォルダを作成し、画像`logo.png`を置きます。この画像は[こちら](/pdf/ja/net/docker/logo.png)からダウンロードできます。
1. `HomeController.cs`のコードを以下のスニペットに置き換えます（別の名前空間を使用することもできますのでご注意ください）：

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

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
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Start");
            // Initialize document object
            using (var document = new Aspose.Pdf.Document())
            {
                // Add page
                var page = document.Pages.Add();

                // Add image
                var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
                page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

                // -------------------------------------------------------------
                // Add Header
                var header = new TextFragment("New ferry routes in Fall 2020");
                header.TextState.Font = FontRepository.FindFont("Arial");
                header.TextState.FontSize = 24;
                header.HorizontalAlignment = HorizontalAlignment.Center;
                header.Position = new Position(130, 720);
                page.Paragraphs.Add(header);

                // Add description
                var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
                var description = new TextFragment(descriptionText);
                description.TextState.Font = FontRepository.FindFont("Times New Roman");
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
            _logger.LogInformation("Finish");
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

1. `Dockerfile`の内容を以下の内容に置き換えます：

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

## Docker Windowsコンテナ用のサンプルアプリケーションを作成する

1. Visual Studio 2022を起動し、**ASP.NET Core Web App (Model-View-Controller)** テンプレートを選択して**次へ**を押します。
1. **新しいプロジェクトの構成**ウィンドウで、希望するプロジェクト名と場所を設定し、**次へ**を押します。
1. **追加情報**ウィンドウで、**.NET 6.0 (長期サポート)**を選択し、Dockerサポートを有効にします。必要に応じて、**Docker OS**を`Windows`に設定することもできます。
1. **作成**を押します。
1. **ツール->Nugetパッケージマネージャ->パッケージマネージャコンソール**を選択し、**Aspose.PDF for .NET**をインストールします（コマンド `Install-Package Aspose.PDF` を使用）。

### Windowsコンテナ内のASP.NET Core Web Appを使用してPDFドキュメントを生成する

前の例と同じコードを使用します。

1. `wwwroot`フォルダ内に`images`フォルダを作成し、画像`logo.png`を置きます。この画像は[こちら](/pdf/ja/net/docker/logo.png)からダウンロードできます。
1. `HomeController.cs`のコードを上記のスニペットに置き換えます。

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