---
title: Rotación de sello alrededor del punto central
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/rotating-stamp-about-the-center-point/
description: Esta sección explica cómo rotar un sello alrededor del punto central utilizando la clase Stamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Rotating stamp about the center point",
    "alternativeHeadline": "Rotate Stamps Precisely Around Their Center Point",
    "abstract": "La función en Aspose.PDF for .NET permite a los usuarios rotar sellos dentro de archivos PDF con precisión alrededor de su punto central. Utilizando la clase Stamp, los desarrolladores pueden establecer fácilmente valores de rotación de 0 a 360 grados, mejorando la flexibilidad y personalización de la colocación de marcas de agua en documentos. Esta funcionalidad es ideal para crear PDFs visualmente dinámicos con orientaciones de sello personalizadas.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "339",
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
    "url": "/net/rotating-stamp-about-the-center-point/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/rotating-stamp-about-the-center-point/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

{{% alert color="primary" %}}

[El espacio de nombres Aspose.Pdf.Facades](https://reference.aspose.com/pdf/net/aspose.pdf.facades) en [Aspose.PDF for .NET](/pdf/net/) le permite agregar un sello en un archivo PDF existente. A veces, los usuarios necesitan rotar el sello. En este artículo, veremos cómo rotar un sello alrededor de su punto central.

{{% /alert %}}

## Detalles de implementación

La clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) le permite agregar una marca de agua en un archivo PDF. Puede especificar la imagen que se agregará como un sello utilizando el método [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.stamp/bindimage/methods/1). El método [SetOrigin](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) le permite establecer el origen del sello agregado; este origen son las coordenadas inferiores izquierdas del sello. También puede establecer el tamaño de la imagen utilizando el método [SetImageSize](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setimagesize).

Ahora, veremos cómo se puede rotar el sello alrededor del centro del sello. La clase [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) proporciona una propiedad llamada Rotation. Esta propiedad establece o obtiene la rotación de 0 a 360 del contenido del sello. Podemos especificar cualquier valor de rotación de 0 a 360. Al especificar el valor de rotación, podemos rotar el sello alrededor de su punto central. Si un Sello es un objeto del tipo Stamp, entonces el valor de rotación se puede especificar como aStamp.Rotation = 90. En este caso, el sello se rotará 90 grados alrededor del centro del contenido del sello. El siguiente fragmento de código le muestra cómo rotar el sello alrededor del punto central:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRotatingStampToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();  

    // Create PdfFileInfo object to get height and width of the pages
    using (var fileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "RotatingStamp.pdf"))
    {
        // Create Stamp object
        var aStamp = new Aspose.Pdf.Facades.Stamp();

        // Bind image file with the Stamp object
        aStamp.BindImage(dataDir + "RotatingStamp.jpg");

        // Specify whether the stamp will be added as a background or not
        aStamp.IsBackground = false;

        // Specifies at which pages to add the watermark
        aStamp.Pages = new int[] { 1 };

        // Specifies the watermark rotation - rotate at 90 degrees
        aStamp.Rotation = 90;

        // Specifies the position of stamp - lower left corner of the stamp
        aStamp.SetOrigin(fileInfo.GetPageWidth(1) / 2, fileInfo.GetPageHeight(1) / 2);

        // Set the size of the watermark
        aStamp.SetImageSize(100, 100);

        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "RotatingStamp_out.pdf"))
        {
            // Create PdfFileStamp class to bind input and output files
            using (var stamper = new Aspose.Pdf.Facades.PdfFileStamp(document))
            {
                // Add the stamp in the PDF file
                stamper.AddStamp(aStamp);
            }
        }
    }
}
```