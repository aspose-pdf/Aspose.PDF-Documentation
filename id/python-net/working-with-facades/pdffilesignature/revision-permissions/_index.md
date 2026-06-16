---
title: Revisi dan Izin
linktitle: Revisi dan Izin
type: docs
weight: 40
url: /id/python-net/revision-permissions/
description: Pelajari cara memeriksa revisi tanda tangan, revisi dokumen, dan izin sertifikasi dalam file PDF menggunakan PdfFileSignature di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Baca Data Revisi Tanda Tangan PDF dan Izin Akses di Python
Abstract: Artikel ini menjelaskan cara memeriksa informasi revisi dan izin dalam file PDF yang ditandatangani atau disertifikasi dengan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara mendapatkan nomor revisi dari sebuah tanda tangan, menghitung total revisi dokumen, dan membaca izin akses dari PDF yang disertifikasi.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fasad untuk bekerja dengan dokumen PDF yang ditandatangani dan disertifikasi. Selain menambahkan tanda tangan, Anda juga dapat memeriksa metadata tanda tangan untuk memahami berapa banyak revisi yang dimiliki dokumen dan perubahan apa yang diizinkan setelah sertifikasi.

Contoh ini menunjukkan tiga tugas inspeksi umum:

1. Dapatkan nomor revisi untuk tanda tangan yang ada.
1. Dapatkan total jumlah revisi dalam dokumen yang ditandatangani.
1. Baca izin akses dari PDF yang bersertifikat.

## Dapatkan nomor revisi untuk tanda tangan

Gunakan pendekatan ini ketika sebuah PDF sudah berisi satu atau lebih tanda tangan dan Anda perlu mengidentifikasi revisi yang terkait dengan tanda tangan tertentu. Contoh ini menyelesaikan nama tanda tangan pertama yang tersedia dan kemudian memanggil `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## Dapatkan total jumlah revisi dokumen

Gunakan `get_total_revision()` ketika Anda perlu mengetahui berapa banyak revisi yang disimpan dalam PDF yang ditandatangani. Ini berguna untuk memeriksa apakah dokumen telah mengalami beberapa pembaruan setelah tanda tangan asli diterapkan.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## Dapatkan izin akses dari PDF bersertifikat

Dokumen bersertifikasi dapat menentukan perubahan apa yang diizinkan setelah sertifikasi. Gunakan `get_access_permissions()` untuk memeriksa tingkat izin tersebut dan menentukan apakah dokumen memungkinkan tidak ada perubahan, pengisian formulir, atau modifikasi terkontrol lainnya.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

