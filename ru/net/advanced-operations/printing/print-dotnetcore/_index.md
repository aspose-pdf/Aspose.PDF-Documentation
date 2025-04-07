---
title: Как распечатать PDF файл в .NET Core
linktitle: Печать PDF в .NET Core
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/print-dotnetcore/
description: Эта страница объясняет, как преобразовать PDF документ в XPS в .NET Core и добавить его в очередь локального принтера.
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
    "abstract": "Узнайте о новой функциональности в .NET Core, которая упрощает процесс печати PDF документов, преобразуя их в формат XPS и эффективно управляя заданиями печати в очереди вашего локального принтера. Эта функция также позволяет улучшить контроль над источниками бумаги в зависимости от размеров страниц PDF, обеспечивая индивидуальный опыт печати. Оптимизируйте управление документами с помощью точных параметров масштабирования прямо из диалога печати.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print PDF, .NET Core, convert PDF to XPS, print queue, Aspose.PDF, paper source by PDF page size, print dialog presets, page scaling, document printing, local printer",
    "wordcount": "1299",
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
    "dateModified": "2025-04-07",
    "description": "Эта страница объясняет, как преобразовать PDF документ в XPS и добавить его в очередь локального принтера."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## **Печать PDF документа в .NET Core**

Библиотека Aspose.PDF позволяет нам преобразовывать PDF файлы в XPS. Эта функция может быть полезна для организации печати документов. Давайте рассмотрим пример использования принтера по умолчанию.

В этом примере мы преобразуем PDF документ в XPS и добавляем его в очередь локального принтера:

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

## Выбор источника бумаги по размеру страницы PDF

С версии 24.4 выбор источника бумаги по размеру страницы PDF в диалоге печати стал возможен. Следующий фрагмент кода позволяет выбрать лоток принтера в зависимости от размера страницы PDF.

Эта настройка может быть включена и выключена с помощью свойства [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/picktraybypdfsize/).

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

## Предустановки диалога печати Масштабирование страниц

Следующий фрагмент кода предназначен для обеспечения правильного применения и сохранения свойства [PrintScaling](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/printscaling/) в PDF.

Свойство [PrintScaling](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/printscaling/) было добавлено в класс [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/) со значениями `Aspose.Pdf.PrintScaling.AppDefault` или `Aspose.Pdf.PrintScaling.None`.

Опция масштабирования страниц, которая должна быть выбрана, когда диалог печати отображается для этого документа. Допустимые значения: `None`, что указывает на отсутствие масштабирования страниц, и `AppDefault`, что указывает на стандартное масштабирование печати для соответствующего читателя. Если это значение не распознано, следует использовать `AppDefault`. Значение по умолчанию: `AppDefault`.

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

## Печать нескольких PDF документов в одном задании печати

Иногда необходимо распечатать несколько связанных документов вместе в одном задании печати. Это гарантирует, что, особенно с удаленными сетевыми принтерами, эти документы не будут перемешаны с выводом от других пользователей. Aspose.PDF поддерживает печать любого количества документов в одном задании печати с общими настройками принтера через статические методы `PrintDocuments` класса [PdfViewer](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfviewer). Документы, которые необходимо распечатать, могут быть предоставлены в виде путей к файлам, потоков документов или объектов [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).

{{% alert color="primary" %}}

При печати нескольких документов свойство [PrinterSettings.PrintRange](https://reference.aspose.com/pdf/ru/net/aspose.pdf.printing/printersettings/printrange/) игнорируется, и все документы печатаются полностью.

{{% /alert %}}

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingMultipleDocumentsInSingleJob()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Paths to documents to be printed
    var path1 = dataDir + "PrintDocument.pdf";
    var path2 = dataDir + "Print-PageRange.pdf";
    var path3 = dataDir + "35925_1_3.xps";
    
    // Set up printer and page settings
    var printDocument = new PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
    printerSettings.PrinterName = printDocument.PrinterSettings.PrinterName;
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings();
    pageSettings.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    pageSettings.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingMultipleDocumentsInSingleJob()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Paths to documents to be printed
    var path1 = dataDir + "PrintDocument.pdf";
    var path2 = dataDir + "Print-PageRange.pdf";
    var path3 = dataDir + "35925_1_3.xps";
    
    // Set up printer and page settings
    var printDocument = new PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings
    {
        PrinterName = printDocument.PrinterSettings.PrinterName
    };
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings
    {
        PaperSize = Aspose.Pdf.Printing.PaperSizes.A4,
        Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0)
    }
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
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