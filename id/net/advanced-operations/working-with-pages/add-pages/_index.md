---
title: Tambahkan Halaman ke Dokumen PDF
linktitle: Tambahkan Halaman
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/add-pages/
description: Jelajahi cara menambahkan halaman ke PDF yang ada di .NET dengan Aspose.PDF untuk meningkatkan dan memperluas dokumen Anda.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/insert-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Pages to PDF Document",
    "alternativeHeadline": "Insert and Manage Pages in PDF Easily with C#",
    "abstract": "Fitur dalam Aspose.PDF for .NET memungkinkan pengguna untuk dengan mudah menyisipkan halaman ke dalam dokumen PDF di lokasi yang ditentukan, meningkatkan fleksibilitas dan organisasi dokumen. Fungsionalitas ini tidak hanya mendukung penambahan halaman tetapi juga mencakup opsi untuk memindahkan atau menghapus halaman yang ada menggunakan C#. Permudah manajemen PDF Anda dengan tambahan intuitif ini ke dalam toolkit pengembangan Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Pages to PDF, insert PDF page, empty page PDF, C# PDF manipulation, PDF document generation, PageCollection, Aspose.PDF for .NET, move PDF pages, remove PDF pages, add pages to PDF",
    "wordcount": "651",
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
    "url": "/net/add-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "Artikel ini mengajarkan cara menyisipkan (menambahkan) halaman di lokasi yang diinginkan dalam file PDF. Pelajari cara memindahkan, menghapus (menghapus) halaman dari file PDF menggunakan C#."
}
</script>

Aspose.PDF for .NET API memberikan fleksibilitas penuh untuk bekerja dengan halaman dalam dokumen PDF menggunakan C# atau bahasa .NET lainnya. Ini mempertahankan semua halaman dari dokumen PDF dalam [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) yang dapat digunakan untuk bekerja dengan halaman PDF.
Aspose.PDF for .NET memungkinkan Anda untuk menyisipkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.
Bagian ini menunjukkan cara menambahkan halaman ke PDF menggunakan C#.

## Tambahkan atau Sisipkan Halaman dalam File PDF

Aspose.PDF for .NET memungkinkan Anda untuk menyisipkan halaman ke dokumen PDF di lokasi mana pun dalam file serta menambahkan halaman ke akhir file PDF.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

### Sisipkan Halaman Kosong dalam File PDF di Lokasi yang Diinginkan

Untuk menyisipkan halaman kosong dalam file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF input.
1. Panggil metode [Insert](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection/methods/insert) dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) dengan indeks yang ditentukan.
1. Simpan PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara menyisipkan halaman dalam file PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPage.pdf"))
    {
       // Insert an empty page in a PDF
       document.Pages.Insert(2);
        // Save PDF document
       document.Save(dataDir + "InsertEmptyPage_out.pdf");
    }
}
```

Dalam contoh di atas, kami menambahkan halaman kosong dengan parameter default. Jika Anda perlu membuat ukuran halaman sama dengan halaman lain dalam dokumen, Anda harus menambahkan beberapa baris kode:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageWithParameters()
{
    var page = document.Pages.Insert(2);
    //copy page parameters from page 1
    page.ArtBox = document.Pages[1].ArtBox;
    page.BleedBox = document.Pages[1].BleedBox;
    page.CropBox = document.Pages[1].CropBox;
    page.MediaBox = document.Pages[1].MediaBox;
    page.TrimBox = document.Pages[1].TrimBox;
}
```

### Tambahkan Halaman Kosong di Akhir File PDF

Terkadang, Anda ingin memastikan bahwa dokumen diakhiri dengan halaman kosong. Topik ini menjelaskan cara menyisipkan halaman kosong di akhir dokumen PDF.

Untuk menyisipkan halaman kosong di akhir file PDF:

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) dengan file PDF input.
1. Panggil metode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1) dari koleksi [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection), tanpa parameter apa pun.
1. Simpan PDF output menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Potongan kode berikut menunjukkan cara menyisipkan halaman kosong di akhir file PDF.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void InsertAnEmptyPageAtTheEnd()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "InsertEmptyPageAtEnd.pdf"))
    {
        // Insert an empty page at the end of a PDF file
        document.Pages.Add();
        // Save PDF document
        document.Save(dataDir + "InsertEmptyPageAtEnd_out.pdf");
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