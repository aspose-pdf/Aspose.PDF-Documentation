---
title: Ajouter un arrière-plan au PDF
linktitle: Ajouter des arrière-plans
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /fr/net/add-backgrounds/
description: Ajoutez une image d'arrière-plan à votre fichier PDF avec C#. Utilisez l'objet BackgroundArtifact.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add background to PDF",
    "alternativeHeadline": "Add Custom Backgrounds to PDFs with C#",
    "abstract": "Présentation de la possibilité d'intégrer sans effort des images d'arrière-plan dans vos documents PDF en utilisant C# avec Aspose.PDF for .NET. Cette fonctionnalité utilise l'objet BackgroundArtifact, permettant des options de conception améliorées telles que des filigranes ou un texturage subtil, parfait pour faire ressortir vos PDF avec un minimum d'effort. Découvrez comment élever vos mises en page de documents en ajoutant des arrière-plans personnalisés sans effort.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add background to PDF, BackgroundArtifact object, PDF manipulation, C# PDF library, watermark in PDF, Aspose.PDF for .NET, add background image, PDF document generation, PDF artifacts, document background settings",
    "wordcount": "228",
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
    "url": "/net/add-backgrounds/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-backgrounds/"
    },
    "dateModified": "2024-11-26",
    "description": "Ajoutez une image d'arrière-plan à votre fichier PDF avec C#. Utilisez l'objet BackgroundArtifact."
}
</script>

Les images d'arrière-plan peuvent être utilisées pour ajouter un filigrane ou un autre design subtil aux documents. Dans Aspose.PDF for .NET, chaque document PDF est une collection de pages et chaque page contient une collection d'artefacts. La classe [BackgroundArtifact](https://reference.aspose.com/pdf/net/aspose.pdf/backgroundartifact) peut être utilisée pour ajouter une image d'arrière-plan à un objet page.

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

Le code suivant montre comment ajouter une image d'arrière-plan aux pages PDF en utilisant l'objet BackgroundArtifact avec C#.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddBackgroundToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Image for background artifact object
        using (var image = File.OpenRead(dataDir + "aspose-total-for-net.jpg"))
        {
            // Add page
            Page page = document.Pages.Add();
            // Create Background Artifact object
            var background = new Aspose.Pdf.BackgroundArtifact();
            // Specify the image for background artifact object
            background.BackgroundImage = image;
            // Add background artifact to artifacts collection of page
            page.Artifacts.Add(background);
            // Save PDF document
            document.Save(dataDir + "ImageAsBackground_out.pdf");
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