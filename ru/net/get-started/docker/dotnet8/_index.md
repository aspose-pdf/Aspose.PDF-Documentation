---
title: Как запустить Aspose.PDF for .NET 8 в Docker
linktitle: Использование Aspose.PDF for .NET 8 в Docker
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/docker/dotnet8/
description: Интеграция функциональности Aspose.PDF в приложение .NET 8 с использованием контейнеров Docker Linux или Windows
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
    "abstract": "Узнайте, как легко интегрировать Aspose.PDF для .NET 8 в свои приложения с помощью Docker, будь то контейнеры Linux или Windows. Эта функция позволяет эффективно создавать и редактировать PDF-документы в приложениях ASP.NET Core, позволяя разработчикам использовать мощные возможности работы с PDF в контейнерной среде. Оптимизируйте свои .NET-проекты, используя это простое руководство по настройке, и улучшите рабочий процесс разработки с помощью надёжных функций Aspose.PDF для .NET",
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
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Необходимые условия

Следующие примеры протестированы с:

* Docker версии 25.0.2 и Docker Desktop версии 4.27.1.
* Visual Studio 2022 Community Edition версии 17.0.5.
* В приведённом ниже примере используется .NET SDK версии 8.
* Aspose.PDF.Drawing версии 24.01.

## Создание примера приложения для контейнера Docker Linux

1. Запустите Visual Studio 2022 и выберите шаблон **ASP.NET Core Web App (Model-View-Controller)** и нажмите **Далее**.
1. В окне **Настройка нового проекта** задайте желаемое имя и расположение проекта и нажмите **Далее**.
1. В окне **Дополнительная информация** выберите **.NET 6.0 (Долгосрочная поддержка)** и включите поддержку Docker. Вы также можете установить **Docker OS** на Linux, если это необходимо.
1. Нажмите **Создать**.
1. Выберите **Инструменты->Диспетчер пакетов Nuget->Консоль диспетчера пакетов** и установите **Aspose.PDF for .NET** (используйте команду `Install-Package Aspose.PDF`).

### Создание PDF-документа с помощью веб-приложения ASP.NET Core в Linux-контейнере

В этом приложении мы будем использовать код из **Сложного примера**. Для более подробного объяснения перейдите по [этой ссылке](/pdf/ru/net/complex-pdf-example/).

1. Создайте папку `images` в папке `wwwroot` и поместите изображение `logo.png`. Вы можете скачать это изображение [здесь](/pdf/ru/net/docker/logo.png).
1. Создайте папку `fonts` в папке `wwwroot` и поместите туда шрифты [Roboto](https://fonts.google.com/specimen/Roboto).
1. Создайте папку `samples` в папке `wwwroot` и поместите в неё образцы данных.
1. Замените код в `HomeController.cs` следующим фрагментом (обратите внимание, что у вас может быть другое пространство имён):

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

1. Замените содержимое в `Dockerfile` следующим содержимым:

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