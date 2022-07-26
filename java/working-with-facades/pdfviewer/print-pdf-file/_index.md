---
title: Working with PDF printing 
type: docs
weight: 10
url: /java/print-pdf-file/
description: This section explains how to print PDF file with Aspose.PDF Facades using PdfViewer Class.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Printing PDF File to Default Printer using Printer and Page Settings

The [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) class allows you to print a PDF file to the default printer. Therefore you need to create a [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) object and open the PDF using the openPdfFile(..) method.

Call the printDocument(..) method to print the PDF to the default printer.

The following code snippet shows how to print PDF to the default printer with printer and page Settings.

```java
 public static void PrintingPDFFile() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation
        viewer.setPrintPageDialog(false); // Do not produce the page number dialog when printing

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set printer name
        printerSettings.setPrinterName("Microsoft Print to PDF");
        

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Print document using printer and page settings
        viewer.printDocumentWithSettings(pageSettings, printerSettings);
        
        // Close the PDF file after printing
        viewer.close();
    }
```

In order to display a print dialog, try using the following code snippet:

```java
public static void PrintingPDFDisplayPrintDialog() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation
        viewer.setPrintPageDialog(true);

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        java.awt.print.PrinterJob pj = java.awt.print.PrinterJob.getPrinterJob();

        if (pj.printDialog()) {
            printerSettings.setPrinterName(pj.getPrintService().getName());
            printerSettings.setCopies((short) pj.getCopies());
            // Print document using printer and page settings
            viewer.printDocumentWithSettings(pageSettings, printerSettings);
        }
        // Close the PDF file after printing
        viewer.close();
    }
```

## Print PDF to Soft Printer

There are printers that print to a file. We set the name of the virtual printer, and, by analogy with the previous example, we make the settings.

```java
public static void PrintingPDFToSoftPrinter() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation
        viewer.setPrintPageDialog(false); // Do not produce the page number dialog when printing

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set printer Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");
        // or Adobe
        // printerSettings.setPrinterName("Adobe PDF");

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Print document using printer and page settings
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Close the PDF file after printing
        viewer.close();
    }
```

## Hiding Print Dialog

Aspose.PDF for Java allows you to hide the print dialog. For this use [getPrintPageDialog](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer#getPrintPageDialog--) method.

The following code snippet shows you how to hide the print dialog.

```java
public static void PrintingPDFHidePrintDialog() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation

        viewer.setPrintPageDialog(false); // Do not produce the page number dialog when printing

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set printer Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Print document using printer and page settings
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Close the PDF file after printing
        viewer.close();
    }
```

## Printing Color PDF to XPS File as Grayscale

A color PDF document can be printed to an XPS printer as grayscale, using [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer). In order to achieve that you need to use the property PdfViewer.PrintAsGrayscale and set it to *true*. 

Following code snippet demonstrates the implementation of PdfViewer.PrintAsGrayscale Property.

```java
 public static void PrintingPDFasGrayscale() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation

        viewer.setPrintAsGrayscale(true);

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set printer Microsoft Soft Printer
        printerSettings.setPrinterName("Microsoft Print to PDF");

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Print document using printer and page settings
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Close the PDF file after printing
        viewer.close();
    }
```

## PDF to PostScript conversion

The [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) class provides the capability to print PDF documents and with the help of this class, we can also convert PDF files to PostScript format. To convert a PDF file into PostScript, first install any PS printer and just print to file with the help of PdfViewer.

The following code snippet shows you how to print and convert a PDF to PostScript format.

```java
public static void PrintingPDFToPostScript() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation

        viewer.setPrintAsGrayscale(true);
        

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set PostSScript Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");
        printerSettings.setPrintToFile(true);
        printerSettings.setPrintFileName(_dataDir+"result.ps");

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Print document using printer and page settings
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // Close the PDF file after printing
        viewer.close();
    }
```

## Checking Print Job Status

A PDF file can be printed to a physical printer as well as to the Microsoft XPS Document Writer, without showing a print dialog, using the [PdfViewer](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfViewer) class. When printing large PDF files, the process might take a long time so the user might not be certain whether the printing process completed or encountered an issue. To determine the status of a printing job, use the PrintStatus property. The following code snippet shows you how to print the PDF file to an XPS file and get the printing status.

```java
public static void CheckingPrintJobStatus() {
        // Create PdfViewer object
        PdfViewer viewer = new PdfViewer();

        // Open input PDF file
        viewer.bindPdf(_dataDir + "sample.pdf");

        // Set attributes for printing
        viewer.setAutoResize(true); // Print the file with adjusted size
        viewer.setAutoRotate(true); // Print the file with adjusted rotation

        viewer.setPrintAsGrayscale(true);

        // Create objects for printer and page settings and PrintDocument
        PdfPrinterSettings printerSettings = new PdfPrinterSettings();
        PrintPageSettings pageSettings = new PrintPageSettings();

        // Set printer Microsoft Soft Printer
        printerSettings.setPrinterName("HP Universal Printing PS (v7.0.0)");

        // Set PageSize (if required)
        pageSettings.setPaperSize(new PrintPaperSize("A4", 827, 1169));

        // Set PageMargins (if required)
        pageSettings.setMargins(new PrinterMargins(0, 0, 0, 0));

        // Print document using printer and page settings
        viewer.printDocumentWithSettings(pageSettings, printerSettings);

        // // Check the print status
        if (viewer.getPrintStatus() != null) {
            Exception ex = (Exception) viewer.getPrintStatus();
            System.out.println(ex.getMessage());
        } else {
            // No errors were found. Printing job has completed successfully
            System.out.println("Everything went OK!");
        }
        // Close the PDF file after printing
        viewer.close();
    }
```

