---
title: Mengubah Gambar ke PDF dalam Python
linktitle: Mengubah Gambar ke file PDF
type: docs
weight: 10
url: /id/python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: Topik ini menunjukkan cara mengubah Gambar menjadi PDF menggunakan Aspose.PDF untuk Python melalui pustaka C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Pustaka kami menunjukkan potongan kode untuk mengonversi format gambar paling populer - JPEG. Anda dapat dengan sangat mudah mengonversi gambar JPG menjadi PDF dengan Aspose.PDF untuk Python melalui C++ dengan mengikuti langkah-langkah berikut:

## Mengubah Gambar ke PDF

Anda dapat dengan sangat mudah mengonversi gambar JPG menjadi PDF dengan Aspose.PDF untuk C++ dengan mengikuti langkah-langkah berikut:

1. Buka file gambar input menggunakan pustaka PIL
1. Dapatkan lebar dan tinggi gambar
1. Buat instance Dokumen baru menggunakan pustaka AsposePDFPythonWrappers
1. Tetapkan tinggi dan lebar gambar secara tetap
1. Tambahkan halaman baru ke dokumen
1. Tambahkan gambar ke halaman
1. Simpan PDF keluaran dengan metode 'document.save'.

Potongan kode di bawah ini menunjukkan cara mengonversi Gambar JPG menjadi PDF menggunakan Python melalui C++:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Tetapkan jalur direktori untuk file data
dataDir = os.path.join(os.getcwd(), "samples")

# Tetapkan jalur file input
input_file = os.path.join(dataDir, "sample.jpg")

# Tetapkan jalur file output
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Buka file gambar input menggunakan pustaka PIL
pil_img = Image.open(input_file)

# Dapatkan lebar dan tinggi gambar
width, height = pil_img.size

# Buat instance Dokumen baru menggunakan pustaka AsposePDFPythonWrappers
document = apw.Document()

# Buat instance Gambar baru menggunakan pustaka AsposePDFPythonWrappers
image = apw.Image()

# Tetapkan jalur file gambar
image.file = input_file

# Tetapkan tinggi dan lebar tetap gambar
image.fix_height = height
image.fix_width = width

# Tambahkan halaman baru ke dokumen
page = document.pages.add()

# Tambahkan gambar ke halaman
page.paragraphs.add(image)

# Simpan dokumen ke jalur file output
document.save(output_file)
```