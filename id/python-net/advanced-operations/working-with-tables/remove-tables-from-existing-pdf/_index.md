---
title: Menghapus Tabel dari PDF yang Ada
linktitle: Menghapus Tabel
type: docs
weight: 50
url: id/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Menghapus Tabel dari PDF yang Ada",
    "alternativeHeadline": "Cara Menghapus Tabel dari PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, menghapus tabel, hapus tabel",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Tim Dokumen Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF untuk Python via .NET menawarkan kemampuan untuk memasukkan/membuat Tabel di dalam dokumen PDF saat sedang dihasilkan dari awal atau Anda juga dapat menambahkan objek tabel di dokumen PDF yang sudah ada. Namun, Anda mungkin memiliki persyaratan untuk [Memanipulasi Tabel dalam PDF yang ada](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/) di mana Anda dapat memperbarui konten dalam sel tabel yang ada. Namun, Anda mungkin menemui persyaratan untuk menghapus objek tabel dari dokumen PDF yang ada.

{{% /alert %}}

Untuk menghapus tabel, kita perlu menggunakan kelas [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) untuk mendapatkan tabel dalam PDF yang ada dan kemudian memanggil [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods).

## Menghapus Tabel dari dokumen PDF

Kami telah menambahkan fungsi baru yaitu.
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) ke Kelas [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) yang ada untuk menghapus tabel dari dokumen PDF. Setelah absorber berhasil menemukan tabel pada halaman, ia menjadi mampu untuk menghapusnya. Silakan periksa potongan kode berikut yang menunjukkan cara menghapus tabel dari dokumen PDF:

```python

    import aspose.pdf as ap

    # Muat dokumen PDF yang ada
    pdf_document = ap.Document(input_file)
    # Buat objek TableAbsorber untuk menemukan tabel
    absorber = ap.text.TableAbsorber()
    # Kunjungi halaman pertama dengan absorber
    absorber.visit(pdf_document.pages[1])
    # Dapatkan tabel pertama pada halaman
    table = absorber.table_list[0]
    # Hapus tabel
    absorber.remove(table)
    # Simpan PDF
    pdf_document.save(output_file)
```

## Menghapus Beberapa Tabel dari dokumen PDF

Kadang-kadang dokumen PDF dapat berisi lebih dari satu tabel dan Anda mungkin memiliki kebutuhan untuk menghapus beberapa tabel darinya. Untuk menghapus beberapa tabel dari dokumen PDF, silakan gunakan potongan kode berikut:

```python

    import aspose.pdf as ap

    # Memuat dokumen PDF yang ada
    pdf_document = ap.Document(input_file)
    # Membuat objek TableAbsorber untuk menemukan tabel
    absorber = ap.text.TableAbsorber()
    # Kunjungi halaman kedua dengan absorber
    absorber.visit(pdf_document.pages[1])
    # Dapatkan salinan koleksi tabel
    tables = absorber.table_list
    #  Melakukan iterasi melalui salinan koleksi dan menghapus tabel
    for table in tables:
        absorber.remove(table)
    # Simpan dokumen
    pdf_document.save(output_file)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>