---
title: Printing PDF to an XPS Printer (Facades)
type: docs
weight: 20
url: /net/printing-pdf-to-an-xps-printer-facades/
description: This page shows how to printing PDF to an XPS printer using PdfViewer class.  
---

You can print a PDF file to an XPS printer, or some other soft printer for that matter, using the [PdfViewer](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) class. In order to do that, create an object of the PdfViewer class and open the PDF file using the [BindPdf](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) method. You can set different print settings using the PrinterSettings and PageSettings classes. You also need to set the PrinterName property to the XPS or other soft printer you have installed.

Finally, use [PrintDocumentWithSettings](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) method to print the PDF to XPS or other soft printer. The following code snippet shows you how to print the PDF file to an XPS printer.

```csharp
public static void PrintToXpsPrinter()
{
    // Create PdfViewer object
    PdfViewer viewer = new PdfViewer();

    // Open input PDF file
    viewer.BindPdf(_dataDir + "input.pdf");

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
