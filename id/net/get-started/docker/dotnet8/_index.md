---
title: Cara Menjalankan Aspose.PDF di Docker
linktitle: Menggunakan Docker
type: docs
weight: 20
url: /id/net/docker/dotnet8/
description: Mengintegrasikan fungsionalitas Aspose.PDF ke dalam aplikasi Anda menggunakan kontainer Linux Docker
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Prasyarat

Contoh berikut diuji dengan:

* Docker v.25.0.2 dan Docker Desktop 4.27.1
* Visual Studio 2022 Community Edition v.17.0.5
* .NET 8 SDK digunakan dalam contoh yang diberikan di bawah ini.
* Aspose.PDF.Drawing v.24.01

## Membuat aplikasi contoh untuk Kontainer Linux Docker

1. Jalankan Visual Studio 2022 dan pilih template **ASP.NET Core Web App (Model-View-Controller)** kemudian tekan **Next**
1. Di jendela **Configure your new project** atur nama proyek yang diinginkan dan lokasi kemudian tekan **Next**
1. Di jendela **Additional information** pilih **.NET 6.0 (Dukungan jangka panjang)** dan aktifkan dukungan Docker. Anda juga dapat mengatur **Docker OS** ke Linux jika diperlukan.
1. Tekan **Create**
1.
### Membuat dokumen PDF menggunakan Aplikasi Web ASP.NET Core di kontainer Linux

Kami akan menggunakan kode dari **Contoh Kompleks** dalam aplikasi ini. Silakan ikuti [tautan ini](/pdf/id/net/complex-pdf-example/) untuk penjelasan lebih rinci.

1. Buat folder `images` di folder `wwwroot` dan letakkan gambar `logo.png`. Anda dapat mengunduh gambar ini dari [sini](/pdf/id/net/docker/logo.png)
1. Buat folder `fonts` di folder `wwwroot` dan letakkan font [Roboto](https://fonts.google.com/specimen/Roboto) di sana.
1. Buat folder `samples` di folder `wwwroot` dan letakkan data sampel di sana.
1. Ganti kode di `HomeController.cs` dengan potongan kode berikut (perhatikan bahwa Anda mungkin memiliki namespace lain):

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
    // Mewakili controller untuk halaman utama dan pembuatan PDF dalam aplikasi demo Linux.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // Menampilkan tampilan indeks.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // Membuat dokumen PDF dan mengembalikannya sebagai file.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Pembuatan PDF: Mulai ");
            // Inisialisasi objek dokumen
            var document = new Document();
            // Tambahkan halaman
            var page = document.Pages.Add();

            // Tambahkan gambar
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // Tambahkan Header
            var header = new TextFragment("Rute ferry baru pada Musim Gugur 2020");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Tambahkan deskripsi
            var descriptionText = "Pengunjung harus membeli tiket secara online dan tiket terbatas untuk 5,000 per hari. Layanan ferry beroperasi setengah kapasitas dan dengan jadwal yang dikurangi. Harapkan antrian.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Tambahkan tabel
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
            headerRow.Cells.Add("Berangkat Kota");
            headerRow.Cells.Add("Berangkat Pulau");
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
            _logger.LogInformation("Pembuatan PDF: Selesai");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Mengonversi file ke format berbeda berdasarkan id yang diberikan.
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
        // Mengonversi file PDF ke format JPEG dan mengembalikannya sebagai file.
        // </summary>
        private FileStreamResult ConvertPdfToJpeg()
        {
            const string fileType = "image/jpeg";
            const string fileName = "sample.jpeg";

            var memoryStream = new MemoryStream();
            var pdfFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.pdf");

            var document = new Document(pdfFileName);
            var resolution = new Resolution(300);
            var renderer = new JpegDevice(resolution, 90);
            renderer.Process(document.Pages[1], memoryStream);
            memoryStream.Seek(0, SeekOrigin.Begin);
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Mengonversi file XPS ke format PDF dan mengembalikannya sebagai file.
        // </summary>
        private FileStreamResult ConvertXpsToPdf()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";

            var memoryStream = new MemoryStream();
            var xpsFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.oxps");

            var document = new Document(xpsFileName, new XpsLoadOptions());
            document.Save(memoryStream);

            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Menampilkan tampilan privasi.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // Menampilkan tampilan kesalahan.
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

