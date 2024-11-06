---
title: Mencetak PDF di .NET Framework
linktitle: Mencetak PDF di .NET Framework
type: docs
weight: 10
url: id/net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: Anda dapat mencetak file PDF ke printer default menggunakan pengaturan printer dan halaman dengan C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mencetak PDF di .NET Framework",
    "alternativeHeadline": "Cara mencetak PDF di .NET Framework",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, pdf di .NET Framework",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat mencetak file PDF ke printer default menggunakan pengaturan printer dan halaman dengan C#."
}
</script>
Potongan kode berikut ini juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **Cetak File Pdf dalam C# - Cetak File PDF ke Printer Default menggunakan Pengaturan Printer dan Halaman**

Artikel ini menjelaskan cara Mencetak File PDF ke Printer Default menggunakan Pengaturan Printer dan Halaman dalam C#.

Kelas [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) memungkinkan Anda untuk mencetak file PDF ke printer default. Anda perlu membuat objek PdfViewer dan membuka PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Untuk menentukan pengaturan cetak yang berbeda, gunakan kelas `PageSettings` dan `PrinterSettings`. Akhirnya, panggil metode [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) untuk mencetak PDF ke printer default. Potongan kode berikut menunjukkan cara mencetak PDF ke printer default dengan pengaturan printer dan halaman.

```csharp
public static void SimplePrint()
{
    // Buat objek PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Buka file PDF masukan
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // Atur atribut untuk pencetakan
    viewer.AutoResize = true;         // Cetak file dengan ukuran disesuaikan
    viewer.AutoRotate = true;         // Cetak file dengan rotasi disesuaikan
    viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak

    // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // Atur nama printer
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Atur PageSize (jika diperlukan)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Atur PageMargins (jika diperlukan)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Cetak dokumen menggunakan pengaturan printer dan halaman
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Tutup file PDF setelah pencetakan
    viewer.Close();
}
```
Untuk menampilkan dialog cetak, coba gunakan potongan kode berikut:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // Kode pencetakan dokumen ada di sini
    // Cetak dokumen menggunakan pengaturan printer dan halaman
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```

