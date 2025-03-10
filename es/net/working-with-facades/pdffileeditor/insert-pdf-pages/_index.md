---
title: Insertar páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /es/net/insert-pdf-pages/
description: Esta sección explica cómo insertar páginas PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Insert PDF pages",
    "alternativeHeadline": "Insert Specific PDF Pages into Existing Documents",
    "abstract": "Optimiza tu gestión de PDF con la nueva función que permite a los usuarios insertar páginas específicas de un PDF en otro utilizando la clase PdfFileEditor. Esta funcionalidad admite tanto la inserción de páginas basada en rangos como en arreglos, mejorando la eficiencia del flujo de trabajo al combinar documentos sin problemas a través de rutas de archivos o flujos.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "751",
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
    "url": "/net/insert-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/insert-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Insertar páginas PDF entre dos números utilizando rutas de archivos

Se puede insertar un rango particular de páginas de un PDF en otro utilizando el método [Insertar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para ello, necesitas un archivo PDF de entrada en el que deseas insertar las páginas, un archivo de puerto del cual se deben tomar las páginas para la inserción, una ubicación donde se deben insertar las páginas y un rango de páginas del archivo de puerto que deben insertarse en el archivo PDF de entrada. Este rango se especifica con los parámetros de página de inicio y página final. Finalmente, el archivo PDF de salida se guarda con el rango especificado de páginas insertadas en el archivo de entrada. El siguiente fragmento de código te muestra cómo insertar páginas PDF entre dos números utilizando flujos de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", 2, 5, 
        dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## Insertar un arreglo de páginas PDF utilizando rutas de archivos

Si deseas insertar algunas páginas específicas en otro archivo PDF, puedes utilizar una sobrecarga del método [Insertar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) que requiere un arreglo de enteros de páginas. En este arreglo, puedes especificar qué páginas particulares deseas insertar en el archivo PDF de entrada. Para ello, necesitas un archivo PDF de entrada en el que deseas insertar las páginas, un archivo de puerto del cual se deben tomar las páginas para la inserción, una ubicación donde se deben insertar las páginas y un arreglo de enteros de las páginas del archivo de puerto que deben insertarse en el archivo PDF de entrada. Este arreglo contiene una lista de páginas particulares que te interesa insertar en el archivo PDF de entrada. Finalmente, el archivo PDF de salida se guarda con el arreglo especificado de páginas insertadas en el archivo de entrada. El siguiente fragmento de código te muestra cómo insertar un arreglo de páginas PDF utilizando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var pagesToInsert = new int[] { 2, 3 };
    // Insert pages
    pdfEditor.Insert(
        dataDir + "MultiplePages.pdf", 1, 
        dataDir + "InsertPages.pdf", pagesToInsert, 
        dataDir + "InsertArrayOfPages_out.pdf");
}
```

## Insertar páginas PDF entre dos números utilizando flujos

Si deseas insertar el rango de páginas utilizando flujos, solo necesitas usar la sobrecarga apropiada del método [Insertar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/insert/index) de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor). Para ello, necesitas un flujo PDF de entrada en el que deseas insertar las páginas, un flujo de puerto del cual se deben tomar las páginas para la inserción, una ubicación donde se deben insertar las páginas y un rango de páginas del flujo de puerto que deben insertarse en el flujo PDF de entrada. Este rango se especifica con los parámetros de página de inicio y página final. Finalmente, el flujo PDF de salida se guarda con el rango especificado de páginas insertadas en el flujo de entrada. El siguiente fragmento de código te muestra cómo insertar páginas PDF entre dos números utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, 1, 4, outputStream);
            }
        }
    }
}
```

## Insertar un arreglo de páginas PDF utilizando flujos

También puedes insertar un arreglo de páginas en otro archivo PDF utilizando flujos con la ayuda de la sobrecarga apropiada del método Insertar que requiere un arreglo de enteros de páginas. En este arreglo, puedes especificar qué páginas particulares deseas insertar en el flujo PDF de entrada. Para ello, necesitas un flujo PDF de entrada en el que deseas insertar las páginas, un flujo de puerto del cual se deben tomar las páginas para la inserción, una ubicación donde se deben insertar las páginas y un arreglo de enteros de las páginas del flujo de puerto que deben insertarse en el archivo PDF de entrada. Este arreglo contiene una lista de páginas particulares que te interesa insertar en el flujo PDF de entrada. Finalmente, el flujo PDF de salida se guarda con el arreglo especificado de páginas insertadas en el archivo de entrada. El siguiente fragmento de código te muestra cómo insertar un arreglo de páginas PDF utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertArrayOfPdfPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Pages to insert
    var pagesToInsert = new int[] { 2, 3 };
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var portStream = new FileStream(dataDir + "InsertPages.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "InsertPagesUsingStreams_out.pdf", FileMode.Create))
            {
                // Insert pages
                pdfEditor.Insert(inputStream, 1, portStream, pagesToInsert, outputStream);
            }
        }
    }
}
```