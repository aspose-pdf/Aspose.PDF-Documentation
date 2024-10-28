---
title: Memanipulasi Tabel di PDF yang Ada
linktitle: Memanipulasi Tabel
type: docs
weight: 40
url: /net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Memanipulasi Tabel di PDF yang Ada",
    "alternativeHeadline": "Cara memperbarui konten Tabel di PDF yang ada",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, memanipulasi tabel",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

## Manipulasi tabel di PDF yang ada

Salah satu fitur terawal yang didukung oleh Aspose.PDF untuk .NET adalah kemampuannya dalam Bekerja dengan Tabel dan ini memberikan dukungan yang besar untuk menambahkan tabel dalam file PDF yang dihasilkan dari awal atau file PDF yang sudah ada. Anda juga mendapatkan kemampuan untuk Mengintegrasikan Tabel dengan Database (DOM) untuk membuat tabel dinamis berdasarkan konten database. Dalam rilis baru ini, kami telah mengimplementasikan fitur baru dalam mencari dan mem-parse tabel sederhana yang sudah ada di halaman dokumen PDF. Kelas baru bernama **Aspose.PDF.Text.TableAbsorber** menyediakan kemampuan ini. Penggunaan TableAbsorber sangat mirip dengan kelas TextFragmentAbsorber yang sudah ada. Potongan kode berikut menunjukkan langkah-langkah untuk memperbarui konten dalam sel tabel tertentu.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Muat file PDF yang ada
Document pdfDocument = new Document(dataDir + "input.pdf");
// Buat objek TableAbsorber untuk menemukan tabel
TableAbsorber absorber = new TableAbsorber();

// Kunjungi halaman pertama dengan absorber
absorber.Visit(pdfDocument.Pages[1]);

// Dapatkan akses ke tabel pertama di halaman, sel pertama mereka dan fragmen teks di dalamnya
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// Ubah teks dari fragmen teks pertama di sel
fragment.Text = "hi world";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## Ganti Tabel Lama dengan Tabel Baru dalam Dokumen PDF

Jika Anda perlu menemukan tabel tertentu dan menggantinya dengan yang diinginkan, Anda dapat menggunakan metode Replace() dari Kelas [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) untuk melakukan hal tersebut. Contoh berikut menunjukkan fungsionalitas untuk mengganti tabel di dalam dokumen PDF:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Muat dokumen PDF yang ada
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// Buat objek TableAbsorber untuk menemukan tabel
TableAbsorber absorber = new TableAbsorber();

// Kunjungi halaman pertama dengan absorber
absorber.Visit(pdfDocument.Pages[1]);

// Dapatkan tabel pertama di halaman
AbsorbedTable table = absorber.TableList[0];

// Buat tabel baru
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Kol 1");
row.Cells.Add("Kol 2");
row.Cells.Add("Kol 3");

// Ganti tabel dengan yang baru
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// Simpan dokumen
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
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
                "availableLanguage": "Inggris"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "penjualan",
                "areaServed": "GB",
                "availableLanguage": "Inggris"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "penjualan",
                "areaServed": "AU",
                "availableLanguage": "Inggris"
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

