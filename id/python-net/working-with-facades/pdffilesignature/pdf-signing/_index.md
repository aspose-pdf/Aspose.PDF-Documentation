---
title: Tandatangani Dokumen PDF
linktitle: Tandatangani Dokumen PDF
type: docs
weight: 10
url: /id/python-net/pdf-signing/
description: Pelajari cara menandatangani dokumen PDF di Python menggunakan PdfFileSignature dengan tanda tangan digital berbasis sertifikat, bernama, dan terlihat.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tandatangani Dokumen PDF dengan Tanda Tangan Digital di Python
Abstract: Artikel ini menunjukkan cara menandatangani dokumen PDF dengan Aspose.PDF for Python via .NET menggunakan antarmuka PdfFileSignature. Artikel ini mencakup konfigurasi sertifikat, penandatanganan dengan parameter dasar, penandatanganan dengan objek PKCS7, penetapan nama tanda tangan, dan penerapan tampilan tanda tangan yang terlihat.
---

Aspose.PDF for Python via .NET menyediakan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) antarmuka untuk menerapkan tanda tangan digital pada dokumen PDF yang ada. Dengan menggunakan file sertifikat, Anda dapat menandatangani dokumen secara programatis, menempatkan tanda tangan pada halaman, menetapkan metadata tanda tangan, dan menyesuaikan cara tampilan tanda tangan.

Artikel ini menunjukkan beberapa alur kerja penandatanganan yang umum:

1. Buat dan ikat sebuah `PdfFileSignature` objek ke PDF masukan.
1. Konfigurasikan sertifikat penandatangan.
1. Terapkan tanda tangan digital pada halaman target.
1. Opsional, tetapkan nama tanda tangan dan penampilan yang terlihat.
1. Simpan PDF yang telah ditandatangani.

## Siapkan pembantu penandatanganan yang dapat digunakan kembali

Sebelum menerapkan tanda tangan digital pada PDF, ada baiknya menyiapkan sekumpulan kecil fungsi pembantu yang dapat digunakan kembali. Pembantu ini menginisialisasi penangan tanda tangan, menentukan area tanda tangan yang terlihat, mengonfigurasi sertifikat, dan membangun objek tanda tangan PKCS#7 yang dapat digunakan kembali sehingga contoh penandatanganan di bawah tetap mandiri dan lebih mudah diikuti.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```

## Tandatangani PDF dengan parameter sertifikat dasar

Pendekatan ini mengonfigurasi sertifikat langsung pada `PdfFileSignature` objek. Ini berguna ketika Anda menginginkan alur penandatanganan yang sederhana dengan metadata tanda tangan standar dan tanpa pengelolaan objek tanda tangan terpisah.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Tandatangani PDF dengan objek PKCS7

Gunakan sebuah `PKCS7` objek ketika Anda perlu menyiapkan tanda tangan terlebih dahulu dan kemudian melewatkannya ke panggilan penandatanganan. Pola ini memberi Anda kontrol lebih besar atas pengaturan tanda tangan dan merupakan dasar yang baik untuk alur kerja yang lebih maju.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Tandatangani PDF dengan tanda tangan bernama

Jika alur kerja dokumen Anda bergantung pada nama bidang tanda tangan yang telah ditentukan, sampaikan nama itu ke `sign()`. Ini membuatnya lebih mudah untuk merujuk tanda tangan nanti untuk validasi, pemrosesan, atau integrasi dengan alur kerja persetujuan.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Terapkan tanda tangan yang terlihat

Anda dapat membuat tanda tangan terlihat di halaman PDF dengan menetapkan tampilan khusus ke `PKCS7` object. Ini berguna ketika dokumen output harus menampilkan detail persetujuan seperti alasan, lokasi, dan informasi kontak kepada pengguna akhir.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
