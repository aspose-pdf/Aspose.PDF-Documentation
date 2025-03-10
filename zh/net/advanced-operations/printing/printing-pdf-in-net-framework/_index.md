---
title: 在 .NET Framework 中打印 PDF
linktitle: 在 .NET Framework 中打印 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/printing-pdf-in-net-framework/
description: 您可以使用 C# 将 PDF 文件打印到默认打印机，使用打印机和页面设置。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Printing PDF in .NET Framework",
    "alternativeHeadline": "Print PDF Files Easily with C# in .NET Framework",
    "abstract": "介绍我们的新功能，允许使用 C# 无缝打印 PDF 文件到默认打印机。通过可自定义的打印机和页面设置，开发人员可以轻松管理打印选项，并根据 PDF 页面大小优化输出，提高操作效率和用户体验。此功能简化了将 PDF 打印功能集成到 .NET 应用程序中的过程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print pdf, C# print pdf, .NET Framework, PdfViewer class, Printer and Page Settings, PrintDocumentWithSettings, choose paper source, PDF page size, Aspose.PDF, document printing",
    "wordcount": "503",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2024-11-25",
    "description": "您可以使用 C# 将 PDF 文件打印到默认打印机，使用打印机和页面设置。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## **在 C# 中打印 PDF 文件 - 使用打印机和页面设置将 PDF 文件打印到默认打印机**

本文描述了如何使用打印机和页面设置在 C# 中将 PDF 文件打印到默认打印机。

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 类允许您将 PDF 文件打印到默认打印机。您需要创建一个 PdfViewer 对象并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) 方法打开 PDF。要指定不同的打印设置，请使用 [PageSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/pagesettings/) 和 [PrinterSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/) 类。最后，调用 [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) 方法将 PDF 打印到默认打印机。以下代码片段演示了如何使用打印机和页面设置将 PDF 打印到默认打印机。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SimplePrint()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        // Create objects for printer and page settings and PrintDocument
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();
        var prtdoc = new System.Drawing.Printing.PrintDocument();

        // Set printer name
        ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

        // Set PageSize (if required)
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;

        // Set PageMargins (if required)
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

        // Print document using printer and page settings
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SimplePrint()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    // Create objects for printer and page settings and PrintDocument
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();
    var prtdoc = new System.Drawing.Printing.PrintDocument();

    // Set printer name
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Set PageSize (if required)
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;

    // Set PageMargins (if required)
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Print document using printer and page settings
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```
{{< /tab >}}
{{< /tabs >}}

为了显示打印对话框，请尝试使用以下代码片段：

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithPrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        var printDialog = new System.Windows.Forms.PrintDialog();
        if (printDialog.ShowDialog() == DialogResult.OK)
        {
            // Document printing code goes here

            // Convert PrinterSettings and PageSettings to Aspose.PDF counterparts via extension methods
            // provided in the Aspose.Pdf.Printing namespace
            Aspose.Pdf.Printing.PrinterSettings ps = printDialog.PrinterSettings.ToAsposePrinterSettings();
            Aspose.Pdf.Printing.PageSettings pgs = printDialog.PrinterSettings.DefaultPageSettings.ToAsposePageSettings();

            // Print document using printer and page settings
            viewer.PrintDocumentWithSettings(pgs, ps);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithPrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    var printDialog = new System.Windows.Forms.PrintDialog();
    if (printDialog.ShowDialog() == DialogResult.OK)
    {
        // Document printing code goes here

        // Convert PrinterSettings and PageSettings to Aspose.PDF counterparts via extension methods
        // provided in the Aspose.Pdf.Printing namespace
        Aspose.Pdf.Printing.PrinterSettings ps = printDialog.PrinterSettings.ToAsposePrinterSettings();
        Aspose.Pdf.Printing.PageSettings pgs = printDialog.PrinterSettings.DefaultPageSettings.ToAsposePageSettings();

        // Print document using printer and page settings
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## 根据 PDF 页面大小选择纸张来源
 
自 24.4 版本以来，可以在打印对话框中根据 PDF 页面大小选择纸张来源。下一个代码片段允许根据 PDF 的页面大小选择打印机托盘。

此偏好可以使用 [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/net/aspose.pdf/document/picktraybypdfsize/) 属性打开和关闭。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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