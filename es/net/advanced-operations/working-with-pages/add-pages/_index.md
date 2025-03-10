---
title: Agregar Páginas a Documento PDF
linktitle: Agregar Páginas
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /es/net/add-pages/
description: Explora cómo agregar páginas a un PDF existente en .NET con Aspose.PDF para mejorar y expandir tus documentos.
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
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "La función en Aspose.PDF for .NET permite a los usuarios insertar fácilmente páginas en un documento PDF en cualquier ubicación especificada, mejorando la flexibilidad y organización del documento. Esta funcionalidad no solo admite la adición de páginas, sino que también incluye opciones para mover o eliminar páginas existentes usando C#. Optimiza la gestión de tu PDF con esta adición intuitiva a tu kit de herramientas de desarrollo.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Este artículo enseña cómo insertar (agregar) una página en la ubicación deseada del archivo PDF. Aprende cómo mover, eliminar (borrar) páginas de un archivo PDF usando C#."
}
</script>

Aspose.PDF for .NET API proporciona total flexibilidad para trabajar con páginas en un documento PDF usando C# o cualquier otro lenguaje .NET. Mantiene todas las páginas de un documento PDF en [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) que se puede usar para trabajar con páginas PDF.
Aspose.PDF for .NET te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF.
Esta sección muestra cómo agregar páginas a un PDF usando C#.

## Agregar o Insertar Página en un Archivo PDF

Aspose.PDF for .NET te permite insertar una página en un documento PDF en cualquier ubicación del archivo, así como agregar páginas al final de un archivo PDF.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

Para insertar una página vacía en un archivo PDF:

1. Crea un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de entrada.
1. Llama al método [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) con el índice especificado.
1. Guarda el PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código te muestra cómo insertar una página en un archivo PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

En el ejemplo anterior, agregamos una página vacía con parámetros predeterminados. Si necesitas que el tamaño de la página sea el mismo que otra página en el documento, deberías agregar
unas líneas de código:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### Agregar una Página Vacía al Final de un Archivo PDF

A veces, deseas asegurarte de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Crea un objeto de clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) con el archivo PDF de entrada.
1. Llama al método [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) de la colección [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), sin ningún parámetro.
1. Guarda el PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

El siguiente fragmento de código te muestra cómo insertar una página vacía al final de un archivo PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
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