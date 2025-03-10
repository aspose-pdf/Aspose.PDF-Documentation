---
title: Cómo imprimir un archivo PDF en .NET Core
linktitle: Imprimir PDF en .NET Core
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /es/net/print-dotnetcore/
description: Esta página explica cómo convertir un documento PDF en XPS en .NET Core y agregarlo como un trabajo a la cola de la impresora local.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to print PDF file in .NET Core",
    "alternativeHeadline": "Print PDFs as XPS in .NET Core with ease",
    "abstract": "Descubre la nueva funcionalidad en .NET Core que simplifica el proceso de impresión de documentos PDF al convertirlos a formato XPS y gestionar eficientemente los trabajos de impresión en la cola de tu impresora local. Esta característica también permite un control mejorado sobre las fuentes de papel según los tamaños de página PDF, asegurando una experiencia de impresión personalizada. Optimiza la gestión de tus documentos con opciones de escalado precisas directamente desde el diálogo de impresión.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print PDF, .NET Core, convert PDF to XPS, print queue, Aspose.PDF, paper source by PDF page size, print dialog presets, page scaling, document printing, local printer",
    "wordcount": "606",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2024-11-25",
    "description": "Esta página explica cómo convertir un documento PDF en XPS y agregarlo como un trabajo a la cola de la impresora local."
}
</script>

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **Imprimir documento Pdf en .NET Core**

La biblioteca Aspose.PDF nos permite convertir archivos PDF a XPS. Esta función puede ser útil para organizar la impresión de documentos. Veamos un ejemplo de uso de la impresora predeterminada.

En este ejemplo, convertimos un documento PDF en XPS y lo agregamos como un trabajo a la cola de la impresora local:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithNetCore()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the secondary thread and pass the printing method for
    // the constructor's ThreadStart delegate parameter.
    var printingThread = new Thread(() => PrintPDF(dataDir + "PrintDocument.pdf"));

    // Set the thread that will use PrintQueue.AddJob to single threading.
    printingThread.SetApartmentState(ApartmentState.STA);

    // Start the printing thread. The method passed to the Thread
    // constructor will execute.
    printingThread.Start();

    // Wait for the printing thread to finish its work
    printingThread.Join();
}

private static void PrintPDF(string pdfFileName)
{
    // Create print server and print queue.
    var defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

    // Convert PDF to XPS
    using (var document = new Aspose.Pdf.Document(pdfFileName))
    {
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName, SaveFormat.Xps);

        // Print the Xps file while providing XPS validation and progress notifications.
        using (PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false))
        {
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithNetCore()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the secondary thread and pass the printing method for
    // the constructor's ThreadStart delegate parameter.
    var printingThread = new Thread(() => PrintPDF(dataDir + "PrintDocument.pdf"));

    // Set the thread that will use PrintQueue.AddJob to single threading.
    printingThread.SetApartmentState(ApartmentState.STA);

    // Start the printing thread. The method passed to the Thread
    // constructor will execute.
    printingThread.Start();

    // Wait for the printing thread to finish its work
    printingThread.Join();
}

private static void PrintPDF(string pdfFileName)
{
    // Create print server and print queue.
    var defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFileName);

    // Convert PDF to XPS
    var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
    document.Save(xpsFileName,SaveFormat.Xps);

    // Print the Xps file while providing XPS validation and progress notifications.
    using PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
    Console.WriteLine(xpsPrintJob.JobIdentifier);
}
```
{{< /tab >}}
{{< /tabs >}}

## Elegir fuente de papel por tamaño de página PDF
 
Desde la versión 24.4, es posible elegir la fuente de papel por tamaño de página PDF en el diálogo de impresión. El siguiente fragmento de código permite seleccionar una bandeja de impresora según el tamaño de página del PDF.

Esta preferencia se puede activar y desactivar utilizando la propiedad [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/net/aspose.pdf/document/picktraybypdfsize/).

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose a paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    var page = document.Pages.Add();
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;

    // Save PDF document
    document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## Preajustes de diálogo de impresión Escalado de página

El siguiente fragmento de código está destinado a asegurar que la propiedad [PrintScaling](https://reference.aspose.com/pdf/net/aspose.pdf/document/printscaling/) se aplique y guarde correctamente en el PDF.

La propiedad [PrintScaling](https://reference.aspose.com/pdf/net/aspose.pdf/document/printscaling/) se ha agregado a la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) con los valores `Aspose.Pdf.PrintScaling.AppDefault` o `Aspose.Pdf.PrintScaling.None`.

La opción de escalado de página que se debe seleccionar cuando se muestra un diálogo de impresión para este documento. Los valores válidos son `None`, que indica que no hay escalado de página, y `AppDefault`, que indica el escalado de impresión predeterminado del lector conforme. Si esta entrada tiene un valor no reconocido, se debe usar `AppDefault`. Valor predeterminado: `AppDefault`.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    document.Pages.Add();

    // Disable print scaling
    document.PrintScaling = PrintScaling.None;

    // Save PDF document
    document.Save(dataDir + "SetPrintScaling_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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