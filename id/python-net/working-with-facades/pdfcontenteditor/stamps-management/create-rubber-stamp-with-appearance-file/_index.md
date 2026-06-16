---
title: Buat Stempel Karet dengan File Tampilan
linktitle: Buat Stempel Karet dengan File Tampilan
type: docs
weight: 20
url: /id/python-net/create-rubber-stamp-with-appearance-file/
description: Contoh ini mengikat PDF masukan, membuat stempel karet pada halaman 1 menggunakan file gambar sebagai tampilan stempel, dan menyimpan PDF yang telah diperbarui.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Buat Stempel Karet dengan Tampilan Kustom dalam PDF Menggunakan PdfContentEditor
Abstract: Contoh ini menunjukkan cara menambahkan anotasi stempel karet dengan tampilan kustom (gambar) ke dokumen PDF menggunakan Aspose.PDF for Python via the Facades API. Stempel kustom memungkinkan Anda menyertakan logo, tanda tangan, atau visual bermerek sebagai bagian dari stempel.
---

Anotasi stempel karet dapat disesuaikan tidak hanya dengan teks tetapi juga dengan menggunakan file gambar sebagai tampilan mereka. Pendekatan ini berguna untuk menambahkan logo perusahaan, stempel tanda tangan, atau indikator visual apa pun ke halaman PDF Anda.

1. Buat sebuah [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Hubungkan dokumen PDF input.
1. Tentukan persegi panjang untuk stempel.
1. Gunakan file gambar khusus untuk menentukan tampilan stempel karet.
1. Atur teks dan warna stempel.
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
