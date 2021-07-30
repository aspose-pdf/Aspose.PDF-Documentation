---
title: Working with PDF printing - Facades
type: docs
weight: 10
url: /net/working-with-pdf-printing-facades/
description: This section explains how to print PDF files with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2021-06-05"
draft: false
---

## Printing PDF File to Default Printer using Printer and Page Settings

Firstly document is converted into image and then printed on the printer.
We create an instance of the [PdfViewer](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/pdfviewer) class that allows you to print a PDF file to the default printer, using BindPdf method for document to it, and make certain settings. In our example, we are using A4 format, portrait orientation. In the printerSettings, first of all, we indicate the name of the printer to which we are printing. Or else it will print to the default printer. Next, put down the number of copies we need.

```csharp
 public static void PrintingPDFFile()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

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

            // Close the PDF file after printing
            viewer.Close();
        }
```

In order to display a print dialog, try using the following code snippet:

```csharp
        public static void PrintingPDFDisplayPrintDialog()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation

            // Create objects for printer and page settings and PrintDocument

            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings
            {

                // Set PageSize (if required)
                PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169),

                // Set PageMargins (if required)
                Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0)
            };

            System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
            if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                // Document printing code goes here
                // Print document using printer and page settings
                System.Drawing.Printing.PrinterSettings ps = printDialog.PrinterSettings;
                viewer.PrintDocumentWithSettings(pgs, ps);
            }

            // Close the PDF file after priting
            viewer.Close();
        }
```

## Print PDF to Soft Printer

There are printers that print to a file. We set the name of the virtual printer, and, by analogy with the previous example, we make the settings.

```csharp
public static void PrintingPDFToSoftPrinter()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation
            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

            viewer.PrintAsImage = false;

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Set printer name
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Or set the PDF printer
            //ps.PrinterName = "Adobe PDF";

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

## Printing PDF to an XPS Printer (Facades)

You can print a PDF file to an XPS printer, or some other soft printer for that matter, using the [PdfViewer](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/pdfviewer) class. In order to do that, create an object of the PdfViewer class and open the PDF file using the BindPdf method. You can set different print settings using the PrinterSettings and PageSettings classes. You also need to set the PrinterName property to the XPS or other soft printer you have installed.

Finally, use PrintDocumentWithSettings method to print the PDF to XPS or other soft printer. The following code snippet shows you how to print the PDF file to an XPS printer.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Printing-PrintoXPSPrinter-PrintoXPSPrinter.cs" >}}

When printing a PDF files that contains text and you want the contents to appear as text instead of vector graphics, please try using the following code snippets.

### Fonts not Embedded

If the document does not contain embedded fonts, it is possible to embed system fonts into the document at the point of printing.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Printing-PrintoXPSPrinter-FontsNotEmbedded.cs" >}}

### Fonts Embedded

For documents that have embedded fonts, the quality can be improved and fonts are embedded to the document. Aspose.PDF has a feature that allows you to substitute embedded fonts with system fonts.

## Hiding Print Dialog

Aspose.PDF for .NET allows you to hide the print dialog. For this use [PrintPageDialog](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog) method.

The following code snippet shows you how to hide the print dialog.

```csharp
public static void PrintingPDFHidePrintDialog()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation


            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Set XPS/PDF printer name
            ps.PrinterName = "OneNote for Windows 10";

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

## Printing Color PDF to XPS File as Grayscale

A color PDF document can be printed to an XPS printer as grayscale, using [PdfViewer](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/pdfviewer). In order to achieve that you need to use the property PdfViewer.PrintAsGrayscale and set it to *true*. Following code snippet demonstrates the implementation of PdfViewer.PrintAsGrayscale Property.

```csharp
public static void PrintingPDFasGrayscale()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation


            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing
            viewer.PrintAsGrayscale = false;

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Set XPS/PDF printer name
            ps.PrinterName = "OneNote for Windows 10";

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

## PDF to PostScript conversion

The [PdfViewer](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/pdfviewer) class provides the capability to print PDF documents and with the help of this class, we can also convert PDF files to PostScript format. To convert a PDF file into PostScript, first install any PS printer and just print to file with the help of PdfViewer.

The following code snippet shows you how to print and convert a PDF to PostScript format.

```csharp
public static void PrintingPDFToPostScript()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation
            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

            viewer.PrintAsImage = false;

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Set XPS/PDF printer name
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Set output file name and PrintToFile attribute
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

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

## Checking Print Job Status

A PDF file can be printed to a physical printer as well as to the Microsoft XPS Document Writer, without showing a print dialog, using the [PdfViewer](https://apireference.aspose.com/net/pdf/aspose.pdf.facades/pdfviewer) class. When printing large PDF files, the process might take a long time so the user might not be certain whether the printing process completed or encountered an issue. To determine the status of a printing job, use the PrintStatus property. The following code snippet shows you how to print the PDF file to an XPS file and get the printing status.

```csharp
public static void CheckingPrintJobStatus()
        {
            // Create PdfViewer object
            PdfViewer viewer = new PdfViewer();

            // Open input PDF file
            viewer.BindPdf(_dataDir + "sample1.pdf");

            // Set attributes for printing
            viewer.AutoResize = true;         // Print the file with adjusted size
            viewer.AutoRotate = true;         // Print the file with adjusted rotation
            viewer.PrintPageDialog = false;   // Do not produce the page number dialog when printing

            viewer.PrintAsImage = false;

            // Create objects for printer and page settings and PrintDocument
            System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
            System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

            // Set XPS/PDF printer name
            ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
            // Set output file name and PrintToFile attribute
            ps.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
            ps.PrintToFile = true;

            // Set PageSize (if required)
            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

            // Set PageMargins (if required)
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            // Print document using printer and page settings
            viewer.PrintDocumentWithSettings(pgs, ps);

            // Check the print status
            if (viewer.PrintStatus != null && viewer.PrintStatus is Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            else
            {
                // No errors were found. Printing job has completed successfully
                Console.WriteLine("Printing completed without any issue..");
            }

            // Close the PDF file after priting
            viewer.Close();
        }

        struct PrintingJobSettings
        {
            public int ToPage { get; set; }
            public int FromPage { get; set; }
            public string OutputFile { get; set; }
            public System.Drawing.Printing.Duplex Mode { get; set; }
        }
```

## Printing pages in Simplex and Duplex mode

In a particular printing job, the pages of PDF document can either be printed in Duplex or in Simplex mode but you cannot print some pages as simplex and some pages as duplex within a single print job. However in order to accomplish the requirement, different page ranges and PrintingJobSettings object can be used. The following code snippet shows how to print some pages of PDF file in Simplex and some pages in Duplex mode.

```csharp
 public static void PrintingPagesInSimplexAndDuplexMode()
        {
            int printingJobIndex = 0;
            string inPdf = _dataDir + "sample-8page.pdf";
            string output = _dataDir;
            IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

            PrintingJobSettings printingJob1 = new PrintingJobSettings
            {
                FromPage = 1,
                ToPage = 3,
                OutputFile = output + "sample_1_3.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob1);

            PrintingJobSettings printingJob2 = new PrintingJobSettings
            {
                FromPage = 4,
                ToPage = 6,
                OutputFile = output + "sample_4_6.xps",
                Mode = Duplex.Simplex
            };

            printingJobs.Add(printingJob2);

            PrintingJobSettings printingJob3 = new PrintingJobSettings
            {
                FromPage = 7,
                ToPage = 7,
                OutputFile = output + "sample_7.xps",
                Mode = Duplex.Default
            };

            printingJobs.Add(printingJob3);

            PdfViewer viewer = new PdfViewer();

            viewer.BindPdf(inPdf);
            viewer.AutoResize = true;
            viewer.AutoRotate = true;
            viewer.PrintPageDialog = false;

            PrinterSettings ps = new PrinterSettings();
            PageSettings pgs = new PageSettings();

            ps.PrinterName = "Microsoft XPS Document Writer";
            ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.PrintToFile = true;
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;
            ps.PrintRange = PrintRange.SomePages;

            pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
            ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
            pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

            viewer.EndPrint += (sender, args) =>
            {
                if (++printingJobIndex < printingJobs.Count)
                {
                    ps.PrintFileName = System.IO.Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                    ps.FromPage = printingJobs[printingJobIndex].FromPage;
                    ps.ToPage = printingJobs[printingJobIndex].ToPage;
                    ps.Duplex = printingJobs[printingJobIndex].Mode;
                    viewer.PrintDocumentWithSettings(pgs, ps);
                }
            };

            viewer.PrintDocumentWithSettings(pgs, ps);
        }
```
