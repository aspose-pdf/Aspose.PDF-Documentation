---
title: Hapus Halaman PDF secara Programatis dengan Python
linktitle: Hapus Halaman PDF
type: docs
weight: 80
url: id/python-net/delete-pages/
description: Anda dapat menghapus halaman dari file PDF Anda menggunakan pustaka Aspose.PDF untuk Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Hapus Halaman PDF secara Programatis dengan Python",
    "alternativeHeadline": "Bagaimana cara menghapus Halaman PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, hapus halaman pdf, hilangkan halaman pdf",
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
    "url": "/python-net/delete-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/delete-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Anda dapat menghapus halaman dari file PDF Anda menggunakan pustaka Aspose.PDF untuk Python via .NET."
}
</script>


Anda dapat menghapus halaman dari file PDF menggunakan Aspose.PDF untuk Python melalui .NET. Untuk menghapus halaman tertentu dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).

## Hapus Halaman dari File PDF

1. Panggil metode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) dan tentukan indeks halaman
1. Panggil metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) untuk menyimpan file PDF yang telah diperbarui
Cuplikan kode berikut menunjukkan cara menghapus halaman tertentu dari file PDF menggunakan Python.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Hapus halaman tertentu
    document.pages.delete(2)

    # Simpan PDF yang telah diperbarui
    document.save(output_pdf)