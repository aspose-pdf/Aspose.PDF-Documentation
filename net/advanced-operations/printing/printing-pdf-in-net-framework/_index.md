---
title: Printing PDF in .NET Framework
linktitle: Printing PDF in .NET Framework
type: docs
weight: 10
url: /net/printing-pdf-in-net-framework/
description: You may print PDF files to the default printer using the printer and page settings with C#.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

This article describes how to Print PDF File to Default Printer using Printer and Page Settings in C#.

The [PdfViewer](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) class allows you to print a PDF file to the default printer. You need to create a PdfViewer object and open the PDF using the [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) method. To specify different print settings, use the `PageSettings` and `PrinterSettings` classes. Finally, call the [PrintDocumentWithSettings](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) method to print the PDF to the default printer. The following code snippet shows how to print PDF to the default printer with printer and page Settings.

```csharp
public static void SimplePrint()
{
    // Create PdfViewer object
    PdfViewer viewer = new PdfViewer();

    // Open input PDF file
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // Set attributes for printing
    viewer.AutoResize = true;         // Print the file with adjusted size
    viewer.AutoRotate = true;         // Print the file with adjusted rotation
    viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

    // Create objects for printer and page settings and PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // Set printer name
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

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

In order to display a print dialog, try using the following code snippet:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // Document printing code goes here
    // Print document using printer and page settings
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```
