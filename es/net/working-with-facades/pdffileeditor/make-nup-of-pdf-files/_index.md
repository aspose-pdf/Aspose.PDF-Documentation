---
title: Hacer NUp de archivos PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /es/net/make-nup-of-pdf-files/
description: Este artículo muestra cómo hacer que NUp de archivos PDF funcione con Aspose.PDF Facades utilizando la clase PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "La función NUp en Aspose.PDF for .NET permite a los usuarios combinar de manera eficiente múltiples archivos PDF en un solo documento de salida, personalizando el tamaño de página y las configuraciones de diseño. Esta funcionalidad admite tanto rutas de archivos como flujos, lo que permite una integración flexible en varios flujos de trabajo mientras mejora la presentación del documento.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF puede realizar no solo tareas simples y fáciles, sino también afrontar objetivos más complejos. Consulta la siguiente sección para usuarios y desarrolladores avanzados."
}
</script>

## Hacer NUp de PDF Usando Rutas de Archivos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp del archivo PDF de entrada y guardarlo en el archivo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando rutas de archivos. El siguiente fragmento de código te muestra cómo hacer NUP utilizando rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## Hacer NUp Usando Tamaño de Página y Rutas de Archivos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp del archivo PDF de entrada y guardarlo en el archivo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando rutas de archivos. También puedes establecer el tamaño de página del archivo PDF de salida utilizando esta sobrecarga. El siguiente fragmento de código te muestra cómo hacer NUp utilizando tamaño de página y rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## Hacer NUp de PDF Usando Tamaño de Página, Valores Horizontales y Verticales, y Rutas de Archivos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp del archivo PDF de entrada y guardarlo en el archivo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando rutas de archivos. También puedes establecer el tamaño de página del archivo PDF de salida y el número horizontal y vertical de páginas en cada página de salida utilizando esta sobrecarga. El siguiente fragmento de código te muestra cómo hacer NUp utilizando tamaño de página, valores horizontales y verticales, y rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Hacer NUp de PDF Usando Array de Archivos PDF y Rutas de Archivos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp de un array de archivos PDF de entrada y guardarlos en un solo archivo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando rutas de archivos. El siguiente fragmento de código te muestra cómo hacer NUp utilizando un array de archivos PDF y rutas de archivos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "MakeNupInput.pdf";
    filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Hacer NUp de PDF Usando Flujos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp del flujo PDF de entrada y guardarlo en el flujo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando flujos en lugar de rutas de archivos. El siguiente fragmento de código te muestra cómo hacer NUp utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## Hacer NUp de PDF Usando Tamaño de Página y Flujos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp del flujo PDF de entrada y guardarlo en el flujo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando flujos en lugar de rutas de archivos. También puedes establecer el tamaño de página del flujo PDF de salida utilizando esta sobrecarga. El siguiente fragmento de código te muestra cómo hacer NUp utilizando tamaño de página y flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## Hacer NUp de PDF Usando Tamaño de Página, Valores Horizontales y Verticales, y Flujos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp del flujo PDF de entrada y guardarlo en el flujo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando flujos en lugar de rutas de archivos. También puedes establecer el tamaño de página del flujo PDF de salida y el número horizontal y vertical de páginas en cada página de salida utilizando esta sobrecarga. El siguiente fragmento de código te muestra cómo hacer NUp utilizando tamaño de página, valores horizontales y verticales, y flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3); 
        }
    }
}
```

## Hacer NUp de PDF Usando Array de Archivos PDF y Flujos

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) método de la clase [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) te permite hacer NUp de un array de flujos PDF de entrada y guardarlos en un solo flujo PDF de salida. Esta sobrecarga te permite hacer NUp utilizando flujos en lugar de rutas de archivos. El siguiente fragmento de código te muestra cómo hacer NUp utilizando un array de archivos PDF utilizando flujos.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var stream1 = new FileStream(dataDir + "MakeNupInput.pdf", FileMode.Open))
    {
        using (var stream2 = new FileStream(dataDir + "MakeNupInput2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", FileMode.Create))
            {
                var fileStreams = new Stream[2];
                fileStreams[0] = stream1;
                fileStreams[1] = stream2;
                // Make NUp
                pdfEditor.MakeNUp(fileStreams, outputStream, true);
            }
        }
    }
}
```