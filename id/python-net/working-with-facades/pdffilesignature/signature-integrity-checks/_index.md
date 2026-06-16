---
title: Pemeriksaan Integritas Tanda Tangan
linktitle: Pemeriksaan Integritas Tanda Tangan
type: docs
weight: 70
url: /id/python-net/signature-integrity-checks/
description: Pelajari cara memeriksa apakah tanda tangan PDF mencakup seluruh dokumen dan memvalidasi integritas dokumen yang ditandatangani menggunakan PdfFileSignature di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validasi Cakupan dan Integritas Tanda Tangan PDF di Python
Abstract: Artikel ini menjelaskan cara memeriksa integritas tanda tangan digital dalam dokumen PDF yang ditandatangani dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara memverifikasi apakah sebuah tanda tangan mencakup seluruh dokumen dan cara memvalidasi integritas konten yang ditandatangani.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) antarmuka untuk memvalidasi dokumen PDF yang ditandatangani. Setelah sebuah file ditandatangani, Anda dapat menggunakannya untuk memeriksa apakah tanda tangan berlaku untuk dokumen lengkap dan apakah konten yang ditandatangani masih valid.

Contoh ini menunjukkan dua pemeriksaan integritas umum:

1. Periksa apakah tanda tangan mencakup seluruh dokumen.
1. Validasi integritas konten PDF yang ditandatangani.

## Periksa apakah tanda tangan mencakup seluruh dokumen

Gunakan `covers_whole_document()` ketika Anda perlu memastikan bahwa tanda tangan berlaku untuk seluruh PDF dan tidak hanya pada sebagian kontennya. Contoh tersebut membaca nama tanda tangan pertama yang tersedia dan memeriksa cakupannya.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## Validasi integritas dokumen

Gunakan `verify_signed()` untuk memastikan bahwa konten dokumen yang ditandatangani tidak berubah setelah tanda tangan diterapkan. Metode ini membantu memverifikasi apakah dokumen tetap valid untuk tanda tangan yang dipilih.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

