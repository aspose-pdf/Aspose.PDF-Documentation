---
title: تحويل المستندات باستخدام وظيفة Microsoft Azure
linktitle: تحويل المستندات باستخدام وظيفة Microsoft Azure
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ar/net/converting-documents-with-microsoft-azure-function/
description: تعلم كيفية تحويل مستندات PDF باستخدام وظائف Microsoft Azure مع Aspose.PDF for .NET، مما يتيح معالجة المستندات المستندة إلى السحابة.
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
    "abstract": "تتيح ميزة تحويل المستندات الجديدة المدعومة من Microsoft Azure للمستخدمين تحويل ملفات PDF بكفاءة إلى تنسيقات مختلفة مثل DOCX و HTML و JPEG باستخدام Aspose.PDF for .NET ووظائف Azure. تتيح هذه الوظيفة التكامل السلس مع موارد Azure، مما يضمن معالجة الملفات بسرعة وموثوقية مصممة للمطورين الذين يسعون لتعزيز تطبيقاتهم",
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
    "description": "يمكن لـ Aspose.PDF أداء المهام البسيطة والسلسة وكذلك التعامل مع الأهداف الأكثر تعقيدًا. تحقق من القسم التالي للمستخدمين المتقدمين والمطورين."
}
</script>

تقدم هذه المقالة تعليمات مفصلة خطوة بخطوة لتحويل مستندات PDF في Microsoft Azure باستخدام Aspose.PDF for .NET ووظيفة Azure.

## المتطلبات الأساسية

* Visual Studio 2022 Community Edition مع تثبيت تطوير Azure أو Visual Studio Code.
* حساب Azure: تحتاج إلى اشتراك Azure، أنشئ حسابًا مجانيًا قبل البدء.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## إنشاء موارد Azure

### إنشاء حساب تخزين

1. انتقل إلى بوابة Azure (https://portal.azure.com).
2. انقر على "إنشاء مورد".
3. ابحث عن "حساب التخزين".
4. انقر على "إنشاء".
5. املأ التفاصيل:
   - الاشتراك: اختر اشتراكك.
   - مجموعة الموارد: أنشئ جديدة أو اختر الموجودة.
   - اسم حساب التخزين: أدخل اسمًا فريدًا.
   - المنطقة: اختر أقرب منطقة.
   - الأداء: قياسي.
   - التكرار: LRS (تخزين متكرر محليًا).
6. انقر على "مراجعة + إنشاء".
7. انقر على "إنشاء".

### إنشاء حاوية

1. افتح حساب التخزين الخاص بك.
2. انتقل إلى "الحاويات" تحت "تخزين البيانات".
3. انقر على "+ حاوية".
4. سمها "pdfdocs".
5. اضبط مستوى الوصول العام على "خاص".
6. انقر على "إنشاء".

## إنشاء مشروع

### إنشاء مشروع Visual Studio

1. افتح Visual Studio 2022.
2. انقر على "إنشاء مشروع جديد".
3. اختر "وظائف Azure".
4. سم مشروعك "PdfConverterAzure".
5. اختر ".NET 6.0" أو أحدث و "HTTP trigger".
6. انقر على "إنشاء".

### إنشاء مشروع Visual Studio Code

#### تثبيت المتطلبات الأساسية

1. ملحقات Visual Code:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. تثبيت أدوات Azure Functions Core:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. تثبيت Azure CLI:
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

## تثبيت حزم NuGet المطلوبة

في Visual Studio، افتح وحدة تحكم إدارة الحزم وقم بتشغيل:
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

في Visual Studio Code، قم بتشغيل:
```bash
dotnet restore
```

## تكوين اتصال تخزين Azure

احصل على مفاتيح الوصول لحساب التخزين تحت مفاتيح الوصول في بوابة Azure. ستستخدم هذه المفاتيح لمصادقة تطبيقك.

1. افتح `local.settings.json`:
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

2. استبدل `YOUR_STORAGE_CONNECTION_STRING` بسلسلة اتصال التخزين الفعلية الخاصة بك من بوابة Azure.

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

## إنشاء الكود

أنشئ ملفًا جديدًا `PdfConverter.cs`:

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

أنشئ ملفًا جديدًا `ConvertPdfFunction.cs`:

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

## الاختبار محليًا

في Visual Studio:
1. ابدأ محاكي تخزين Azure.
2. قم بتشغيل المشروع في Visual Studio.
3. استخدم Postman أو curl للاختبار:

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

في Visual Studio Code:
1. ابدأ تطبيق الوظيفة:
```bash
func start
```

2. قم بتحميل PDF للاختبار:
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. استخدم Postman أو curl للاختبار:
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## النشر إلى Azure

في Visual Studio:
1. انقر بزر الماوس الأيمن على المشروع في Visual Studio.
2. اختر "نشر".
3. اختر "تطبيق وظيفة Azure".
4. اختر اشتراكك.
5. أنشئ تطبيق وظيفة جديد أو اختر الموجود.
6. انقر على "نشر".

في Visual Studio Code:
1. اضغط على F1 أو Ctrl+Shift+P.
2. اختر "وظائف Azure: نشر إلى تطبيق وظيفة".
3. اختر اشتراكك.
4. اختر تطبيق الوظيفة الذي تم إنشاؤه أعلاه.
5. انقر على "نشر".

## تكوين تطبيق وظيفة Azure

1. انتقل إلى بوابة Azure.
2. افتح تطبيق الوظيفة الخاص بك.
3. انتقل إلى "التكوين".
4. أضف إعدادات التطبيق:
   - المفتاح: "ContainerName".
   - القيمة: "pdfdocs".
5. احفظ التغييرات.

## اختبار الخدمة المنشورة

استخدم Postman أو curl للاختبار:
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## التنسيقات المدعومة

يمكن العثور على قائمة التنسيقات المدعومة [هنا](https://docs.aspose.com/pdf/net/supported-file-formats/).

## استكشاف الأخطاء وإصلاحها

### خيارات التكوين المهمة

1. إضافة المصادقة:
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

2. بالنسبة للملفات الكبيرة، ضع في اعتبارك:
   - زيادة مهلة الوظيفة.
   - استخدام خطة استهلاك مع مزيد من الذاكرة.
   - تنفيذ تحميل/تنزيل مجزأ.
   - إضافة تتبع التقدم.

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "العمل مع مستندات PDF باستخدام وظيفة Microsoft Azure",
    "alternativeHeadline": "استخدام وظيفة Microsoft Azure لمعالجة مستندات PDF",
    "author": {
        "@type": "Person",
        "name":"أنستاسيا هولوب",
        "givenName": "أنستاسيا",
        "familyName": "هولوب"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, c#, عمليات متقدمة في pdf, microsoft azure, وظيفة",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
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
    "description": "يمكن لـ Aspose.PDF for .NET معالجة المستندات باستخدام وظيفة Microsoft Azure."
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