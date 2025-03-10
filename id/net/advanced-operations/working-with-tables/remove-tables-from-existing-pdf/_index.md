---
title: Hapus Tabel dari PDF yang Ada
linktitle: Hapus Tabel
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /id/net/remove-tables-from-existing-pdf/
description: Pahami cara menghapus tabel dari dokumen PDF menggunakan Aspose.PDF for .NET, meningkatkan kejelasan dan struktur dokumen.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Tables from existing PDF",
    "alternativeHeadline": "Effortlessly Eliminate Tables from Existing PDF Files",
    "abstract": "Fitur Hapus Tabel di Aspose.PDF for .NET memungkinkan pengguna untuk secara efisien menghapus objek tabel dari dokumen PDF yang ada menggunakan kelas TableAbsorber. Fungsionalitas ini menyederhanakan proses pengelolaan konten PDF dengan menyediakan metode yang sederhana untuk menemukan dan menghapus tabel, meningkatkan kemampuan pengeditan dokumen",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF tidak hanya dapat melakukan tugas sederhana dan mudah tetapi juga dapat menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

{{% alert color="primary" %}}

Aspose.PDF untuk NET menawarkan kemampuan untuk menyisipkan/membuat Tabel di dalam dokumen PDF saat dibuat dari awal atau Anda juga dapat menambahkan objek tabel di dokumen PDF yang ada. Namun, Anda mungkin memiliki kebutuhan untuk [Memanipulasi Tabel di PDF yang Ada](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) di mana Anda dapat memperbarui konten di sel tabel yang ada. Namun, Anda mungkin menghadapi kebutuhan untuk menghapus objek tabel dari dokumen PDF yang ada.

{{% /alert %}}

Untuk menghapus tabel, kita perlu menggunakan kelas [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) untuk mendapatkan tabel di PDF yang ada dan kemudian memanggil [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Hapus Tabel dari dokumen PDF

Kami telah menambahkan fungsi baru yaitu Remove() ke kelas TableAbsorber yang ada untuk menghapus tabel dari dokumen PDF. Setelah absorber berhasil menemukan tabel di halaman, ia menjadi mampu untuk menghapusnya. Silakan periksa potongan kode berikut yang menunjukkan cara menghapus tabel dari dokumen PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Remove the table
        absorber.Remove(table);

        // Save PDF document
        document.Save(dataDir + "RemoveTable_out.pdf");
    }
}
```

## Hapus Beberapa Tabel dari dokumen PDF

Terkadang dokumen PDF mungkin berisi lebih dari satu tabel dan Anda mungkin memiliki kebutuhan untuk menghapus beberapa tabel darinya. Untuk menghapus beberapa tabel dari dokumen PDF, silakan gunakan potongan kode berikut:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveMultipleTables()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit second page with absorber
        absorber.Visit(document.Pages[1]);

        // Get copy of table collection
        Aspose.Pdf.Text.AbsorbedTable[] tables = new Aspose.Pdf.Text.AbsorbedTable[absorber.TableList.Count];
        absorber.TableList.CopyTo(tables, 0);

        // Loop through the copy of collection and removing tables
        foreach (var table in tables)
        {
            absorber.Remove(table);
        }

        // Save PDF document
        document.Save(dataDir + "RemoveMultipleTables_out.pdf");
    }
}
```

{{% alert color="primary" %}}

Harap diperhatikan bahwa penghapusan atau penggantian tabel mengubah koleksi TableList. Oleh karena itu, dalam kasus penghapusan/penggantian tabel dalam sebuah loop, penyalinan koleksi TableList adalah hal yang penting.

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