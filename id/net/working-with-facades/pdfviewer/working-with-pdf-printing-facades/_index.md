---
title: Bekerja dengan pencetakan PDF - Facades
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/working-with-pdf-printing-facades/
description: Bagian ini menjelaskan cara mencetak file PDF dengan Aspose.PDF Facades menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF printing - Facades",
    "alternativeHeadline": "Enhancing PDF Printing Capabilities with C#",
    "abstract": "Aspose.PDF for .NET Fitur Facades menyederhanakan pencetakan PDF dengan kontrol yang lebih baik atas pengaturan printer dan format output. Pengguna dapat mencetak dokumen ke printer default atau virtual, mendefinisikan tata letak halaman, dan bahkan mengelola pekerjaan cetak dalam mode simplex atau duplex, sementara opsi seperti mencetak dalam skala abu-abu dan menyembunyikan dialog cetak menambah fleksibilitasnya. Fungsionalitas ini secara signifikan mengoptimalkan alur kerja pencetakan untuk dokumen PDF, menjadikannya ideal bagi pengembang dan pengguna yang mencari solusi manajemen dokumen yang efisien.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "4174",
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
    "url": "/net/working-with-pdf-printing-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pdf-printing-facades/"
    },
    "dateModified": "2025-04-07",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Mencetak File PDF ke Printer Default menggunakan Pengaturan Printer dan Halaman

Pertama, dokumen dikonversi menjadi gambar, dan kemudian, dicetak pada printer.
Buat instance dari kelas [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer) yang memungkinkan pencetakan file PDF ke printer default, gunakan metode [BindPdf](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/bindpdf/) untuk membuka dokumen ke dalamnya, dan ubah pengaturan yang diperlukan. Contoh ini menggunakan format A4, orientasi potret. Di [PrinterSettings](https://reference.aspose.com/pdf/id/net/aspose.pdf.printing/printersettings/), pertama-tama, nama printer, ke mana pencetakan dilakukan, harus diatur. Jika tidak, itu akan mencetak ke printer default. Selanjutnya, masukkan jumlah salinan yang diperlukan.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

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
private static void PrintingPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

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

Untuk menampilkan dialog cetak, gunakan potongan kode berikut:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFDisplayPrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;

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
private static void PrintingPDFDisplayPrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;

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

## Mencetak PDF ke Printer Virtual

Ada printer yang mencetak ke file. Untuk menggunakannya, atur nama printer virtual, dan, sama seperti contoh sebelumnya, buat pengaturannya.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFToSoftPrinter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;
        // Do not convert document pages to images
        viewer.PrintAsImage = false;

        // Create objects for printer and page settings and PrintDocument
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set printer name
        ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
        // Or set the PDF printer
        // ps.PrinterName = "Adobe PDF";

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
private static void PrintingPDFToSoftPrinter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;
    // Do not convert document pages to images
    viewer.PrintAsImage = false;

    // Create objects for printer and page settings and PrintDocument
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set printer name
    ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
    // Or set the PDF printer
    // ps.PrinterName = "Adobe PDF";

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

## Menyembunyikan Dialog Cetak

Aspose.PDF for .NET mendukung menyembunyikan dialog cetak. Untuk ini, gunakan properti [PrintPageDialog](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog).

Potongan kode berikut menunjukkan cara menyembunyikan dialog cetak.

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFHidePrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

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

        // Set XPS/PDF printer name
        ps.PrinterName = "OneNote for Windows 10";

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
private static void PrintingPDFHidePrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printin
    viewer.PrintPageDialog = false;

    // Create objects for printer and page settings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set XPS/PDF printer name
    ps.PrinterName = "OneNote for Windows 10";

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

## Mencetak PDF Berwarna ke File XPS sebagai Skala Abu-abu

Dokumen PDF berwarna dapat dicetak ke printer XPS sebagai skala abu-abu, menggunakan [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer). Untuk mencapai itu, atur properti [PdfViewer.PrintAsGrayscale](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/printasgrayscale/) ke *true*. Potongan kode berikut menunjukkan penggunaan properti `PdfViewer.PrintAsGrayscale`.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFAsGrayscale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;
        // Print the file as grayscale
        viewer.PrintAsGrayscale = false;

        // Create objects for printer and page settings
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set XPS/PDF printer name
        ps.PrinterName = "OneNote for Windows 10";

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
private static void PrintingPDFAsGrayscale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;
    // Print the file as grayscale
    viewer.PrintAsGrayscale = false;

    // Create objects for printer and page settings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set XPS/PDF printer name
    ps.PrinterName = "OneNote for Windows 10";

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

## Konversi PDF ke PostScript

Kelas [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer) menyediakan kemampuan untuk mencetak dokumen PDF dan dengan bantuan kelas ini, seseorang juga dapat mengonversi file PDF ke format PostScript. Untuk mengonversi file PDF menjadi PostScript, pertama instal printer PS apa pun dan cukup cetak ke file dengan bantuan `PdfViewer`.

Potongan kode berikut menunjukkan cara mencetak dan mengonversi PDF ke format PostScript.

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFToPostScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;
        // Do not convert document pages to images
        viewer.PrintAsImage = false;

        // Create objects for printer and page settings and PrintDocument
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set printer name
        ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
        
        // Set output file name and PrintToFile attribute
        ps.PrintFileName = dataDir + "PdfToPostScript_out.ps";
        ps.PrintToFile = true;

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
private static void PrintingPDFToSoftPrinter()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;
    // Do not convert document pages to images
    viewer.PrintAsImage = false;

    // Create objects for printer and page settings and PrintDocument
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set printer name
    ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
    
    // Set output file name and PrintToFile attribute
    ps.PrintFileName = dataDir + "PdfToPostScript_out.ps";
    ps.PrintToFile = true;

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

## Memeriksa Status Pekerjaan Cetak

File PDF dapat dicetak ke printer fisik serta ke Microsoft XPS Document Writer, tanpa menampilkan dialog cetak, menggunakan kelas [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer). Ketika mencetak file PDF besar, prosesnya mungkin memakan waktu lama sehingga pengguna mungkin tidak yakin apakah proses pencetakan selesai atau mengalami masalah. Untuk menentukan status pekerjaan pencetakan, gunakan properti [PrintStatus](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer/printstatus/). Potongan kode berikut menunjukkan cara mencetak file PDF ke file XPS dan mendapatkan status pencetakan.

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;
        // Do not convert document pages to images
        viewer.PrintAsImage = false;

        // Create Printer Settings object
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Specify the printer name
        ps.PrinterName = "Microsoft XPS Document Writer";

        // Set output file name and PrintToFile attribute
        ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";
        ps.PrintToFile = true;

        // Set PageSize (if required)
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
        
        // Set PageMargins (if required)
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);
        
        // Print document using printer and page settings
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

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;
    // Do not convert document pages to images
    viewer.PrintAsImage = false;

    // Create Printer Settings object
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Specify the printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Set output file name and PrintToFile attribute
    ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";
    ps.PrintToFile = true;

    // Set PageSize (if required)
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;

    // Set PageMargins (if required)
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Print document using printer and page settings
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

## Mencetak halaman dalam mode Simplex dan Duplex

Dalam pekerjaan pencetakan tertentu, halaman dokumen PDF dapat dicetak baik dalam mode Duplex atau dalam mode Simplex tetapi Anda tidak dapat mencetak beberapa halaman sebagai simplex dan beberapa halaman sebagai duplex dalam satu pekerjaan cetak. Namun, untuk memenuhi kebutuhan tersebut, rentang halaman yang berbeda dan objek PrintingJobSettings dapat digunakan. Potongan kode berikut menunjukkan cara mencetak beberapa halaman dari file PDF dalam mode Simplex dan beberapa halaman dalam mode Duplex.

{{< tabs tabID="8" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

private static void PrintingPagesInSimplexAndDuplexMode()
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
    printingJob1.OutputFile = outputDir + "PrintPageRange_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = outputDir + "PrintPageRange_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = outputDir + "PrintPageRange_p7_out.xps";
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

private static void PrintingPagesInSimplexAndDuplexMode()
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
    printingJob1.OutputFile = outputDir + "PrintPageRange_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = outputDir + "PrintPageRange_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = outputDir + "PrintPageRange_p7_out.xps";
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

## Mencetak beberapa dokumen PDF dalam satu pekerjaan cetak

Terkadang, perlu untuk mencetak beberapa dokumen terkait bersama-sama sebagai satu pekerjaan cetak. Ini memastikan bahwa, terutama dengan printer jaringan jarak jauh, dokumen-dokumen ini tidak tercampur dengan output dari pengguna lain. Aspose.PDF mendukung pencetakan sejumlah dokumen dalam satu pekerjaan cetak dengan pengaturan printer yang dibagikan melalui metode statis `PrintDocuments` dari kelas [PdfViewer](https://reference.aspose.com/pdf/id/net/aspose.pdf.facades/pdfviewer). Dokumen yang akan dicetak dapat diberikan sebagai jalur file, aliran dokumen, atau objek [Document](https://reference.aspose.com/pdf/id/net/aspose.pdf/document).

{{% alert color="primary" %}}

Saat mencetak beberapa dokumen, properti [PrinterSettings.PrintRange](https://reference.aspose.com/pdf/id/net/aspose.pdf.printing/printersettings/printrange/) diabaikan, dan semua dokumen dicetak secara penuh.

{{% /alert %}}

{{< tabs tabID="9" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingMultipleDocumentsInSingleJob()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Paths to documents to be printed
    var path1 = dataDir + "PrintDocument.pdf";
    var path2 = dataDir + "Print-PageRange.pdf";
    var path3 = dataDir + "35925_1_3.xps";
    
    // Set up printer and page settings
    var printDocument = new PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
    printerSettings.PrinterName = printDocument.PrinterSettings.PrinterName;
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings();
    pageSettings.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    pageSettings.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingMultipleDocumentsInSingleJob()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Paths to documents to be printed
    var path1 = dataDir + "PrintDocument.pdf";
    var path2 = dataDir + "Print-PageRange.pdf";
    var path3 = dataDir + "35925_1_3.xps";
    
    // Set up printer and page settings
    var printDocument = new PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings
    {
        PrinterName = printDocument.PrinterSettings.PrinterName
    };
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings
    {
        PaperSize = Aspose.Pdf.Printing.PaperSizes.A4,
        Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0)
    }
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
}
```
{{< /tab >}}
{{< /tabs >}}