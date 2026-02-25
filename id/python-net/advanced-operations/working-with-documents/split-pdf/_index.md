---
title: Memisahkan PDF secara programatis dengan Python
linktitle: Memisahkan file PDF
type: docs
weight: 60
url: /id/python-net/split-pdf-document/
description: Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF terpisah dalam aplikasi Python Anda.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Memisahkan halaman PDF menggunakan Python
Abstract: Artikel ini membahas proses memisahkan halaman PDF menjadi file terpisah menggunakan Python, menyoroti kegunaan fitur tersebut untuk mengelola dokumen PDF besar. Artikel ini merujuk pada Aspose.PDF Splitter, sebuah alat daring yang dirancang untuk menunjukkan fungsi pemisahan PDF. Artikel ini menyediakan metode terperinci untuk mencapainya dalam aplikasi Python, melibatkan iterasi melalui halaman dokumen PDF melalui koleksi `PageCollection` objek `Document`. Untuk setiap halaman, dibuat objek `Document` baru, halaman tersebut ditambahkan ke dalamnya, dan file PDF baru disimpan menggunakan metode `save()`. Potongan kode Python yang menyertainya menggambarkan proses ini, menampilkan langkah-langkah yang diperlukan untuk memisahkan dokumen PDF menjadi file terpisah dengan mengiterasi halaman-halamannya dan menyimpan masing-masing sebagai PDF terpisah.
---

Memisahkan halaman PDF dapat menjadi fitur berguna bagi mereka yang ingin membagi file besar menjadi halaman terpisah atau kelompok halaman.

## Contoh Langsung

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) adalah aplikasi web gratis daring yang memungkinkan Anda menyelidiki cara kerja fungsi pemisahan PDF.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Topik ini menunjukkan cara memisahkan halaman PDF menjadi file PDF terpisah dalam aplikasi Python Anda. Untuk memisahkan halaman PDF menjadi file PDF satu halaman menggunakan Python, langkah-langkah berikut dapat diikuti:

1. Loop melalui halaman dokumen PDF melalui koleksi objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) milik [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/)
1. Untuk setiap iterasi, buat objek Document baru dan tambahkan objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) individu ke dalam dokumen kosong
1. Simpan PDF baru menggunakan metode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)

## Memisahkan PDF menjadi beberapa file atau PDF terpisah di Python

Potongan kode Python berikut menunjukkan cara memisahkan halaman PDF menjadi file PDF terpisah.

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


