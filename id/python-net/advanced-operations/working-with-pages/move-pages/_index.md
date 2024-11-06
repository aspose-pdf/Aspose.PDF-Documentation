---
title: Pindahkan Halaman PDF secara programatis melalui Python
linktitle: Pindahkan Halaman PDF
type: docs
weight: 100
url: id/python-net/move-pages/
description: Cobalah untuk memindahkan halaman ke lokasi yang diinginkan atau ke akhir file PDF menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2023-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pindahkan Halaman PDF secara programatis Python",
    "alternativeHeadline": "Bagaimana cara memindahkan Halaman PDF dengan Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, pindahkan halaman pdf",
    "wordcount": "302",
    "proficiencyLevel":"Pemula",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/move-pages/"
    },
    "dateModified": "2023-04-04",
    "description": "Cobalah untuk memindahkan halaman ke lokasi yang diinginkan atau ke akhir file PDF menggunakan Aspose.PDF untuk Python via .NET."
}
</script>


## Memindahkan Halaman dari satu Dokumen PDF ke Dokumen Lain

Topik ini menjelaskan cara memindahkan halaman dari satu dokumen PDF ke akhir dokumen lain menggunakan Python. Untuk memindahkan halaman kita harus:

1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF sumber.
1. Membuat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF tujuan.
1. Mendapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) halaman ke dokumen tujuan.
1. Menyimpan PDF keluaran menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) halaman di dokumen sumber.

1. Simpan PDF sumber menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan cara memindahkan satu halaman.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(src_file_name)
    dstDocument = ap.Document(dst_File_name)
    page = srcDocument.pages[2]
    dstDocument.pages.add(page)
    # Simpan file keluaran
    dstDocument.save(dst_File_name_new)
    srcDocument.pages.delete(2)
    srcDocument.save(src_file_name_new)
```

## Memindahkan Sekumpulan Halaman dari satu Dokumen PDF ke Dokumen Lain

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF sumber.
1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF tujuan.
1. Tentukan array dengan nomor halaman yang akan dipindahkan.
1. Jalankan loop melalui array:

1. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
1. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) halaman ke dokumen tujuan.
1. Simpan PDF keluaran menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) halaman dalam dokumen sumber menggunakan array.
1. Simpan PDF sumber menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Cuplikan kode berikut menunjukkan kepada Anda cara menyisipkan halaman kosong di akhir file PDF.

```python

    import aspose.pdf as ap

    srcDocument = ap.Document(input_pdf)
    dstDocument = ap.Document()
    pages = [1, 3]
    for page_index in pages:
        page = srcDocument.pages[page_index]
        dstDocument.pages.add(page)
    # Simpan file keluaran
    dstDocument.save(output_pdf_1)
    srcDocument.pages.delete(pages)
    srcDocument.save(output_pdf_2)
```


## Memindahkan Halaman ke Lokasi Baru dalam Dokumen PDF Saat Ini

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) dengan file PDF sumber.
2. Dapatkan Halaman dari koleksi [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/).
3. [add()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) halaman ke lokasi baru (misalnya ke akhir).
4. [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/#methods) halaman di lokasi sebelumnya.
5. Simpan output PDF menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python
import aspose.pdf as ap

srcDocument = ap.Document(input_pdf)

page = srcDocument.pages[2]
srcDocument.pages.add(page)
srcDocument.pages.delete(2)

# Simpan file output
srcDocument.save(output_pdf)