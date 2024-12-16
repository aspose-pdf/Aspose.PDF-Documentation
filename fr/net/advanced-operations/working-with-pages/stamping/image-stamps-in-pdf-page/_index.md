---
title: Ajouter des tampons d'image dans un PDF en utilisant C#
linktitle: Tampons d'image dans un fichier PDF
type: docs
weight: 10
url: /fr/net/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter des tampons d'image dans un PDF en utilisant C#",
    "alternativeHeadline": "Ajouter des tampons d'image dans un PDF en utilisant C#",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de documents PDF",
    "keywords": "pdf, c#, génération de documents",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2022-02-04",
    "description": "Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF."
}
</script>
## Ajouter un tampon d'image dans un fichier PDF

Vous pouvez utiliser la classe ImageStamp pour ajouter un tampon d'image à un fichier PDF. La classe ImageStamp fournit les propriétés nécessaires pour créer un tampon basé sur une image, telles que la hauteur, la largeur, l'opacité, etc.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Pour ajouter un tampon d'image :

1. Créez un objet Document et un objet ImageStamp en utilisant les propriétés requises.
1. Appelez la méthode AddStamp de la classe Page pour ajouter le tampon au PDF.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller à https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Créer un tampon d'image
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");
imageStamp.Background = true;
imageStamp.XIndent = 100;
imageStamp.YIndent = 100;
imageStamp.Height = 300;
imageStamp.Width = 300;
imageStamp.Rotate = Rotation.on270;
imageStamp.Opacity = 0.5;
// Ajouter un tampon à une page particulière
pdfDocument.Pages[1].AddStamp(imageStamp);

dataDir = dataDir + "AddImageStamp_out.pdf";
// Sauvegarder le document de sortie
pdfDocument.Save(dataDir);
```
## Contrôler la qualité de l'image lors de l'ajout d'un tampon

Lors de l'ajout d'une image comme objet tampon, vous pouvez contrôler la qualité de l'image. La propriété Quality de la classe ImageStamp est utilisée à cet effet. Elle indique la qualité de l'image en pourcentage (les valeurs valides sont de 0 à 100).

```csharp
// Pour des exemples complets et des fichiers de données, veuillez aller sur https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Ouvrir le document
Document pdfDocument = new Document(dataDir+ "AddImageStamp.pdf");

// Créer un tampon image
ImageStamp imageStamp = new ImageStamp(dataDir + "aspose-logo.jpg");

imageStamp.Quality = 10;
pdfDocument.Pages[1].AddStamp(imageStamp);
pdfDocument.Save(dataDir + "ControlImageQuality_out.pdf");
```

## Tampon d'image comme arrière-plan dans une boîte flottante

L'API Aspose.PDF vous permet d'ajouter un tampon d'image comme arrière-plan dans une boîte flottante.
L'API Aspose.PDF vous permet d'ajouter un tampon image comme arrière-plan dans une boîte flottante.

```csharp
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Le chemin vers le répertoire des documents.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Instancier l'objet Document
Document doc = new Document();
// Ajouter une page au document PDF
Page page = doc.Pages.Add();
// Créer un objet FloatingBox
FloatingBox aBox = new FloatingBox(200, 100);
// Définir la position gauche pour FloatingBox
aBox.Left = 40;
// Définir la position haute pour FloatingBox
aBox.Top = 80;
// Définir l'alignement horizontal pour FloatingBox
aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Ajouter un fragment de texte à la collection de paragraphes de FloatingBox
aBox.Paragraphs.Add(new TextFragment("texte principal"));
// Définir la bordure pour FloatingBox
aBox.Border = new BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
// Ajouter une image d'arrière-plan
aBox.BackgroundImage = new Image
{
    File = dataDir + "aspose-logo.jpg"
};
// Définir la couleur de fond pour FloatingBox
aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
// Ajouter FloatingBox à la collection de paragraphes de l'objet page
page.Paragraphs.Add(aBox);
// Sauvegarder le document PDF
doc.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF pour la bibliothèque .NET",
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
    "applicationCategory": "Bibliothèque de manipulation PDF pour .NET",
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

