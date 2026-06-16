---
title: Sertifikasi PDF
linktitle: Sertifikasi PDF
type: docs
weight: 30
url: /id/python-net/pdf-certification/
description: Pelajari cara mensertifikasi dokumen PDF dalam Python menggunakan PdfFileSignature dan DocMDPSignature dengan berbagai izin modifikasi dokumen.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sertifikasi Dokumen PDF dengan Izin DocMDP dalam Python
Abstract: Artikel ini menjelaskan cara mensertifikasi dokumen PDF dengan Aspose.PDF for Python via .NET menggunakan antarmuka PdfFileSignature. Artikel ini menunjukkan cara membuat DocMDPSignature, menerapkan sertifikasi dengan izin pengisian formulir, dan mengunci dokumen dengan tingkat sertifikasi tanpa perubahan.
---

Aspose.PDF for Python via .NET memungkinkan Anda mensertifikasi dokumen PDF dengan menerapkan tanda tangan tingkat dokumen dengan [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). Sertifikasi berbeda dari tanda tangan persetujuan standar karena mendefinisikan perubahan apa, jika ada, yang diizinkan setelah dokumen disertifikasi.

Artikel ini menunjukkan dua alur kerja sertifikasi yang umum:

1. Sertifikasi PDF dan izinkan pengisian formulir setelah sertifikasi.
1. Sertifikasi PDF dan cegah perubahan lebih lanjut.

## Sertifikasi PDF untuk pengisian formulir

Gunakan pendekatan ini ketika dokumen harus tetap bersertifikat tetapi pengguna masih perlu mengisi formulir interaktif atau melanjutkan penandatanganan file. The `FILLING_IN_FORMS` tingkat izin mengizinkan perubahan terkendali tersebut sekaligus menjaga sertifikasi tetap valid.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Terapkan sertifikasi tingkat dokumen tanpa perubahan diizinkan

Gunakan mode ini ketika dokumen bersertifikat harus tetap tidak berubah setelah sertifikasi. The `NO_CHANGES` tingkat izin cocok untuk PDF yang telah selesai dimana modifikasi selanjutnya harus menginvalidasi status sertifikasi.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
