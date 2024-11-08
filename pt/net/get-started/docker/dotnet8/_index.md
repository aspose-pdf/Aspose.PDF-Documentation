---
title: Como executar Aspose.PDF em Docker
linktitle: Usando Docker
type: docs
weight: 20
url: /pt/net/docker/dotnet8/
description: Integre a funcionalidade Aspose.PDF em sua aplicação usando contêineres Linux Docker
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Pré-requisitos

Os seguintes exemplos foram testados com:

* Docker v.25.0.2 e Docker Desktop 4.27.1
* Visual Studio 2022 Community Edition v.17.0.5
* .NET 8 SDK é usado no exemplo fornecido abaixo.
* Aspose.PDF.Drawing v.24.01

## Criar aplicativo de exemplo para contêiner Linux Docker

1. Inicie o Visual Studio 2022 e escolha o modelo **ASP.NET Core Web App (Model-View-Controller)** e pressione **Next**
1. Na janela **Configure seu novo projeto**, defina o nome e localização desejados do projeto e pressione **Next**
1. Na janela **Informação adicional**, escolha **.NET 6.0 (Suporte a longo prazo)** e habilite o suporte Docker. Você também pode definir **Docker OS** para Linux, se necessário.
1. Pressione **Criar**
1.
### Gerar documento PDF usando o aplicativo Web ASP.NET Core em contêiner Linux

Vamos usar o código do **Exemplo Complexo** neste aplicativo. Por favor, siga [este link](/pdf/pt/net/complex-pdf-example/) para uma explicação mais detalhada.

1. Crie a pasta `images` na pasta `wwwroot` e coloque a imagem `logo.png`. Você pode baixar esta imagem [aqui](/pdf/pt/net/docker/logo.png)
1. Crie a pasta `fonts` na pasta `wwwroot` e coloque as fontes [Roboto](https://fonts.google.com/specimen/Roboto) lá.
1. Crie a pasta `samples` na pasta `wwwroot` e coloque os dados de exemplo lá.
1. Substitua o código em `HomeController.cs` pelo seguinte trecho (observe que você pode ter outro namespace):

```cs
using Aspose.Pdf;
using Aspose.Pdf.Devices;
using Aspose.Pdf.Text;
using Docker.LinuxDemo.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;

namespace Docker.LinuxDemo.Controllers
{
    // Representa um controlador para a página inicial e geração de PDF em uma aplicação de demonstração Linux.
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // Exibe a visualização do índice.
        public IActionResult Index()
        {
            return View();
        }

        // Gera um documento PDF e o retorna como um arquivo.
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Geração de PDF: Início ");
            // Inicializa o objeto do documento
            var document = new Document();
            // Adiciona página
            var page = document.Pages.Add();

            // Adiciona imagem
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // Adiciona cabeçalho
            var header = new TextFragment("Novas rotas de balsas no Outono de 2020");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Adiciona descrição
            var descriptionText = "Os visitantes devem comprar ingressos online e os ingressos são limitados a 5.000 por dia. O serviço de balsa está operando com metade da capacidade e em um cronograma reduzido. Espere filas.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Adiciona tabela
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
            headerRow.Cells.Add("Cidade de Partida");
            headerRow.Cells.Add("Ilha de Partida");
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
            _logger.LogInformation("Geração de PDF: Conclusão");
            return File(memoryStream, fileType, fileName);
        }

        // Converte um arquivo para um formato diferente com base no id fornecido.
        public FileStreamResult Convert(string id)
        {
            return id switch
            {
                "xps-to-pdf" => ConvertXpsToPdf(),
                "pdf-to-jpeg" => ConvertPdfToJpeg(),
                _ => throw new NotImplementedException(),
            };
        }

        // Converte um arquivo PDF para o formato JPEG e o retorna como um arquivo.
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

        // Converte um arquivo XPS para o formato PDF e o retorna como um arquivo.
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

        // Exibe a visualização da privacidade.
        public IActionResult Privacy()
        {
            return View();
        }

        // Exibe a visualização de erro.
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```
1. Substitua o conteúdo em `Dockerfile` com o seguinte conteúdo:

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

