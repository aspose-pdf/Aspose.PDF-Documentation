---
title: Kelas PdfFileSignature
linktitle: Kelas PdfFileSignature
type: docs
weight: 60
url: /id/python-net/pdffilesignature-class/
description: Jelajahi cara menambahkan, memverifikasi, dan menghapus tanda tangan digital dari dokumen PDF di Python menggunakan kelas PDFFileSignature dengan Aspose.PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

- [Penandatanganan PDF](/pdf/id/python-net/pdf-signing/)
- [Sertifikasi PDF](/pdf/id/python-net/pdf-certification/)
- [Manajemen Tanda Tangan](/pdf/id/python-net/signature-management/)
- [Verifikasi Tanda Tangan](/pdf/id/python-net/signature-verification/)
- [Informasi Tanda Tangan](/pdf/id/python-net/signature-information/)
- [Pemeriksaan Integritas Tanda Tangan](/pdf/id/python-net/signature-integrity-checks/)
- [Revisi & Izin](/pdf/id/python-net/revision-permissions/)
- [Ekstraksi Tanda Tangan](/pdf/id/python-net/signature-extraction/)
- [Manajemen Hak Penggunaan](/pdf/id/python-net/usage-rights-management/)

## Menyiapkan Pembantu Tanda Tangan Digital PDF

Sebelum menerapkan tanda tangan digital ke PDF, merupakan praktik terbaik untuk menyiapkan sekumpulan fungsi pembantu yang dapat digunakan kembali. Fungsi-fungsi ini mengenkapsulasi tugas-tugas umum—seperti menginisialisasi handler tanda tangan, menentukan penempatan visual tanda tangan, dan mengonfigurasi penandatanganan berbasis sertifikat—sehingga logika penandatanganan utama Anda tetap bersih, konsisten, dan mudah dipelihara.

### Apa yang Dicapai oleh Pengaturan Ini

Lapisan pembantu ini mempersiapkan semua yang dibutuhkan untuk alur kerja penandatanganan yang lancar:

- Menginisialisasi objek PdfFileSignature dan mengaitkannya dengan dokumen
- Mendefinisikan di mana tanda tangan akan muncul pada halaman
- Memuat dan menerapkan sertifikat penandatanganan
- Membuat objek tanda tangan PKCS#7 yang dapat digunakan kembali dengan metadata
- Menyesuaikan tampilan visual tanda tangan

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
