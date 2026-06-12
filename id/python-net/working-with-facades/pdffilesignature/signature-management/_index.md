---
title: Manajemen Tanda Tangan
linktitle: Manajemen Tanda Tangan
type: docs
weight: 80
url: /id/python-net/signature-management/
description: Pelajari cara menghapus tanda tangan digital dari dokumen PDF dan secara opsional membersihkan bidang tanda tangan menggunakan PdfFileSignature di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus Tanda Tangan PDF dan Bersihkan Bidang Tanda Tangan di Python
Abstract: Artikel ini menjelaskan cara mengelola tanda tangan digital yang ada dalam dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara menghapus tanda tangan dari PDF dan cara menghapus tanda tangan bersama dengan bidang tanda tangan yang terkait.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) Antarmuka untuk bekerja dengan tanda tangan digital yang ada dalam dokumen PDF. Selain membaca dan memvalidasi tanda tangan, Anda juga dapat menghapusnya ketika alur kerja memerlukan konten yang ditandatangani diperbarui atau bidang tanda tangan dibersihkan.

Contoh ini menunjukkan dua tugas manajemen tanda tangan yang umum:

1. Hapus tanda tangan dari dokumen PDF.
1. Hapus tanda tangan dan bersihkan bidang tanda tangan yang terkait.

## Hapus tanda tangan dari PDF

Gunakan `remove_signature()` ketika Anda ingin menghapus tanda tangan yang dipilih dari dokumen sambil mempertahankan struktur bidang tanda tangan yang mendasarinya. Contoh ini membuka PDF yang ditandatangani, menemukan nama tanda tangan, menghapusnya, dan menyimpan file output yang diperbarui.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Hapus tanda tangan dan bersihkan bidang

Gunakan overload dengan tambahan `True` tandai ketika Anda ingin menghapus tanda tangan dan juga membersihkan bidang tanda tangan yang terkait. Ini berguna ketika bidang tersebut tidak seharusnya tetap berada di dokumen setelah tanda tangan dihapus.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
