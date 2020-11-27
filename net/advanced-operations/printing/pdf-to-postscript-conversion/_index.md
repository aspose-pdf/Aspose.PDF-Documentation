---
title: PDF to PostScript conversion
type: docs
weight: 30
url: /net/pdf-to-postscript-conversion/
description: We have a solution for PDF to PostScript conversion. Use for this task printing and PdfViewer class. Also, this article describes how to checking print job status, how to get and set print job owner name.
---

The PdfViewer class provides the capability to print PDF documents and with the help of this class, we can also convert PDF files to PostScript format. To convert a PDF file into PostScript, first install any PS printer and just print to file with the help of PdfViewer. You may follow the instructions specified by the University of Hawaii on how to install PS printer. The following code snippet shows you how to print and convert a PDF to PostScript format.

```csharp
public static void PrintToPostscriptFile()
{
    // The path to the documents directory.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // Set PrinterSettings and PageSettings
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // Set PS printer, one can find this driver in the list of preinstalled printer drivers in Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // Set output file name and PrintToFile attribute
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // Disable print page dialog
    viewer.PrintPageDialog = false;
    // Pass printer settings object to the method
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```

## Checking Print Job Status

A PDF file can be printed to a physical printer as well as to the Microsoft XPS Document Writer, without showing a print dialog, using the PdfViewer class. When printing large PDF files, the process might take a long time so the user might not be certain whether the printing process completed or encountered an issue. To determine the status of a printing job, use the PrintStatus property. The following code snippet shows you how to print the PDF file to an XPS file and get the printing status.

```csharp
public static void CheckingPrintJobStatus()
{
    // For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // The path to the documents directory.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instantiate PdfViewer object
    PdfViewer viewer = new PdfViewer();

    // Bind source PDF file
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // Hide printing dialog
    viewer.PrintPageDialog = false;

    // Create Printer Settings object
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Specify the printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Resultant Printout name
    ps.PrintFileName = "ResultantPrintout.xps";

    // Print the output to file
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // Specify the page size of printout
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Print the document with settings specified above
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Check the print status
    if (viewer.PrintStatus != null)
    {
        // An exception was thrown
        if (viewer.PrintStatus is Exception ex)
        {
            // Get exception message
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // No errors were found. Printing job has completed successfully
        Console.WriteLine("printing completed without any issue..");
    }
}
```

## Get/Set Print Job Owner name

Recently we received a requirement to get/set the print job Owner name (the actual user who pressed print button on web page). This information is required when printing the PDF file. In order to accomplish this requirement, you can use the property named PrinterJobName:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// Bind source PDF file
viewer.BindPdf(dataDir + "input.pdf");
// Specify the name of Print job
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // The implementation depends on type of running application (ASP.NET, Windows forms, etc.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```

## Using Impersonation

Another approach of getting Print Job owner name is to use impersonation (running printing routines in another user context) or user may change owner name directly by using SetJob routine.

Please note that there is no possibility to set owner value using Aspose.PDF printing API by security considerations. The property PrinterJobName may be used to set document name column value in spooler print application. Code snippet shared above just shows how the user can join user name into document name column (for example using syntax UserName\documentName). But the setting of Owner columns can be implemented in following ways directly by user:

1) Impersonation. As owner column value contains the value of user who runs the printing code, there is a way to invoke Aspose.PDF printing API inside another user context. For example please take a look on solution described here. Using this class the user can reach a goal:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf( dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// Do not produce the page number dialog when printing
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName is a value of Owner column in spooler app
    viewer.Close();
}
```

2) Using Spooler API and SetJob routine

The following code snippet shows how to print some pages of PDF file in Simplex and some pages in Duplex mode.


```csharp
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public System.Drawing.Printing.Duplex Mode { get; set; }
}
```

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

int printingJobIndex = 0;
string inPdf = dataDir + "input.pdf";
string output = dataDir;
IList<PrintingJobSettings> printingJobs = new List<PrintingJobSettings>();

PrintingJobSettings printingJob1 = new PrintingJobSettings();
printingJob1.FromPage = 1;
printingJob1.ToPage = 3;
printingJob1.OutputFile = output + "35925_1_3.xps";
printingJob1.Mode = Duplex.Default;

printingJobs.Add(printingJob1);

PrintingJobSettings printingJob2 = new PrintingJobSettings();
printingJob2.FromPage = 4;
printingJob2.ToPage = 6;
printingJob2.OutputFile = output + "35925_4_6.xps";
printingJob2.Mode = Duplex.Simplex;

printingJobs.Add(printingJob2);

PrintingJobSettings printingJob3 = new PrintingJobSettings();
printingJob3.FromPage = 7;
printingJob3.ToPage = 7;
printingJob3.OutputFile = output + "35925_7.xps";
printingJob3.Mode = Duplex.Default;

printingJobs.Add(printingJob3);

PdfViewer viewer = new PdfViewer();

viewer.BindPdf(inPdf);
viewer.AutoResize = true;
viewer.AutoRotate = true;
viewer.PrintPageDialog = false;

PrinterSettings ps = new PrinterSettings();
PageSettings pgs = new PageSettings();

ps.PrinterName = "Microsoft XPS Document Writer";
ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
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
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
};

viewer.PrintDocumentWithSettings(pgs, ps);
```
