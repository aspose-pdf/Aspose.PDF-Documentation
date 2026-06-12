---
title: Buat dokumen PDF secara programatis
linktitle: Buat PDF
type: docs
weight: 10
url: /id/python-net/create-document/
description: Halaman ini menjelaskan cara membuat dokumen PDF dari awal dengan pustaka Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Membuat file PDF dengan Aspose.PDF for Python
Abstract: Dalam pengembangan perangkat lunak, menghasilkan file PDF secara programatis merupakan kebutuhan umum, terutama untuk membuat laporan dan dokumen lainnya. Menulis kode khusus untuk tugas ini dapat tidak efisien dan memakan waktu. Sebagai gantinya, pengembang dapat memanfaatkan **Aspose.PDF for Python via .NET**, solusi yang kuat untuk membuat file PDF menggunakan Python. Proses tersebut melibatkan pembuatan objek `Document`, menambahkan objek `Page` ke koleksi `Pages` dokumen, menyisipkan `TextFragment` ke dalam koleksi `paragraphs` halaman, dan kemudian menyimpan dokumen. Sebuah potongan kode Python contoh memperlihatkan langkah‑langkah ini, menampilkan betapa mudahnya menghasilkan file PDF menggunakan Aspose.PDF.
---

Untuk pengembang, ada banyak skenario di mana menjadi perlu untuk secara programatis menghasilkan file PDF. Anda mungkin perlu secara programatis menghasilkan laporan PDF dan file PDF lain dalam perangkat lunak Anda. Menulis kode dan fungsi Anda sendiri dari awal terasa cukup panjang dan tidak efisien. Untuk membuat file PDF dengan Python, ada solusi yang lebih baik - **Aspose.PDF for Python via .NET**.

## Cara Membuat File PDF menggunakan Python

Untuk membuat file PDF menggunakan Python, langkah‑langkah berikut dapat digunakan.

1. Buat sebuah objek dari [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas
1. Tambahkan [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objek ke [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) koleksi objek Document
1. Tambah [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ke [paragraf](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) koleksi halaman
1. Simpan dokumen PDF yang dihasilkan

```python
import aspose.pdf as ap

# Initialize document object
document = ap.Document()
# Add page
page = document.pages.add()
# Add text to new page
page.paragraphs.add(ap.text.TextFragment("Hello World!"))
# Define output file path
output_pdf = "output.pdf"
# Save updated PDF
output_pdf = "output.pdf"
document.save(output_pdf)
```
