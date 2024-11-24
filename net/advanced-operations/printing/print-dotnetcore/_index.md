---
title: How to print PDF file in .NET Core
linktitle: Printing PDF in .NET Core
type: docs
weight: 40
url: /net/print-dotnetcore/
keywords: "print pdf .net core"
description: This page explains how to convert a PDF document into XPS in .NET Core and add it as a job to the queue of the local printer.
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
    "alternativeHeadline": "Print PDF file in .NET Core",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, pdf in .NET Core",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "This page explains how to convert a PDF document into XPS and add it as a job to the queue of the local printer."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## **Print Pdf document in .NET Core**

The Aspose.PDF library allows us to convert PDF files to XPS. This function can be useful for organizing the printing of documents. Let's take a look at an example for using the default printer.

In this example, we convert PDF document into XPS and add it as a job to the queue of the local printer:

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
    }

    private static void PrintPDF(string pdfFileName)
    {
        // Create print server and print queue.
        PrintQueue defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

        Document document = new Document(pdfFileName);
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
}
```

## Choosing paper source by PDF page size
 
Since the 24.4 release, choosing paper source by PDF page size in the print dialog is possible. The next code snippet enables picking a printer tray based on the PDF's page size.

This preference can be switched on and off using the 'Document.PickTrayByPdfSize' property.

```cs
using (Document document = new Document())
{
    Page page = document.Pages.Add();
    page.Paragraphs.Add(new TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;
    document.Save("result.pdf");
}
```

## Print Dialog Presets Page Scaling

The next code snippet is intended to ensure that the [PrintScaling](https://reference.aspose.com/pdf/net/aspose.pdf/document/printscaling/) property is correctly applied and saved in the PDF.

The [PrintScaling](https://reference.aspose.com/pdf/net/aspose.pdf/document/printscaling/) property has been added to the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) class with values ​​Aspose.Pdf.PrintScaling.AppDefault or Aspose.Pdf.PrintScaling.None.

The page scaling option that shall be selected when a print dialog is displayed for this document. Valid values are None, which indicates no page scaling, and AppDefault, which indicates the conforming reader's default print scaling. If this entry has an unrecognized value, AppDefault should be used. Default value: AppDefault.

```cs
const string dataDir = @"Samples\"; 
public void PDFNET_111()
{
    Object[] printScalingValues = { null, PrintScaling.None, PrintScaling.Default };
    PrintScaling[] printScalingExpected = { PrintScaling.Default, PrintScaling.None, PrintScaling.Default };
    for (int i = 0; i < printScalingValues.Length; i++)
    {
        Document document = new Document();
        document.Pages.Add();
        Object printScalingValue = printScalingValues[i];
        if (printScalingValue != null)
        {
            document.PrintScaling = (PrintScaling)printScalingValue;
        }
        String outputPdf = dataDir + "PDFNET-111_" + i + ".pdf";
        document.Save(outputPdf);
        Document documentOutput = new Document(outputPdf);
        if (printScalingExpected[i] == documentOutput.PrintScaling) 
        {
            Console.WriteLine("Print scaling matched");
        }
    }
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
