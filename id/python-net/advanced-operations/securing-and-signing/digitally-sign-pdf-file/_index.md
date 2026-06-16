---
title: Tambahkan tanda tangan digital atau tanda tangani PDF secara digital di Python
linktitle: Tanda tangani PDF secara digital
type: docs
weight: 10
url: /id/python-net/digitally-sign-pdf-file/
description: Pelajari cara menandatangani PDF secara digital, menambahkan stempel waktu, dan memvalidasi tanda tangan di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menandatangani PDF secara digital dengan Python
Abstract: Panduan ini menjelaskan cara menandatangani dokumen PDF secara digital menggunakan Aspose.PDF for Python via .NET. Panduan ini merinci proses penerapan tanda tangan digital standar dan lanjutan, menggunakan sertifikat (PFX dan PKCS#12), serta menyesuaikan tampilan dan perilaku tanda tangan. Dokumentasi ini menyertakan contoh kode yang menunjukkan cara menandatangani PDF yang sudah ada, menambahkan cap waktu, dan memverifikasi keabsahan tanda tangan. Hal ini memungkinkan pengembang memastikan keaslian, integritas, dan kepatuhan dokumen terhadap standar tanda tangan digital dalam Aplikasi Python mereka.
---

## Tandatangani PDF dengan tanda tangan digital

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

Sebuah **tanda tangan terpisah PKCS#7** menambahkan tanda tangan digital ke dokumen tanpa menyematkan konten ke dalam blok tanda tangan.

Gunakan contoh-contoh ini ketika Anda perlu menerapkan tanda tangan berbasis sertifikat pada file PDF, memverifikasi keabsahan tanda tangan, atau menambahkan cap waktu tepercaya ke dokumen yang ditandatangani.

Contoh berikut menandatangani dokumen PDF menggunakan tanda tangan digital PKCS#7 terpisah, menerapkan tanda tangan pada halaman pertama di area persegi panjang yang ditentukan.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Verifikasi semua tanda tangan digital dalam dokumen PDF**

1. Membuat sebuah instance PdfFileSignature yang memungkinkan Anda berinteraksi dengan tanda tangan dalam PDF.
1. Dapatkan daftar nama tanda tangan `get_signature_names(True)`.
1. Memeriksa tanda tangan pertama dalam daftar `verify_signature` untuk kepatuhan terhadap sertifikat yang ditentukan.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**Verifikasi tanda tangan dengan file sertifikat kunci publik**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**Verifikasi tanda tangan dengan sertifikat yang diekstrak dari file**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**Verifikasi tanda tangan dengan validasi rantai sertifikat diaktifkan**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## Tambahkan cap waktu ke tanda tangan digital

### Cara menandatangani PDF secara digital dengan cap waktu

Aspose.PDF for Python mendukung penandatanganan digital PDF dengan server timestamp atau layanan Web.

Untuk memenuhi persyaratan ini, [PengaturanTimestamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) kelas telah ditambahkan ke namespace Aspose.PDF. Silakan lihat cuplikan kode berikut yang memperoleh timestamp dan menambahkannya ke dokumen PDF:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## Menandatangani dokumen PDF menggunakan ECDSA

Menandatangani dokumen PDF menggunakan ECDSA (Elliptic Curve Digital Signature Algorithm) melibatkan penggunaan kriptografi kurva eliptik untuk menghasilkan tanda tangan digital.

Potongan kode di atas menggambarkan cara menerapkan tanda tangan digital terpisah PKCS#7 pada dokumen PDF menggunakan Aspose.PDF for Python. Dengan memuat dokumen, mengonfigurasi tampilan tanda tangan dan pengaturan keamanan, serta menyimpan hasilnya, contoh ini menunjukkan alur kerja lengkap dan dapat diandalkan untuk menandatangani file PDF secara digital.

Metode ini memastikan keaslian dan integritas dokumen dengan menyematkan tanda tangan yang aman dan dapat diverifikasi pada halaman pertama. Penggunaan SHA-256 sebagai algoritma digest memenuhi standar kriptografi modern, sementara kemampuan untuk mengontrol penempatan tanda tangan memberikan fleksibilitas untuk tanda persetujuan yang terlihat.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Verifikasi tanda tangan ECDSA dalam dokumen PDF**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Topik Keamanan Terkait

- [Amankan dan tanda tangani file PDF di Python](/pdf/id/python-net/securing-and-signing/)
- [Ekstrak informasi gambar dan tanda tangan dalam Python](/pdf/id/python-net/extract-image-and-signature-information/)
- [Tanda tangani dokumen PDF dari kartu pintar menggunakan Python](/pdf/id/python-net/sign-pdf-document-from-smart-card/)
- [Enkripsi dan dekripsi file PDF dengan Python](/pdf/id/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)