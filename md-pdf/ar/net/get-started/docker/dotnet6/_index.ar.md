---
title: كيفية تشغيل Aspose.PDF لـ .NET 6 في Docker
linktitle: استخدام Aspose.PDF لـ .NET 6 في Docker
type: docs
weight: 10
url: /net/docker/dotnet6/
description: دمج وظائف Aspose.PDF في تطبيقك باستخدام حاويات Docker لنظامي Linux أو Windows
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## متطلبات مسبقة

الأمثلة التالية تم اختبارها مع:

* Docker v.20.10.11 و Docker Desktop 4.3.2
* Visual Studio 2022 Community Edition v.17.0.5
* يستخدم .NET 6 SDK في المثال المقدم أدناه.
* Aspose.PDF لـ .NET v.22.01

## إنشاء تطبيق نموذجي لحاوية Docker Linux

1. قم بتشغيل Visual Studio 2022 واختر قالب **ASP.NET Core Web App (Model-View-Controller)** واضغط **التالي**
1. في نافذة **تكوين مشروعك الجديد** حدد اسم المشروع والموقع المطلوب واضغط **التالي**
1. في نافذة **معلومات إضافية** اختر **.NET 6.0 (الدعم طويل المدى)** وفعل دعم Docker. يمكنك أيضًا تعيين **نظام تشغيل Docker** إلى Linux إذا لزم الأمر.
1.
1. اختر **الأدوات -> مدير حزم Nuget -> وحدة تحكم مدير الحزم** وقم بتثبيت **Aspose.PDF لـ.NET** (استخدم الأمر `Install-Package Aspose.PDF`)

### إنشاء مستند PDF باستخدام تطبيق ويب ASP.NET Core في حاوية Linux

سنستخدم الكود من **مثال معقد** في هذا التطبيق. يرجى اتباع [هذا الرابط](/pdf/net/complex-pdf-example/) للحصول على شرح أكثر تفصيلاً.

1. قم بإنشاء مجلد `images` في مجلد `wwwroot` وضع الصورة `logo.png`. يمكنك تحميل هذه الصورة من [هنا](/pdf/net/docker/logo.png)
1. استبدل الكود في `HomeController.cs` بالشفرة التالية (يرجى ملاحظة أنه يمكن أن يكون لديك مساحة أسماء أخرى):

هذه الشفرة تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

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
            var memoryStream = new System.IO.MemoryStream();

            _logger.LogInformation("ابدأ");
            // تهيئة كائن المستند
            var document = new Document();
            // إضافة صفحة
            var page = document.Pages.Add();

            // إضافة صورة
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // إضافة العنوان
            var header = new TextFragment("مسارات العبارات الجديدة في خريف 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // إضافة الوصف
            var descriptionText = "يجب على الزوار شراء التذاكر عبر الإنترنت والتذاكر محدودة بـ 5000 في اليوم. تعمل خدمة العبارة بنصف طاقتها وبجدول مخفض. توقع وجود طوابير.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // إضافة جدول
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
            headerRow.Cells.Add("مدينة المغادرة");
            headerRow.Cells.Add("جزيرة المغادرة");
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
            _logger.LogInformation("إنهاء");
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
1. استبدل المحتوى في `Dockerfile` بالمحتوى التالي:

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

## إنشاء تطبيق عينة لحاوية Docker Windows

1.
1.
1. في نافذة **تكوين مشروعك الجديد** حدد اسم المشروع والموقع المطلوبين ثم اضغط **التالي**
1. في نافذة **معلومات إضافية** اختر **.NET 6.0 (الدعم طويل الأجل)** وفعّل دعم Docker. إذا لزم الأمر، يمكنك أيضاً تعيين **نظام تشغيل Docker** إلى `Windows`.
1. اضغط **إنشاء**
1. اختر **أدوات->مدير حزم Nuget->وحدة تحكم مدير الحزم** وقم بتثبيت **Aspose.PDF لـ.NET** (استخدم الأمر `Install-Package Aspose.PDF`)

### توليد مستند PDF باستخدام تطبيق ويب ASP.NET Core في حاوية Windows

سنستخدم نفس الكود كما في المثال السابق.

1. أنشئ مجلد `images` في مجلد `wwwroot` وضع الصورة `logo.png`. يمكنك تحميل هذه الصورة من [هنا](/pdf/net/docker/logo.png)
1. استبدل الكود في `HomeController.cs` بالجزء العلوي.

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0.101-nanoserver-ltsc2022 AS build
WORKDIR /src
COPY ["Docker.Windows.Demo01/Docker.Windows.Demo01.csproj", "Docker.Windows.Demo01/"]
RUN dotnet restore "Docker.Windows.Demo01.Docker.Windows.Demo01.csproj"
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

