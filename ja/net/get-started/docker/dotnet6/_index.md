---
title: DockerでAspose.PDF for .NET 6を実行する方法
linktitle: DockerでのAspose.PDF for .NET 6の使用
type: docs
weight: 10
url: ja/net/docker/dotnet6/
description: Docker LinuxまたはWindowsコンテナを使用してアプリケーションにAspose.PDF機能を統合する
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 前提条件

以下の例はテスト済みです:

* Docker v.20.10.11 および Docker Desktop 4.3.2
* Visual Studio 2022 Community Edition v.17.0.5
* 下記の例に使用される .NET 6 SDK
* Aspose.PDF for .NET v.22.01

## Docker Linuxコンテナ用のサンプルアプリケーションを作成

1. Visual Studio 2022を起動し、**ASP.NET Core Web App (Model-View-Controller)** テンプレートを選択して**次へ**を押します
1. **新しいプロジェクトを設定**ウィンドウで、希望のプロジェクト名と場所を設定して**次へ**を押します
1. **追加情報**ウィンドウで**.NET 6.0 (長期サポート)** を選択し、Dockerサポートを有効にします。必要に応じて**Docker OS**をLinuxに設定することもできます。
1.
1. **ツール->Nugetパッケージマネージャー->パッケージマネージャーコンソール** を選択し、**Aspose.PDF for .NET** をインストールします（コマンド `Install-Package Aspose.PDF` を使用）。

### ASP.NET Core Webアプリを使用してLinuxコンテナでPDFドキュメントを生成する

このアプリでは**複雑な例**からコードを使用します。詳細な説明については、[このリンク](/pdf/net/complex-pdf-example/)をご覧ください。

1. `wwwroot`フォルダに`images`フォルダを作成し、画像`logo.png`を配置します。この画像は[こちら](/pdf/net/docker/logo.png)からダウンロードできます。
1. `HomeController.cs`のコードを以下のスニペットに置き換えてください（別の名前空間を使用している可能性があることに注意してください）：

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリとも動作します。

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

            _logger.LogInformation("開始");
            // ドキュメントオブジェクトの初期化
            var document = new Document();
            // ページの追加
            var page = document.Pages.Add();

            // 画像の追加
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // ヘッダーの追加
            var header = new TextFragment("2020年秋の新しいフェリールート");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 説明の追加
            var descriptionText = "訪問者はオンラインでチケットを購入する必要があり、チケットは1日あたり5,000枚に限定されています。フェリーサービスは半分のキャパシティで、縮小されたスケジュールで運行されています。列を予想してください。";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // テーブルの追加
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
            headerRow.Cells.Add("出発都市");
            headerRow.Cells.Add("出発島");
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
            _logger.LogInformation("完了");
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
`Dockerfile` の内容を以下の内容に置き換えてください：

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

## Docker Windows コンテナ用サンプルアプリケーションを作成する

1.
1. **新しいプロジェクトの設定** ウィンドウで、希望のプロジェクト名と場所を設定して、**次へ**を押します
1. **追加情報** ウィンドウで **.NET 6.0 (長期サポート)** を選択し、Docker サポートを有効にします。必要に応じて **Docker OS** を `Windows` に設定することもできます。
1. **作成**を押す
1. **ツール->Nuget パッケージ マネージャー->パッケージ マネージャー コンソール** を選択し、**Aspose.PDF for .NET** をインストールします（コマンド `Install-Package Aspose.PDF` を使用）

### Windows コンテナーで ASP.NET Core Web アプリを使用して PDF ドキュメントを生成する

前の例と同じコードを使用します。

1. `wwwroot` フォルダーに `images` フォルダーを作成し、画像 `logo.png` を置きます。この画像は[こちら](/pdf/net/docker/logo.png)からダウンロードできます
1. `HomeController.cs` のコードを上記のスニペットに置き換えます。

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

