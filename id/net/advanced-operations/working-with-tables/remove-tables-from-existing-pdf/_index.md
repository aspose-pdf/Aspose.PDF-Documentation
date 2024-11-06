---
title: Hapus Tabel dari PDF yang Ada
linktitle: Hapus Tabel
type: docs
weight: 50
url: id/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Hapus Tabel dari PDF yang Ada",
    "alternativeHeadline": "Cara Menghapus Tabel dari PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, c#, hapus tabel, menghapus tabel",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dok. Aspose.PDF",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF untuk NET menawarkan kemampuan untuk memasukkan/membuat Tabel di dalam dokumen PDF saat sedang dibuat dari awal atau Anda juga dapat menambahkan objek tabel di dokumen PDF yang sudah ada. Namun Anda mungkin memiliki kebutuhan untuk [Memanipulasi Tabel di PDF yang ada](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) di mana Anda dapat memperbarui isi di sel tabel yang ada. Namun Anda mungkin menemukan kebutuhan untuk menghapus objek tabel dari dokumen PDF yang ada.

{{% /alert %}}

Untuk menghapus tabel, kita perlu menggunakan kelas [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) untuk mendapatkan tabel di PDF yang ada dan kemudian memanggil [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Menghapus Tabel dari Dokumen PDF

Kami telah menambahkan fungsi baru yaitu
Kami telah menambahkan fungsi baru yaitu.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Memuat dokumen PDF yang ada
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// Membuat objek TableAbsorber untuk menemukan tabel
TableAbsorber absorber = new TableAbsorber();

// Mengunjungi halaman pertama dengan absorber
absorber.Visit(pdfDocument.Pages[1]);

// Mendapatkan tabel pertama di halaman
AbsorbedTable table = absorber.TableList[0];

// Menghapus tabel
absorber.Remove(table);

// Menyimpan PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## Menghapus Beberapa Tabel dari Dokumen PDF

Terkadang dokumen PDF mungkin mengandung lebih dari satu tabel dan Anda mungkin perlu menghapus beberapa tabel dari dokumen tersebut. Untuk menghapus beberapa tabel dari dokumen PDF, silakan gunakan potongan kode berikut:

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Memuat dokumen PDF yang ada
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// Membuat objek TableAbsorber untuk menemukan tabel
TableAbsorber absorber = new TableAbsorber();

// Mengunjungi halaman kedua dengan absorber
absorber.Visit(pdfDocument.Pages[1]);

// Mendapatkan salinan koleksi tabel
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// Melakukan perulangan melalui salinan koleksi dan menghapus tabel
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// Menyimpan dokumen
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

Harap diperhatikan bahwa menghapus atau mengganti tabel akan mengubah koleksi TableList. Oleh karena itu, jika menghapus/mengganti tabel dalam loop, menduplikasi koleksi TableList sangat penting.

{{% /alert %}}

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

