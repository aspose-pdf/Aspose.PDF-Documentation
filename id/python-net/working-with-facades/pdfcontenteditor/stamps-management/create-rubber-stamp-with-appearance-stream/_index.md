---
title: Buat Stempel Karet dengan Aliran Penampilan
linktitle: Buat Stempel Karet dengan Aliran Penampilan
type: docs
weight: 30
url: /id/python-net/create-rubber-stamp-with-appearance-stream/
description: Contoh ini memuat PDF, membuat stempel karet pada halaman 1 menggunakan file gambar untuk penampilannya, dan menyimpan dokumen yang telah dimodifikasi. ✨
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Stempel Karet dengan Penampilan Gambar Kustom Menggunakan PdfContentEditor dalam Python
Abstract: Contoh ini menunjukkan cara membuat anotasi stempel karet dengan penampilan gambar kustom dalam PDF menggunakan Aspose.PDF for Python melalui API Facades. Pendekatan ini memungkinkan Anda menerapkan stempel bermerek atau visual yang kaya seperti logo, segel, atau tanda tangan.
---

Anotasi stempel karet dapat disesuaikan menggunakan file gambar eksternal. Alih‑alih hanya mengandalkan stempel berbasis teks, Anda dapat mendefinisikan penampilan visual (misalnya, logo perusahaan atau lencana persetujuan) dan menempatkannya pada halaman.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instansi.
1. Hubungkan dokumen PDF masukan.
1. Tentukan persegi panjang untuk lokasi stempel.
1. Gunakan file gambar sebagai tampilan stempel.
1. Terapkan pengaturan teks dan warna.
1. Simpan dokumen PDF yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Create rubber stamp using appearance_file overload (image path)
    content_editor.create_rubber_stamp(
        1,
        apd.Rectangle(100, 400, 200, 60),
        "Stamp with custom appearance",
        apd.Color.dark_green,
        image_file,
    )
    # Save updated document
    content_editor.save(outfile)
```    
