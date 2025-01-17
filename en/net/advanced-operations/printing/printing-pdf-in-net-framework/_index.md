---
title: Printing PDF in .NET Framework
linktitle: Printing PDF in .NET Framework
type: docs
weight: 10
url: /net/printing-pdf-in-net-framework/
description: You may print PDF files to the default printer using the printer and page settings with C#.
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
    "abstract": "Introducing our new feature that allows seamless printing of PDF files to the default printer using C#. With customizable printer and page settings, developers can effortlessly manage print options and optimize output based on PDF page size, enhancing operational efficiency and user experience. This functionality simplifies the process of integrating PDF printing capabilities into .NET applications",
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
    "description": "You may print PDF files to the default printer using the printer and page settings with C#."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## **Print Pdf File in C# - Print PDF File to Default Printer using Printer and Page Settings**

This article describes how to Print PDF File to Default Printer using Printer and Page Settings in C#.

The [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) class allows you to print a PDF file to the default printer. You need to create a PdfViewer object and open the PDF using the [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) method. To specify different print settings, use the [PageSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/pagesettings/) and [PrinterSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/) classes. Finally, call the [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) method to print the PDF to the default printer. The following code snippet shows how to print PDF to the default printer with printer and page settings.

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
        viewer.AutoResize = true;         // Print the file with adjusted size
        viewer.AutoRotate = true;         // Print the file with adjusted rotation
        viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

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
    viewer.AutoResize = true;         // Print the file with adjusted size
    viewer.AutoRotate = true;         // Print the file with adjusted rotation
    viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

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

In order to display a print dialog, try using the following code snippet:

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
        viewer.AutoResize = true;         // Print the file with adjusted size
        viewer.AutoRotate = true;         // Print the file with adjusted rotation
        viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

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

    // Open PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    viewer.AutoResize = true;         // Print the file with adjusted size
    viewer.AutoRotate = true;         // Print the file with adjusted rotation
    viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

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

## Choosing paper source by PDF page size
 
Since the 24.4 release, choosing paper source by PDF page size in the print dialog is possible. The next code snippet enables picking a printer tray based on the PDF's page size.

This preference can be switched on and off using the [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/net/aspose.pdf/document/picktraybypdfsize/) property.

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
