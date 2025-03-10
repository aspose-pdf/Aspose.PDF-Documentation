---
title: Définir le nom de police par défaut
linktitle: Définir le nom de police par défaut
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /fr/net/set-default-font-name/
description: Cette section décrit comment définir le nom de police par défaut lors du processus de conversion de PDF en image.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Default Font Name",
    "alternativeHeadline": "Customize PDF to image conversion with default font",
    "abstract": "Spécifiez des polices par défaut personnalisées pour la conversion de PDF en image en utilisant Aspose.PDF for .NET. La propriété DefaultFontName vous permet de sélectionner une police de remplacement lorsque l'original n'est pas disponible, améliorant ainsi la cohérence du rendu. Cette nouvelle fonctionnalité améliore le contrôle sur l'apparence de l'image de sortie",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Default Font Name, PDF to image conversion, Aspose.PDF for .NET, RenderingOptions, DefaultFontName property, .NET API",
    "wordcount": "198",
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
    "url": "/net/set-default-font-name/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-default-font-name/"
    },
    "dateModified": "2024-11-26",
    "description": "Cette section décrit comment définir le nom de police par défaut lors du processus de conversion de PDF en image."
}
</script>

**Aspose.PDF for .NET** API vous permet de définir un nom de police par défaut lorsqu'une police n'est pas disponible dans le document. Vous pouvez utiliser la propriété DefaultFontName de la classe RenderingOptions pour définir le nom de police par défaut. Si DefaultFontName est défini sur null, la police **Times New Roman** sera utilisée. Le code suivant montre comment définir un nom de police par défaut lors de l'enregistrement d'un PDF en tant qu'image :

Le code suivant fonctionne également avec la bibliothèque [Aspose.Drawing](/pdf/fr/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPdfToImageWithDefaultFont()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PdfToImageWithDefaultFont.pdf"))
    {
        // Open the image stream
        using (var imageStream = new FileStream(dataDir + "SetDefaultFontName.png", FileMode.Create))
        {
            // Set the resolution for the image
            var resolution = new Aspose.Pdf.Devices.Resolution(300);

            // Create the PNG device and set rendering options
            var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);
            var ro = new Aspose.Pdf.RenderingOptions
            {
                DefaultFontName = "Arial"
            };
            pngDevice.RenderingOptions = ro;

            // Process the first page of the document and save it as an image
            pngDevice.Process(document.Pages[1], imageStream);
        }
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