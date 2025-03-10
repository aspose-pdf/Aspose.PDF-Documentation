---
title: Dividir páginas PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /es/net/split-pdf-pages/
description: Esta sección explica cómo dividir páginas PDF con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "La nueva función Dividir Páginas PDF en Aspose.PDF for .NET permite a los usuarios dividir eficientemente documentos PDF en varios segmentos utilizando la clase PdfFileEditor. Esta funcionalidad admite la división desde la primera página hasta una página especificada, la división en conjuntos masivos e incluso la aislamiento de páginas individuales, todo a través de rutas de archivos o flujos, proporcionando opciones versátiles para la manipulación de PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también hacer frente a objetivos más complejos. Consulta la siguiente sección para usuarios avanzados y desarrolladores."
}
</script>

## Dividir Páginas PDF desde el Inicio Usando Rutas de Archivos

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir el archivo PDF comenzando desde la primera página y terminando en el número de página especificado. Si deseas manipular los archivos PDF desde el disco, puedes pasar las rutas de archivo de los archivos PDF de entrada y salida a este método. El siguiente fragmento de código te muestra cómo dividir páginas PDF desde el inicio usando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");
}
```

## Dividir Páginas PDF desde el Inicio Usando Flujos de Archivos

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir el archivo PDF comenzando desde la primera página y terminando en el número de página especificado. Si deseas manipular los archivos PDF desde los flujos, puedes pasar los flujos de entrada y salida PDF a este método. El siguiente fragmento de código te muestra cómo dividir páginas PDF desde el inicio usando flujos de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitFromFirst(inputStream, 3, outputStream);
        }
    }
}
```

## Dividir Páginas PDF a Granel Usando Rutas de Archivos

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir el archivo PDF en múltiples conjuntos de páginas. En este ejemplo, requerimos dos conjuntos de páginas (1, 2) y (5, 6). Si deseas acceder al archivo PDF desde el disco, necesitas pasar el PDF de entrada como ruta de archivo. Este método devuelve un arreglo de MemoryStream. Puedes recorrer este arreglo y guardar los conjuntos individuales de páginas como archivos separados. El siguiente fragmento de código te muestra cómo dividir páginas PDF a granel usando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Create array of pages to split
    var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
    // Split to bulk
    var outBuffer = pdfEditor.SplitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Dividir Páginas PDF a Granel Usando Flujos

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittobulks/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir el archivo PDF en múltiples conjuntos de páginas. En este ejemplo, requerimos dos conjuntos de páginas (1, 2) y (5, 6). Puedes pasar un flujo a este método en lugar de acceder al archivo desde el disco. Este método devuelve un arreglo de MemoryStream. Puedes recorrer este arreglo y guardar los conjuntos individuales de páginas como archivos separados. El siguiente fragmento de código te muestra cómo dividir páginas PDF a granel usando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Create array of pages to split
        var numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
        // Split to bulk
        var outBuffer = pdfEditor.SplitToBulks(inputStream, numberOfPages);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```

## Dividir Páginas PDF hasta el Final Usando Rutas de Archivos

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittoend/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir el PDF desde el número de página especificado hasta el final del archivo PDF y guardarlo como un nuevo PDF. Para hacer esto, usando rutas de archivos, necesitas pasar las rutas de archivo de entrada y salida y el número de página desde donde se debe iniciar la división. El PDF de salida se guardará en el disco. El siguiente fragmento de código te muestra cómo dividir páginas PDF hasta el final usando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Split pages
    pdfEditor.SplitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## Dividir Páginas PDF hasta el Final Usando Flujos

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/splittoend/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) permite dividir el PDF desde el número de página especificado hasta el final del archivo PDF y guardarlo como un nuevo PDF. Para hacer esto, usando flujos, necesitas pasar flujos de entrada y salida y el número de página desde donde se debe iniciar la división. El PDF de salida se guardará en el flujo de salida. El siguiente fragmento de código te muestra cómo dividir páginas PDF hasta el final usando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MultiplePages.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "SplitPagesToEndUsingStreams_out.pdf", FileMode.Create))
        {
            // Split pages
            pdfEditor.SplitToEnd(inputStream, 3, outputStream);   
        }
    }
}
```

## Dividir PDF a Páginas Individuales Usando Rutas de Archivos

{{% alert color="primary" %}}

Puedes intentar dividir el documento PDF y ver los resultados en línea en este enlace:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

Para dividir el archivo PDF en páginas individuales, necesitas pasar el PDF como ruta de archivo al método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método devolverá un arreglo de MemoryStream que contiene las páginas individuales del archivo PDF. Puedes recorrer este arreglo de MemoryStream y guardar las páginas individuales como archivos PDF individuales en el disco. El siguiente fragmento de código te muestra cómo dividir PDF en páginas individuales usando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    var fileNumber = 1;
    // Split to pages
    var outBuffer = pdfEditor.SplitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
    // Save individual files
    foreach (var outStream in outBuffer)
    {
        using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
        {
            outStream.WriteTo(outFileStream);
            fileNumber++;
        }
    }
}
```

## Dividir PDF a Páginas Individuales Usando Flujos

Para dividir el archivo PDF en páginas individuales, necesitas pasar el PDF como flujo al método [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index). Este método devolverá un arreglo de MemoryStream que contiene las páginas individuales del archivo PDF. Puedes recorrer este arreglo de MemoryStream y guardar las páginas individuales como archivos PDF individuales en el disco, o puedes mantener estas páginas individuales en el flujo de memoria para su uso posterior en tu aplicación. El siguiente fragmento de código te muestra cómo dividir PDF en páginas individuales usando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create input stream
    using (var inputStream = new FileStream(dataDir + "splitPdfToIndividualPagesInput.pdf", FileMode.Open))
    {
        var fileNumber = 1;
        // Split to pages
        var outBuffer = pdfEditor.SplitToPages(inputStream);
        // Save individual files
        foreach (var outStream in outBuffer)
        {
            using (var outFileStream = new FileStream(dataDir + "File_" + fileNumber.ToString() + "_out.pdf", FileMode.Create))
            {
                outStream.WriteTo(outFileStream);
                fileNumber++;
            }
        }
    }
}
```