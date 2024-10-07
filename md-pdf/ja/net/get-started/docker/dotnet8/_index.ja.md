---
title: DockerでAspose.PDFを実行する方法
linktitle: Dockerの使用
type: docs
weight: 20
url: /net/docker/dotnet8/
description: Docker Linuxコンテナを使用してアプリケーションにAspose.PDF機能を統合する
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 前提条件

以下の例は、次でテストされました：

* Docker v.25.0.2 および Docker Desktop 4.27.1
* Visual Studio 2022 Community Edition v.17.0.5
* 下記の例で使用されている .NET 8 SDK。
* Aspose.PDF.Drawing v.24.01

## Docker Linuxコンテナ用のサンプルアプリケーションを作成する

1. Visual Studio 2022を起動し、**ASP.NET Core Web App (Model-View-Controller)** テンプレートを選択し、**次へ**を押す
1. **新しいプロジェクトの設定**ウィンドウで、希望のプロジェクト名と場所を設定し、**次へ**を押す
1. **追加情報**ウィンドウで、**.NET 6.0 (長期サポート)** を選択し、Dockerサポートを有効にする。必要に応じて**Docker OS**をLinuxに設定することもできます。
1. **作成**を押す
1.
### ASP.NET Core Web Appを使用してLinuxコンテナでPDFドキュメントを生成

**Complex Example**からのコードをこのアプリで使用します。詳細な説明については、[このリンク](/pdf/net/complex-pdf-example/)をご覧ください。

1. `wwwroot`フォルダに`images`フォルダを作成し、画像`logo.png`を配置します。この画像は[こちら](/pdf/net/docker/logo.png)からダウンロードできます。
1. `wwwroot`フォルダに`fonts`フォルダを作成し、[Roboto](https://fonts.google.com/specimen/Roboto)フォントを配置します。
1. `wwwroot`フォルダに`samples`フォルダを作成し、サンプルデータを配置します。
1. `HomeController.cs`のコードを以下のスニペットに置き換えてください（別の名前空間を使用している場合がありますので注意してください）：

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
    // LinuxデモアプリケーションのホームページとPDF生成のためのコントローラーを表します。
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // インデックスビューを表示します。
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // PDFドキュメントを生成し、ファイルとして返します。
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("PDF生成: 開始");
            // ドキュメントオブジェクトを初期化
            var document = new Document();
            // ページを追加
            var page = document.Pages.Add();

            // 画像を追加
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // ヘッダーを追加
            var header = new TextFragment("2020年秋の新しいフェリールート");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // 説明を追加
            var descriptionText = "訪問者はオンラインでチケットを購入する必要があり、チケットは1日あたり5,000枚に限定されています。フェリーサービスは半分のキャパシティで、縮小されたスケジュールで運行しています。列に並ぶことを予想してください。";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);

            // テーブルを追加
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
            _logger.LogInformation("PDF生成: 完了");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // 提供されたIDに基づいてファイルを異なる形式に変換します。
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
        // PDFファイルをJPEG形式に変換し、ファイルとして返します。
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
        // XPSファイルをPDF形式に変換し、ファイルとして返します。
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
        // プライバシービューを表示します。
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // エラービューを表示します。
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```

1. `Dockerfile` の内容を以下の内容に置き換えてください：

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
```

