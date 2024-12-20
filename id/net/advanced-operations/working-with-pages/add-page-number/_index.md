---
title: Menambahkan Nomor Halaman ke PDF dengan C#
linktitle: Tambahkan Nomor Halaman
type: docs
weight: 100
url: /id/net/add-page-number/
description: Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan Stempel Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menambahkan Nomor Halaman ke PDF dengan C#",
    "alternativeHeadline": "Cara menambahkan Stempel Nomor Halaman ke PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, stempel nomor halaman",
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
    "url": "/net/add-page-number/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-page-number/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF untuk .NET memungkinkan Anda untuk menambahkan Stempel Nomor Halaman ke file PDF Anda menggunakan kelas PageNumber Stamp."
}
</script>

Semua dokumen harus memiliki nomor halaman di dalamnya. Nomor halaman memudahkan pembaca untuk menemukan berbagai bagian dokumen.
**Aspose.PDF for .NET** memungkinkan Anda untuk menambahkan nomor halaman dengan PageNumberStamp.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

Anda dapat menggunakan kelas [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) untuk menambahkan cap nomor halaman dalam file PDF.
Anda dapat menggunakan kelas [PageNumberStamp](https://reference.aspose.com/pdf/net/aspose.pdf/pagenumberstamp) untuk menambahkan cap nomor halaman dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_StampsWatermarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir+ "PageNumberStamp.pdf");

// Buat cap nomor halaman
PageNumberStamp pageNumberStamp = new PageNumberStamp();
// Apakah cap tersebut sebagai latar belakang
pageNumberStamp.Background = false;
pageNumberStamp.Format = "Halaman # dari " + pdfDocument.Pages.Count;
pageNumberStamp.BottomMargin = 10;
pageNumberStamp.HorizontalAlignment = HorizontalAlignment.Center;
pageNumberStamp.StartingNumber = 1;
// Atur properti teks
pageNumberStamp.TextState.Font = FontRepository.FindFont("Arial");
pageNumberStamp.TextState.FontSize = 14.0F;
pageNumberStamp.TextState.FontStyle = FontStyles.Bold;
pageNumberStamp.TextState.FontStyle = FontStyles.Italic;
pageNumberStamp.TextState.ForegroundColor = Color.Aqua;

// Tambahkan cap ke halaman tertentu
pdfDocument.Pages[1].AddStamp(pageNumberStamp);

dataDir = dataDir + "PageNumberStamp_out.pdf";
// Simpan dokumen keluaran
pdfDocument.Save(dataDir);
```
## Contoh Langsung

[Menambahkan nomor halaman PDF](https://products.aspose.app/pdf/page-number) adalah aplikasi web gratis online yang memungkinkan Anda untuk menyelidiki bagaimana fungsi menambahkan nomor halaman bekerja.

[![Cara menambahkan nomor halaman di pdf menggunakan C#](page_number.png)](https://products.aspose.app/pdf/page-number)

## Menambah/Menghapus penomoran Bates

**Penomoran Bates** (juga dikenal sebagai stempel Bates) digunakan di bidang hukum, medis, dan bisnis untuk menempatkan nomor identifikasi dan/atau cap tanggal/waktu pada gambar dan dokumen saat mereka discan atau diproses, misalnya, selama tahap penemuan persiapan untuk persidangan atau mengidentifikasi tanda terima bisnis. Proses ini memberikan identifikasi, perlindungan, dan penomoran berurutan otomatis dari gambar atau dokumen.

Aspose.PDF saat ini memiliki dukungan terbatas untuk Penomoran Bates. Fungsionalitas ini akan diperbarui sesuai permintaan pelanggan.

### Cara menghapus penomoran Bates

```csharp
static void Demo03()
{
    Document doc = new Document(@"C:\Samples\Sample-Document03.pdf");
    foreach (var page in doc.Pages)
    {
        var batesNum = page.Artifacts.First(ar => ar.CustomSubtype == "BatesN");
        page.Artifacts.Delete(batesNum);
    }
    doc.Save(@"C:\Samples\Sample-Document04.pdf");
}
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

