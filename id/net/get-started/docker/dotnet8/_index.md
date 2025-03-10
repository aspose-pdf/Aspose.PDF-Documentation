---
title: Cara menjalankan Aspose.PDF for .NET 8 di Docker
linktitle: Menggunakan Aspose.PDF for .NET 8 di Docker
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/docker/dotnet8/
description: Mengintegrasikan fungsionalitas Aspose.PDF ke dalam aplikasi .NET 8 menggunakan kontainer Docker Linux atau Windows
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to run Aspose.PDF for .NET 8 in Docker",
    "alternativeHeadline": "Integrate Aspose.PDF with .NET 8 in Docker",
    "abstract": "Temukan cara untuk mengintegrasikan Aspose.PDF for .NET 8 ke dalam aplikasi Anda menggunakan Docker, baik di kontainer Linux atau Windows. Fitur ini memungkinkan pembuatan dan manipulasi dokumen PDF yang efisien dalam aplikasi ASP.NET Core, memungkinkan pengembang memanfaatkan kemampuan PDF yang kuat dalam lingkungan terkontainer. Optimalkan proyek .NET Anda dengan menggunakan panduan pengaturan yang sederhana ini dan tingkatkan alur kerja pengembangan Anda dengan fungsionalitas kuat Aspose.PDF for .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1045",
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
    "url": "/net/docker/dotnet8/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/docker/dotnet8/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Prasyarat

Contoh berikut diuji dengan:

* Docker v.25.0.2 dan Docker Desktop 4.27.1.
* Visual Studio 2022 Community Edition v.17.0.5.
* .NET 8 SDK digunakan dalam contoh yang diberikan di bawah.
* Aspose.PDF.Drawing v.24.01.

## Buat aplikasi contoh untuk Kontainer Docker Linux

1. Luncurkan Visual Studio 2022 dan pilih template **ASP.NET Core Web App (Model-View-Controller)** dan tekan **Next**.
1. Di jendela **Konfigurasi proyek baru Anda**, atur nama proyek dan lokasi yang diinginkan dan tekan **Next**.
1. Di jendela **Informasi tambahan**, pilih **.NET 6.0 (Dukungan jangka panjang)** dan aktifkan dukungan Docker. Anda juga dapat mengatur **Docker OS** ke Linux jika diperlukan.
1. Tekan **Create**.
1. Pilih **Tools->Nuget Package Manager->Package Manager Console** dan instal **Aspose.PDF for .NET** (gunakan perintah `Install-Package Aspose.PDF`).

### Hasilkan dokumen PDF menggunakan Aplikasi Web ASP.NET Core di kontainer Linux

Kami akan menggunakan kode dari **Contoh Kompleks** dalam aplikasi ini. Silakan ikuti [tautan ini](/pdf/net/complex-pdf-example/) untuk penjelasan yang lebih rinci.

1. Buat folder `images` di folder `wwwroot` dan letakkan gambar `logo.png`. Anda dapat mengunduh gambar ini dari [sini](/pdf/net/docker/logo.png).
1. Buat folder `fonts` di folder `wwwroot` dan letakkan font [Roboto](https://fonts.google.com/specimen/Roboto) di sana.
1. Buat folder `samples` di folder `wwwroot` dan letakkan data contoh di sana.
1. Ganti kode di `HomeController.cs` dengan cuplikan berikut (harap dicatat bahwa Anda dapat memiliki namespace lain):

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
    // Represents a controller for the home page and PDF generation in a Linux demo application.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // Displays the index view.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // Generates a PDF document and returns it as a file.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("PDF Generation: Start ");
            // Create PDF document
            using (var document = new Aspose.Pdf.Document())
            {
                // Add page
                var page = document.Pages.Add();

                // Add image
                var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
                page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

                // Add Header
                var header = new TextFragment("New ferry routes in Fall 2020");
                header.TextState.Font = FontRepository.FindFont("Roboto");
                header.TextState.FontSize = 24;
                header.HorizontalAlignment = HorizontalAlignment.Center;
                header.Position = new Position(130, 720);
                page.Paragraphs.Add(header);

                // Add description
                var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
                var description = new TextFragment(descriptionText);
                description.TextState.Font = FontRepository.FindFont("Helvetica");
                description.TextState.FontSize = 14;
                description.HorizontalAlignment = HorizontalAlignment.Left;
                page.Paragraphs.Add(description);

                // Add table
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
                headerRow.Cells.Add("Departs City");
                headerRow.Cells.Add("Departs Island");
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
            }
            _logger.LogInformation("PDF Generation: Finish");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Converts a file to a different format based on the provided id.
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
        // Converts a PDF file to JPEG format and returns it as a file.
        // </summary>
        private FileStreamResult ConvertPdfToJpeg()
        {
            const string fileType = "image/jpeg";
            const string fileName = "sample.jpeg";

            var memoryStream = new MemoryStream();
            var pdfFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.pdf");

            // Open PDF document
            using (var document = new Aspose.Pdf.Document(pdfFileName))
            {
                var resolution = new Resolution(300);
                var renderer = new JpegDevice(resolution, 90);
                renderer.Process(document.Pages[1], memoryStream);
                memoryStream.Seek(0, SeekOrigin.Begin);
                return File(memoryStream, fileType, fileName);
            }
        }

        // <summary>
        // Converts an XPS file to PDF format and returns it as a file.
        // </summary>
        private FileStreamResult ConvertXpsToPdf()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";

            var memoryStream = new MemoryStream();
            var xpsFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.oxps");

            // Open XPS document
            using (var document = new Aspose.Pdf.Document(xpsFileName, new Aspose.Pdf.XpsLoadOptions()))
            {
                document.Save(memoryStream);
            }

            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Displays the privacy view.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // Displays the error view.
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```

1. Ganti konten di `Dockerfile` dengan konten berikut:

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