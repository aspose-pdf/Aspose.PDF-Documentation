---
title: Informasi Tanda Tangan
linktitle: Informasi Tanda Tangan
type: docs
weight: 60
url: /id/python-net/signature-information/
description: Pelajari cara membaca nama tanda tangan, detail penandatangan, cap waktu, dan metadata tanda tangan dari file PDF yang ditandatangani menggunakan PdfFileSignature dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Baca Detail Tanda Tangan dari Dokumen PDF dalam Python
Abstract: Artikel ini menjelaskan cara memeriksa metadata tanda tangan dalam dokumen PDF yang ditandatangani dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara menampilkan nama tanda tangan, membaca detail penandatangan, mendapatkan tanggal dan waktu penandatanganan, serta mengekstrak alasan dan lokasi tanda tangan.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) antarmuka untuk memeriksa tanda tangan digital dalam dokumen PDF. Setelah dokumen ditandatangani, Anda dapat menggunakannya untuk membaca nama tanda tangan dan mengambil metadata seperti nama penandatangan, informasi kontak, waktu penandatanganan, alasan, dan lokasi.

Contoh ini menunjukkan empat tugas informasi tanda tangan yang umum:

1. Daftar semua nama tanda tangan dalam PDF yang ditandatangani.
1. Baca detail penandatangan untuk tanda tangan yang dipilih.
1. Dapatkan tanggal dan waktu penandatanganan.
1. Baca alasan dan lokasi tanda tangan.

## Dapatkan nama tanda tangan

Gunakan metode ini ketika PDF mungkin berisi satu atau lebih tanda tangan dan Anda ingin memeriksa entri tanda tangan mana yang tersedia. Contoh ini membuka dokumen dan mencetak daftar yang dikembalikan oleh `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Dapatkan detail penandatangan

Setelah Anda mengetahui nama tanda tangan, Anda dapat mengambil metadata khusus penandatangan. Contoh ini membaca nama penandatangan dan informasi kontak untuk tanda tangan pertama yang tersedia dalam dokumen.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Dapatkan tanggal dan waktu tanda tangan

Gunakan `get_date_time()` untuk menentukan kapan tanda tangan tertentu diterapkan. Ini berguna untuk audit dan untuk menampilkan riwayat tanda tangan dalam alur kerja dokumen.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Dapatkan alasan dan lokasi tanda tangan

Tanda tangan digital juga dapat menyimpan metadata deskriptif seperti alasan penandatanganan dan lokasi. Contoh ini mengambil kedua nilai untuk tanda tangan yang dipilih dan mencetaknya bersama.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

