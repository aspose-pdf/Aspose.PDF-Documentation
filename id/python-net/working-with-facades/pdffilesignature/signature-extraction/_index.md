---
title: Ekstraksi Tanda Tangan
linktitle: Ekstraksi Tanda Tangan
type: docs
weight: 50
url: /id/python-net/signature-extraction/
description: Pelajari cara mengekstrak gambar tanda tangan dan sertifikat penandatangan dari PDF yang ditandatangani menggunakan PdfFileSignature dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak Gambar Tanda Tangan dan Sertifikat dari PDF dalam Python
Abstract: Artikel ini menjelaskan cara mengekstrak data terkait tanda tangan dari dokumen PDF yang ditandatangani dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara membaca tanda tangan pertama yang tersedia, mengekspor gambarnya, dan menyimpan aliran sertifikat yang terkait ke file output.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) antarmuka untuk memeriksa dan mengekstrak data dari dokumen PDF yang ditandatangani. Setelah PDF ditandatangani, Anda dapat menggunakannya untuk mengekspor sumber daya tanda tangan seperti gambar tanda tangan visual dan sertifikat yang terkait dengan tanda tangan.

Contoh ini menunjukkan dua tugas ekstraksi umum:

1. Ekstrak gambar visual yang terkait dengan tanda tangan.
1. Ekstrak sertifikat penandatangan dari PDF yang ditandatangani.

## Ekstrak gambar tanda tangan

Gunakan metode ini ketika PDF berisi tanda tangan yang terlihat dan Anda ingin mengekspor data gambarannya. Contoh ini membuka dokumen yang ditandatangani, mengambil nama tanda tangan pertama yang tersedia, mengekstrak aliran gambar, dan menulisnya ke sebuah file.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Ekstrak sertifikat tanda tangan

Gunakan `extract_certificate()` ketika Anda membutuhkan data sertifikat yang dilampirkan pada tanda tangan. Ini berguna untuk inspeksi, alur kerja validasi, atau menyimpan sertifikat penanda tangan secara terpisah dari dokumen PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

