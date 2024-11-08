---
title: Cómo ejecutar Aspose.PDF para .NET 6 en Docker
linktitle: Usando Aspose.PDF para .NET 6 en Docker
type: docs
weight: 10
url: /es/net/docker/dotnet6/
description: Integra la funcionalidad de Aspose.PDF en tu aplicación utilizando contenedores Docker Linux o Windows
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Prerrequisitos

Los siguientes ejemplos se probaron con:

* Docker v.20.10.11 y Docker Desktop 4.3.2
* Visual Studio 2022 Community Edition v.17.0.5
* Se utiliza el SDK de .NET 6 en el ejemplo proporcionado a continuación.
* Aspose.PDF para .NET v.22.01

## Crear aplicación de muestra para contenedor Docker Linux

1. Inicia Visual Studio 2022 y elige la plantilla **Aplicación Web ASP.NET Core (Model-View-Controller)** y presiona **Siguiente**
1. En la ventana **Configura tu nuevo proyecto** establece el nombre y ubicación del proyecto deseados y presiona **Siguiente**
1. En la ventana **Información adicional** elige **.NET 6.0 (Soporte a largo plazo)** y habilita el soporte de Docker. También puedes establecer **Docker OS** a Linux si es necesario.
1. Elija **Herramientas -> Administrador de paquetes Nuget -> Consola del administrador de paquetes** e instale **Aspose.PDF para .NET** (use el comando `Install-Package Aspose.PDF`)

### Generar documento PDF usando ASP.NET Core Web App en contenedor Linux

Usaremos el código de **Ejemplo Complejo** en esta aplicación. Por favor, siga [este enlace](/pdf/es/net/complex-pdf-example/) para una explicación más detallada.

1. Cree una carpeta `images` en la carpeta `wwwroot` y coloque la imagen `logo.png`. Puede descargar esta imagen desde [aquí](/pdf/es/net/docker/logo.png)
1. Reemplace el código en `HomeController.cs` con el siguiente fragmento (tenga en cuenta que puede tener otro espacio de nombres):

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

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

            _logger.LogInformation("Inicio");
            // Inicializar el objeto documento
            var document = new Document();
            // Añadir página
            var page = document.Pages.Add();

            // Añadir imagen
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Añadir encabezado
            var header = new TextFragment("Nuevas rutas de ferry en otoño de 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Añadir descripción
            var descriptionText = "Los visitantes deben comprar los boletos en línea y los boletos están limitados a 5,000 por día. El servicio de ferry opera a media capacidad y con un horario reducido. Espere filas.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Añadir tabla
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
            headerRow.Cells.Add("Ciudad de Salida");
            headerRow.Cells.Add("Isla de Salida");
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
            _logger.LogInformation("Finalizar");
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
1. Reemplaza el contenido en `Dockerfile` con el siguiente contenido:

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

## Crear aplicación de muestra para Docker Windows Container

1.
1.
1. En la ventana **Configura tu nuevo proyecto**, establece el nombre y ubicación deseados del proyecto y presiona **Siguiente**
1. En la ventana **Información adicional**, selecciona **.NET 6.0 (Soporte a largo plazo)** y habilita el soporte de Docker. Si es necesario, también puedes establecer **Docker OS** a `Windows`.
1. Presiona **Crear**
1. Elige **Herramientas->Gestor de Paquetes Nuget->Consola del Gestor de Paquetes** e instala **Aspose.PDF para .NET** (usa el comando `Install-Package Aspose.PDF`)

### Generar documento PDF usando ASP.NET Core Web App en contenedor de Windows

Usaremos el mismo código que en el ejemplo anterior.

1. Crea una carpeta `images` en la carpeta `wwwroot` y coloca la imagen `logo.png`. Puedes descargar esta imagen desde [aquí](/pdf/es/net/docker/logo.png)
1. Reemplaza el código en `HomeController.cs` con el fragmento de arriba.

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

