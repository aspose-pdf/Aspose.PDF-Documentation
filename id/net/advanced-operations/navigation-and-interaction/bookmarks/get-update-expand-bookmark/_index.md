---
title: Tambah dan Hapus Penanda
linktitle: Tambah dan Hapus Penanda
type: docs
weight: 10
url: /id/net/add-and-delete-bookmark/
description: Anda dapat menambahkan penanda pada dokumen PDF dengan C#. Anda juga dapat menghapus semua atau penanda tertentu dari dokumen PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/add-and-delete-a-bookmark/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambah dan Hapus Penanda",
    "alternativeHeadline": "Cara menambahkan dan menghapus Penanda dari PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, hapus penanda, tambah penanda",
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
    "url": "/net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-and-delete-bookmark/"
    },
    "dateModified": "2022-02-04",
    "description": "Anda dapat menambahkan penanda pada dokumen PDF dengan C#. Anda juga dapat menghapus semua atau penanda tertentu dari dokumen PDF."
}
</script>
Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Menambahkan Bookmark pada Dokumen PDF

Bookmark disimpan dalam koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) dari objek Dokumen, yang berada dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).

Untuk menambahkan bookmark ke PDF:

1. Buka dokumen PDF menggunakan objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Buat bookmark dan tentukan propertinya.
1. Tambahkan koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection) ke koleksi Outlines.

Potongan kode berikut menunjukkan cara menambahkan bookmark dalam dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "AddBookmark.pdf");

// Buat objek bookmark
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Test Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;
// Tetapkan nomor halaman tujuan
pdfOutline.Action = new GoToAction(pdfDocument.Pages[1]);
// Tambahkan bookmark dalam koleksi garis besar dokumen.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddBookmark_out.pdf";
// Simpan output
pdfDocument.Save(dataDir);
```
## Menambahkan Bookmark Anak ke Dokumen PDF

Bookmark dapat bersarang, menunjukkan hubungan hierarkis dengan bookmark induk dan anak. Artikel ini menjelaskan cara menambahkan bookmark anak, yaitu, bookmark tingkat kedua, ke PDF.

Untuk menambahkan bookmark anak ke file PDF, pertama tambahkan bookmark induk:

1. Buka dokumen.
1. Tambahkan bookmark ke [OutlineItemCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlineitemcollection), mendefinisikan propertinya.
1. Tambahkan OutlineItemCollection ke koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection) dari objek Dokumen.

Bookmark anak dibuat seperti bookmark induk, dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines dari bookmark induk

Potongan kode berikut menunjukkan cara menambahkan bookmark anak ke dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "AddChildBookmark.pdf");

// Buat objek bookmark induk
OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfOutline.Title = "Parent Outline";
pdfOutline.Italic = true;
pdfOutline.Bold = true;

// Buat objek bookmark anak
OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.Outlines);
pdfChildOutline.Title = "Child Outline";
pdfChildOutline.Italic = true;
pdfChildOutline.Bold = true;

// Tambahkan bookmark anak dalam koleksi bookmark induk
pdfOutline.Add(pdfChildOutline);
// Tambahkan bookmark induk dalam koleksi outline dokumen.
pdfDocument.Outlines.Add(pdfOutline);

dataDir = dataDir + "AddChildBookmark_out.pdf";
// Simpan output
pdfDocument.Save(dataDir);
```
## Menghapus Semua Bookmark dari Dokumen PDF

Semua bookmark dalam PDF disimpan dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Artikel ini menjelaskan cara menghapus semua bookmark dari file PDF.

Untuk menghapus semua bookmark dari file PDF:

1. Panggil metode Delete dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Simpan file yang telah dimodifikasi menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) dari objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Berikut adalah potongan kode yang menunjukkan cara menghapus semua bookmark dari dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "DeleteAllBookmarks.pdf");

// Hapus semua bookmark
pdfDocument.Outlines.Delete();

dataDir = dataDir + "DeleteAllBookmarks_out.pdf";
// Simpan file yang telah diperbarui
pdfDocument.Save(dataDir);
```
## Menghapus Bookmark Tertentu dari Dokumen PDF

Untuk menghapus bookmark tertentu dari file PDF:

1. Berikan judul bookmark sebagai parameter ke metode Delete koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection).
1. Kemudian simpan file yang telah diperbarui dengan metode Save objek Document.

Kelas [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) menyediakan koleksi [OutlineCollection](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection). Metode [Delete](https://reference.aspose.com/pdf/net/aspose.pdf/outlinecollection/methods/delete) menghapus bookmark dengan judul yang diberikan ke metode tersebut.

Potongan kode berikut menunjukkan cara menghapus bookmark tertentu dari dokumen PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Bookmarks();

// Buka dokumen
Document pdfDocument = new Document(dataDir + "DeleteParticularBookmark.pdf");

// Hapus garis besar tertentu dengan Judul
pdfDocument.Outlines.Delete("Child Outline");

// Simpan file yang telah diperbarui
pdfDocument.Save(dataDir + "DeleteParticularBookmark_out.pdf");
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

