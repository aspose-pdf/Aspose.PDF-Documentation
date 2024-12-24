---
title: Ajouter un numéro de page au PDF avec C#
linktitle: Ajouter un numéro de page
type: docs
weight: 100
url: /fr/net/add-page-number/
description: Aspose.PDF pour .NET vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter un numéro de page au PDF avec C#",
    "alternativeHeadline": "Comment ajouter un tampon de numéro de page au PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, tampon de numéro de page",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de documentation Aspose.PDF",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF pour .NET vous permet d'ajouter un tampon de numéro de page à votre fichier PDF en utilisant la classe PageNumber Stamp."
}
</script>

Tous les documents doivent comporter des numéros de page. Le numéro de page facilite la localisation des différentes parties du document pour le lecteur.
**Aspose.PDF pour .NET** vous permet d'ajouter des numéros de page avec PageNumberStamp.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Vous pouvez utiliser la classe [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) pour ajouter un tampon de numéro de page dans un fichier PDF.
Vous pouvez utiliser la classe [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) pour ajouter un tampon de numéro de page dans un fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// Créer un tampon de numéro de page
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// Si le tampon est en arrière-plan
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Page # de " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// Définir les propriétés du texte
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// Ajouter le tampon à une page spécifique
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// Sauvegarder le document de sortie
pdfDocument.Save(dataDir);
```
## Exemple en Direct

[Ajouter des numéros de page PDF](https://products.aspose.app/pdf/page-number) est une application web gratuite en ligne qui vous permet d'explorer le fonctionnement de l'ajout de numéros de pages.

[![Comment ajouter un numéro de page dans un pdf en utilisant C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## Ajouter/Supprimer la numérotation Bates

**La numérotation Bates** (également connue sous le nom de marquage Bates) est utilisée dans les domaines juridique, médical et commercial pour placer des numéros identifiants et/ou des marques de date/heure sur des images et des documents au fur et à mesure qu'ils sont numérisés ou traités, par exemple, pendant la phase de découverte des préparatifs d'un procès ou l'identification des reçus commerciaux. Ce processus fournit l'identification, la protection et la numérotation consécutive automatique des images ou des documents.

Aspose.PDF a un support limité pour la numérotation Bates pour le moment. Cette fonctionnalité sera mise à jour selon les demandes des clients.

### Comment supprimer la numérotation Bates

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bibliothèque Aspose.PDF pour .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
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
    "applicationCategory": "Bibliothèque de manipulation de PDF pour .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

