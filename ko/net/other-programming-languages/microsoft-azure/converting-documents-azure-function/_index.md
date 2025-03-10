---
title: Microsoft Azure 기능을 사용한 문서 변환
linktitle: Microsoft Azure 기능을 사용한 문서 변환
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/converting-documents-with-microsoft-azure-function/
description: Microsoft Azure Functions를 사용하여 PDF 문서를 변환하는 방법을 배우고 Aspose.PDF for .NET를 통해 클라우드 기반 문서 처리를 가능하게 합니다.
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
    "abstract": "Microsoft Azure의 새로운 문서 변환 기능은 사용자가 Aspose.PDF for .NET 및 Azure Functions를 사용하여 PDF 파일을 DOCX, HTML 및 JPEG와 같은 다양한 형식으로 효율적으로 변환할 수 있도록 합니다. 이 기능은 Azure 리소스와의 원활한 통합을 가능하게 하여 개발자가 애플리케이션을 향상시키기 위해 신속하고 신뢰할 수 있는 파일 처리를 보장합니다.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

이 문서에서는 Microsoft Azure를 사용하여 PDF 문서를 변환하는 단계별 지침을 제공합니다. Aspose.PDF for .NET 및 Azure 기능을 사용합니다.

## 전제 조건

* Azure 개발이 설치된 Visual Studio 2022 Community Edition 또는 Visual Studio Code.
* Azure 계정: Azure 구독이 필요하며 시작하기 전에 무료 계정을 생성해야 합니다.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## Azure 리소스 생성

### 스토리지 계정 생성

1. Azure 포털로 이동합니다 (https://portal.azure.com).
2. "리소스 만들기"를 클릭합니다.
3. "스토리지 계정"을 검색합니다.
4. "만들기"를 클릭합니다.
5. 세부 정보를 입력합니다:
   - 구독: 구독을 선택합니다.
   - 리소스 그룹: 새로 만들거나 기존 것을 선택합니다.
   - 스토리지 계정 이름: 고유한 이름을 입력합니다.
   - 지역: 가장 가까운 지역을 선택합니다.
   - 성능: 표준.
   - 중복성: LRS(로컬 중복 스토리지).
6. "검토 + 만들기"를 클릭합니다.
7. "만들기"를 클릭합니다.

### 컨테이너 생성

1. 스토리지 계정을 엽니다.
2. "데이터 저장소" 아래의 "컨테이너"로 이동합니다.
3. "+ 컨테이너"를 클릭합니다.
4. 이름을 "pdfdocs"로 지정합니다.
5. 공개 액세스 수준을 "비공개"로 설정합니다.
6. "만들기"를 클릭합니다.

## 프로젝트 생성

### Visual Studio 프로젝트 생성

1. Visual Studio 2022를 엽니다.
2. "새 프로젝트 만들기"를 클릭합니다.
3. "Azure Functions"를 선택합니다.
4. 프로젝트 이름을 "PdfConverterAzure"로 지정합니다.
5. ".NET 6.0" 이상 및 "HTTP 트리거"를 선택합니다.
6. "만들기"를 클릭합니다.

### Visual Studio Code 프로젝트 생성

#### 전제 조건 설치

1. Visual Code 확장:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. Azure Functions Core Tools 설치:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Azure CLI 설치:
- Windows: Microsoft 웹사이트에서 다운로드합니다.
- macOS: `brew install azure-cli`.
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.

#### 프로젝트 구성

1. Visual Studio Code에서 프로젝트를 엽니다:
```bash
code .
```

2. `PdfConverterApp.csproj`를 생성/업데이트하여 NuGet 패키지를 추가합니다:
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

## 필요한 NuGet 패키지 설치

Visual Studio에서 패키지 관리자 콘솔을 열고 실행합니다:
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

Visual Studio Code에서 실행합니다:
```bash
dotnet restore
```

## Azure 스토리지 연결 구성

Azure 포털의 액세스 키에서 스토리지 계정의 액세스 키를 가져옵니다. 이 키는 애플리케이션을 인증하는 데 사용됩니다.

1. `local.settings.json`을 엽니다:
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

2. `YOUR_STORAGE_CONNECTION_STRING`을 Azure 포털에서 가져온 실제 스토리지 연결 문자열로 교체합니다.

## Aspose 라이센스 구성

Visual Studio에서:

1. Aspose.PDF 라이센스 파일을 프로젝트에 복사합니다.
2. 라이센스 파일을 마우스 오른쪽 버튼으로 클릭하고 "속성"을 선택합니다.
3. "출력 디렉터리에 복사"를 "항상 복사"로 설정합니다.
4. Program.cs에 라이센스 초기화 코드를 추가합니다:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

## 코드 생성

새 파일 `PdfConverter.cs`를 생성합니다:

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

새 파일 `ConvertPdfFunction.cs`를 생성합니다:

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

## 로컬에서 테스트

Visual Studio에서:
1. Azure 스토리지 에뮬레이터를 시작합니다.
2. Visual Studio에서 프로젝트를 실행합니다.
3. Postman 또는 curl을 사용하여 테스트합니다:

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

Visual Studio Code에서:
1. 함수 앱을 시작합니다:
```bash
func start
```

2. 테스트할 PDF를 업로드합니다:
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. Postman 또는 curl을 사용하여 테스트합니다:
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Azure에 배포

Visual Studio에서:
1. Visual Studio에서 프로젝트를 마우스 오른쪽 버튼으로 클릭합니다.
2. "게시"를 선택합니다.
3. "Azure Function App"을 선택합니다.
4. 구독을 선택합니다.
5. 새로 만들거나 기존 Function App을 선택합니다.
6. "게시"를 클릭합니다.

Visual Studio Code에서:
1. F1 또는 Ctrl+Shift+P를 누릅니다.
2. "Azure Functions: Function App에 배포"를 선택합니다.
3. 구독을 선택합니다.
4. 위에서 생성한 함수 앱을 선택합니다.
5. "배포"를 클릭합니다.

## Azure Function App 구성

1. Azure 포털로 이동합니다.
2. Function App을 엽니다.
3. "구성"으로 이동합니다.
4. 애플리케이션 설정을 추가합니다:
   - 키: "ContainerName".
   - 값: "pdfdocs".
5. 변경 사항을 저장합니다.

## 배포된 서비스 테스트

Postman 또는 curl을 사용하여 테스트합니다:
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## 지원되는 형식

지원되는 형식 목록은 [여기](https://docs.aspose.com/pdf/net/supported-file-formats/)에서 확인할 수 있습니다.

## 문제 해결

### 중요한 구성 옵션

1. 인증 추가:
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

2. 대용량 파일의 경우 고려 사항:
   - 함수 타임아웃 증가.
   - 더 많은 메모리를 가진 소비 계획 사용.
   - 청크 업로드/다운로드 구현.
   - 진행 상황 추적 추가.

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