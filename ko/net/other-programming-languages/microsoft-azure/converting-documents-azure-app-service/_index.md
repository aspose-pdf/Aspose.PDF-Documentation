---
title: Microsoft Azure 앱 서비스로 문서 변환하기
linktitle: Microsoft Azure 앱 서비스로 문서 변환하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/converting-documents-with-microsoft-azure-app-service/
description: Microsoft Azure App Service와 Aspose.PDF for .NET를 사용하여 PDF 문서를 변환하는 방법을 알아보고 클라우드에서 문서 워크플로를 최적화하세요.
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
    "abstract": "Microsoft Azure App Service를 사용하여 PDF 파일을 DOCX, HTML, JPG 및 PNG를 포함한 다양한 형식으로 원활하게 변환할 수 있는 새로운 기능으로 문서 변환의 힘을 활용하세요. 이 기능은 Aspose.PDF for .NET를 활용하여 클라우드 애플리케이션 내에서 문서 변환을 처리하기 위한 강력하고 효율적인 솔루션을 제공합니다. 오늘 Azure 프로젝트에 이 변환 기능을 통합하여 워크플로를 향상시키세요.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

이 문서에서는 Microsoft Azure와 Aspose.PDF for .NET 및 Azure 앱 서비스를 사용하여 PDF 문서를 변환하는 단계별 지침을 제공합니다.

## 전제 조건

* Azure 개발이 설치된 Visual Studio 2022 Community Edition 또는 Visual Studio Code.
* Azure 계정: Azure 구독이 필요하며 시작하기 전에 무료 계정을 생성하세요.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## Azure 리소스 생성

### 앱 서비스 생성

1. Azure 포털로 이동합니다 (https://portal.azure.com).
2. 새 리소스 그룹을 생성합니다.
3. 새 앱 서비스를 생성합니다:
   - .NET 6 (LTS) 런타임을 선택합니다.
   - 적절한 가격 책정 계층을 선택합니다.
4. 로깅을 위한 Application Insights 리소스를 생성합니다.

## 프로젝트 생성

### Visual Studio 프로젝트 생성

1. Visual Studio 2022를 엽니다.
2. "새 프로젝트 만들기"를 클릭합니다.
3. "ASP.NET Core Web API"를 선택합니다.
4. 프로젝트 이름을 "PdfConversionService"로 지정합니다.
5. ".NET 6.0" 또는 이후 버전을 선택합니다.
6. "생성"을 클릭합니다.

### Visual Studio Code 프로젝트 생성

#### 전제 조건 설치

1. Visual Code 확장:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azureappservice
```

2. Azure CLI 설치:
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
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Aspose.PDF" Version="24.10.0" />
    <PackageReference Include="Microsoft.ApplicationInsights.AspNetCore" Version="2.22.0" />
    <PackageReference Include="Microsoft.Extensions.Logging.AzureAppServices" Version="8.0.10" />
  </ItemGroup>
</Project>
```

3. 구성 추가:
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

4. 프로젝트 구조 생성:
```bash
mkdir Controllers
touch Controllers/PdfController.cs
```

## 필요한 NuGet 패키지 설치

Visual Studio에서 패키지 관리자 콘솔을 열고 실행합니다:
```powershell
Install-Package Aspose.PDF
Install-Package Microsoft.ApplicationInsights.AspNetCore
Install-Package Microsoft.Extensions.Logging.AzureAppServices
```

Visual Studio Code에서 실행합니다:
```bash
dotnet restore
```

## Aspose 라이센스 구성

Visual Studio에서:

1. Aspose.PDF 라이센스 파일을 프로젝트에 복사합니다.
2. 라이센스 파일을 마우스 오른쪽 버튼으로 클릭하고 "속성"을 선택합니다.
3. "출력 디렉토리에 복사"를 "항상 복사"로 설정합니다.
4. Program.cs에 라이센스 초기화 코드를 추가합니다:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

### 코드 생성

Visual Studio에서:
1. Controllers 폴더를 마우스 오른쪽 버튼으로 클릭합니다.
2. 추가 → 새 항목 → API 컨트롤러 - 비어 있음.
3. 파일 이름을 "PdfController.cs"로 지정합니다.

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

## 애플리케이션 설정 구성

1. appsettings.json을 엽니다.
2. 구성 추가:
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
Azure 포털에서 실제 연결 문자열로 `Your-Connection-StringG`를 교체합니다.

## 로컬 테스트

Visual Studio에서:
1. F5를 눌러 애플리케이션을 실행합니다.
2. Swagger UI가 열립니다.
3. /api/pdf/convert 엔드포인트를 테스트합니다:
   - "Try it out"을 클릭합니다.
   - PDF 파일을 업로드합니다.
   - 출력 형식을 선택합니다.
   - 실행하고 변환을 확인합니다.

Visual Studio Code에서:
```bash
dotnet run

curl -X POST "https://localhost:5001/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## Azure에 배포

Visual Studio에서:
1. 프로젝트를 마우스 오른쪽 버튼으로 클릭합니다.
2. "게시"를 선택합니다.
3. 대상을 "Azure"로 선택합니다.
4. "Azure App Service (Windows)"를 선택합니다.
5. 구독 및 앱 서비스를 선택합니다.
6. "게시"를 클릭합니다.

Visual Studio Code에서:
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

## Azure 앱 서비스 구성

1. Azure 포털로 이동합니다.
2. 앱 서비스를 엽니다.
3. 설정을 구성합니다:
   ```
   App Settings:
   - WEBSITE_RUN_FROM_PACKAGE=1
   - ASPNETCORE_ENVIRONMENT=Production
   ```

## 배포된 서비스 테스트

Postman 또는 curl을 사용하여 테스트합니다:
```bash
curl -X POST "https://your-app.azurewebsites.net/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## 지원되는 형식

지원되는 형식 목록은 [여기](https://docs.aspose.com/pdf/net/supported-file-formats/)에서 확인할 수 있습니다.

## 문제 해결

### 중요한 구성 옵션

1. **파일 크기 제한**
web.config에 추가합니다:
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

2. **CORS** (필요한 경우)
Program.cs에서:
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

3. **인증** (필요한 경우)
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
    "headline": "Microsoft Azure 앱 서비스를 사용한 PDF 문서 작업",
    "alternativeHeadline": "PDF 문서 처리를 위한 Microsoft Azure 앱 서비스 사용",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, pdf의 고급 작업, microsoft azure, 앱 서비스",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
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
    "description": "Aspose.PDF for .NET는 Microsoft Azure 앱 서비스를 사용하여 문서를 처리할 수 있습니다."
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