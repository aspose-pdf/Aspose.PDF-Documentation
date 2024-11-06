---
title: Comment exécuter Aspose.PDF pour .NET 6 dans Docker
linktitle: Utiliser Aspose.PDF pour .NET 6 dans Docker
type: docs
weight: 10
url: fr/net/docker/dotnet6/
description: Intégrer les fonctionnalités d'Aspose.PDF dans votre application en utilisant des conteneurs Docker Linux ou Windows
lastmod: "2024-01-21"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Prérequis

Les exemples suivants ont été testés avec :

* Docker v.20.10.11 et Docker Desktop 4.3.2
* Visual Studio 2022 Édition Communautaire v.17.0.5
* SDK .NET 6 utilisé dans l'exemple ci-dessous.
* Aspose.PDF pour .NET v.22.01

## Créer une application exemple pour le conteneur Docker Linux

1. Lancez Visual Studio 2022 et choisissez le modèle **Application web ASP.NET Core (Model-View-Controller)** puis appuyez sur **Suivant**
1. Dans la fenêtre **Configurer votre nouveau projet**, définissez le nom et l'emplacement souhaités du projet puis appuyez sur **Suivant**
1. Dans la fenêtre **Informations supplémentaires**, choisissez **.NET 6.0 (support à long terme)** et activez le support Docker. Vous pouvez également définir le **système d'exploitation Docker** sur Linux si nécessaire.
1.
1. Choisissez **Outils -> Gestionnaire de Packages Nuget -> Console du Gestionnaire de Packages** et installez **Aspose.PDF pour .NET** (utilisez la commande `Install-Package Aspose.PDF`)

### Générer un document PDF en utilisant une application Web ASP.NET Core dans un conteneur Linux

Nous utiliserons le code de **Exemple Complex** dans cette application. Veuillez suivre [ce lien](/pdf/net/complex-pdf-example/) pour une explication plus détaillée.

1. Créez un dossier `images` dans le dossier `wwwroot` et placez l'image `logo.png`. Vous pouvez télécharger cette image [ici](/pdf/net/docker/logo.png)
1. Remplacez le code dans `HomeController.cs` par le fragment suivant (veuillez noter que vous pouvez avoir un autre espace de noms) :

Le fragment de code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

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

            _logger.LogInformation("Début");
            // Initialiser l'objet document
            var document = new Document();
            // Ajouter une page
            var page = document.Pages.Add();

            // Ajouter une image
            var imageFileName = System.IO.Path.Combine(_appEnvironment.WebRootPath, "images", "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Ajouter un en-tête
            var header = new TextFragment("Nouvelles routes de ferry à l'automne 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Ajouter une description
            var descriptionText = "Les visiteurs doivent acheter des billets en ligne et les billets sont limités à 5 000 par jour. Le service de ferry fonctionne à demi-capacité et selon un horaire réduit. Attendez-vous à des files d'attente.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);


            // Ajouter un tableau
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
            headerRow.Cells.Add("Ville de départ");
            headerRow.Cells.Add("Île de départ");
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
            _logger.LogInformation("Fin");
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
1. Remplacez le contenu dans `Dockerfile` par le contenu suivant :

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

## Créez une application exemple pour le conteneur Docker Windows

1.
1.
1. Dans la fenêtre **Configurer votre nouveau projet**, définissez le nom et l'emplacement souhaités du projet et appuyez sur **Suivant**
1. Dans la fenêtre **Informations supplémentaires**, choisissez **.NET 6.0 (Support à long terme)** et activez le support Docker. Si nécessaire, vous pouvez également définir **Docker OS** sur `Windows`.
1. Appuyez sur **Créer**
1. Choisissez **Outils->Gestionnaire de Packages Nuget->Console du Gestionnaire de Packages** et installez **Aspose.PDF pour .NET** (utilisez la commande `Install-Package Aspose.PDF`)

### Générer un document PDF en utilisant ASP.NET Core Web App dans un conteneur Windows

Nous utiliserons le même code que dans l'exemple précédent.

1. Créez un dossier `images` dans le dossier `wwwroot` et placez-y l'image `logo.png`. Vous pouvez télécharger cette image [ici](/pdf/net/docker/logo.png)
1. Remplacez le code dans `HomeController.cs` par le snippet ci-dessus.

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

