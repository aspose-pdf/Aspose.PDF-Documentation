title: Contoh Hello World menggunakan Python
linktitle: Contoh Hello World
type: docs
weight: 20
url: /id/python-net/hello-world-example/
description: Contoh ini menunjukkan cara membuat dokumen PDF sederhana dengan teks Hello World menggunakan Aspose.PDF untuk Python via .NET.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Contoh "Hello World" menunjukkan sintaks paling sederhana dan program paling sederhana dalam bahasa pemrograman tertentu. Pengembang diperkenalkan ke sintaks bahasa pemrograman dasar dengan belajar bagaimana mencetak "Hello World" di layar perangkat. Oleh karena itu, kita secara tradisional akan memulai perkenalan kita dengan pustaka kita dari sini.

Dalam artikel ini, kita membuat dokumen PDF berisi teks "Hello World!". Setelah menginstal **Aspose.PDF untuk Python via .NET** di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat bagaimana API Aspose.PDF bekerja.

Cuplikan kode di bawah ini mengikuti langkah-langkah ini:

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Tambahkan [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke objek dokumen
1. Buat objek [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Tambahkan TextFragment ke koleksi [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) dari halaman
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) dokumen PDF yang dihasilkan

Cuplikan kode berikut adalah program "Hello World" untuk menunjukkan cara kerja Aspose.PDF untuk Python melalui .NET API.

```python

    import aspose.pdf as ap

    # Inisialisasi objek dokumen
    document = ap.Document()
    # Tambahkan halaman
    page = document.pages.add()
    # Inisialisasi objek textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Tambahkan fragmen teks ke halaman baru
    page.paragraphs.add(text_fragment)
    # Simpan PDF yang diperbarui
    document.save("output.pdf")
```