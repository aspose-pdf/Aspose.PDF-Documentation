---
title: Как запустить Aspose.PDF для .NET 6 в Docker
linktitle: Использование Aspose.PDF для .NET 6 в Docker
type: docs
weight: 10
url: /ru/net/docker/dotnet6/
description: Интегрируйте функциональность Aspose.PDF в ваше приложение с использованием контейнеров Docker Linux или Windows
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Предварительные требования

Следующие примеры были протестированы с:

* Docker v.20.10.11 и Docker Desktop 4.3.2
* Visual Studio 2022 Community Edition v.17.0.5
* В представленном ниже примере используется .NET 6 SDK.
* Aspose.PDF для .NET v.22.01

## Создание примера приложения для Docker Linux Container

1. Запустите Visual Studio 2022 и выберите шаблон **ASP.NET Core Web App (Model-View-Controller)**, затем нажмите **Далее**
1. В окне **Настройка вашего нового проекта** установите желаемое имя проекта и местоположение, затем нажмите **Далее**
1. В окне **Дополнительная информация** выберите **.NET 6.0 (Долгосрочная поддержка)** и включите поддержку Docker. Также можно установить **ОС Docker** на Linux, если это необходимо.
1. Выберите **Инструменты->Nuget Package Manager->Консоль управления пакетами** и установите **Aspose.PDF для .NET** (используйте команду `Install-Package Aspose.PDF`)

### Генерация PDF документа с использованием ASP.NET Core Web App в Linux контейнере

Мы будем использовать код из **Сложного примера** в этом приложении. Пожалуйста, перейдите по [этой ссылке](/pdf/ru/net/complex-pdf-example/) для получения более подробной информации.

1. Создайте папку `images` в папке `wwwroot` и поместите туда изображение `logo.png`. Вы можете скачать это изображение [здесь](/pdf/ru/net/docker/logo.png)
1. Замените код в `HomeController.cs` на следующий фрагмент (обратите внимание, что у вас может быть другое пространство имен):

Этот фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

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

            _logger.LogInformation("Start");
            // Инициализация объекта документа
            var document = new Document();
            // Добавление страницы
            var page = document.Pages.Add();

            // Добавление изображения
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Добавление заголовка
            var header = new TextFragment("Новые маршруты паромов осенью 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Добавление описания
            var descriptionText = "Посетители должны покупать билеты онлайн, и количество билетов ограничено 5,000 в день. Сервис паромов работает с половинной загрузкой и по сокращенному расписанию. Ожидайте очередей.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
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
1. Замените содержимое в `Dockerfile` следующим содержимым:

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

## Создайте пример приложения для Docker Windows контейнера

1.
1. В окне **Настройка вашего нового проекта** установите желаемое имя проекта и местоположение, затем нажмите **Далее**
1. В окне **Дополнительная информация** выберите **.NET 6.0 (Долгосрочная поддержка)** и включите поддержку Docker. При необходимости вы также можете установить **Docker OS** на `Windows`.
1. Нажмите **Создать**
1. Выберите **Инструменты->Менеджер пакетов Nuget->Консоль менеджера пакетов** и установите **Aspose.PDF для .NET** (используйте команду `Install-Package Aspose.PDF`)

### Создание PDF-документа с использованием ASP.NET Core Web App в контейнере Windows

Мы будем использовать тот же код, что и в предыдущем примере.

1. Создайте папку `images` в папке `wwwroot` и поместите туда изображение `logo.png`. Вы можете скачать это изображение [здесь](/pdf/ru/net/docker/logo.png)
1. Замените код в `HomeController.cs` на приведенный выше фрагмент.

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

