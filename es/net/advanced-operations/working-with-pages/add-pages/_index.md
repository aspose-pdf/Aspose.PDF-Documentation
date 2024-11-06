---
title: Añadir Páginas al Documento PDF
linktitle: Añadir Páginas
type: docs
weight: 10
url: es/net/add-pages/
description: Este artículo enseña cómo insertar (añadir) una página en la ubicación deseada del archivo PDF. Aprende cómo mover, eliminar (borrar) páginas de un archivo PDF usando C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir Páginas en PDF con C#",
    "alternativeHeadline": "Cómo añadir Páginas en un documento PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, añadir página pdf, insertar página pdf",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artículo enseña cómo insertar (añadir) una página en la ubicación deseada del archivo PDF. Aprende cómo mover, eliminar (borrar) páginas de un archivo PDF usando C#."
}
</script>
Aspose.PDF para .NET API proporciona total flexibilidad para trabajar con páginas en un documento PDF usando C# u otro lenguaje .NET. Mantiene todas las páginas de un documento PDF en [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que se puede utilizar para trabajar con páginas PDF.
Aspose.PDF para .NET le permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF.
Esta sección muestra cómo agregar páginas a un PDF usando C#.

## Agregar o Insertar Página en un Archivo PDF

Aspose.PDF para .NET le permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

Para insertar una página vacía en un archivo PDF:

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de entrada.
1.
1. Guarde el PDF de salida utilizando el método [Guardar](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código le muestra cómo insertar una página en un archivo PDF.

```cs
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Abrir documento
Document pdfDocument = new Document(dataDir + "InsertEmptyPage.pdf");

// Insertar una página vacía en un PDF
pdfDocument.Pages.Insert(2);
// Guardar archivo de salida
pdfDocument.Save(dataDir + "InsertEmptyPage_out.pdf");
```

En el ejemplo anterior, agregamos una página vacía con parámetros predeterminados. Si necesita hacer que el tamaño de la página sea el mismo que otra página en el documento, debe agregar algunas líneas de código:

```cs
var page = pdfDocument.Pages.Insert(2);
//copiar parámetros de página de la página 1
page.ArtBox = pdfDocument.Pages[1].ArtBox;
page.BleedBox = pdfDocument.Pages[1].BleedBox;
page.CropBox = pdfDocument.Pages[1].CropBox;
page.MediaBox = pdfDocument.Pages[1].MediaBox;
page.TrimBox = pdfDocument.Pages[1].TrimBox;
```
### Agregar una Página Vacía al Final de un Archivo PDF

A veces, quieres asegurarte de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de entrada.
1. Llama al método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), sin ningún parámetro.
1. Guarda el PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código te muestra cómo insertar una página vacía al final de un archivo PDF.

```cs
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// Abrir documento
Document pdfDocument = new Document(dataDir + "InsertEmptyPageAtEnd.pdf");

// Insertar una página vacía al final de un archivo PDF
pdfDocument.Pages.Add();

// Guardar archivo de salida
pdfDocument.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
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

