---
title: Tambah dan Hapus Penanda Buku menggunakan Python
linktitle: Tambah dan Hapus Penanda Buku
type: docs
weight: 10
url: /python-net/add-and-delete-bookmark/
description: Anda dapat menambahkan penanda buku ke dokumen PDF dengan Python. Dimungkinkan untuk menghapus semua atau penanda buku tertentu dari dokumen PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Tambah dan Hapus Penanda Buku",
    "alternativeHeadline": "Cara menambah dan menghapus Penanda Buku dari PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pembuatan dokumen pdf",
    "keywords": "pdf, python, hapus penanda buku, tambah penanda buku",
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
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Anda dapat menambahkan penanda buku ke dokumen PDF dengan Python. Dimungkinkan untuk menghapus semua atau penanda buku tertentu dari dokumen PDF."
}
</script>


## Tambahkan Penanda Buku ke Dokumen PDF

Penanda buku disimpan dalam koleksi objek [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), yang berada di dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Untuk menambahkan penanda buku ke PDF:

1. Buka dokumen PDF menggunakan objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Buat penanda buku dan tentukan propertinya.
3. Tambahkan koleksi [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) ke koleksi Outlines.

Cuplikan kode berikut menunjukkan cara menambahkan penanda buku dalam dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat objek penanda buku
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Penanda Buku Tes"
    outline.italic = True
    outline.bold = True
    # Tetapkan nomor halaman tujuan
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Tambahkan penanda buku dalam koleksi outline dokumen.
    document.outlines.append(outline)

    # Simpan output
    document.save(output_pdf)
```


## Tambahkan Penanda Halaman Anak ke Dokumen PDF

Penanda halaman dapat bersarang, menunjukkan hubungan hierarkis dengan penanda halaman induk dan anak. Artikel ini menjelaskan cara menambahkan penanda halaman anak, yaitu penanda halaman tingkat kedua, ke PDF.

Untuk menambahkan penanda halaman anak ke file PDF, pertama-tama tambahkan penanda halaman induk:

1. Buka dokumen.
1. Tambahkan penanda halaman ke [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), mendefinisikan propertinya.
1. Tambahkan OutlineItemCollection ke koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) objek Dokumen.

Penanda halaman anak dibuat seperti penanda halaman induk, dijelaskan di atas, tetapi ditambahkan ke koleksi Outlines penanda halaman induk.

Cuplikan kode berikut menunjukkan cara menambahkan penanda halaman anak ke dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Buat objek penanda halaman induk
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Induk Outline"
    outline.italic = True
    outline.bold = True

    # Buat objek penanda halaman anak
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Anak Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Tambahkan penanda halaman anak ke koleksi penanda halaman induk
    outline.append(childOutline)
    # Tambahkan penanda halaman induk ke koleksi outline dokumen.
    document.outlines.append(outline)

    # Simpan output
    document.save(output_pdf)
```


## Hapus Semua Bookmark dari Dokumen PDF

Semua bookmark dalam PDF disimpan dalam koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Artikel ini menjelaskan cara menghapus semua bookmark dari file PDF.

Untuk menghapus semua bookmark dari file PDF:

1. Panggil metode Delete dari koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
2. Simpan file yang telah dimodifikasi menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dari objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Cuplikan kode berikut menunjukkan cara menghapus semua bookmark dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Hapus semua bookmark
    document.outlines.delete()

    # Simpan file yang telah diperbarui
    document.save(output_pdf)

```

## Hapus Bookmark Tertentu dari Dokumen PDF

Untuk menghapus bookmark tertentu dari file PDF:

1. Masukkan judul penanda buku sebagai parameter ke metode Delete koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Kemudian simpan file yang diperbarui dengan metode Save objek Document.

Kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) menyediakan koleksi [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Metode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) menghapus penanda buku apa pun dengan judul yang diteruskan ke metode.

Cuplikan kode berikut menunjukkan cara menghapus penanda buku tertentu dari dokumen PDF.

```python

    import aspose.pdf as ap

    # Buka dokumen
    document = ap.Document(input_pdf)

    # Hapus outline tertentu berdasarkan Judul
    document.outlines.delete("Child Outline")

    # Simpan file yang diperbarui
    document.save(output_pdf)