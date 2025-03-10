---
title: Ajouter des tampons d'image dans un PDF en utilisant C#
linktitle: Tampons d'image dans un fichier PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /fr/net/image-stamps-in-pdf-page/
description: Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Image stamps in PDF using C#",
    "alternativeHeadline": "Add Custom Image Stamps to PDF Documents",
    "abstract": "La nouvelle fonctionnalité de la bibliothèque Aspose.PDF permet aux utilisateurs d'ajouter facilement des tampons d'image aux documents PDF en utilisant C#. Avec la classe ImageStamp, les développeurs peuvent personnaliser des attributs tels que la taille, l'opacité et la qualité, améliorant ainsi considérablement la présentation et l'accessibilité des documents. Cette fonctionnalité inclut également la possibilité d'ajouter un texte alternatif, favorisant une meilleure utilisabilité pour les lecteurs d'écran.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "646",
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
    "url": "/net/image-stamps-in-pdf-page/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/image-stamps-in-pdf-page/"
    },
    "dateModified": "2024-11-26",
    "description": "Ajoutez le tampon d'image dans votre document PDF en utilisant la classe ImageStamp avec la bibliothèque Aspose.PDF."
}
</script>

## Ajouter un tampon d'image dans un fichier PDF

Vous pouvez utiliser la classe ImageStamp pour ajouter un tampon d'image à un fichier PDF. La classe ImageStamp fournit les propriétés nécessaires pour créer un tampon basé sur une image, telles que la hauteur, la largeur, l'opacité, etc.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Pour ajouter un tampon d'image :

1. Créez un objet Document et un objet ImageStamp en utilisant les propriétés requises.
1. Appelez la méthode AddStamp de la classe Page pour ajouter le tampon au PDF.

Le code suivant montre comment ajouter un tampon d'image dans le fichier PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Background = true;
        imageStamp.XIndent = 100;
        imageStamp.YIndent = 100;
        imageStamp.Height = 300;
        imageStamp.Width = 300;
        imageStamp.Rotate = Rotation.on270;
        imageStamp.Opacity = 0.5;
        // Add stamp to particular page
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "AddImageStamp_out.pdf");
    }
}
```

## Contrôler la qualité de l'image lors de l'ajout du tampon

Lors de l'ajout d'une image en tant qu'objet tampon, vous pouvez contrôler la qualité de l'image. La propriété Quality de la classe ImageStamp est utilisée à cet effet. Elle indique la qualité de l'image en pourcentages (valeurs valides de 0 à 100).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlImageQualityWhenAddingStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg");
        imageStamp.Quality = 10;
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "ControlImageQuality_out.pdf");
    }
}
```

## Tampon d'image en tant qu'arrière-plan dans une boîte flottante

L'API Aspose.PDF vous permet d'ajouter un tampon d'image en tant qu'arrière-plan dans une boîte flottante. La propriété BackgroundImage de la classe FloatingBox peut être utilisée pour définir le tampon d'image d'arrière-plan pour une boîte flottante comme montré dans l'exemple de code suivant.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImageStampAsBackgroundInFloatingBox()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page to PDF document
        Page page = document.Pages.Add();
        // Create FloatingBox object
        var aBox = new Aspose.Pdf.FloatingBox(200, 100);
        // Set left position for FloatingBox
        aBox.Left = 40;
        // Set Top position for FloatingBox
        aBox.Top = 80;
        // Set the Horizontal alignment for FloatingBox
        aBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        // Add text fragment to paragraphs collection of FloatingBox
        aBox.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("main text"));
        // Set border for FloatingBox
        aBox.Border = new Aspose.Pdf.BorderInfo(BorderSide.All, Aspose.Pdf.Color.Red);
        // Add background image
        aBox.BackgroundImage = new Aspose.Pdf.Image
        {
            File = dataDir + "aspose-logo.jpg"
        };
        // Set background color for FloatingBox
        aBox.BackgroundColor = Aspose.Pdf.Color.Yellow;
        // Add FloatingBox to paragraphs collection of page object
        page.Paragraphs.Add(aBox);
        // Save PDF document
        document.Save(dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```

## Ajouter un texte alternatif au tampon d'image

Depuis la version 24.6, il est possible d'ajouter un texte alternatif au tampon d'image.

Ce code ouvre un fichier PDF, ajoute une image en tant que tampon à une position spécifique et inclut un texte alternatif pour l'accessibilité. Le PDF mis à jour est ensuite enregistré avec un nouveau nom de fichier.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAlternativeTextToTheImageStamp()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ImageStampInput.pdf"))
    {
        // Create image stamp
        var imageStamp = new Aspose.Pdf.ImageStamp(dataDir + "aspose-logo.jpg")
        {
            XIndent = 100,
            YIndent = 700,
            Quality = 100,
            AlternativeText = "Your alt text"  // This property added.
        };
        // Add stamp
        document.Pages[1].AddStamp(imageStamp);
        // Save PDF document
        document.Save(dataDir + "DocWithImageStamp_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
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
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>