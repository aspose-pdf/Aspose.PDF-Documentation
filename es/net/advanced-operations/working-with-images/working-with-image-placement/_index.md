---
title: Trabajando con la Colocación de Imágenes
linktitle: Trabajando con la Colocación de Imágenes
type: docs
weight: 50
url: /es/net/working-with-image-placement/
description: Esta sección describe las características de trabajar con la colocación de imágenes en archivos PDF utilizando la biblioteca C#.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Trabajando con la Colocación de Imágenes",
    "alternativeHeadline": "Cómo obtener la posición de una Imagen en Archivo PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos pdf",
    "keywords": "pdf, c#, colocación de imágenes en pdf",
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
    "url": "/net/working-with-image-placement/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-image-placement/"
    },
    "dateModified": "2022-02-04",
    "description": "Esta sección describe las características de trabajar con la colocación de imágenes en archivos PDF utilizando la biblioteca C#."
}
</script>
Con el lanzamiento de Aspose.PDF para .NET 7.0.0, introdujimos clases llamadas [ImagePlacement](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacement), [ImagePlacementAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementabsorber) y [ImagePlacementCollection](https://reference.aspose.com/pdf/net/aspose.pdf/imageplacementcollection) que ofrecen capacidades similares a las clases descritas anteriormente para obtener la resolución y posición de una imagen en un documento PDF.

- ImagePlacementAbsorber realiza la búsqueda de uso de imagen como la colección de objetos ImagePlacement.
- ImagePlacement proporciona los miembros Resolution y Rectangle que devuelven los valores reales de colocación de imágenes.

El siguiente fragmento de código también funciona con la nueva interfaz gráfica [Aspose.Drawing](/pdf/es/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();


// Cargar el documento PDF fuente
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir+ "ImagePlacement.pdf");
ImagePlacementAbsorber abs = new ImagePlacementAbsorber();

// Cargar el contenido de la primera página
doc.Pages[1].Accept(abs);
foreach (ImagePlacement imagePlacement in abs.ImagePlacements)
{
    // Obtener propiedades de la imagen
    Console.Out.WriteLine("ancho de imagen:" + imagePlacement.Rectangle.Width);
    Console.Out.WriteLine("altura de imagen:" + imagePlacement.Rectangle.Height);
    Console.Out.WriteLine("LLX de imagen:" + imagePlacement.Rectangle.LLX);
    Console.Out.WriteLine("LLY de imagen:" + imagePlacement.Rectangle.LLY);
    Console.Out.WriteLine("resolución horizontal de imagen:" + imagePlacement.Resolution.X);
    Console.Out.WriteLine("resolución vertical de imagen:" + imagePlacement.Resolution.Y);

    // Recuperar imagen con dimensiones visibles
    Bitmap scaledImage;
    using (MemoryStream imageStream = new MemoryStream())
    {
        // Recuperar imagen de recursos
        imagePlacement.Image.Save(imageStream, System.Drawing.Imaging.ImageFormat.Png);
        Bitmap resourceImage = (Bitmap)Bitmap.FromStream(imageStream);
        // Crear bitmap con dimensiones reales
        scaledImage = new Bitmap(resourceImage, (int)imagePlacement.Rectangle.Width, (int)imagePlacement.Rectangle.Height);
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
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/destacado",
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
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
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

