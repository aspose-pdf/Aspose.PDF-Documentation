---
title: Obtener y Buscar Imágenes en PDF
linktitle: Buscar y Obtener Imágenes
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /es/net/search-and-get-images-from-pdf-document/
description: Aprenda cómo buscar y extraer imágenes de un documento PDF en Java utilizando Aspose.PDF para la recuperación de medios.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Search Images in PDF",
    "alternativeHeadline": "Effortlessly Extract Images from PDF Documents",
    "abstract": "Descubra la nueva capacidad de buscar y extraer imágenes de documentos PDF utilizando la biblioteca Aspose.PDF. Esta función simplifica el proceso de localización de imágenes en múltiples páginas, permitiendo a los usuarios recuperar fácilmente propiedades de imagen como dimensiones y resolución con fragmentos de código simples. Mejore sus habilidades de manipulación de documentos PDF aprovechando esta funcionalidad eficiente de manejo de imágenes.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "get images, search images, PDF document, Aspose.PDF library, ImagePlacementAbsorber, ImagePlacements, .NET PDF manipulation, document image extraction, image placement properties, code examples",
    "wordcount": "316",
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
    "url": "/net/search-and-get-images-from-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/search-and-get-images-from-pdf-document/"
    },
    "dateModified": "2024-11-26",
    "description": "Esta sección explica cómo buscar y obtener imágenes de un documento PDF con la biblioteca Aspose.PDF."
}
</script>

El ImagePlacementAbsorber le permite buscar entre imágenes en todas las páginas de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para buscar imágenes en todo un documento:

1. Llame al método Accept de la colección Pages. El método Accept toma un objeto ImagePlacementAbsorber como parámetro. Esto devuelve una colección de objetos ImagePlacement.
1. Recorra los objetos ImagePlacements y obtenga sus propiedades (Imagen, dimensiones, resolución, etc.).

El siguiente fragmento de código muestra cómo buscar un documento para todas sus imágenes.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf"))
    {
        // Create ImagePlacementAbsorber object to perform image placement search
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(abs);

        // Loop through all ImagePlacements, get image and ImagePlacement properties
        foreach (var imagePlacement in abs.ImagePlacements)
        {
            // Get the image using ImagePlacement object
            var image = imagePlacement.Image;

            // Display image placement properties for all placements
            Console.Out.WriteLine("image width: " + imagePlacement.Rectangle.Width);
            Console.Out.WriteLine("image height: " + imagePlacement.Rectangle.Height);
            Console.Out.WriteLine("image LLX: " + imagePlacement.Rectangle.LLX);
            Console.Out.WriteLine("image LLY: " + imagePlacement.Rectangle.LLY);
            Console.Out.WriteLine("image horizontal resolution: " + imagePlacement.Resolution.X);
            Console.Out.WriteLine("image vertical resolution: " + imagePlacement.Resolution.Y);
        }
    }
}

```

Para obtener una imagen de una página individual, use el siguiente código:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImageFromAnIndividualPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchAndGetImages.pdf"))
    {
        // Create ImagePlacementAbsorber object to perform image placement search
        var abs = new Aspose.Pdf.ImagePlacementAbsorber();

        // Accept the absorber for all the pages
        document.Pages[1].Accept(abs);
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