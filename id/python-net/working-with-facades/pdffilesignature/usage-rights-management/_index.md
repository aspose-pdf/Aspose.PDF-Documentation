---
title: Manajemen Hak Penggunaan
linktitle: Manajemen Hak Penggunaan
type: docs
weight: 100
url: /id/python-net/usage-rights-management/
description: Pelajari cara mendeteksi dan menghapus hak penggunaan dari dokumen PDF menggunakan PdfFileSignature dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Hak Penggunaan PDF dalam Python
Abstract: Artikel ini menjelaskan cara memeriksa dan menghapus hak penggunaan dari dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara memeriksa apakah PDF berisi hak penggunaan dan cara menyimpan versi baru dokumen setelah hak tersebut dihapus.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fasad untuk bekerja dengan PDF yang ditandatangani dan pengaturan hak penggunaan terkait. Dalam beberapa alur kerja, Anda mungkin perlu memeriksa apakah sebuah dokumen berisi hak penggunaan dan menghapusnya sebelum menyimpan versi terbaru file.

Contoh ini menunjukkan satu tugas manajemen hak penggunaan yang umum:

1. Periksa apakah PDF berisi hak penggunaan.
1. Hapus hak penggunaan dari dokumen.
1. Simpan file PDF yang diperbarui.

## Periksa apakah PDF berisi hak penggunaan

Sebelum menghapus hak penggunaan, contoh memeriksa status dokumen saat ini dengan memanggil `contains_usage_rights()`. Ini memungkinkan Anda mengonfirmasi apakah hak penggunaan ada sebelum melakukan perubahan.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Hapus hak penggunaan dari PDF

Gunakan `remove_usage_rights()` ketika dokumen tidak lagi harus mempertahankan pengaturan hak penggunaan yang ada. Contohnya memeriksa status awal, menghapus hak tersebut, dan menyimpan PDF yang diperbarui ke file baru.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
