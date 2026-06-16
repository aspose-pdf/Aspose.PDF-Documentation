---
title: Buat File PDF di Python
linktitle: Buat Dokumen PDF
type: docs
weight: 10
url: /id/python-net/create-pdf-document/
description: Pelajari cara membuat file PDF dan membangun PDF yang dapat dicari di Python menggunakan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat File PDF dengan Python
Abstract: Aspose.PDF for Python via .NET adalah API serbaguna yang dirancang untuk pengembang guna memanipulasi file PDF dalam aplikasi Python yang menargetkan kerangka kerja .NET. API ini memungkinkan pengguna untuk membuat, memuat, memodifikasi, dan mengonversi dokumen PDF dengan mudah. Artikel ini memberikan panduan langkah demi langkah untuk membuat file PDF sederhana menggunakan Aspose.PDF. Prosesnya melibatkan inisialisasi objek `Document`, menambahkan `Page` ke dokumen, menyisipkan `TextFragment` ke dalam paragraf halaman, dan menyimpan file sebagai PDF. Potongan kode Python yang disertakan menunjukkan langkah-langkah ini dengan membuat dokumen PDF yang berisi teks "Hello World!". API ini menyederhanakan penanganan PDF dengan kode minimal, meningkatkan produktivitas pengembang yang bekerja dengan PDF di lingkungan .NET.
---

**Aspose.PDF for Python via .NET** adalah API manipulasi PDF yang memungkinkan pengembang untuk membuat, memuat, memodifikasi, dan mengonversi file PDF langsung dari Python untuk aplikasi .NET dengan hanya beberapa baris kode.

Gunakan contoh-contoh ini ketika Anda perlu membuat file PDF baru dari awal atau mengonversi output OCR menjadi dokumen PDF yang dapat dicari di Python.

## Cara Membuat File PDF Sederhana

Untuk membuat PDF menggunakan Python via .NET dengan Aspose.PDF, Anda dapat mengikuti langkah-langkah berikut:

1. Buat objek dari [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas
1. Tambahkan sebuah [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objek ke [pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) koleksi objek Document
1. Tambah [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) ke [Paragraph](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) koleksi halaman
1. Simpan dokumen PDF yang dihasilkan

```python
import sys
from os import path
import aspose.pdf as ap

def create_new_document(output_pdf):
    """Create a simple PDF with a single “Hello World!” page."""
    document = ap.Document()
    page = document.pages.add()
    page.paragraphs.add(ap.text.TextFragment("Hello World!"))
    document.save(output_pdf)
```

## Cara Membuat Dokumen PDF yang Dapat Dicari

Aspose.PDF for Python via .NET memungkinkan pembuatan dan manipulasi dokumen PDF yang ada. Saat menambahkan elemen Text ke file PDF, PDF yang dihasilkan dapat dicari. Namun, saat mengonversi gambar yang berisi teks ke file PDF, konten PDF yang dihasilkan tidak dapat dicari. Sebagai solusi, kita dapat menerapkan OCR pada file yang dihasilkan sehingga menjadi dapat dicari.

Berikut ini adalah kode lengkap untuk memenuhi kebutuhan ini:

1. Muat PDF menggunakan 'ap.Document'.
1. Konfigurasikan resolusi rendering.
1. Gunakan 'PngDevice.process' untuk mengubah halaman PDF yang dipilih menjadi gambar.
1. Jalankan OCR pada gambar yang dihasilkan.
1. Buat PDF baru dari output OCR.
1. Simpan PDF yang dapat dicari.

```python
import aspose.pdf as ap
import io

# Requires: pip install pytesseract
# Also ensure the Tesseract OCR engine is installed and available on your system PATH.
import pytesseract
from pathlib import Path


# Path to the source PDF
input_pdf_path = "input.pdf"
# Path for the temporary image
temp_image_path = "temp_image.png"
# Path for the searchable PDF
output_pdf_path = "output_searchable.pdf"
page_number = 1
image_stream = io.FileIO(temp_image_path, "w")
try:
    document = ap.Document(input_pdf_path)
    resolution = ap.devices.Resolution(300)
    png_device = ap.devices.PngDevice(resolution)
    png_device.process(document.pages[page_number], image_stream)
    image_stream.close()
    pdf = pytesseract.image_to_pdf_or_hocr(temp_image_path, extension="pdf")
    document = ap.Document(io.BytesIO(pdf))
    document.save(output_pdf_path)
finally:
    image_file = Path(temp_image_path)
    image_file.unlink(missing_ok=True)
```

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Format dokumen PDF dalam Python](/pdf/id/python-net/formatting-pdf-document/)
- [Manipulasi dokumen PDF dalam Python](/pdf/id/python-net/manipulate-pdf-document/)
- [Optimalkan file PDF dalam Python](/pdf/id/python-net/optimize-pdf/)

