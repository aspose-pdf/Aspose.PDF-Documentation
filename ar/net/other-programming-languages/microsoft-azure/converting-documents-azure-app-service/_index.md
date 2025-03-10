---
title: تحويل المستندات باستخدام خدمة تطبيقات Microsoft Azure
linktitle: تحويل المستندات باستخدام خدمة تطبيقات Microsoft Azure
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ar/net/converting-documents-with-microsoft-azure-app-service/
description: اكتشف كيفية تحويل مستندات PDF باستخدام خدمة تطبيقات Microsoft Azure وAspose.PDF for .NET، مما يحسن سير العمل للمستندات في السحابة.
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
    "abstract": "افتح قوة تحويل المستندات مع الميزة الجديدة التي تسمح للمستخدمين بتحويل ملفات PDF بسلاسة إلى تنسيقات مختلفة، بما في ذلك DOCX وHTML وJPG وPNG، باستخدام خدمة تطبيقات Microsoft Azure. تستفيد هذه الميزة من Aspose.PDF for .NET، مما يوفر حلاً قويًا وفعالًا للتعامل مع تحويلات المستندات داخل التطبيقات السحابية. حسّن سير العمل الخاص بك من خلال دمج هذه القدرة على التحويل في مشاريع Azure الخاصة بك اليوم.",
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
    "description": "يمكن لـ Aspose.PDF تنفيذ المهام البسيطة والسريعة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تقدم هذه المقالة تعليمات مفصلة خطوة بخطوة لتحويل مستندات PDF في Microsoft Azure باستخدام Aspose.PDF for .NET وخدمة تطبيقات Azure.

## المتطلبات الأساسية

* Visual Studio 2022 Community Edition مع تثبيت تطوير Azure أو Visual Studio Code.
* حساب Azure: تحتاج إلى اشتراك Azure، أنشئ حسابًا مجانيًا قبل البدء.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## إنشاء موارد Azure

### إنشاء خدمة تطبيقات

1. انتقل إلى بوابة Azure (https://portal.azure.com).
2. أنشئ مجموعة موارد جديدة.
3. أنشئ خدمة تطبيقات جديدة:
   - اختر وقت تشغيل .NET 6 (LTS).
   - اختر مستوى التسعير المناسب.
4. أنشئ مورد Application Insights للتسجيل.

## إنشاء مشروع

### إنشاء مشروع في Visual Studio

1. افتح Visual Studio 2022.
2. انقر على "إنشاء مشروع جديد".
3. اختر "ASP.NET Core Web API".
4. سمِّ مشروعك "PdfConversionService".
5. اختر ".NET 6.0" أو أحدث.
6. انقر على "إنشاء".

### إنشاء مشروع في Visual Studio Code

#### تثبيت المتطلبات الأساسية

1. ملحقات Visual Code:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azureappservice
```

2. تثبيت Azure CLI:
- Windows: قم بالتنزيل من موقع Microsoft.
- macOS: `brew install azure-cli`.
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.

#### تكوين المشروع

1. افتح المشروع في Visual Studio Code:
```bash
code .
```

2. أضف حزم NuGet عن طريق إنشاء/تحديث `PdfConverterApp.csproj`:
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

3. أضف التكوين:
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

4. أنشئ هيكل المشروع:
```bash
mkdir Controllers
touch Controllers/PdfController.cs
```

## تثبيت حزم NuGet المطلوبة

في Visual Studio، افتح وحدة تحكم إدارة الحزم وقم بتشغيل:
```powershell
Install-Package Aspose.PDF
Install-Package Microsoft.ApplicationInsights.AspNetCore
Install-Package Microsoft.Extensions.Logging.AzureAppServices
```

في Visual Studio Code، قم بتشغيل:
```bash
dotnet restore
```

## تكوين ترخيص Aspose

في Visual Studio:

1. انسخ ملف ترخيص Aspose.PDF إلى المشروع.
2. انقر بزر الماوس الأيمن على ملف الترخيص، واختر "خصائص".
3. اضبط "نسخ إلى دليل الإخراج" على "نسخ دائمًا".
4. أضف كود تهيئة الترخيص في Program.cs:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

### إنشاء الكود

في Visual Studio:
1. انقر بزر الماوس الأيمن على مجلد Controllers.
2. أضف → عنصر جديد → وحدة تحكم API - فارغة.
3. سمِّ ملفك "PdfController.cs".

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

## تكوين إعدادات التطبيق

1. افتح appsettings.json.
2. أضف التكوين:
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
استبدل `Your-Connection-StringG` بسلسلة الاتصال الفعلية الخاصة بك من بوابة Azure.

## اختبار محليًا

في Visual Studio:
1. اضغط على F5 لتشغيل التطبيق.
2. ستفتح واجهة Swagger.
3. اختبر نقطة النهاية /api/pdf/convert:
   - انقر على "جربها".
   - قم بتحميل ملف PDF.
   - اختر تنسيق الإخراج.
   - نفذ وتحقق من التحويل.

في Visual Studio Code:
```bash
dotnet run

curl -X POST "https://localhost:5001/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## نشر إلى Azure

في Visual Studio:
1. انقر بزر الماوس الأيمن على المشروع.
2. اختر "نشر".
3. اختر "Azure" كهدف.
4. اختر "خدمة تطبيقات Azure (Windows)".
5. اختر اشتراكك وخدمة التطبيقات.
6. انقر على "نشر".

في Visual Studio Code:
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

## تكوين خدمة تطبيقات Azure

1. انتقل إلى بوابة Azure.
2. افتح خدمة التطبيقات الخاصة بك.
3. قم بتكوين الإعدادات:
   ```
   App Settings:
   - WEBSITE_RUN_FROM_PACKAGE=1
   - ASPNETCORE_ENVIRONMENT=Production
   ```

## اختبار الخدمة المنشورة

استخدم Postman أو curl للاختبار:
```bash
curl -X POST "https://your-app.azurewebsites.net/api/pdf/convert?outputFormat=docx" \
     -F "file=@sample.pdf" \
     -o converted.docx
```

## التنسيقات المدعومة

يمكن العثور على قائمة بالتنسيقات المدعومة [هنا](https://docs.aspose.com/pdf/net/supported-file-formats/).

## استكشاف الأخطاء وإصلاحها

### خيارات التكوين المهمة

1. **حدود حجم الملف**
أضف إلى web.config:
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

2. **CORS** (إذا لزم الأمر)
في Program.cs:
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

3. **المصادقة** (إذا لزم الأمر)
```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options => {
        // Configure JWT options
    });
```

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