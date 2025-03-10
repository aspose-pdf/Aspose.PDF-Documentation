---
title: 使用 Microsoft Azure 函数转换文档
linktitle: 使用 Microsoft Azure 函数转换文档
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/converting-documents-with-microsoft-azure-function/
description: 了解如何使用 Microsoft Azure Functions 和 Aspose.PDF for .NET 转换 PDF 文档，实现基于云的文档处理。
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
    "abstract": "由 Microsoft Azure 提供支持的新文档转换功能使用户能够高效地将 PDF 文件转换为 DOCX、HTML 和 JPEG 等多种格式，使用 Aspose.PDF for .NET 和 Azure Functions。此功能实现与 Azure 资源的无缝集成，确保快速可靠的文件处理，旨在帮助希望增强其应用程序的开发人员。",
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
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还能应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

本文提供了使用 Aspose.PDF for .NET 和 Azure 函数在 Microsoft Azure 中转换 PDF 文档的详细逐步说明。

## 先决条件

* 安装了 Azure 开发的 Visual Studio 2022 Community Edition 或 Visual Studio Code。
* Azure 账户：您需要一个 Azure 订阅，在开始之前创建一个免费账户。
* .NET 6 SDK。
* Aspose.PDF for .NET。

## 创建 Azure 资源

### 创建存储账户

1. 转到 Azure 门户 (https://portal.azure.com)。
2. 点击“创建资源”。
3. 搜索“存储账户”。
4. 点击“创建”。
5. 填写详细信息：
   - 订阅：选择您的订阅。
   - 资源组：创建新资源组或选择现有资源组。
   - 存储账户名称：输入一个唯一名称。
   - 区域：选择最近的区域。
   - 性能：标准。
   - 冗余：LRS（本地冗余存储）。
6. 点击“审核 + 创建”。
7. 点击“创建”。

### 创建容器

1. 打开您的存储账户。
2. 在“数据存储”下转到“容器”。
3. 点击“+ 容器”。
4. 命名为“pdfdocs”。
5. 将公共访问级别设置为“私有”。
6. 点击“创建”。

## 创建项目

### 创建 Visual Studio 项目

1. 打开 Visual Studio 2022。
2. 点击“创建新项目”。
3. 选择“Azure Functions”。
4. 将项目命名为“PdfConverterAzure”。
5. 选择“.NET 6.0”或更高版本和“HTTP 触发器”。
6. 点击“创建”。

### 创建 Visual Studio Code 项目

#### 安装先决条件

1. Visual Code 扩展：
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. 安装 Azure Functions Core Tools：
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. 安装 Azure CLI：
- Windows：从 Microsoft 网站下载。
- macOS：`brew install azure-cli`。
- Linux：`curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`。

#### 配置项目

1. 在 Visual Studio Code 中打开项目：
```bash
code .
```

2. 通过创建/更新 `PdfConverterApp.csproj` 添加 NuGet 包：
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

## 安装所需的 NuGet 包

在 Visual Studio 中打开包管理器控制台并运行：
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

在 Visual Studio Code 中运行：
```bash
dotnet restore
```

## 配置 Azure 存储连接

在 Azure 门户的访问密钥下获取存储账户的访问密钥。这些密钥将用于验证您的应用程序。

1. 打开 `local.settings.json`：
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

2. 将 `YOUR_STORAGE_CONNECTION_STRING` 替换为您在 Azure 门户中的实际存储连接字符串。

## 配置 Aspose 许可证

在 Visual Studio 中：

1. 将您的 Aspose.PDF 许可证文件复制到项目中。
2. 右键单击许可证文件，选择“属性”。
3. 将“复制到输出目录”设置为“始终复制”。
4. 在 Program.cs 中添加许可证初始化代码：
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

## 创建代码

创建一个新文件 `PdfConverter.cs`：

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

创建一个新文件 `ConvertPdfFunction.cs`：

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

## 本地测试

在 Visual Studio 中：
1. 启动 Azure 存储模拟器。
2. 在 Visual Studio 中运行项目。
3. 使用 Postman 或 curl 进行测试：

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

在 Visual Studio Code 中：
1. 启动函数应用：
```bash
func start
```

2. 上传 PDF 进行测试：
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. 使用 Postman 或 curl 进行测试：
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## 部署到 Azure

在 Visual Studio 中：
1. 在 Visual Studio 中右键单击项目。
2. 选择“发布”。
3. 选择“Azure Function App”。
4. 选择您的订阅。
5. 创建新 Function App 或选择现有的 Function App。
6. 点击“发布”。

在 Visual Studio Code 中：
1. 按 F1 或 Ctrl+Shift+P。
2. 选择“Azure Functions: 部署到 Function App”。
3. 选择您的订阅。
4. 选择上面创建的函数应用。
5. 点击“部署”。

## 配置 Azure Function App

1. 转到 Azure 门户。
2. 打开您的 Function App。
3. 转到“配置”。
4. 添加应用程序设置：
   - 键：“ContainerName”。
   - 值：“pdfdocs”。
5. 保存更改。

## 测试已部署的服务

使用 Postman 或 curl 进行测试：
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## 支持的格式

支持的格式列表可以在 [这里](https://docs.aspose.com/pdf/net/supported-file-formats/) 找到。

## 故障排除

### 重要配置选项

1. 添加身份验证：
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

2. 对于大文件，请考虑：
   - 增加函数超时。
   - 使用更多内存的消费计划。
   - 实现分块上传/下载。
   - 添加进度跟踪。

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Microsoft Azure 函数处理 PDF 文档",
    "alternativeHeadline": "使用 Microsoft Azure 函数处理 PDF 文档",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, pdf 中的高级操作, microsoft azure, function",
    "wordcount": "302",
    "proficiencyLevel":"初学者",
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
    "description": "Aspose.PDF for .NET 可以使用 Microsoft Azure Function 处理文档。"
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