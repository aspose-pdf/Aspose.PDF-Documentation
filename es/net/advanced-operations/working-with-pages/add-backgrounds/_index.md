---
title: Agregar fondo a PDF
linktitle: Agregar fondos
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /es/net/add-backgrounds/
description: Agregar imagen de fondo a su archivo PDF con C#. Utilice el objeto BackgroundArtifact.
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
    "abstract": "Presentando la capacidad de integrar sin problemas imágenes de fondo en sus documentos PDF utilizando C# con Aspose.PDF for .NET. Esta función utiliza el objeto BackgroundArtifact, lo que permite opciones de diseño mejoradas como marcas de agua o texturización sutil, perfecto para hacer que sus PDFs se destaquen con un esfuerzo mínimo. Descubra cómo elevar el diseño de sus documentos agregando fondos personalizados sin esfuerzo.",
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
    "description": "Agregar imagen de fondo a su archivo PDF con C#. Utilice el objeto BackgroundArtifact."
}
</script>

Las imágenes de fondo se pueden utilizar para agregar una marca de agua u otro diseño sutil a los documentos. En Aspose.PDF for .NET, cada documento PDF es una colección de páginas y cada página contiene una colección de artefactos. La clase [BackgroundArtifact](https://reference.aspose.com/pdf/es/net/aspose.pdf/backgroundartifact) se puede utilizar para agregar una imagen de fondo a un objeto de página.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

El siguiente fragmento de código muestra cómo agregar una imagen de fondo a las páginas PDF utilizando el objeto BackgroundArtifact con C#.

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