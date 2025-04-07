---
title: 如何在 .NET Core 中打印 PDF 文件
linktitle: 在 .NET Core 中打印 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/print-dotnetcore/
description: 本页面解释了如何在 .NET Core 中将 PDF 文档转换为 XPS，并将其作为作业添加到本地打印机的队列中。
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
    "abstract": "发现 .NET Core 中的新功能，通过将 PDF 文档转换为 XPS 格式并高效管理本地打印机队列中的打印作业，简化打印 PDF 文档的过程。此功能还允许根据 PDF 页面大小增强对纸张来源的控制，确保量身定制的打印体验。通过打印对话框直接优化文档管理，提供精确的缩放选项。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print PDF, .NET Core, convert PDF to XPS, print queue, Aspose.PDF, paper source by PDF page size, print dialog presets, page scaling, document printing, local printer",
    "wordcount": "1122",
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
    "description": "本页面解释了如何将 PDF 文档转换为 XPS，并将其作为作业添加到本地打印机的队列中。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## **在 .NET Core 中打印 PDF 文档**

Aspose.PDF 库允许我们将 PDF 文件转换为 XPS。此功能对于组织文档的打印非常有用。让我们看一个使用默认打印机的示例。

在此示例中，我们将 PDF 文档转换为 XPS，并将其作为作业添加到本地打印机的队列中：

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

## 按 PDF 页面大小选择纸张来源
 
自 24.4 版本以来，在打印对话框中可以按 PDF 页面大小选择纸张来源。下一个代码片段启用根据 PDF 的页面大小选择打印机托盘。

此偏好可以使用 [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/picktraybypdfsize/) 属性打开和关闭。

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

## 打印对话框预设页面缩放

下一个代码片段旨在确保 [PrintScaling](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/printscaling/) 属性正确应用并保存在 PDF 中。

[PrintScaling](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/printscaling/) 属性已添加到 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/) 类中，值为 `Aspose.Pdf.PrintScaling.AppDefault` 或 `Aspose.Pdf.PrintScaling.None`。

在显示此文档的打印对话框时应选择的页面缩放选项。有效值为 `None`，表示不进行页面缩放，以及 `AppDefault`，表示符合阅读器的默认打印缩放。如果此条目的值无法识别，则应使用 `AppDefault`。默认值：`AppDefault`。

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

## 在单个打印作业中打印多个 PDF 文档

有时，需要将多个相关文档作为单个打印作业一起打印。这确保了，尤其是在远程网络打印机上，这些文档不会与其他用户的输出交错。Aspose.PDF 支持通过 [PdfViewer](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfviewer) 类的静态 `PrintDocuments` 方法在单个打印作业中打印任意数量的文档，使用共享的打印机设置。要打印的文档可以作为文件路径、文档流或 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象提供。

{{% alert color="primary" %}}

在打印多个文档时，忽略 [PrinterSettings.PrintRange](https://reference.aspose.com/pdf/zh/net/aspose.pdf.printing/printersettings/printrange/) 属性，所有文档都将完整打印。

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