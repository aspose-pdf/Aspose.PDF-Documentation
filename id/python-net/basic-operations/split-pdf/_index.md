---
title: Membagi File PDF di Python
linktitle: Membagi file PDF
type: docs
weight: 60
url: /id/python-net/split-pdf/
description: Pelajari cara memisahkan halaman PDF menjadi file PDF terpisah dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memisahkan halaman PDF menggunakan Python
Abstract: Artikel ini membahas proses memisahkan halaman PDF menjadi file terpisah menggunakan Python, menyoroti kegunaan fitur tersebut untuk mengelola dokumen PDF besar. Artikel ini merujuk pada Aspose.PDF Splitter, sebuah alat online yang dirancang untuk mendemonstrasikan fungsi pemisahan PDF. Artikel menyajikan metode terperinci untuk mencapai hal ini dalam aplikasi Python, melibatkan iterasi melalui halaman dokumen PDF melalui `Document` object's `PageCollection`. Untuk setiap halaman, sebuah objek `Document` baru dibuat, halaman ditambahkan ke objek tersebut, dan file PDF baru disimpan menggunakan metode `save()`. Sebuah potongan kode Python yang menyertainya mengilustrasikan proses ini, menampilkan langkah-langkah yang diperlukan untuk memisahkan dokumen PDF menjadi file terpisah dengan mengiterasi halaman-halamannya dan menyimpan masing-masing sebagai PDF individual.
---

Memisahkan halaman PDF dapat menjadi fitur yang berguna bagi mereka yang ingin membagi file besar menjadi halaman terpisah atau kelompok halaman.

Gunakan alur kerja ini ketika Anda perlu memecah PDF besar menjadi file satu halaman atau set dokumen yang lebih kecil untuk distribusi, peninjauan, atau pemrosesan lanjutan.

## Contoh Langsung

[Pemecah Aspose.PDF](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis daring yang memungkinkan Anda menyelidiki cara kerja fungsi pemisahan presentasi.

[![Aspose Membagi PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF terpisah dalam aplikasi Python Anda. Untuk memisahkan halaman PDF menjadi file PDF satu halaman menggunakan Python, langkah-langkah berikut dapat diikuti:

1. Lakukan loop melalui halaman dokumen PDF melalui [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [KoleksiHalaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) koleksi
1. Untuk setiap iterasi, buat objek Document baru dan tambahkan masing-masing [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objek ke dalam dokumen kosong
1. Simpan PDF baru menggunakan [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode

## Pisahkan PDF menjadi beberapa file atau PDF terpisah dalam Python

Cuplikan kode Python berikut menunjukkan cara memisahkan halaman PDF menjadi file PDF terpisah.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    page_count = 1

    # Loop through all the pages
    for pdfPage in document.pages:
        new_document = ap.Document()
        new_document.pages.add(pdfPage)
        new_document.save(output_path + "_page_" + str(page_count) + ".pdf")
        page_count = page_count + 1
```

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Gabungkan file PDF di Python](/pdf/id/python-net/merge-pdf-documents/)
- [Optimalkan file PDF dalam Python](/pdf/id/python-net/optimize-pdf/)
- [Manipulasi dokumen PDF dalam Python](/pdf/id/python-net/manipulate-pdf-document/)

