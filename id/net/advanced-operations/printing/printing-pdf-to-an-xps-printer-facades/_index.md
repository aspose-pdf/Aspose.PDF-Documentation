---
title: Mencetak PDF ke Printer XPS
linktitle: Mencetak PDF ke Printer XPS (Facades)
type: docs
weight: 20
url: /id/net/printing-pdf-to-an-xps-printer-facades/
keywords: "print pdf to xps, print pdf to xps c#"
description: Halaman ini menunjukkan cara mencetak PDF ke printer XPS menggunakan kelas PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Mencetak PDF ke Printer XPS",
    "alternativeHeadline": "Cara mencetak PDF ke Printer XPS",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, pdf ke printer XPS",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "Halaman ini menunjukkan cara mencetak PDF ke printer XPS menggunakan kelas PdfViewer."
}
</script>
Kode berikut juga berfungsi dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## **Mencetak PDF ke printer XPS dalam C#**

Anda dapat mencetak file PDF ke printer XPS, atau printer lunak lainnya, menggunakan kelas [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Untuk melakukan itu, buat objek dari kelas PdfViewer dan buka file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Anda dapat mengatur berbagai pengaturan cetak menggunakan kelas PrinterSettings dan PageSettings. Anda juga perlu mengatur properti PrinterName ke printer XPS atau printer lunak lain yang telah Anda instal.

Akhirnya, gunakan metode [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) untuk mencetak PDF ke XPS atau printer lunak lainnya. Kode berikut menunjukkan cara mencetak file PDF ke printer XPS.

```csharp
public static void PrintToXpsPrinter()
{
    // Buat objek PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Buka file PDF masukan
    viewer.BindPdf(_dataDir + "input.pdf");

    // Atur atribut untuk pencetakan
    viewer.AutoResize = true;         // Cetak file dengan ukuran yang disesuaikan
    viewer.AutoRotate = true;         // Cetak file dengan rotasi yang disesuaikan
    viewer.PrintPageDialog = false;   // Jangan tampilkan dialog nomor halaman saat mencetak

    // Buat objek untuk pengaturan printer dan halaman serta PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Atur nama printer XPS/PDF
    ps.PrinterName = "Microsoft XPS Document Writer";
    // Atau atur printer PDF
    // Ps.PrinterName = "Adobe PDF";

    // Atur UkuranHalaman (jika diperlukan)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Atur MarginHalaman (jika diperlukan)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Cetak dokumen menggunakan pengaturan printer dan halaman
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Tutup file PDF setelah pencetakan
    viewer.Close();
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

