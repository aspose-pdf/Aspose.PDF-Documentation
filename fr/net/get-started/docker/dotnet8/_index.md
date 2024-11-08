---
title: Comment exécuter Aspose.PDF dans Docker
linktitle: Utiliser Docker
type: docs
weight: 20
url: /fr/net/docker/dotnet8/
description: Intégrer les fonctionnalités de Aspose.PDF dans votre application en utilisant les conteneurs Linux Docker
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Prérequis

Les exemples suivants ont été testés avec :

* Docker v.25.0.2 et Docker Desktop 4.27.1
* Visual Studio 2022 Édition Communauté v.17.0.5
* Le SDK .NET 8 est utilisé dans l'exemple fourni ci-dessous.
* Aspose.PDF.Drawing v.24.01

## Créer une application exemple pour le conteneur Linux Docker

1. Lancez Visual Studio 2022 et choisissez le modèle **ASP.NET Core Web App (Model-View-Controller)** puis appuyez sur **Suivant**
1. Dans la fenêtre **Configurer votre nouveau projet**, définissez le nom et l'emplacement souhaités du projet puis appuyez sur **Suivant**
1. Dans la fenêtre **Informations supplémentaires**, choisissez **.NET 6.0 (Support à long terme)** et activez le support Docker. Vous pouvez également définir **Docker OS** sur Linux si nécessaire.
1. Appuyez sur **Créer**
1.
### Générer un document PDF en utilisant une application Web ASP.NET Core dans un conteneur Linux

Nous utiliserons le code de **l'Exemple Complexe** dans cette application. Veuillez suivre [ce lien](/pdf/fr/net/complex-pdf-example/) pour une explication plus détaillée.

1. Créez un dossier `images` dans le dossier `wwwroot` et placez l'image `logo.png`. Vous pouvez télécharger cette image [ici](/pdf/fr/net/docker/logo.png)
1. Créez un dossier `fonts` dans le dossier `wwwroot` et placez les polices [Roboto](https://fonts.google.com/specimen/Roboto) là-bas.
1. Créez un dossier `samples` dans le dossier `wwwroot` et placez des données d'exemple là-bas.
1. Remplacez le code dans `HomeController.cs` avec l'extrait suivant (veuillez noter que vous pouvez avoir un autre espace de noms) :

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
    // Représente un contrôleur pour la page d'accueil et la génération de PDF dans une application de démonstration Linux.
    // </summary>
    public class HomeController(ILogger<HomeController> logger, IWebHostEnvironment appEnvironment) : Controller
    {
        private readonly ILogger<HomeController> _logger = logger;
        private readonly IWebHostEnvironment _appEnvironment = appEnvironment;

        // <summary>
        // Affiche la vue index.
        // </summary>
        public IActionResult Index()
        {
            return View();
        }

        // <summary>
        // Génère un document PDF et le retourne en tant que fichier.
        // </summary>
        public IActionResult Generate()
        {
            const string fileType = "application/pdf";
            const string fileName = "sample.pdf";
            FontRepository.Sources.Add(new FolderFontSource(Path.Combine(_appEnvironment.WebRootPath, "fonts")));
            var memoryStream = new MemoryStream();

            _logger.LogInformation("Génération de PDF : Début ");
            // Initialise l'objet document
            var document = new Document();
            // Ajoute une page
            var page = document.Pages.Add();

            // Ajoute une image
            var imageFileName = Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // Ajoute un en-tête
            var header = new TextFragment("Nouvelles routes de ferry en automne 2020");
            header.TextState.Font = FontRepository.FindFont("Roboto");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Ajoute une description
            var descriptionText = "Les visiteurs doivent acheter des billets en ligne et les billets sont limités à 5 000 par jour. Le service de ferry fonctionne à demi-capacité et selon un horaire réduit. Attendez-vous à des files d'attente.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Helvetica");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Ajoute une table
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
            headerRow.Cells.Add("Départ Ville");
            headerRow.Cells.Add("Départ Île");
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
            _logger.LogInformation("Génération de PDF : Fin");
            return File(memoryStream, fileType, fileName);
        }

        // <summary>
        // Convertit un fichier dans un format différent en fonction de l'ID fourni.
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
        // Convertit un fichier PDF en format JPEG et le retourne en tant que fichier.
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
        // Convertit un fichier XPS en format PDF et le retourne en tant que fichier.
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
        // Affiche la vue de confidentialité.
        // </summary>
        public IActionResult Privacy()
        {
            return View();
        }

        // <summary>
        // Affiche la vue d'erreur.
        // </summary>
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
```
1. Remplacez le contenu dans `Dockerfile` par le contenu suivant :

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

