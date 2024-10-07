---
title: Mover páginas PDF programáticamente C#
linktitle: Mover páginas PDF
type: docs
weight: 20
url: /net/move-pages/
description: Intente mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mover páginas PDF programáticamente C#",
    "alternativeHeadline": "Cómo mover páginas PDF con .NET",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, mover página pdf",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Intente mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para .NET."
}
</script>
## Mover una Página de un Documento PDF a Otro

Este tema explica cómo mover una página de un documento PDF al final de otro documento utilizando C#.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

Para mover una página debemos:

1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF fuente.
1. Crear un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF destino.
1. Obtener la Página de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Añadir](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la página al documento destino.
1. Guardar el PDF resultante usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Eliminar](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la página en el documento fuente.
1.
1.

El siguiente fragmento de código te muestra cómo mover una página.

```csharp
var srcFileName = "<ingresa el nombre del archivo>";
var dstFileName = "<ingresa el nombre del archivo>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// Guardar el archivo de salida
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## Mover un conjunto de páginas de un documento PDF a otro

1. Crea un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF fuente.
1. Crea un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF destino.
1. Define un arreglo con los números de página a mover.
1. Ejecutar bucle a través del arreglo:
    1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. Guarde el PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).
1. [Elimine](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) la página en el documento fuente usando un array.
1. Guarde el PDF fuente utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código muestra cómo mover un conjunto de páginas de un documento PDF a otro.

```csharp
var srcFileName = "<ingrese el nombre del archivo>";
var dstFileName = "<ingrese el nombre del archivo>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// Guardar archivos de salida
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## Mover una Página a una nueva ubicación en el documento PDF actual

1.
1. Obtén la página de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection).
1. [Añade](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) la página a la nueva ubicación (por ejemplo, al final).
1. [Elimina](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1) la página en la ubicación anterior.
1. Guarda el PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

```csharp
var srcFileName = "<enter file name>";
var dstFileName = "<enter file name>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Guardar archivo de salida
srcDocument.Save(dstFileName);
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

