---
title: كيفية تشغيل Aspose.PDF في Docker
linktitle: استخدام Docker
type: docs
weight: 20
url: /net/docker/dotnet8/
description: دمج وظائف Aspose.PDF في تطبيقك باستخدام حاويات لينكس Docker
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## المتطلبات الأساسية

الأمثلة التالية تم اختبارها مع:

* Docker v.25.0.2 و Docker Desktop 4.27.1
* Visual Studio 2022 Community Edition v.17.0.5
* يستخدم .NET 8 SDK في المثال المقدم أدناه.
* Aspose.PDF.Drawing v.24.01

## إنشاء تطبيق نموذجي لحاوية لينكس Docker

1. قم بتشغيل Visual Studio 2022 واختر قالب **ASP.NET Core Web App (Model-View-Controller)** واضغط على **التالي**
1. في نافذة **تكوين مشروعك الجديد** حدد اسم المشروع والموقع المطلوبين واضغط على **التالي**
1. في نافذة **معلومات إضافية** اختر **.NET 6.0 (الدعم طويل الأمد)** وفعّل دعم Docker. يمكنك أيضًا تحديد **نظام تشغيل Docker** إلى لينكس إذا لزم الأمر.
1. اضغط على **إنشاء**
1.
### إنشاء مستند PDF باستخدام تطبيق ويب ASP.NET Core في حاوية لينكس

سنستخدم الكود من **المثال المعقد** في هذا التطبيق. يرجى اتباع [هذا الرابط](/pdf/net/complex-pdf-example/) للحصول على شرح أكثر تفصيلاً.

1. قم بإنشاء مجلد `images` في مجلد `wwwroot` وضع صورة `logo.png`. يمكنك تحميل هذه الصورة من [هنا](/pdf/net/docker/logo.png)
1. قم بإنشاء مجلد `fonts` في مجلد `wwwroot` وضع خطوط [Roboto](https://fonts.google.com/specimen/Roboto) هناك.
1. قم بإنشاء مجلد `samples` في مجلد `wwwroot` وضع بيانات العينة هناك.
1. استبدل الكود في `HomeController.cs` بالجزء التالي (يرجى ملاحظة أن لديك مساحة اسم أخرى):

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
    // يمثل متحكم للصفحة الرئيسية وإنشاء مستند PDF في تطبيق تجريبي لينكس.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // يعرض عرض الفهرس.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // ينشئ مستند PDF ويعيده كملف.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("PDF Generation: Start ");
            // Initialize document object
            var document = new Document();
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
            _logger.LogInformation("PDF Generation: Finish");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // يحول ملف إلى تنسيق مختلف بناءً على المعرف المقدم.
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
        // يحول ملف PDF إلى تنسيق JPEG ويعيده كملف.
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
        // يحول ملف XPS إلى تنسيق PDF ويعيده كملف.
        // </summary>
        private FileStreamResult ConvertXpsToPdf()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";

            var memoryStream = a MemoryStream();
            var xpsFileName = Path.Combine(_appEnvironment.WebRootPath, "samples", "samples-new.oxps");

            var document = new Document(xpsFileName, new XpsLoadOptions());
            document.Save(memoryStream);

            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // يعرض عرض الخصوصية.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // يعرض عرض الخطأ.
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```
1. استبدل المحتوى في `Dockerfile` بالمحتوى التالي:

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

