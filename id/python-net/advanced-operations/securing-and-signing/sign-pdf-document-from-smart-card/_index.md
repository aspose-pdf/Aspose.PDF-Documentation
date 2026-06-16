---
title: Menandatangani Dokumen PDF dari Kartu Pintar dengan Python
linktitle: Penandatanganan PDF dengan Kartu Pintar
type: docs
weight: 30
url: /id/python-net/sign-pdf-document-from-smart-card/
description: Pelajari cara menandatangani dokumen PDF dengan kartu pintar dan sertifikat eksternal menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Menandatangani dokumen PDF dari Kartu Pintar dengan Python
Abstract: Panduan ini menjelaskan cara menandatangani dokumen PDF secara digital menggunakan kartu pintar dengan Aspose.PDF for Python via .NET. Panduan ini menunjukkan cara mengakses sertifikat yang disimpan pada perangkat keras (seperti token USB atau kartu pintar) melalui Windows Certificate Store dan menerapkannya untuk menandatangani file PDF. Dokumentasi mencakup contoh kode yang menunjukkan cara menemukan sertifikat yang sesuai, mengonfigurasi properti tanda tangan, dan menyisipkan tanda tangan digital ke dalam PDF. Hal ini memungkinkan penandatanganan yang aman dan berbasis perangkat keras sesuai dengan standar tanda tangan digital, cocok untuk alur kerja perusahaan dan hukum yang memerlukan tingkat kepercayaan tinggi.
---

Aspose.PDF menyediakan kemampuan kuat untuk mengintegrasikan komponen tanda tangan visual dan kriptografis, memastikan keaslian serta tampilan profesional dalam dokumen PDF yang ditandatangani secara digital.

Gunakan alur kerja ini ketika proses penandatanganan Anda bergantung pada sertifikat yang disimpan dalam perangkat berbasis perangkat keras seperti kartu pintar, token USB, atau penyimpanan sertifikat yang dikelola.

## Menandatangani dengan Kartu Pintar Menggunakan Bidang Tanda Tangan

Contoh ini menunjukkan cara menandatangani dokumen PDF secara digital menggunakan sertifikat eksternal dengan Aspose.PDF for Python dan menerapkan gambar tampilan tanda tangan khusus:

1. Membuka dokumen PDF.
1. Membuat objek PdfFileSignature dan mengaitkannya ke dokumen.
1. Mengambil sertifikat digital lokal menggunakan metode khusus `get_local_certificate()`.
1. Menyiapkan ExternalSignature berdasarkan sertifikat yang dipilih.
1. Menerapkan gambar tampilan tanda tangan khusus (mis., logo perusahaan atau tanda tangan tulisan tangan).
1. Menandatangani secara digital halaman pertama dokumen dengan metadata yang ditentukan (alasan, kontak, lokasi).
1. Menyimpan dokumen yang ditandatangani ke file output baru.

Metode ini ideal untuk kasus di mana tanda tangan harus diterapkan secara programatis menggunakan sertifikat eksternal—seperti token perangkat keras, penyimpanan sertifikat, atau penyedia tepercaya—dan ditampilkan dengan tata letak visual yang dipersonalisasi.

Berikut adalah cuplikan kode untuk menandatangani dokumen PDF dari kartu pintar:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## Verifikasi Tanda Tangan Digital

Potongan kode ini menunjukkan cara memverifikasi tanda tangan digital dalam dokumen PDF menggunakan Aspose.PDF for Python:

1. Membuka file PDF.
1. Membuat 'PdfFileSignature object' dan mengaitkannya ke dokumen.
1. Mengambil daftar semua nama bidang tanda tangan menggunakan 'get_signature_names()'.
1. Melakukan iterasi melalui setiap tanda tangan dan memverifikasi keabsahannya dengan 'verify_signature()'.
1. Menaikkan pengecualian jika ada tanda tangan yang gagal verifikasi.

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

## Tanda tangani dengan Sertifikat Eksternal

Potongan kode ini menunjukkan cara menambahkan dan menandatangani bidang tanda tangan digital dalam dokumen PDF menggunakan Aspose.PDF for Python dengan sertifikat eksternal:

1. Membuka file PDF sebagai aliran biner.
1. Membuat SignatureField dan menempatkannya pada halaman pertama dokumen pada posisi yang ditentukan.
1. Mengambil sertifikat digital lokal menggunakan metode khusus `get_local_certificate()`.
1. Menyiapkan ExternalSignature dengan metadata seperti otoritas, alasan, dan informasi kontak.
1. Menetapkan nama field unik ke bidang tanda tangan (partial_name = \"sig1\").
1. Menambahkan bidang tanda tangan ke bidang formulir PDF.
1. Menandatangani bidang dengan sertifikat eksternal.
1. Menyimpan dokumen yang ditandatangani ke file output.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## Topik Keamanan Terkait

- [Amankan dan tanda tangani file PDF di Python](/pdf/id/python-net/securing-and-signing/)
- [Menandatangani file PDF secara digital dengan Python](/pdf/id/python-net/digitally-sign-pdf-file/)
- [Ekstrak informasi tanda tangan dari PDF dengan Python](/pdf/id/python-net/extract-image-and-signature-information/)
- [Enkripsi dan dekripsi file PDF dengan Python](/pdf/id/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

