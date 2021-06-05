---
title: How to print PDF file in .NET Core
linktitle: Printing PDF in .NET Core
type: docs
weight: 40
url: /net/print-dotnetcore/
description: This page explains how to convert a PDF document into XPS and add it as a job to the queue of the local printer.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

The Aspose.PDF library allows us to convert PDF files to XPS. This function can be useful for organizing the printing of documents. Let's take a look at an example for using the default printer:

```csharp
class Program
{
    static void Main()
    {
        // Create the secondary thread and pass the printing method for
        // the constructor's ThreadStart delegate parameter.
        Thread printingThread = new Thread(() => PrintPDF(@"C:\tmp\doc-pdf.pdf"));

        // Set the thread that will use PrintQueue.AddJob to single threading.
        printingThread.SetApartmentState(ApartmentState.STA);

        // Start the printing thread. The method passed to the Thread
        // constructor will execute.
        printingThread.Start();
    }//end Main

    private static void PrintPDF(string pdfFileName)
    {
        // Create print server and print queue.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Aspose.Pdf.Document document = new Document(pdfFileName);
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName,SaveFormat.Xps);

        try
        {
            // Print the Xps file while providing XPS validation and progress notifications.
            PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
        catch (PrintJobException e)
        {
            Console.WriteLine("\n\t{0} could not be added to the print queue.", pdfFileName);
            if (e.InnerException != null && e.InnerException.Message == "File contains corrupted data.")
            {
                Console.WriteLine("\tIt is not a valid XPS file. Use the isXPS Conformance Tool to debug it.");
            }
            Console.WriteLine("\tContinuing with next XPS file.\n");
        }
    }
}//end Program class
```

In this example, we convert PDF document into XPS and add it as a job to the queue of the local printer.
