---
title: Buat dokumen PDF secara programatis
linktitle: Buat PDF
type: docs
weight: 10
url: /id/python-net/create-document/
description: Halaman ini menjelaskan cara membuat dokumen PDF dari awal dengan perpustakaan Aspose.PDF untuk Python via .NET.
TechArticle: true
AlternativeHeadline: Menghasilkan file PDF dengan Aspose.PDF untuk Python
Abstract: Dalam pengembangan perangkat lunak, menghasilkan file PDF secara programatis merupakan kebutuhan umum, terutama untuk membuat laporan dan dokumen lainnya. Menulis kode khusus untuk tugas ini dapat tidak efisien dan memakan waktu. Sebagai gantinya, pengembang dapat memanfaatkan **Aspose.PDF untuk Python via .NET**, solusi yang kuat untuk membuat file PDF menggunakan Python. Prosesnya melibatkan pembuatan objek `Document`, menambahkan objek `Page` ke koleksi `Pages` dokumen, menyisipkan `TextFragment` ke koleksi `paragraphs` halaman, dan kemudian menyimpan dokumen. Sebuah contoh potongan kode Python menunjukkan langkah-langkah ini, menampilkan kemudahan dalam menghasilkan file PDF menggunakan Aspose.PDF.
---

Bagi pengembang, ada banyak skenario di mana diperlukan untuk menghasilkan file PDF secara programatis. Anda mungkin perlu menghasilkan laporan PDF dan file PDF lain secara programatis dalam perangkat lunak Anda. Menulis kode dan fungsi sendiri dari awal cukup panjang dan tidak efisien. Untuk membuat file PDF dengan Python, ada solusi yang lebih baik - **Aspose.PDF untuk Python via .NET**.

## Cara Membuat File PDF menggunakan Python

Untuk membuat file PDF menggunakan Python, langkah-langkah berikut dapat digunakan.

1. Buat objek kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Tambahkan objek [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ke koleksi [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) dari objek Document
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ke koleksi [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) pada halaman
1. Simpan dokumen PDF hasil

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



