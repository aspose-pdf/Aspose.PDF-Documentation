---
title: Как запустить Aspose.PDF в Docker
linktitle: Использование Docker
type: docs
weight: 20
url: /ru/net/docker/dotnet8/
description: Интеграция функционала Aspose.PDF в ваше приложение с использованием контейнеров Linux Docker
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Предварительные требования

Следующие примеры были протестированы с:

* Docker v.25.0.2 и Docker Desktop 4.27.1
* Visual Studio 2022 Community Edition v.17.0.5
* В приведенном ниже примере используется .NET 8 SDK.
* Aspose.PDF.Drawing v.24.01

## Создание примера приложения для Docker Linux Container

1. Запустите Visual Studio 2022 и выберите шаблон **ASP.NET Core Web App (Model-View-Controller)** и нажмите **Далее**
1. В окне **Настройка вашего нового проекта** установите желаемое имя проекта и местоположение, затем нажмите **Далее**
1. В окне **Дополнительная информация** выберите **.NET 6.0 (Долгосрочная поддержка)** и включите поддержку Docker. Также можно установить **Docker OS** на Linux, если это необходимо.
1. Нажмите **Создать**
1.
### Генерация PDF документа с использованием ASP.NET Core Web App в контейнере Linux

Мы будем использовать код из **Сложного примера** в этом приложении. Пожалуйста, перейдите по [этой ссылке](/pdf/ru/net/complex-pdf-example/) для более подробного объяснения.

1. Создайте папку `images` в папке `wwwroot` и поместите туда изображение `logo.png`. Вы можете скачать это изображение [здесь](/pdf/ru/net/docker/logo.png)
1. Создайте папку `fonts` в папке `wwwroot` и поместите туда шрифты [Roboto](https://fonts.google.com/specimen/Roboto).
1. Создайте папку `samples` в папке `wwwroot` и поместите туда образцы данных.
1. Замените код в `HomeController.cs` следующим фрагментом (пожалуйста, обратите внимание, что у вас может быть другое пространство имен):

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
    // Представляет контроллер для главной страницы и генерации PDF в демонстрационном приложении Linux.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // Отображает индексное представление.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // Генерирует документ PDF и возвращает его как файл.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Генерация PDF: Начало ");
            // Инициализация объекта документа
            var document = new Document();
            // Добавление страницы
            var page = document.Pages.Add();

            // Добавление изображения
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // Добавление заголовка
            var header = new TextFragment("Новые маршруты паромов осенью 2020");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Добавление описания
            var descriptionText = "Посетители должны покупать билеты онлайн, и билетов ограниченное количество — 5000 в день. Паром работает с половинной загрузкой и по сокращенному расписанию. Ожидайте очереди.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Добавление таблицы
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
            headerRow.Cells.Add("Город отправления");
            headerRow.Cells.Add("Остров отправления");
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
            _logger.LogInformation("Генерация PDF: Завершение");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Конвертирует файл в другой формат на основе предоставленного id.
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
        // Конвертирует файл PDF в формат JPEG и возвращает его как файл.
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
        // Конвертирует файл XPS в формат PDF и возвращает его как файл.
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
        // Отображает представление конфиденциальности.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // Отображает представление ошибки.
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```
1. Замените содержимое в `Dockerfile` на следующее содержимое:

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

