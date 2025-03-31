---
title: Extraer páginas de PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/extract-pdf-pages/
description: Esta sección explica cómo extraer páginas de PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract PDF pages",
    "alternativeHeadline": "Effortlessly Extract Selected Pages from PDF Files",
    "abstract": "La función Extraer Páginas de PDF en Aspose.PDF for .NET Facades proporciona a los usuarios capacidades mejoradas para extraer selectivamente páginas de documentos PDF. Al utilizar la clase PdfFileEditor, los usuarios pueden extraer de manera eficiente un rango especificado o un conjunto de páginas a través de rutas de archivos o flujos, lo que hace que la manipulación de documentos sea más fluida y flexible. Esta funcionalidad es particularmente beneficiosa para los usuarios que buscan personalizar su contenido PDF sin alterar los archivos originales.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "660",
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
    "url": "/net/extract-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulte la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Extraer páginas de PDF entre dos números utilizando rutas de archivos

El método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor) permite extraer un rango especificado de páginas de un archivo PDF. Esta sobrecarga permite extraer páginas mientras se manipulan los archivos PDF desde el disco. Esta sobrecarga requiere los siguientes parámetros: ruta del archivo de entrada, página de inicio, página final y ruta del archivo de salida. Las páginas desde la página de inicio hasta la página final serán extraídas y la salida se guardará en el disco. El siguiente fragmento de código muestra cómo extraer páginas de PDF entre dos números utilizando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Extract pages
    pdfEditor.Extract(dataDir + "MultiplePages.pdf", 1, 3, dataDir + "ExtractPagesBetweenNumbers_out.pdf");
}
```

## Extraer un array de páginas de PDF utilizando rutas de archivos

Si no desea extraer un rango de páginas, sino un conjunto de páginas particulares, el método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) también permite hacerlo. Primero necesita crear un array de enteros con todos los números de página que necesitan ser extraídos. Esta sobrecarga del método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) toma los siguientes parámetros: archivo PDF de entrada, array de enteros de páginas a extraer y archivo PDF de salida. El siguiente fragmento de código muestra cómo extraer páginas de PDF utilizando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_PDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();

    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractPagesBetweenTwoNumbers_out.pdf", FileMode.Create))
        {
            // Extract pages
            pdfEditor.Extract(inputStream, 1, 3, outputStream);
        }
    }
}
```

## Extraer páginas de PDF entre dos números utilizando flujos

El método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor) permite extraer un rango de páginas utilizando flujos. Necesita pasar los siguientes parámetros a esta sobrecarga: flujo de entrada, página de inicio, página final y flujo de salida. Las páginas especificadas por el rango entre la página de inicio y la página final serán extraídas del flujo de entrada y guardadas en el flujo de salida. El siguiente fragmento de código muestra cómo extraer páginas de PDF entre dos números utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_FilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();

    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    int[] pagesToExtract = new int[] { 1, 2 };
    // Extract pages
    pdfEditor.Extract(dataDir + "Extract.pdf", pagesToExtract, dataDir + "ExtractArrayOfPages_out.pdf");
}
```

## Extraer un array de páginas de PDF utilizando flujos

Un array de páginas puede ser extraído del flujo PDF y guardado en el flujo de salida utilizando la sobrecarga apropiada del método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index). Si no desea extraer un rango de páginas, sino un conjunto de páginas particulares, el método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) también permite hacerlo. Primero necesita crear un array de enteros con todos los números de página que necesitan ser extraídos. Esta sobrecarga del método [Extract](https://reference.aspose.com/pdf/es/net/aspose.pdf.facades/pdffileeditor/methods/extract/index) toma los siguientes parámetros: flujo de entrada, array de enteros de páginas a extraer y flujo de salida. El siguiente fragmento de código muestra cómo extraer páginas de PDF utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Extract_ArrayPDFPages_Streams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    
    // Create PdfFileEditor object
    PdfFileEditor pdfEditor = new PdfFileEditor();
    // Create streams
    using (FileStream inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (FileStream outputStream = new FileStream(dataDir + "ExtractArrayOfPagesUsingStreams_out.pdf", FileMode.Create))
        {
            int[] pagesToExtract = new int[] { 1, 2 };
            // Extract pages
            pdfEditor.Extract(inputStream, pagesToExtract, outputStream);
        }
    }
}
```