---
title: Cara menjalankan Aspose.PDF for .NET 6 di Docker
linktitle: Menggunakan Aspose.PDF for .NET 6 di Docker
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/docker/dotnet6/
description: Mengintegrasikan fungsionalitas Aspose.PDF ke dalam aplikasi .NET 6 menggunakan kontainer Docker Linux atau Windows
lastmod: "2024-08-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to run Aspose.PDF for .NET 6 in Docker",
    "alternativeHeadline": "Run Aspose.PDF in .NET 6 with Docker Support",
    "abstract": "Fitur ini memungkinkan pengembang untuk mengintegrasikan fungsionalitas Aspose.PDF secara mulus ke dalam aplikasi .NET 6 yang memanfaatkan kontainer Docker Linux atau Windows. Fungsionalitas ini menyederhanakan proses pembuatan dokumen PDF langsung dari aplikasi ASP.NET Core, meningkatkan efisiensi manajemen dokumen di lingkungan berbasis cloud",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1067",
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
    "url": "/net/docker/dotnet6/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/docker/dotnet6/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Prasyarat

Contoh berikut diuji dengan:

* Docker v.20.10.11 dan Docker Desktop 4.3.2.
* Visual Studio 2022 Community Edition v.17.0.5.
* .NET 6 SDK digunakan dalam contoh yang diberikan di bawah ini.
* Aspose.PDF for .NET v.22.01.

## Buat aplikasi contoh untuk Kontainer Docker Linux

1. Luncurkan Visual Studio 2022 dan pilih template **ASP.NET Core Web App (Model-View-Controller)** dan tekan **Next**.
1. Di jendela **Konfigurasi proyek baru Anda**, atur nama dan lokasi proyek yang diinginkan dan tekan **Next**.
1. Di jendela **Informasi tambahan**, pilih **.NET 6.0 (Dukungan jangka panjang)** dan aktifkan dukungan Docker. Anda juga dapat mengatur **Docker OS** ke Linux jika diperlukan.
1. Tekan **Create**.
1. Pilih **Tools->Nuget Package Manager->Package Manager Console** dan instal **Aspose.PDF for .NET** (gunakan perintah `Install-Package Aspose.PDF`).

### Hasilkan dokumen PDF menggunakan ASP.NET Core Web App di kontainer Linux

Kami akan menggunakan kode dari **Contoh Kompleks** dalam aplikasi ini. Silakan ikuti [tautan ini](/pdf/id/net/complex-pdf-example/) untuk penjelasan yang lebih rinci.

1. Buat folder `images` di folder `wwwroot` dan letakkan gambar `logo.png`. Anda dapat mengunduh gambar ini dari [sini](/pdf/id/net/docker/logo.png).
1. Ganti kode di `HomeController.cs` dengan cuplikan berikut (harap dicatat bahwa Anda dapat memiliki namespace lain):

Cuplikan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

```cs
using Aspose.Pdf;
using Aspose.Pdf.Text;
using Docker.Linux.Demo01.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Docker.Linux.Demo01.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IWebHostEnvironment _appEnvironment;

        public HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment)
        {
            _logger = logger;
            _appEnvironment = appEnvironment;
        }

        public IActionResult Index()
        {
            return View();
        }
        
        public IActionResult Generate()
        {
            const string file_type = "application/pdf";
            const string file_name = "sample.pdf";
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Start");
            // Initialize document object
            using (var document = new Aspose.Pdf.Document())
            {
                // Add page
                var page = document.Pages.Add();

                // Add image
                var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
                page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

                // -------------------------------------------------------------
                // Add Header
                var header = new TextFragment("New ferry routes in Fall 2020");
                header.TextState.Font = FontRepository.FindFont("Arial");
                header.TextState.FontSize = 24;
                header.HorizontalAlignment = HorizontalAlignment.Center;
                header.Position = new Position(130, 720);
                page.Paragraphs.Add(header);

                // Add description
                var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
                var description = new TextFragment(descriptionText);
                description.TextState.Font = FontRepository.FindFont("Times New Roman");
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
            _logger.LogInformation("Finish");
            return File(memoryStream, file_type, file_name);
        }

        public IActionResult Privacy()
        {
            return View();
        }

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
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
RUN apt-get update && apt-get install -y libgdiplus
RUN sed -i'.bak' 's/$/ contrib/' /etc/apt/sources.list
RUN apt-get update; apt-get install -y ttf-mscorefonts-installer fontconfig

WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Docker.Linux.Demo01/Docker.Linux.Demo01.csproj", "Docker.Linux.Demo01/"]
RUN dotnet restore "Docker.Linux.Demo01/Docker.Linux.Demo01.csproj"
COPY . .
WORKDIR "/src/Docker.Linux.Demo01"
RUN dotnet build "Docker.Linux.Demo01.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Docker.Linux.Demo01.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.Linux.Demo01.dll"]
```

## Buat aplikasi contoh untuk Kontainer Docker Windows

1. Luncurkan Visual Studio 2022 dan pilih template **ASP.NET Core Web App (Model-View-Controller)** dan tekan **Next**.
1. Di jendela **Konfigurasi proyek baru Anda**, atur nama dan lokasi proyek yang diinginkan dan tekan **Next**.
1. Di jendela **Informasi tambahan**, pilih **.NET 6.0 (Dukungan jangka panjang)** dan aktifkan dukungan Docker. Jika diperlukan, Anda juga dapat mengatur **Docker OS** ke `Windows`.
1. Tekan **Create**.
1. Pilih **Tools->Nuget Package Manager->Package Manager Console** dan instal **Aspose.PDF for .NET** (gunakan perintah `Install-Package Aspose.PDF`).

### Hasilkan dokumen PDF menggunakan ASP.NET Core Web App di kontainer Windows

Kami akan menggunakan kode yang sama seperti di contoh sebelumnya.

1. Buat folder `images` di folder `wwwroot` dan letakkan gambar `logo.png`. Anda dapat mengunduh gambar ini dari [sini](/pdf/id/net/docker/logo.png).
1. Ganti kode di `HomeController.cs` dengan cuplikan di atas.

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0.101-nanoserver-ltsc2022 AS build
WORKDIR /src
COPY ["Docker.Windows.Demo01/Docker.Windows.Demo01.csproj", "Docker.Windows.Demo01/"]
RUN dotnet restore "Docker.Windows.Demo01/Docker.Windows.Demo01.csproj"
COPY . .
WORKDIR "/src/Docker.Windows.Demo01"
RUN dotnet build "Docker.Windows.Demo01.csproj" -c Release -o /app/build -r win-x64 --self-contained true

FROM build AS publish
RUN dotnet publish "Docker.Windows.Demo01.csproj" -c Release -o /app/publish -r win-x64 --self-contained true

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Docker.Windows.Demo01.dll"]
```