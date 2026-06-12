---
title: Ekstrak Informasi Tanda Tangan dari PDF di Python
linktitle: Ekstrak detail dari Tanda Tangan
type: docs
weight: 20
url: /id/python-net/extract-image-and-signature-information/
description: Pelajari cara mengekstrak gambar tanda tangan, sertifikat, dan detail tanda tangan digital dari file PDF menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak gambar tanda tangan dan detail sertifikat dari PDF menggunakan Python.
Abstract: Artikel ini menjelaskan cara mengekstrak gambar dan informasi tanda tangan digital dari dokumen PDF menggunakan Aspose.PDF for Python. Pelajari cara mengambil gambar tanda tangan, mengekstrak data sertifikat, memeriksa algoritma tanda tangan, dan mendeteksi tanda tangan yang telah dirusak dalam file PDF yang ditandatangani.
---

## Ekstrak Gambar dari Field Tanda Tangan

Aspose.PDF for Python via .NET memungkinkan Anda mengambil gambar visual yang disematkan dalam sebuah [BidangTandaTangan](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Ini berguna ketika Anda perlu menampilkan atau mengarsipkan tampilan tanda tangan tanpa merender PDF lengkap.

Contoh di bawah ini mengiterasi semua bidang formulir, menemukan masing-masing `SignatureField`, dan menyimpan gambarnya sebagai file JPEG:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## Baca Detail Algoritma Tanda Tangan

Gunakan `PdfFileSignature.get_signatures_info()` untuk membaca metadata kriptografi untuk setiap tanda tangan dalam dokumen — termasuk algoritma digest, tipe algoritma, standar kriptografi, dan nama tanda tangan:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## Ekstrak Sertifikat Digital dari Bidang Tanda Tangan

Gunakan [extract_certificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) metode pada sebuah `SignatureField` untuk mengambil sertifikat yang disematkan sebagai aliran byte dan menyimpannya ke disk untuk validasi eksternal:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## Ekstrak Sertifikat menggunakan Facade PdfFileSignature

`PdfFileSignature.try_extract_certificate()` menyediakan cara alternatif untuk mengambil sertifikat berdasarkan nama tanda tangan. Contoh berikut mengiterasi semua nama tanda tangan dan mencoba ekstraksi untuk masing-masing:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## Verifikasi Tanda Tangan Digital Eksternal

Untuk memastikan bahwa dokumen tidak dimodifikasi setelah penandatanganan, verifikasi setiap tanda tangan eksternal menggunakan `PdfFileSignature.verify_signature()`. Contoh di bawah ini menimbulkan pengecualian untuk setiap tanda tangan yang gagal verifikasi:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Deteksi Tanda Tangan yang Terkompromi

`SignaturesCompromiseDetector` memeriksa apakah tanda tangan digital apa pun dalam dokumen telah dibatalkan oleh perubahan selanjutnya. Gunakan ini dalam alur kerja hukum, keuangan, atau kepatuhan di mana integritas dokumen harus dijamin.

Contoh di bawah ini memeriksa tanda tangan yang terkompromi dan melaporkan nama-namanya bersama dengan cakupan tanda tangan keseluruhan dari dokumen:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## Topik Keamanan Terkait

- [Amankan dan tanda tangani file PDF di Python](/pdf/id/python-net/securing-and-signing/)
- [Menandatangani file PDF secara digital dengan Python](/pdf/id/python-net/digitally-sign-pdf-file/)
- [Tanda tangani dokumen PDF dari kartu pintar menggunakan Python](/pdf/id/python-net/sign-pdf-document-from-smart-card/)
- [Enkripsi dan dekripsi file PDF dengan Python](/pdf/id/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
