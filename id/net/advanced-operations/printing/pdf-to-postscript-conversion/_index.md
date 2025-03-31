---
title: Konversi PDF ke PostScript
linktitle: Konversi PDF ke PostScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/pdf-to-postscript-conversion/
description: Kami memiliki solusi untuk konversi PDF ke PostScript. Gunakan untuk tugas ini kelas printing dan PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF to PostScript conversion",
    "alternativeHeadline": "Effortlessly Convert PDF Files to PostScript Format",
    "abstract": "Fitur konversi PDF ke PostScript yang baru memungkinkan transformasi dokumen PDF menjadi format PostScript secara mulus menggunakan kelas PdfViewer di C#. Fungsionalitas ini meningkatkan alur kerja pencetakan Anda dengan memungkinkan keluaran file langsung ke printer PS, sehingga lebih mudah untuk mengelola dan memanfaatkan file PDF di berbagai lingkungan pencetakan.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf to postscript, PDF to PostScript conversion, PdfViewer class, printing PDF documents, convert PDF files, C# PDF printing, print job status, PrinterJobName property, Aspose.PDF library, PS printer installation",
    "wordcount": "1224",
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
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2024-11-25",
    "description": "Kami memiliki solusi untuk konversi PDF ke PostScript. Gunakan untuk tugas ini kelas printing dan PdfViewer."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## **PDF ke Postscript di C#**

Kelas [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/) menyediakan kemampuan untuk mencetak dokumen PDF dan dengan bantuan kelas ini, kita juga dapat mengonversi file PDF ke format PostScript. Untuk mengonversi file PDF menjadi PostScript, pertama instal printer PS dan cukup cetak ke file dengan bantuan PdfViewer. Untuk menginstal printer PS, lihat instruksi yang diberikan oleh vendor printer Anda. Potongan kode berikut menunjukkan cara mencetak dan mengonversi PDF ke format PostScript.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintToPostscriptFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set PrinterSettings and PageSettings
        var printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
        printerSettings.Copies = 1;

        // Set PS printer, one can find this driver in the list of preinstalled printer drivers in Windows
        printerSettings.PrinterName = "HP LaserJet 2300 Series PS";

        // Set output file name and PrintToFile attribute
        printerSettings.PrintFileName = dataDir + "PdfToPostScript_out.ps";
        printerSettings.PrintToFile = true;
        
        // Disable print page dialog
        viewer.PrintPageDialog = false;
        
        // Pass printer settings object to the method
        viewer.PrintDocumentWithSettings(printerSettings);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintToPostscriptFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set PrinterSettings and PageSettings
    var printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
    printerSettings.Copies = 1;

    // Set PS printer, one can find this driver in the list of preinstalled printer drivers in Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";

    // Set output file name and PrintToFile attribute
    printerSettings.PrintFileName = dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
        
    // Disable print page dialog
    viewer.PrintPageDialog = false;
        
    // Pass printer settings object to the method
    viewer.PrintDocumentWithSettings(printerSettings);
}
```
{{< /tab >}}
{{< /tabs >}}

## Memeriksa Status Pekerjaan Cetak

File PDF dapat dicetak ke printer fisik serta ke Microsoft XPS Document Writer, tanpa menampilkan dialog cetak, menggunakan kelas [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/). Saat mencetak file PDF besar, prosesnya mungkin memakan waktu lama sehingga pengguna mungkin tidak yakin apakah proses pencetakan selesai atau mengalami masalah. Untuk menentukan status pekerjaan pencetakan, gunakan properti [PrintStatus](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/printstatus/). Potongan kode berikut menunjukkan cara mencetak file PDF ke file XPS dan mendapatkan status pencetakan.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckingPrintJobStatus()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instantiate PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Print the file with adjusted size
        viewer.AutoResize = true;

        // Hide printing dialog
        viewer.PrintPageDialog = false;

        // Create Printer Settings object
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Specify the printer name
        ps.PrinterName = "Microsoft XPS Document Writer";

        // Resultant Printout name
        ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";

        // Print the output to file
        ps.PrintToFile = true;

        // Set a range of pages to print
        ps.FromPage = 1;
        ps.ToPage = 2;
        ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

        // Specify the page size of printout
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
        ps.DefaultPageSettings.PaperSize = pgs.PaperSize;

        // Specify page margins
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

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
            Console.WriteLine("Printing completed without any issue.");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckingPrintJobStatus()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instantiate PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Print the file with adjusted size
    viewer.AutoResize = true;

    // Hide printing dialog
    viewer.PrintPageDialog = false;

    // Create Printer Settings object
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Specify the printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Resultant Printout name
    ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";

    // Print the output to file
    ps.PrintToFile = true;

    // Set a range of pages to print
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

    // Specify the page size of printout
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;

    // Specify page margins
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

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
        Console.WriteLine("Printing completed without any issue.");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## Mendapatkan/Mengatur Nama Pemilik Pekerjaan Cetak

Terkadang ada kebutuhan untuk mendapatkan atau mengatur nama pemilik pekerjaan cetak (yaitu, pengguna sebenarnya yang menekan tombol cetak di halaman web). Informasi ini diperlukan saat mencetak file PDF. Untuk memenuhi kebutuhan ini, properti [PrinterJobName](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/printerjobname/) digunakan.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrinterJobName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Specify the name of Print job
        viewer.PrinterJobName = GetCurrentUserCredentials();

        // Fill the necessary settings and print the documents, as shown in examples in this section
    }
}

private static string GetCurrentUserCredentials()
{
    // The implementation depends on type of running application (ASP.NET, Windows forms, etc.)
    var userCredentials = string.Empty;
    return userCredentials;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrinterJobName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Specify the name of Print job
    viewer.PrinterJobName = GetCurrentUserCredentials();

    // Fill the necessary settings and print the documents, as shown in examples in this section
}

private static string GetCurrentUserCredentials()
{
    // The implementation depends on type of running application (ASP.NET, Windows forms, etc.)
    var userCredentials = string.Empty;
    return userCredentials;
}
```
{{< /tab >}}
{{< /tabs >}}

## Menggunakan Peniruan

Pendekatan lain untuk mendapatkan nama pemilik Pekerjaan Cetak adalah dengan menggunakan peniruan (menjalankan rutinitas pencetakan dalam konteks pengguna lain) atau pengguna dapat mengubah nama pemilik secara langsung dengan menggunakan rutinitas SetJob.

Harap dicatat bahwa tidak ada kemungkinan untuk mengatur nilai pemilik menggunakan API pencetakan Aspose.PDF karena pertimbangan keamanan. Properti PrinterJobName dapat digunakan untuk mengatur nilai kolom nama dokumen dalam aplikasi cetak spooler. Potongan kode yang dibagikan di atas hanya menunjukkan bagaimana pengguna dapat menggabungkan nama pengguna ke dalam kolom nama dokumen (misalnya menggunakan sintaks UserName\documentName). Namun, pengaturan kolom Pemilik dapat diimplementasikan dengan cara berikut secara langsung oleh pengguna:

1) Peniruan. Karena nilai kolom pemilik berisi nilai pengguna yang menjalankan kode pencetakan, ada cara untuk memanggil API pencetakan Aspose.PDF di dalam konteks pengguna lain. Misalnya, lihat solusi yang dijelaskan di sini. Menggunakan [kelas Peniru ini](https://www.codeproject.com/articles/10090/a-small-csharp-class-for-impersonating-a-user) pengguna dapat mencapai tujuan:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithImpersonation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        // Impersonate another user
        using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserPassword"))
        {
            // Set PrinterSettings
            var ps = new Aspose.Pdf.Printing.PrinterSettings();

            // Set the name of the printer
            ps.PrinterName = "Microsoft XPS Document Writer";

            // Pass printer settings object to the method
            viewer.PrintDocumentWithSettings(ps); // OwnerUserName is a value of Owner column in spooler app
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithImpersonation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    // Impersonate another user
    using var impersonator = new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserPassword");

    // Set PrinterSettings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();

    // Set the name of the printer
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Pass printer settings object to the method
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName is a value of Owner column in spooler app
}
```
{{< /tab >}}
{{< /tabs >}}

2) Menggunakan API Spooler dan rutinitas SetJob

Potongan kode berikut menunjukkan cara mencetak beberapa halaman file PDF dalam mode Simplex dan beberapa halaman dalam mode Duplex.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public Aspose.Pdf.Printing.Duplex Mode { get; set; }
}

private static void PrintUsingSpoolerApi()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    int printingJobIndex = 0;
    string outputDir = dataDir;
    var printingJobs = new List<PrintingJobSettings>();

    // Create multiple printing jobs to print different page ranges with different duplex settings
    var printingJob1 = new PrintingJobSettings();
    printingJob1.FromPage = 1;
    printingJob1.ToPage = 3;
    printingJob1.OutputFile = outputDir + "PrintUsingSpoolerApi_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = outputDir + "PrintUsingSpoolerApi_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = outputDir + "PrintUsingSpoolerApi_p7_out.xps";
    printingJob3.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob3);

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "Print-PageRange.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        // Create objects for printer and page settings
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set printer name
        ps.PrinterName = "Microsoft XPS Document Writer";

        // Set output file name and PrintToFile attribute
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.PrintToFile = true;

        // Set parameters for the first print job
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

        // Set paper size and margins
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
        ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

        // Chain other print jobs at the end of the finished job
        viewer.EndPrint += (sender, args) =>
        {
            if (++printingJobIndex < printingJobs.Count)
            {
                // Set the next print job parameters
                ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                ps.FromPage = printingJobs[printingJobIndex].FromPage;
                ps.ToPage = printingJobs[printingJobIndex].ToPage;
                ps.Duplex = printingJobs[printingJobIndex].Mode;

                // Run the next print job
                viewer.PrintDocumentWithSettings(pgs, ps);
            }
        };

        // Run the first print job
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public Aspose.Pdf.Printing.Duplex Mode { get; set; }
}

private static void PrintUsingSpoolerApi()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    int printingJobIndex = 0;
    var printingJobs = new List<PrintingJobSettings>();

    // Create multiple printing jobs to print different page ranges with different duplex settings
    var printingJob1 = new PrintingJobSettings();
    printingJob1.FromPage = 1;
    printingJob1.ToPage = 3;
    printingJob1.OutputFile = dataDir + "PrintUsingSpoolerApi_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = dataDir + "PrintUsingSpoolerApi_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = dataDir + "PrintUsingSpoolerApi_p7_out.xps";
    printingJob3.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob3);

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "Print-PageRange.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    // Create objects for printer and page settings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Set output file name and PrintToFile attribute
    ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
    ps.PrintToFile = true;

    // Set parameters for the first print job
    ps.FromPage = printingJobs[printingJobIndex].FromPage;
    ps.ToPage = printingJobs[printingJobIndex].ToPage;
    ps.Duplex = printingJobs[printingJobIndex].Mode;
    ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

    // Set paper size and margins
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Chain other print jobs at the end of the finished job
    viewer.EndPrint += (sender, args) =>
    {
        if (++printingJobIndex < printingJobs.Count)
        {
            // Set the next print job parameters
            ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;

            // Run the next print job
            viewer.PrintDocumentWithSettings(pgs, ps);
        }
    };

    // Run the first print job
    viewer.PrintDocumentWithSettings(pgs, ps);
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