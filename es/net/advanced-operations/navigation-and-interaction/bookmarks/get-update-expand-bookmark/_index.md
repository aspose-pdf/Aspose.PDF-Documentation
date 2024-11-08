---
title: Añadir y Eliminar un Marcador
linktitle: Añadir y Eliminar un Marcador
type: docs
weight: 10
url: /es/net/add-and-delete-bookmark/
description: Puedes añadir un marcador a un documento PDF con C#. Es posible eliminar todos o ciertos marcadores de un documento PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Añadir y Eliminar un Marcador",
    "alternativeHeadline": "Cómo añadir y eliminar un marcador de un PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, eliminar marcador, añadir marcador",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "Puedes añadir un marcador a un documento PDF con C#. Es posible eliminar todos o ciertos marcadores de un documento PDF."
}
</script>
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/es/net/drawing/).

## Agregar un marcador a un documento PDF

Los marcadores se encuentran en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) del objeto Documento, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Para agregar un marcador a un PDF:

1. Abrir un documento PDF utilizando el objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Crear un marcador y definir sus propiedades.
1. Agregar la colección [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) a la colección de Outlines.

El siguiente fragmento de código muestra cómo agregar un marcador en un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// Crear un objeto de marcador
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Esquema de prueba";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// Establecer el número de página de destino
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// Agregar marcador en la colección de esquemas del documento.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// Guardar salida
pdfDocument.Save(dataDir);
```
## Agregar un marcador hijo al documento PDF

Los marcadores pueden anidarse, indicando una relación jerárquica con marcadores padre e hijo. Este artículo explica cómo agregar un marcador hijo, es decir, un marcador de segundo nivel, a un PDF.

Para agregar un marcador hijo a un archivo PDF, primero agrega un marcador padre:

1. Abre un documento.
1. Agrega un marcador a la [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), definiendo sus propiedades.
1. Agrega la OutlineItemCollection a la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) del objeto Document.

El marcador hijo se crea de la misma manera que el marcador padre, explicado anteriormente, pero se agrega a la colección de Outlines del marcador padre.

Los siguientes fragmentos de código muestran cómo agregar un marcador hijo a un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Crear un objeto de marcador padre
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Esquema Padre";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Crear un objeto de marcador hijo
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Esquema Hijo";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Agregar el marcador hijo en la colección del marcador padre
pdfOutline.Add(pdfChildOutline);
// Agregar el marcador padre en la colección de esquemas del documento.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Guardar salida
pdfDocument.Save(dataDir);
```
## Eliminar todos los marcadores de un documento PDF

Todos los marcadores en un PDF se encuentran en la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Este artículo explica cómo eliminar todos los marcadores de un archivo PDF.

Para eliminar todos los marcadores de un archivo PDF:

1. Llame al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Guarde el archivo modificado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) del objeto [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Los siguientes fragmentos de código muestran cómo eliminar todos los marcadores de un documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// Eliminar todos los marcadores
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// Guardar archivo actualizado
pdfDocument.Save(dataDir);
```
## Eliminar un Marcador Específico de un Documento PDF

Para eliminar un marcador específico de un archivo PDF:

1. Pasa el título del marcador como parámetro al método Delete de la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Luego guarda el archivo actualizado con el método Save del objeto Document.

La clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) proporciona la colección [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). El método [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) elimina cualquier marcador con el título pasado al método.

Los siguientes fragmentos de código muestran cómo eliminar un marcador específico del documento PDF.

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Abrir documento
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// Eliminar un contorno particular por Título
pdfDocument.Outlines.Delete("Child Outline");

// Guardar archivo actualizado
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF para la biblioteca .NET",
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

