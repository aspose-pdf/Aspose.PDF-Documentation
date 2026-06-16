---
title: Verifikasi Tanda Tangan
linktitle: Verifikasi Tanda Tangan
type: docs
weight: 90
url: /id/python-net/signature-verification/
description: Pelajari cara memverifikasi tanda tangan digital dan memeriksa apakah PDF berisi tanda tangan menggunakan PdfFileSignature di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verifikasi Tanda Tangan PDF di Python
Abstract: Artikel ini menjelaskan cara memverifikasi tanda tangan digital dalam dokumen PDF dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara memvalidasi tanda tangan yang ada dan cara memeriksa apakah PDF berisi tanda tangan apa pun.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) antarmuka untuk memvalidasi dokumen PDF yang ditandatangani. Setelah PDF ditandatangani, Anda dapat menggunakannya untuk mengonfirmasi bahwa tanda tangan valid dan mendeteksi apakah dokumen tersebut berisi entri tanda tangan apa pun.

Contoh ini menunjukkan dua tugas verifikasi umum:

1. Verifikasi bahwa tanda tangan PDF yang ada valid.
1. Periksa apakah PDF berisi tanda tangan apa pun.

## Verifikasi tanda tangan PDF

Gunakan `verify_signature()` ketika Anda perlu memvalidasi tanda tangan tertentu dalam dokumen. Contoh ini menemukan nama tanda tangan pertama yang tersedia dan memverifikasi apakah tanda tangan tersebut valid.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Periksa apakah PDF berisi tanda tangan

Gunakan `contains_signature()` ketika Anda hanya perlu mengetahui apakah PDF menyertakan tanda tangan apa pun. Ini berguna sebagai pemeriksaan cepat sebelum menjalankan logika verifikasi atau ekstraksi yang lebih detail.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
