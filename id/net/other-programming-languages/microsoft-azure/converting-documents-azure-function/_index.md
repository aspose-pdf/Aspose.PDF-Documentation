---
title: Mengonversi Dokumen dengan Microsoft Azure function
linktitle: Mengonversi Dokumen dengan Microsoft Azure function
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/converting-documents-with-microsoft-azure-function/
description: Pelajari cara mengonversi dokumen PDF menggunakan Microsoft Azure Functions dengan Aspose.PDF for .NET, memungkinkan pemrosesan dokumen berbasis cloud.
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
    "abstract": "Fitur konversi dokumen baru yang didukung oleh Microsoft Azure memungkinkan pengguna untuk secara efisien mengubah file PDF ke berbagai format seperti DOCX, HTML, dan JPEG menggunakan Aspose.PDF for .NET dan Azure Functions. Fungsionalitas ini memungkinkan integrasi yang mulus dengan sumber daya Azure, memastikan pemrosesan file yang cepat dan dapat diandalkan yang disesuaikan untuk pengembang yang ingin meningkatkan aplikasi mereka.",
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
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

Artikel ini memberikan instruksi langkah demi langkah yang terperinci untuk mengonversi dokumen PDF di Microsoft Azure menggunakan Aspose.PDF for .NET dan fungsi Azure.

## Prasyarat

* Visual Studio 2022 Community Edition dengan pengembangan Azure yang terinstal atau Visual Studio Code.
* Akun Azure: Anda memerlukan langganan Azure, buat akun gratis sebelum memulai.
* .NET 6 SDK.
* Aspose.PDF for .NET.

## Buat Sumber Daya Azure

### Buat Akun Penyimpanan

1. Buka Azure Portal (https://portal.azure.com).
2. Klik "Buat sumber daya".
3. Cari "Akun penyimpanan".
4. Klik "Buat".
5. Isi detailnya:
   - Langganan: Pilih langganan Anda.
   - Grup sumber daya: Buat baru atau pilih yang sudah ada.
   - Nama akun penyimpanan: Masukkan nama yang unik.
   - Wilayah: Pilih wilayah terdekat.
   - Kinerja: Standar.
   - Redundansi: LRS (Penyimpanan redundan lokal).
6. Klik "Tinjau + buat".
7. Klik "Buat".

### Buat Kontainer

1. Buka akun penyimpanan Anda.
2. Pergi ke "Kontainer" di bawah "Penyimpanan data".
3. Klik "+ Kontainer".
4. Namai "pdfdocs".
5. Atur tingkat akses publik ke "Pribadi".
6. Klik "Buat".

## Buat Proyek

### Buat Proyek Visual Studio

1. Buka Visual Studio 2022.
2. Klik "Buat proyek baru".
3. Pilih "Azure Functions".
4. Namai proyek Anda "PdfConverterAzure".
5. Pilih ".NET 6.0" atau lebih baru dan "Pemicu HTTP".
6. Klik "Buat".

### Buat Proyek Visual Studio Code

#### Instal Prasyarat

1. Ekstensi Visual Code:
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. Instal Azure Functions Core Tools:
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Instal Azure CLI:
- Windows: Unduh dari situs web Microsoft.
- macOS: `brew install azure-cli`.
- Linux: `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.

#### Konfigurasi Proyek

1. Buka proyek di Visual Studio Code:
```bash
code .
```

2. Tambahkan paket NuGet dengan membuat/memperbarui `PdfConverterApp.csproj`:
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

## Instal Paket NuGet yang Diperlukan

Di Visual Studio buka Package Manager Console dan jalankan:
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

Di Visual Studio Code jalankan:
```bash
dotnet restore
```

## Konfigurasi Koneksi Penyimpanan Azure

Dapatkan Kunci Akses untuk akun penyimpanan di bawah Kunci akses di Azure Portal. Kunci ini akan digunakan untuk mengautentikasi aplikasi Anda.

1. Buka `local.settings.json`:
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

2. Ganti `YOUR_STORAGE_CONNECTION_STRING` dengan string koneksi penyimpanan Anda yang sebenarnya dari Azure Portal.

## Konfigurasi Lisensi Aspose

Di Visual Studio:

1. Salin file lisensi Aspose.PDF Anda ke proyek.
2. Klik kanan pada file lisensi, dan pilih "Properti".
3. Atur "Salin ke Direktori Output" ke "Salin selalu".
4. Tambahkan kode inisialisasi lisensi di Program.cs:
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

## Buat kode

Buat file baru `PdfConverter.cs`:

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

Buat file baru `ConvertPdfFunction.cs`:

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

## Uji Secara Lokal

Di Visual Studio:
1. Mulai Emulator Penyimpanan Azure.
2. Jalankan proyek di Visual Studio.
3. Gunakan Postman atau curl untuk menguji:

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

Di Visual Studio Code:
1. Mulai aplikasi fungsi:
```bash
func start
```

2. Unggah PDF untuk diuji:
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. Gunakan Postman atau curl untuk menguji:
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Deploy ke Azure

Di Visual Studio:
1. Klik kanan proyek di Visual Studio.
2. Pilih "Publikasikan".
3. Pilih "Azure Function App".
4. Pilih langganan Anda.
5. Buat baru atau pilih Function App yang ada.
6. Klik "Publikasikan".

Di Visual Studio Code:
1. Tekan F1 atau Ctrl+Shift+P.
2. Pilih "Azure Functions: Deploy to Function App".
3. Pilih langganan Anda.
4. Pilih function app yang dibuat di atas.
5. Klik "Deploy".

## Konfigurasi Azure Function App

1. Buka Azure Portal.
2. Buka Function App Anda.
3. Pergi ke "Konfigurasi".
4. Tambahkan pengaturan aplikasi:
   - Kunci: "ContainerName".
   - Nilai: "pdfdocs".
5. Simpan perubahan.

## Uji Layanan yang Diterapkan

Gunakan Postman atau curl untuk menguji:
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Format yang Didukung

Daftar format yang didukung dapat ditemukan [di sini](https://docs.aspose.com/pdf/net/supported-file-formats/).

## Pemecahan Masalah

### Opsi Konfigurasi Penting

1. Tambahkan otentikasi:
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

2. Untuk file besar, pertimbangkan:
   - Meningkatkan waktu tunggu fungsi.
   - Menggunakan rencana konsumsi dengan lebih banyak memori.
   - Mengimplementasikan unggah/unduh terchunk.
   - Menambahkan pelacakan kemajuan.

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