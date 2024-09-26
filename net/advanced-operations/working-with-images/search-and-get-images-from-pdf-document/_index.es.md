---
title: Obtener y Buscar Imágenes en PDF
linktitle: Buscar y Obtener Imágenes
type: docs
weight: 60
url: /net/search-and-get-images-from-pdf-document/
description: Esta sección explica cómo buscar y obtener imágenes de un documento PDF con la biblioteca Aspose.PDF.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Obtener y Buscar Imágenes en PDF",
    "alternativeHeadline": "Cómo Obtener y Buscar Imágenes en un archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, .net, obtener imagen, buscar imagen",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "dateModified": "2022-02-04",
    "description": "Esta sección explica cómo buscar y obtener imágenes de un documento PDF con la biblioteca Aspose.PDF."
}
</script>
El ImagePlacementAbsorber te permite buscar entre imágenes en todas las páginas de un documento PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para buscar un documento completo por imágenes:

1. Llamar al método Accept de la colección Pages. El método Accept toma un objeto ImagePlacementAbsorber como parámetro. Esto devuelve una colección de objetos ImagePlacement.
1. Recorrer los objetos ImagePlacements y obtener sus propiedades (imagen, dimensiones, resolución, etc.).

El siguiente fragmento de código muestra cómo buscar un documento por todas sus imágenes.

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// Abrir documento
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "SearchAndGetImages.pdf");

// Crear un objeto ImagePlacementAbsorber para realizar la búsqueda de colocación de imágenes
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Aceptar el absorber para todas las páginas
doc.Pages.Accept(abs);

// Recorrer todos los ImagePlacements, obtener la imagen y las propiedades de ImagePlacement
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Obtener la imagen usando el objeto ImagePlacement
    XImage image = imagePlacement.Image;

    // Mostrar las propiedades de colocación de imágenes para todas las colocaciones
    Console.Out.WriteLine("ancho de la imagen:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("altura de la imagen:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("LLX de la imagen:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("LLY de la imagen:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("resolución horizontal de la imagen:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("resolución vertical de la imagen:" + imagePlacement.Resolution.Y);
}
```
Para obtener una imagen de una página individual, utiliza el siguiente código:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
doc.Pages[1].Accept(abs);
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
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
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
    "applicationCategory": "Biblioteca de Manipulación de PDF para .NET",
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


