---
title: Printing PDF to an XPS Printer
linktitle: Printing PDF to an XPS Printer (Facades)
type: docs
weight: 20
url: /net/printing-pdf-to-an-xps-printer-facades/
description: This page shows how to printing PDF to an XPS printer using PdfViewer class.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Printing PDF to an XPS Printer",
    "alternativeHeadline": "Print PDFs Directly to XPS Printers with Ease",
    "abstract": "The new feature enables seamless printing of PDF documents directly to XPS printers using the PdfViewer class in C#. This functionality supports configuring various print settings, allowing enhanced control over the printing process, including auto resizing and rotation adjustments. Ideal for developers, this feature streamlines the integration of PDF printing capabilities into .NET applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print pdf to xps, PdfViewer class, print document settings, C# PDF printing, XPS printer, printer settings, page settings, choose paper tray, soft printer, Aspose.PDF library",
    "wordcount": "458",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "This page shows how to printing PDF to an XPS printer using PdfViewer class."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## **Print PDF to XPS printer in C#**

You can print a PDF file to an XPS printer, or some other soft printer for that matter, using the [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) class. In order to do that, create an object of the PdfViewer class and open the PDF file using the [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) method. You can set different print settings using the PrinterSettings and PageSettings classes. You also need to set the PrinterName property to the XPS or other soft printer you have installed.

Finally, use [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) method to print the PDF to XPS or other soft printer. The following code snippet shows you how to print the PDF file to an XPS printer.

```csharp
public static void PrintToXpsPrinter()
{
    // Create PdfViewer object
    PdfViewer viewer = new PdfViewer();

    // Open input PDF file
    viewer.BindPdf(dataDir + "input.pdf");

    // Set attributes for printing
    viewer.AutoResize = true;         // Print the file with adjusted size
    viewer.AutoRotate = true;         // Print the file with adjusted rotation
    viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

    // Create objects for printer and page settings and PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Set XPS/PDF printer name
    ps.PrinterName = "Microsoft XPS Document Writer";
    // Or set the PDF printer
    // Ps.PrinterName = "Adobe PDF";

    // Set PageSize (if required)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Set PageMargins (if required)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Print document using printer and page settings
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Close the PDF file after priting
    viewer.Close();
}
```

## Choosing paper source by PDF page size
 
Since the 24.4 release, choosing paper source by PDF page size in the print dialog is possible. The next code snippet enables picking a printer tray based on the PDF's page size.

This preference can be switched on and off using the 'PdfContentEditor' facade.

```cs
using (PdfContentEditor contentEditor = new PdfContentEditor())
{
    contentEditor.BindPdf("input.pdf");

    // Set the flag to choose a paper tray using the PDF page size
    contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
    contentEditor.Save("result.pdf");
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
