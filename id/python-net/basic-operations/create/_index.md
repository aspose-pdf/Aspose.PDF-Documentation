---
title: Membuat Dokumen PDF secara Programatis
linktitle: Membuat PDF
type: docs
weight: 10
url: id/python-net/create-document/
description: Halaman ini menjelaskan cara membuat dokumen PDF dari awal dengan Aspose.PDF untuk Python via .NET library.
---

Bagi pengembang, ada banyak skenario di mana menjadi perlu untuk membuat file PDF secara programatis. Anda mungkin perlu membuat laporan PDF dan file PDF lainnya secara programatis dalam perangkat lunak Anda. Menulis kode dan fungsi sendiri dari awal cukup lama dan tidak efisien. Untuk membuat file PDF dengan Python, ada solusi yang lebih baik - **Aspose.PDF untuk Python via .NET**.

## Cara Membuat File PDF menggunakan Python

Untuk membuat file PDF menggunakan Python, langkah-langkah berikut dapat digunakan.

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

1. Tambahkan objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke koleksi [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) dari objek Document
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ke koleksi [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) dari halaman
1. Simpan dokumen PDF yang dihasilkan

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