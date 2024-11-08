---
title: Konversi PDF ke PostScript
linktitle: Konversi PDF ke PostScript
type: docs
weight: 30
url: /id/net/pdf-to-postscript-conversion/
keywords: "pdf to postscript c#"
description: Kami memiliki solusi untuk konversi PDF ke PostScript. Gunakan untuk tugas ini pencetakan dan kelas PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Konversi PDF ke PostScript",
    "alternativeHeadline": "Mengonversi PDF ke PostScript",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, pdf to postscript",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok Aspose.PDF",
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
    "dateModified": "2022-02-04",
    "description": "Kami memiliki solusi untuk konversi PDF ke PostScript. Gunakan untuk tugas ini pencetakan dan kelas PdfViewer."
}
</script>
Kode berikut ini juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## **PDF Ke Postscript dalam C#**

Kelas PdfViewer menyediakan kemampuan untuk mencetak dokumen PDF dan dengan bantuan kelas ini, kita juga dapat mengonversi file PDF ke format PostScript. Untuk mengonversi file PDF menjadi PostScript, pertama-tama instal printer PS apa pun dan cukup cetak ke file dengan bantuan PdfViewer. Anda dapat mengikuti instruksi yang ditentukan oleh Universitas Hawaii tentang cara menginstal printer PS. Cuplikan kode berikut menunjukkan kepada Anda cara mencetak dan mengonversi PDF ke format PostScript.

```csharp
public static void PrintToPostscriptFile()
{
    // Jalur ke direktori dokumen.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    Aspose.Pdf.Facades.PdfViewer viewer = new Aspose.Pdf.Facades.PdfViewer();
    viewer.BindPdf(_dataDir + "input.pdf");
    // Atur PrinterSettings dan PageSettings
    System.Drawing.Printing.PrinterSettings printerSettings = new System.Drawing.Printing.PrinterSettings();
    printerSettings.Copies = 1;
    // Atur printer PS, seseorang dapat menemukan driver ini dalam daftar driver printer yang telah terpasang di Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";
    // Atur nama file keluaran dan atribut PrintToFile
    printerSettings.PrintFileName = _dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
    // Nonaktifkan dialog halaman cetak
    viewer.PrintPageDialog = false;
    // Teruskan objek pengaturan printer ke metode
    viewer.PrintDocumentWithSettings(printerSettings);
    viewer.Close();
}
```
## Memeriksa Status Pekerjaan Cetak

Sebuah file PDF dapat dicetak ke printer fisik maupun ke Microsoft XPS Document Writer, tanpa menampilkan dialog cetak, menggunakan kelas PdfViewer. Saat mencetak file PDF yang besar, prosesnya mungkin memakan waktu lama sehingga pengguna mungkin tidak yakin apakah proses pencetakan telah selesai atau menemui masalah. Untuk menentukan status pekerjaan cetak, gunakan properti PrintStatus. Potongan kode berikut menunjukkan cara mencetak file PDF ke file XPS dan mendapatkan status pencetakan.

```csharp
public static void CheckingPrintJobStatus()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
    // Jalur ke direktori dokumen.
    // string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instansiasi objek PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Mengikat file PDF sumber
    viewer.BindPdf(_dataDir + "input.pdf");
    viewer.AutoResize = true;

    // Sembunyikan dialog pencetakan
    viewer.PrintPageDialog = false;

    // Buat objek Pengaturan Printer
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Tentukan nama printer
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Nama hasil cetakan
    ps.PrintFileName = "ResultantPrintout.xps";

    // Cetak output ke file
    ps.PrintToFile = true;
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = System.Drawing.Printing.PrintRange.SomePages;

    // Tentukan ukuran kertas cetakan
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Cetak dokumen dengan pengaturan yang ditentukan di atas
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Periksa status cetak
    if (viewer.PrintStatus != null)
    {
        // Sebuah pengecualian dilemparkan
        if (viewer.PrintStatus is Exception ex)
        {
            // Dapatkan pesan pengecualian
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // Tidak ada kesalahan yang ditemukan. Pekerjaan cetak telah selesai dengan sukses
        Console.WriteLine("printing completed without any issue..");
    }
}
```
## Mendapatkan/Mengatur Nama Pemilik Pekerjaan Cetak

Baru-baru ini kami menerima kebutuhan untuk mendapatkan/mengatur nama pemilik pekerjaan cetak (pengguna yang sebenarnya menekan tombol cetak di halaman web). Informasi ini diperlukan saat mencetak file PDF. Untuk memenuhi kebutuhan ini, Anda dapat menggunakan properti bernama PrinterJobName:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
// Mengikat file PDF sumber
viewer.BindPdf(dataDir + "input.pdf");
// Tentukan nama pekerjaan cetak
viewer.PrinterJobName = GetCurrentUserCredentials();
```

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static string GetCurrentUserCredentials()
{
    // Implementasi tergantung pada jenis aplikasi yang berjalan (ASP.NET, Windows forms, dll.)
    string userCredentials = string.Empty;
    return userCredentials;
}
```
## Menggunakan Impersonasi

Pendekatan lain untuk mendapatkan nama pemilik Pekerjaan Cetak adalah menggunakan impersonasi (menjalankan rutinitas pencetakan dalam konteks pengguna lain) atau pengguna dapat mengubah nama pemilik langsung dengan menggunakan rutinitas SetJob.

Harap dicatat bahwa tidak ada kemungkinan untuk mengatur nilai pemilik menggunakan API pencetakan Aspose.PDF karena pertimbangan keamanan. Properti PrinterJobName dapat digunakan untuk mengatur nilai kolom nama dokumen dalam aplikasi cetak spooler. Cuplikan kode yang dibagikan di atas hanya menunjukkan bagaimana pengguna dapat menggabungkan nama pengguna ke dalam kolom nama dokumen (misalnya menggunakan sintaks UserName\documentName). Tetapi pengaturan kolom Pemilik dapat diimplementasikan dengan cara berikut secara langsung oleh pengguna:

1) Impersonasi. Karena nilai kolom pemilik berisi nilai pengguna yang menjalankan kode pencetakan, ada cara untuk memanggil API pencetakan Aspose.PDF di dalam konteks pengguna lain. Sebagai contoh, silakan lihat solusi yang dijelaskan di sini. Dengan menggunakan kelas ini, pengguna dapat mencapai tujuan:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();
PdfViewer viewer = new PdfViewer();
viewer.BindPdf(dataDir + "input.pdf");
viewer.PrintPageDialog = false;
// Jangan memunculkan dialog nomor halaman saat mencetak
using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserNamePassword"))
{
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    ps.PrinterName = "Microsoft XPS Document Writer";
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName adalah nilai kolom Pemilik dalam aplikasi spooler
    viewer.Close();
}
```
2) Menggunakan API Spooler dan rutin SetJob

Potongan kode berikut menunjukkan cara mencetak beberapa halaman file PDF dalam mode Simplex dan beberapa halaman dalam mode Duplex.

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
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
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

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Perpustakaan Aspose.PDF untuk .NET",
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
                "contactType": "penjualan",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
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
    "applicationCategory": "Perpustakaan Manipulasi PDF untuk .NET",
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
```

