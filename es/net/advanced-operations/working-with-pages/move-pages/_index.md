---
title: Mover páginas PDF programáticamente C#
linktitle: Mover páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /es/net/move-pages/
description: Intenta mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF for .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move PDF Pages programmatically C#",
    "alternativeHeadline": "Programmatically Rearrange PDF Pages with .NET",
    "abstract": "Aspose.PDF for .NET introduce una nueva característica poderosa que permite a los usuarios mover programáticamente páginas PDF entre documentos o reorganizarlas dentro del mismo documento. Esta funcionalidad mejora las capacidades de manipulación de PDF al permitir a los desarrolladores insertar páginas en ubicaciones designadas y gestionar la organización de páginas sin esfuerzo, manteniendo la integridad del documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "668",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Intenta mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF for .NET."
}
</script>

## Mover una página de un documento PDF a otro

Este tema explica cómo mover una página de un documento PDF al final de otro documento usando C#.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para mover una página debemos:

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de origen.
1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de destino.
1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Agregar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la página al documento de destino.
1. Guardar el PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Eliminar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la página en el documento de origen.
1. Guardar el PDF de origen usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo mover una página.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingPageInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var page = srcDocument.Pages[2];
            dstDocument.Pages.Add(page);
            // Save PDF document
            dstDocument.Save(dataDir + "MovingPage_out.pdf");
            srcDocument.Pages.Delete(2);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingPageInput_out.pdf");
        }
    }
}
```

## Mover un grupo de páginas de un documento PDF a otro

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de origen.
1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de destino.
1. Definir un arreglo con los números de página a mover.
1. Ejecutar un bucle a través del arreglo:
    1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
    1. [Agregar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la página al documento de destino.
1. Guardar el PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Eliminar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) la página en el documento de origen usando el arreglo.
1. Guardar el PDF de origen usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo mover un grupo de páginas de un documento PDF a otro.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingBunchOfPagesFromOnePdfDocumentToAnother()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF documents
    using (var srcDocument = new Aspose.Pdf.Document(dataDir + "MovingBunchOfPagesInput.pdf"))
    {
        using (var dstDocument = new Aspose.Pdf.Document())
        {
            var pages = new[] { 1, 3 };
            foreach (int pageIndex in pages)
            {
                var page = srcDocument.Pages[pageIndex];
                dstDocument.Pages.Add(page);
            }
            // Save PDF document
            dstDocument.Save(dataDir + "MovingBunchOfPages_out.pdf");
            srcDocument.Pages.Delete(pages);
            // Save PDF document
            srcDocument.Save(dataDir + "MovingBunchOfPagesInput_out.pdf";
        }
    }
}
```

## Mover una página a una nueva ubicación en el documento PDF actual

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de origen.
1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Agregar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la página a la nueva ubicación (por ejemplo, al final).
1. [Eliminar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la página en la ubicación anterior.
1. Guardar el PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MovingAPageInNewLocationInTheCurrentPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocumentInput.pdf"))
    {
        var page = document.Pages[2];
        document.Pages.Add(page);
        document.Pages.Delete(2);
        // Save PDF document
        document.Save(dataDir + "MovingAPageInNewLocationInTheCurrentPdfDocument_out.pdf");
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