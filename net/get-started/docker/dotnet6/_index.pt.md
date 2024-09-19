---
title: Como executar Aspose.PDF para .NET 6 no Docker
linktitle: Usando Aspose.PDF para .NET 6 no Docker
type: docs
weight: 10
url: /net/docker/dotnet6/
description: Integre a funcionalidade Aspose.PDF em sua aplicação usando contêineres Docker Linux ou Windows
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Pré-requisitos

Os seguintes exemplos foram testados com:

* Docker v.20.10.11 e Docker Desktop 4.3.2
* Visual Studio 2022 Community Edition v.17.0.5
* O SDK do .NET 6 é usado no exemplo fornecido abaixo.
* Aspose.PDF para .NET v.22.01

## Criar aplicação de exemplo para Contêiner Docker Linux

1. Inicie o Visual Studio 2022 e escolha o template **ASP.NET Core Web App (Model-View-Controller)** e pressione **Next**
1. Na janela **Configure your new project** defina o nome e localização desejados para o projeto e pressione **Next**
1. Na janela **Additional information** escolha **.NET 6.0 (Suporte de longo prazo)** e habilite o suporte Docker. Você também pode definir o **Docker OS** para Linux, se necessário.
1.
1.
1. Escolha **Ferramentas->Gerenciador de Pacotes Nuget->Console do Gerenciador de Pacotes** e instale **Aspose.PDF for .NET** (use o comando `Install-Package Aspose.PDF`)

### Gerar documento PDF usando ASP.NET Core Web App em contêiner Linux

Vamos usar o código do **Exemplo Complexo** neste aplicativo. Por favor, siga [este link](/pdf/net/complex-pdf-example/) para uma explicação mais detalhada.

1. Crie uma pasta `images` na pasta `wwwroot` e coloque a imagem `logo.png`. Você pode baixar esta imagem [aqui](/pdf/net/docker/logo.png)
1. Substitua o código em `HomeController.cs` com o seguinte trecho (observe que você pode ter outro namespace):

O seguinte trecho de código também funciona com a biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

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
            // Initialize document object
            var document = new Document();
            // Add page
            var page = document.Pages.Add();

            // Add image
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
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
1. Substitua o conteúdo em `Dockerfile` pelo seguinte conteúdo:

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

## Criar aplicação de exemplo para Docker Windows Container

1.
1. Na janela **Configure seu novo projeto**, defina o nome e o local do projeto desejados e pressione **Next**
1. Na janela **Informações adicionais**, escolha **.NET 6.0 (Suporte de longo prazo)** e habilite o suporte ao Docker. Se necessário, você também pode definir o **Docker OS** para `Windows`.
1. Pressione **Create**
1. Escolha **Tools->Nuget Package Manager->Package Manager Console** e instale **Aspose.PDF for .NET** (use o comando `Install-Package Aspose.PDF`)

### Gerar documento PDF usando ASP.NET Core Web App em contêiner Windows

Usaremos o mesmo código do exemplo anterior.

1. Crie uma pasta `images` na pasta `wwwroot` e coloque a imagem `logo.png`. Você pode baixar esta imagem [aqui](/pdf/net/docker/logo.png)
1. Substitua o código em `HomeController.cs` com o trecho acima.

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

