---
title: Dapatkan Hak Istimewa Dokumen
linktitle: Dapatkan Hak Istimewa Dokumen
type: docs
weight: 10
url: /id/python-net/get-document-privileges/
description: Pelajari cara memeriksa hak istimewa dokumen PDF secara programatis menggunakan Aspose.PDF for Python. Tutorial ini menunjukkan cara menggunakan kelas PdfFileInfo untuk membaca pengaturan keamanan dokumen, seperti izin mencetak, menyalin, atau memodifikasi.
lastmod: "2026-06-12"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Mendapatkan Hak Istimewa Dokumen PDF Menggunakan Aspose.PDF for Python
Abstract: Dokumen PDF dapat memiliki pembatasan keamanan yang membatasi tindakan seperti mencetak, menyalin, memodifikasi, atau mengisi formulir. Dengan mengakses hak istimewa ini secara programatis, pengembang dapat menentukan operasi apa yang diizinkan pada PDF. Panduan ini menunjukkan cara menggunakan kelas PdfFileInfo untuk mengambil hak istimewa dokumen PDF dan menampilkannya di Python.
---

Hak istimewa PDF mengontrol apa yang dapat dan tidak dapat dilakukan pengguna dengan dokumen. Izin umum meliputi:

- Mencetak dokumen
- Menyalin konten
- Memodifikasi anotasi atau konten
- Mengisi bidang formulir
- Menggunakan pembaca layar
- Menyusun atau menggabungkan dokumen

Dengan Aspose.PDF for Python, Anda dapat memeriksa pengaturan ini secara programatis menggunakan [PdfFileInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileinfo/) class. Ini sangat berguna saat bekerja dengan banyak PDF dalam alur kerja otomatis, memverifikasi kepatuhan, atau mengendalikan penanganan dokumen dalam aplikasi.

1. Muat file PDF.
1. Ambil hak istimewa dokumen tersebut.
1. Tampilkan tindakan yang diizinkan untuk dokumen.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def get_document_privileges(input_file_name):
    pdf_metadata = pdf_facades.PdfFileInfo(input_file_name)

    privileges = pdf_metadata.get_document_privilege()

    print("Document Privileges:")
    print(f"  Can Print: {privileges.allow_print}")
    print(f"  Can Degraded Print: {privileges.allow_degraded_printing}")
    print(f"  Can Copy: {privileges.allow_copy}")
    print(f"  Can Modify Contents: {privileges.allow_modify_contents}")
    print(f"  Can Modify Annotations: {privileges.allow_modify_annotations}")
    print(f"  Can Fill In: {privileges.allow_fill_in}")
    print(f"  Can Screen Readers: {privileges.allow_screen_readers}")
    print(f"  Can Assembly: {privileges.allow_assembly}")
```
