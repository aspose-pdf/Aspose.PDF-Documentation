---
title: Conversion de documents avec la fonction Microsoft Azure
linktitle: Conversion de documents avec la fonction Microsoft Azure
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /fr/net/converting-documents-with-microsoft-azure-function/
description: Apprenez à convertir des documents PDF en utilisant les fonctions Microsoft Azure avec Aspose.PDF for .NET, permettant un traitement de documents basé sur le cloud.
lastmod: "2024-10-25"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Converting Documents with Microsoft Azure function",
    "alternativeHeadline": "Integrate PDF Conversion with Microsoft Azure Functions",
    "abstract": "La nouvelle fonctionnalité de conversion de documents alimentée par Microsoft Azure permet aux utilisateurs de transformer efficacement des fichiers PDF en divers formats tels que DOCX, HTML et JPEG en utilisant Aspose.PDF for .NET et les fonctions Azure. Cette fonctionnalité permet une intégration transparente avec les ressources Azure, garantissant un traitement rapide et fiable des fichiers adapté aux développeurs cherchant à améliorer leurs applications.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1256",
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
    "url": "/net/converting-documents-with-microsoft-azure-function/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/converting-documents-with-microsoft-azure-function/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs avancés et les développeurs."
}
</script>

Cet article fournit des instructions détaillées étape par étape pour convertir des documents PDF dans Microsoft Azure en utilisant Aspose.PDF for .NET et la fonction Azure.

## Prérequis

* Visual Studio 2022 Community Edition avec développement Azure installé ou Visual Studio Code.
* Compte Azure : Vous avez besoin d'un abonnement Azure, créez un compte gratuit avant de commencer.
* SDK .NET 6.
* Aspose.PDF for .NET.

## Créer des ressources Azure

### Créer un compte de stockage

1. Allez sur le portail Azure (https://portal.azure.com).
2. Cliquez sur "Créer une ressource".
3. Recherchez "Compte de stockage".
4. Cliquez sur "Créer".
5. Remplissez les détails :
   - Abonnement : Choisissez votre abonnement.
   - Groupe de ressources : Créez un nouveau ou sélectionnez un existant.
   - Nom du compte de stockage : Entrez un nom unique.
   - Région : Choisissez la région la plus proche.
   - Performance : Standard.
   - Redondance : LRS (Stockage redondant localement).
6. Cliquez sur "Vérifier + créer".
7. Cliquez sur "Créer".

### Créer un conteneur

1. Ouvrez votre compte de stockage.
2. Allez dans "Conteneurs" sous "Stockage de données".
3. Cliquez sur "+ Conteneur".
4. Nommez-le "pdfdocs".
5. Définissez le niveau d'accès public sur "Privé".
6. Cliquez sur "Créer".

## Créer un projet

### Créer un projet Visual Studio

1. Ouvrez Visual Studio 2022.
2. Cliquez sur "Créer un nouveau projet".
3. Sélectionnez "Fonctions Azure".
4. Nommez votre projet "PdfConverterAzure".
5. Choisissez ".NET 6.0" ou plus récent et "Déclencheur HTTP".
6. Cliquez sur "Créer".

### Créer un projet Visual Studio Code

#### Installer les prérequis

1. Extensions Visual Code :
```bash
code --install-extension ms-dotnettools.csharp
code --install-extension ms-azuretools.vscode-azurefunctions
code --install-extension ms-vscode.azure-account
```

2. Installer les outils de base Azure Functions :
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

3. Installer Azure CLI :
- Windows : Téléchargez depuis le site de Microsoft.
- macOS : `brew install azure-cli`.
- Linux : `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash`.

#### Configurer le projet

1. Ouvrez le projet dans Visual Studio Code :
```bash
code .
```

2. Ajoutez des packages NuGet en créant/mis à jour `PdfConverterApp.csproj` :
```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net6.0</TargetFramework>
    <AzureFunctionsVersion>v4</AzureFunctionsVersion>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.NET.Sdk.Functions" Version="4.1.1" />
    <PackageReference Include="Aspose.PDF" Version="24.10.0" />
    <PackageReference Include="Azure.Storage.Blobs" Version="12.14.1" />
    <PackageReference Include="Microsoft.Azure.WebJobs.Extensions.Storage" Version="5.0.1" />
  </ItemGroup>
</Project>
```

## Installer les packages NuGet requis

Dans Visual Studio, ouvrez la console du gestionnaire de packages et exécutez :
```powershell
Install-Package Aspose.PDF
Install-Package Azure.Storage.Blobs
Install-Package Microsoft.Azure.WebJobs.Extensions.Storage
```

Dans Visual Studio Code, exécutez :
```bash
dotnet restore
```

## Configurer la connexion de stockage Azure

Obtenez les clés d'accès pour le compte de stockage sous Clés d'accès dans le portail Azure. Ces clés seront utilisées pour authentifier votre application.

1. Ouvrez `local.settings.json` :
```json
{
    "IsEncrypted": false,
    "Values": {
        "AzureWebJobsStorage": "YOUR_STORAGE_CONNECTION_STRING",
        "FUNCTIONS_WORKER_RUNTIME": "dotnet",
        "ContainerName": "pdfdocs"
    }
}
```

2. Remplacez `YOUR_STORAGE_CONNECTION_STRING` par votre véritable chaîne de connexion de stockage depuis le portail Azure.

## Configurer la licence Aspose

Dans Visual Studio :

1. Copiez votre fichier de licence Aspose.PDF dans le projet.
2. Cliquez avec le bouton droit sur le fichier de licence et sélectionnez "Propriétés".
3. Définissez "Copier dans le répertoire de sortie" sur "Toujours copier".
4. Ajoutez le code d'initialisation de la licence dans le Program.cs :
```csharp
var license = new Aspose.Pdf.License();
license.SetLicense("Aspose.PDF.lic");
```

## Créer le code

Créez un nouveau fichier `PdfConverter.cs` :

```csharp
using Azure.Storage.Blobs;
using System;
using System.IO;
using System.Threading.Tasks;

public class PdfConverter
{
    private readonly BlobContainerClient _containerClient;

    public PdfConverter(string connectionString, string containerName)
    {
        _containerClient = new BlobContainerClient(connectionString, containerName);
    }

    public async Task<string> ConvertToFormat(string sourceBlobName, string targetFormat)
    {
        // Download source PDF
        var sourceBlob = _containerClient.GetBlobClient(sourceBlobName);
        using var sourceStream = new MemoryStream();
        await sourceBlob.DownloadToAsync(sourceStream);
        sourceStream.Position = 0;

        // Open PDF document
        var document = new Aspose.Pdf.Document(sourceStream);

        // Create output stream
        using var outputStream = new MemoryStream();
        string targetBlobName = Path.GetFileNameWithoutExtension(sourceBlobName);

        // Convert based on format
        switch (targetFormat.ToLower())
        {
            case "docx":
                targetBlobName += ".docx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.DocX);
                break;

            case "html":
                targetBlobName += ".html";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Html);
                break;

            case "xlsx":
                targetBlobName += ".xlsx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Excel);
                break;

            case "pptx":
                targetBlobName += ".pptx";
                document.Save(outputStream, Aspose.Pdf.SaveFormat.Pptx);
                break;

            case "jpeg":
            case "jpg":
                targetBlobName += ".jpg";
                foreach (var page in document.Pages)
                {
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(new Aspose.Pdf.Devices.Resolution(300));
                    jpegDevice.Process(page, outputStream);
                }
                break;

            default:
                throw new ArgumentException($"Unsupported format: {targetFormat}");
        }

        // Upload converted file
        outputStream.Position = 0;
        var targetBlob = _containerClient.GetBlobClient(targetBlobName);
        await targetBlob.UploadAsync(outputStream, true);

        return targetBlob.Uri.ToString();
    }
}
```

Créez un nouveau fichier `ConvertPdfFunction.cs` :

```csharp
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;
using System.Threading.Tasks;
using System;
using System.IO;
using Newtonsoft.Json;
using Microsoft.AspNetCore.Mvc;

public static class ConvertPdfFunction
{
    [FunctionName("ConvertPdf")]
    public static async Task<IActionResult> Run(
        [HttpTrigger(AuthorizationLevel.Function, "post"), Route = "convert"] HttpRequest req,
        ILogger log)
    {
        try
        {
            // Read request body
            string requestBody = await new StreamReader(req.Body).ReadToEndAsync();
            dynamic data = JsonConvert.DeserializeObject(requestBody);

            string sourceBlob = data?.sourceBlob;
            string targetFormat = data?.targetFormat;

            if (string.IsNullOrEmpty(sourceBlob) || string.IsNullOrEmpty(targetFormat))
            {
                return new BadRequestObjectResult("Please provide sourceBlob and targetFormat");
            }

            // Get configuration
            string connectionString = Environment.GetEnvironmentVariable("AzureWebJobsStorage");
            string containerName = Environment.GetEnvironmentVariable("ContainerName");

            // Convert PDF
            var converter = new PdfConverter(connectionString, containerName);
            string resultUrl = await converter.ConvertToFormat(sourceBlob, targetFormat);

            return new OkObjectResult(new { url = resultUrl });
        }
        catch (Exception ex)
        {
            log.LogError(ex, "Error converting PDF");
            return new StatusCodeResult(500);
        }
    }
}
```

```csharp
// Startup.cs
[assembly: FunctionsStartup(typeof(PdfConverterAzure.Functions.Startup))]
namespace PdfConverterAzure.Functions
{
    public class Startup : FunctionsStartup
    {
        public override void Configure(IFunctionsHostBuilder builder)
        {
            // Read configuration
            var config = builder.GetContext().Configuration;

            // Register services
            builder.Services.AddLogging();

            // Register Azure Storage
            builder.Services.AddSingleton(x => 
                new BlobServiceClient(config["AzureWebJobsStorage"]));

            // Configure Aspose License
            var license = new Aspose.Pdf.License();
            license.SetLicense("Aspose.PDF.lic");
        }
    }
}
```

## Tester localement

Dans Visual Studio :
1. Démarrez l'émulateur de stockage Azure.
2. Exécutez le projet dans Visual Studio.
3. Utilisez Postman ou curl pour tester :

```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

Dans Visual Studio Code :
1. Démarrez l'application de fonction :
```bash
func start
```

2. Téléchargez un PDF pour tester :
```bash
az storage blob upload \
    --account-name $AccountName \
    --container-name pdfdocs \
    --name sample.pdf \
    --file /path/to/your/sample.pdf
```

3. Utilisez Postman ou curl pour tester :
```bash
curl -X POST http://localhost:7071/api/convert \
-H "Content-Type: application/json" \
-d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Déployer sur Azure

Dans Visual Studio :
1. Cliquez avec le bouton droit sur le projet dans Visual Studio.
2. Sélectionnez "Publier".
3. Choisissez "Application de fonction Azure".
4. Sélectionnez votre abonnement.
5. Créez une nouvelle ou sélectionnez une application de fonction existante.
6. Cliquez sur "Publier".

Dans Visual Studio Code :
1. Appuyez sur F1 ou Ctrl+Shift+P.
2. Sélectionnez "Fonctions Azure : Déployer sur l'application de fonction".
3. Choisissez votre abonnement.
4. Sélectionnez l'application de fonction créée ci-dessus.
5. Cliquez sur "Déployer".

## Configurer l'application de fonction Azure

1. Allez sur le portail Azure.
2. Ouvrez votre application de fonction.
3. Allez dans "Configuration".
4. Ajoutez des paramètres d'application :
   - Clé : "ContainerName".
   - Valeur : "pdfdocs".
5. Enregistrez les modifications.

## Tester le service déployé

Utilisez Postman ou curl pour tester :
```bash
curl -X POST "https://your-function.azurewebsites.net/api/convert" \
     -H "x-functions-key: your-function-key" \
     -H "Content-Type: application/json" \
     -d '{"sourceBlob": "sample.pdf", "targetFormat": "docx"}'
```

## Formats pris en charge

La liste des formats pris en charge peut être trouvée [ici](https://docs.aspose.com/pdf/net/supported-file-formats/).

## Dépannage

### Options de configuration importantes

1. Ajouter une authentification :
```csharp
[FunctionName("ConvertPdf")]
public async Task<IActionResult> Run(
    [HttpTrigger(AuthorizationLevel.Function, "post", Route = "convert")] HttpRequest req,
    ClaimsPrincipal principal,
    ILogger log)
{
    // Check authentication
    if (!principal.Identity.IsAuthenticated)
    {
        return new UnauthorizedResult();
    }
    // ...
}
```

2. Pour les fichiers volumineux, envisagez :
   - D'augmenter le délai d'expiration de la fonction.
   - D'utiliser un plan de consommation avec plus de mémoire.
   - D'implémenter un téléchargement/téléchargement par morceaux.
   - D'ajouter un suivi de progression.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "",
    "softwareVersion": "2024.10",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>