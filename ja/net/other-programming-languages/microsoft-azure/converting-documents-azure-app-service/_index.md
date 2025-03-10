---
title: Microsoft Azure Appサービスを使用したドキュメントの変換
linktitle: Microsoft Azure Appサービスを使用したドキュメントの変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/converting-documents-with-microsoft-azure-app-service/
description: Microsoft Azure App Serviceを使用してPDFドキュメントを変換し、クラウドでのドキュメントワークフローを最適化する方法を見つけてください。
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting Documents with Microsoft Azure App service",
    "alternativeHeadline": "Convert PDF Documents with Azure App Service Easily",
    "abstract": "Microsoft Azure App Serviceを使用して、PDFファイルをDOCX、HTML、JPG、PNGなどのさまざまな形式にシームレスに変換できる新機能を活用してください。この機能はAspose.PDF for .NETを活用し、クラウドアプリケーション内でのドキュメント変換を効率的に処理するための堅牢で効率的なソリューションを提供します。この変換機能をAzureプロジェクトに統合して、ワークフローを向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1042",
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
    "url": "/net/converting-documents-with-microsoft-azure-app-service/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-app-service/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

この記事では、Microsoft Azureを使用してPDFドキュメントを変換するための詳細な手順を提供します。Aspose.PDF for .NETとAzure Appサービスを使用します。

## 前提条件

* Azure開発がインストールされたVisual Studio 2022 Community EditionまたはVisual Studio Code。
* Azureアカウント: Azureサブスクリプションが必要です。開始する前に無料アカウントを作成してください。
* .NET 6 SDK。
* Aspose.PDF for .NET。

## Azureリソースの作成

### Appサービスの作成

1. Azureポータルに移動します (https://portal.azure.com)。
2. 新しいリソースグループを作成します。
3. 新しいAppサービスを作成します:
   - .NET 6 (LTS)ランタイムを選択します。
   - 適切な価格帯を選択します。
4. ロギング用のApplication Insightsリソースを作成します。

## プロジェクトの作成

### Visual Studioプロジェクトの作成

1. Visual Studio 2022を開きます。
2. 「新しいプロジェクトを作成」をクリックします。
3. 「ASP.NET Core Web API」を選択します。
4. プロジェクト名を「PdfConversionService」とします。
5. 「.NET 6.0」またはそれ以降を選択します。
6. 「作成」をクリックします。

### Visual Studio Codeプロジェクトの作成

#### 前提条件のインストール

1. Visual Code拡張機能:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azureappservice
```

2. Azure CLIをインストールします:
- Windows: Microsoftのウェブサイトからダウンロードします。
- macOS: `brew install azure-cli`。
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`。

#### プロジェクトの構成

1. Visual Studio Codeでプロジェクトを開きます:
```bash
code .
```

2. `PdfConverterApp.csproj`を作成/更新してNuGetパッケージを追加します:
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Aspose.PDF" Version="24.10.0" />
    <PackageReference Include="Microsoft.ApplicationInsights.AspNetCore" Version="2.22.0" />
    <PackageReference Include="Microsoft.Extensions.Logging.AzureAppServices" Version="8.0.10" />
  </ItemGroup>
</Project>
```

3. 構成を追加します:
```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": ".NET Core Launch (web)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            "program": "${workspaceFolder}/bin/Debug/net6.0/PdfConversionService.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            "stopAtEntry": false,
            "env": {
                "ASPNETCORE_ENVIRONMENT": "Development"
            }
        }
    ]
}
```

4. プロジェクト構造を作成します:
```bash
mkdir Controllers
touch Controllers/PdfController.cs
```

## 必要なNuGetパッケージのインストール

Visual Studioでパッケージマネージャーコンソールを開き、次を実行します:
```powershell
Install-Package Aspose.PDF
Install-Package Microsoft.ApplicationInsights.AspNetCore
Install-Package Microsoft.Extensions.Logging.AzureAppServices
```

Visual Studio Codeで実行します:
```bash
dotnet restore
```

## Asposeライセンスの構成

Visual Studioで:

1. Aspose.PDFライセンスファイルをプロジェクトにコピーします。
2. ライセンスファイルを右クリックし、「プロパティ」を選択します。
3. 「出力ディレクトリにコピー」を「常にコピー」に設定します。
4. Program.csにライセンス初期化コードを追加します:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

### コードの作成

Visual Studioで:
1. Controllersフォルダーを右クリックします。
2. 追加 → 新しいアイテム → APIコントローラー - 空を選択します。
3. ファイル名を「PdfController.cs」とします。

```csharp
// PdfController.cs
using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class PdfController : ControllerBase
{
    private readonly ILogger<PdfController> _logger;

    public PdfController(ILogger<PdfController> logger)
    {
        _logger = logger;
    }

    [HttpPost("convert")]
    public async Task<IActionResult> ConvertPdf(
        IFormFile file,
        [FromQuery] string outputFormat = "docx")
    {
        try
        {
            if (file == null || file.Length == 0)
            {
                return BadRequest("No file uploaded");
            }

            // Validate input file is PDF
            if (!file.ContentType.Equals("application/pdf", StringComparison.OrdinalIgnoreCase))
            {
                return BadRequest("File must be a PDF");
            }

            using var inputStream = file.OpenReadStream();
            using var document = new Aspose.Pdf.Document(inputStream);
            using var outputStream = new MemoryStream();

            switch (outputFormat.ToLower())
            {
                case "docx":
                    document.Save(outputStream, Aspose.Pdf.SaveFormat.DocX);
                    return File(outputStream.ToArray(),
                        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        "converted.docx");

                case "html":
                    document.Save(outputStream, Aspose.Pdf.SaveFormat.Html);
                    return File(outputStream.ToArray(),
                        "text/html",
                        "converted.html");

                case "jpg":
                case "jpeg":
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice();
                    jpegDevice.Process(document.Pages[1], outputStream);
                    return File(outputStream.ToArray(),
                        "image/jpeg",
                        "converted.jpg");

                case "png":
                    var pngDevice = new Aspose.Pdf.Devices.PngDevice();
                    pngDevice.Process(document.Pages[1], outputStream);
                    return File(outputStream.ToArray(),
                        "image/png",
                        "converted.png");

                default:
                    return BadRequest("Unsupported output format");
            }
        }
        catch (Exception ex)
        {
            _logger.LogError(ex, "Error converting PDF");
            return StatusCode(500, "Internal server error");
        }
    }
}
```

```csharp
// Program.cs
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Add logging
builder.Services.AddApplicationInsightsTelemetry();
builder.Services.AddLogging(logging =>
{
    logging.AddConsole();
    logging.AddDebug();
    logging.AddAzureWebAppDiagnostics();
});

var app = builder.Build();

// Initialize license
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();
```

## アプリケーション設定の構成

1. appsettings.jsonを開きます。
2. 構成を追加します:
```json
{
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*",
  "ApplicationInsights": {
    "ConnectionString": "Your-Connection-String"
  }
}
```
`Your-Connection-StringG`をAzureポータルからの実際の接続文字列に置き換えます。

## ローカルでのテスト

Visual Studioで:
1. F5を押してアプリケーションを実行します。
2. Swagger UIが開きます。
3. /api/pdf/convertエンドポイントをテストします:
   - 「試してみる」をクリックします。
   - PDFファイルをアップロードします。
   - 出力形式を選択します。
   - 実行して変換を確認します。

Visual Studio Codeで:
```bash
dotnet run

curl -X POST "https://localhost:5001/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## Azureへのデプロイ

Visual Studioで:
1. プロジェクトを右クリックします。
2. 「発行」を選択します。
3. ターゲットとして「Azure」を選択します。
4. 「Azure App Service (Windows)」を選択します。
5. サブスクリプションとAppサービスを選択します。
6. 「発行」をクリックします。

Visual Studio Codeで:
```bash
dotnet publish -c Release

az webapp deployment source config-zip \
    --resource-group $resourceGroup \
    --name $appName \
    --src bin/Release/net6.0/publish.zip

az webapp deploy \
    --resource-group $resourceGroup \
    --name $appName \
    --src-path "Aspose.PDF.lic" \
    --target-path "site/wwwroot/Aspose.PDF.lic"
```

## Azure Appサービスの構成

1. Azureポータルに移動します。
2. Appサービスを開きます。
3. 設定を構成します:
   ```
   App Settings:
   - WEBSITE_RUN_FROM_PACKAGE=1
   - ASPNETCORE_ENVIRONMENT=Production
   ```

## デプロイされたサービスのテスト

Postmanまたはcurlを使用してテストします:
```bash
curl -X POST "https://your-app.azurewebsites.net/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## サポートされている形式

サポートされている形式のリストは[こちら](https://docs.aspose.com/pdf/net/supported-file-formats/)で確認できます。

## トラブルシューティング

### 重要な構成オプション

1. **ファイルサイズ制限**
web.configに追加します:
```xml
<configuration>
  <system.webServer>
    <security>
      <requestFiltering>
        <requestLimits maxAllowedContentLength="104857600" />
      </requestFiltering>
    </security>
  </system.webServer>
</configuration>
```

2. **CORS** (必要に応じて)
Program.csで:
```csharp
builder.Services.AddCors(options =>
{
    options.AddPolicy("AllowSpecificOrigin",
        builder => builder
            .WithOrigins("https://your-frontend-domain.com")
            .AllowAnyMethod()
            .AllowAnyHeader());
});
```

3. **認証** (必要に応じて)
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => {
        // Configure JWT options
    });
```

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Microsoft Azure Appサービスを使用したPDFドキュメントの操作",
    "alternativeHeadline": "PDFドキュメントを処理するためのMicrosoft Azure Appサービスの使用",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, c#, pdfの高度な操作, microsoft azure, app service",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/net/converting-documents-with-microsoft-azure-app-service/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-app-service/"
    },
    "dateModified": "2024-10-25",
    "description": "Aspose.PDF for .NETはMicrosoft Azure App Serviceを使用してドキュメントを処理できます。"
}
</script>

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "",
    "softwareVersion": "2024.10",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>