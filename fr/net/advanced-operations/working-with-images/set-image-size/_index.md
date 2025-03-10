---
title: Définir la taille de l'image
linktitle: Définir la taille de l'image
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /fr/net/set-image-size/
description: Cette section décrit comment définir la taille d'une image dans un fichier PDF en utilisant la bibliothèque C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Image Size",
    "alternativeHeadline": "Set Custom Image Dimensions in PDFs with C#",
    "abstract": "Découvrez la nouvelle fonctionnalité Définir la taille de l'image dans la bibliothèque Aspose.PDF pour .NET, vous permettant de définir facilement les dimensions des images ajoutées aux documents PDF. Avec des propriétés comme FixWidth et FixHeight, vous pouvez personnaliser les tailles d'image pour un aspect poli et professionnel dans vos fichiers PDF. Optimisez votre flux de travail de génération de PDF en maîtrisant cette fonctionnalité essentielle.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Set Image Size, PDF generation, C# library, FixWidth, FixHeight, Aspose.Pdf.Image, image dimensions, PDF file manipulation, Aspose.PDF for .NET",
    "wordcount": "216",
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
    "url": "/net/set-image-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-image-size/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette section décrit comment définir la taille d'une image dans un fichier PDF en utilisant la bibliothèque C#."
}
</script>

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/fr/net/drawing/).

Il est possible de définir la taille d'une image qui est ajoutée à un fichier PDF. Pour définir la taille, vous pouvez utiliser les propriétés FixWidth et FixHeight de la classe Aspose.Pdf.Image. Le code suivant démontre comment définir la taille d'une image :

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetImageSizeInPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create an image instance
        var img = new Aspose.Pdf.Image();

        // Set Image Width and Height in Points
        img.FixWidth = 100;
        img.FixHeight = 100;

        // Set image type as SVG
        img.FileType = Aspose.Pdf.ImageFileType.Unknown;

        // Path for source file
        img.File = dataDir + "InputImage.jpg";

        // Add image to the page
        page.Paragraphs.Add(img);

        // Set page properties
        page.PageInfo.Width = 800;
        page.PageInfo.Height = 800;

        // Save PDF document
        document.Save(dataDir + "SetImageSize_out.pdf");
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