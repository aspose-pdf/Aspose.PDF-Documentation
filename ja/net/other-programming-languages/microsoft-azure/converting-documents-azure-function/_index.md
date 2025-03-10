---
title: Microsoft Azure Functionを使用したドキュメントの変換
linktitle: Microsoft Azure Functionを使用したドキュメントの変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/converting-documents-with-microsoft-azure-function/
description: Microsoft Azure Functionsを使用してPDFドキュメントを変換する方法を学び、クラウドベースのドキュメント処理を可能にします。
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting Documents with Microsoft Azure function",
    "alternativeHeadline": "Integrate PDF Conversion with Microsoft Azure Functions",
    "abstract": "Microsoft Azureによって提供される新しいドキュメント変換機能により、ユーザーはAspose.PDF for .NETとAzure Functionsを使用してPDFファイルをDOCX、HTML、JPEGなどのさまざまな形式に効率的に変換できます。この機能は、Azureリソースとのシームレスな統合を可能にし、アプリケーションを強化しようとする開発者向けに迅速かつ信頼性の高いファイル処理を保証します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1256",
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
    "url": "/net/converting-documents-with-microsoft-azure-function/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-function/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

この記事では、Aspose.PDF for .NETとAzure Functionを使用してMicrosoft AzureでPDFドキュメントを変換するための詳細な手順を提供します。

## 前提条件

* Azure開発がインストールされたVisual Studio 2022 Community EditionまたはVisual Studio Code。
* Azureアカウント: Azureサブスクリプションが必要で、開始する前に無料アカウントを作成してください。
* .NET 6 SDK。
* Aspose.PDF for .NET。

## Azureリソースの作成

### ストレージアカウントの作成

1. Azureポータルに移動します (https://portal.azure.com)。
2. 「リソースの作成」をクリックします。
3. 「ストレージアカウント」を検索します。
4. 「作成」をクリックします。
5. 詳細を入力します:
   - サブスクリプション: あなたのサブスクリプションを選択します。
   - リソースグループ: 新規作成または既存のものを選択します。
   - ストレージアカウント名: 一意の名前を入力します。
   - リージョン: 最寄りのリージョンを選択します。
   - パフォーマンス: スタンダード。
   - 冗長性: LRS（ローカル冗長ストレージ）。
6. 「レビュー + 作成」をクリックします。
7. 「作成」をクリックします。

### コンテナの作成

1. ストレージアカウントを開きます。
2. 「データストレージ」の下の「コンテナ」に移動します。
3. 「+ コンテナ」をクリックします。
4. 名前を「pdfdocs」とします。
5. 公開アクセスレベルを「プライベート」に設定します。
6. 「作成」をクリックします。

## プロジェクトの作成

### Visual Studioプロジェクトの作成

1. Visual Studio 2022を開きます。
2. 「新しいプロジェクトを作成」をクリックします。
3. 「Azure Functions」を選択します。
4. プロジェクト名を「PdfConverterAzure」とします。
5. 「.NET 6.0」またはそれ以降と「HTTPトリガー」を選択します。
6. 「作成」をクリックします。

### Visual Studio Codeプロジェクトの作成

#### 前提条件のインストール

1. Visual Code拡張機能:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. Azure Functions Core Toolsをインストールします:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Azure CLIをインストールします:
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
    <AzureFunctionsVersion>v4</AzureFunctionsVersion>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Sdk.Functions" Version="4.1.1" />
    <PackageReference Include="Aspose.PDF" Version="24.10.0" />
    <PackageReference Include="Azure.Storage.Blobs" Version="12.14.1" />
    <PackageReference Include="Microsoft.Azure.WebJobs.Extensions.Storage" Version="5.0.1" />
  </ItemGroup>
</Project>
```

## 必要なNuGetパッケージのインストール

Visual Studioでパッケージマネージャーコンソールを開き、次を実行します:
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

Visual Studio Codeで次を実行します:
```bash
dotnet restore
```

## Azureストレージ接続の構成

Azureポータルのアクセスキーの下でストレージアカウントのアクセスキーを取得します。これらのキーは、アプリケーションを認証するために使用されます。

1. `local.settings.json`を開きます:
```json
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "YOUR_STORAGE_CONNECTION_STRING",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet",
        "ContainerName": "pdfdocs"
    }
}
```

2. `YOUR_STORAGE_CONNECTION_STRING`をAzureポータルからの実際のストレージ接続文字列に置き換えます。

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

## コードの作成

新しいファイル`PdfConverter.cs`を作成します:

```csharp
using Azure.Storage.Blobs;
using System;
using System.IO;
using System.Threading.Tasks;

public class PdfConverter
{
    private readonly BlobContainerClient _containerClient;

    public PdfConverter(string connectionString, string containerName)
    {
        _containerClient = new BlobContainerClient(connectionString, containerName);
    }

    public async Task<string> ConvertToFormat(string sourceBlobName, string targetFormat)
    {
        // Download source PDF
        var sourceBlob = _containerClient.GetBlobClient(sourceBlobName);
        using var sourceStream = new MemoryStream();
        await sourceBlob.DownloadToAsync(sourceStream);
        sourceStream.Position = 0;

        // Open PDF document
        var document = new Aspose.Pdf.Document(sourceStream);

        // Create output stream
        using var outputStream = new MemoryStream();
        string targetBlobName = Path.GetFileNameWithoutExtension(sourceBlobName);

        // Convert based on format
        switch (targetFormat.ToLower())
        {
            case "docx":
                targetBlobName += ".docx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.DocX);
                break;

            case "html":
                targetBlobName += ".html";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Html);
                break;

            case "xlsx":
                targetBlobName += ".xlsx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Excel);
                break;

            case "pptx":
                targetBlobName += ".pptx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Pptx);
                break;

            case "jpeg":
            case "jpg":
                targetBlobName += ".jpg";
                foreach (var page in document.Pages)
                {
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(new Aspose.Pdf.Devices.Resolution(300));
                    jpegDevice.Process(page, outputStream);
                }
                break;

            default:
                throw new ArgumentException($"Unsupported format: {targetFormat}");
        }

        // Upload converted file
        outputStream.Position = 0;
        var targetBlob = _containerClient.GetBlobClient(targetBlobName);
        await targetBlob.UploadAsync(outputStream, true);

        return targetBlob.Uri.ToString();
    }
}
```

新しいファイル`ConvertPdfFunction.cs`を作成します:

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using System.Threading.Tasks;
using System;
using System.IO;
using Newtonsoft.Json;
using Microsoft.AspNetCore.Mvc;

public static class ConvertPdfFunction
{
    [FunctionName("ConvertPdf")]
    public static async Task<IActionResult> Run(
        [HttpTrigger(AuthorizationLevel.Function, "post"), Route = "convert"] HttpRequest req,
        ILogger log)
    {
        try
        {
            // Read request body
            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);

            string sourceBlob = data?.sourceBlob;
            string targetFormat = data?.targetFormat;

            if (string.IsNullOrEmpty(sourceBlob) || string.IsNullOrEmpty(targetFormat))
            {
                return new BadRequestObjectResult("Please provide sourceBlob and targetFormat");
            }

            // Get configuration
            string connectionString = Environment.GetEnvironmentVariable("AzureWebJobsStorage");
            string containerName = Environment.GetEnvironmentVariable("ContainerName");

            // Convert PDF
            var converter = new PdfConverter(connectionString, containerName);
            string resultUrl = await converter.ConvertToFormat(sourceBlob, targetFormat);

            return new OkObjectResult(new { url = resultUrl });
        }
        catch (Exception ex)
        {
            log.LogError(ex, "Error converting PDF");
            return new StatusCodeResult(500);
        }
    }
}
```

```csharp
// Startup.cs
[assembly: FunctionsStartup(typeof(PdfConverterAzure.Functions.Startup))]
namespace PdfConverterAzure.Functions
{
    public class Startup : FunctionsStartup
    {
        public override void Configure(IFunctionsHostBuilder builder)
        {
            // Read configuration
            var config = builder.GetContext().Configuration;

            // Register services
            builder.Services.AddLogging();

            // Register Azure Storage
            builder.Services.AddSingleton(x => 
                new BlobServiceClient(config["AzureWebJobsStorage"]));

            // Configure Aspose License
            var license = new Aspose.Pdf.License();
            license.SetLicense("Aspose.PDF.lic");
        }
    }
}
```

## ローカルでのテスト

Visual Studioで:
1. Azureストレージエミュレーターを起動します。
2. Visual Studioでプロジェクトを実行します。
3. Postmanまたはcurlを使用してテストします:

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

Visual Studio Codeで:
1. 関数アプリを起動します:
```bash
func start
```

2. テスト用にPDFをアップロードします:
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. Postmanまたはcurlを使用してテストします:
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Azureへのデプロイ

Visual Studioで:
1. Visual Studioのプロジェクトを右クリックします。
2. 「発行」を選択します。
3. 「Azure Function App」を選択します。
4. あなたのサブスクリプションを選択します。
5. 新規作成または既存のFunction Appを選択します。
6. 「発行」をクリックします。

Visual Studio Codeで:
1. F1またはCtrl+Shift+Pを押します。
2. 「Azure Functions: Function Appにデプロイ」を選択します。
3. あなたのサブスクリプションを選択します。
4. 上記で作成した関数アプリを選択します。
5. 「デプロイ」をクリックします。

## Azure Function Appの構成

1. Azureポータルに移動します。
2. あなたのFunction Appを開きます。
3. 「構成」に移動します。
4. アプリケーション設定を追加します:
   - キー: "ContainerName"。
   - 値: "pdfdocs"。
5. 変更を保存します。

## デプロイされたサービスのテスト

Postmanまたはcurlを使用してテストします:
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## サポートされている形式

サポートされている形式のリストは[こちら](https://docs.aspose.com/pdf/net/supported-file-formats/)で確認できます。

## トラブルシューティング

### 重要な構成オプション

1. 認証を追加します:
```csharp
[FunctionName("ConvertPdf")]
public async Task<IActionResult> Run(
    [HttpTrigger(AuthorizationLevel.Function, "post", Route = "convert")] HttpRequest req,
    ClaimsPrincipal principal,
    ILogger log)
{
    // Check authentication
    if (!principal.Identity.IsAuthenticated)
    {
        return new UnauthorizedResult();
    }
    // ...
}
```

2. 大きなファイルの場合は、次を考慮してください:
   - 関数のタイムアウトを増やす。
   - より多くのメモリを持つ消費プランを使用する。
   - チャンクアップロード/ダウンロードを実装する。
   - 進捗追跡を追加する。

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Microsoft Azure Functionを使用したPDFドキュメントの操作",
    "alternativeHeadline": "PDFドキュメントの処理にMicrosoft Azure Functionを使用する",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ"
    },
    "genre": "pdfドキュメント生成",
    "keywords": "pdf, c#, pdfの高度な操作, microsoft azure, function",
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
    "url": "/net/converting-documents-with-microsoft-azure-function/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-function/"
    },
    "dateModified": "2024-10-25",
    "description": "Aspose.PDF for .NETはMicrosoft Azure Functionを使用してドキュメントを処理できます。"
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