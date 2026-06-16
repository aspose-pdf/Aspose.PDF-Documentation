---
title: Bekerja dengan Metadata File PDF di Python
linktitle: Metadata File PDF
type: docs
weight: 200
url: /id/python-net/pdf-file-metadata/
description: Pelajari cara mengekstrak, memperbarui, dan mengelola metadata file PDF serta properti XMP di Python menggunakan Aspose.PDF.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dapatkan dan atur informasi dokumen PDF serta metadata XMP di Python
Abstract: Artikel ini menjelaskan cara bekerja dengan metadata PDF di Aspose.PDF for Python via .NET. Pelajari cara membaca informasi dokumen seperti penulis, judul, dan kata kunci, memperbarui properti file, mengatur bidang metadata XMP, dan mendaftarkan prefiks metadata khusus untuk file PDF dalam Python.
---

Gunakan panduan ini ketika Anda perlu memeriksa properti dokumen, memperbarui informasi file PDF untuk pencarian atau pengkatalogan, atau mengelola metadata XMP secara programatis di Python.

## Dapatkan Informasi File PDF

Potongan kode ini menunjukkan cara mengekstrak metadata dari dokumen PDF menggunakan Aspose.PDF for Python via .NET. Dengan mengakses properti info dari objek Document, ia mengambil informasi kunci seperti penulis, tanggal pembuatan, kata kunci, tanggal modifikasi, subjek, dan judul. Fungsionalitas ini penting bagi aplikasi yang memerlukan katalogisasi dokumen, optimalisasi pencarian, atau validasi properti dokumen.

1. Buka file PDF menggunakan kelas Document
1. Ambil metadata dokumen melalui properti info
1. Tampilkan Informasi Metadata. Cetak bidang metadata yang diinginkan

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def get_pdf_file_information(infile):
    # Open PDF document
    document = ap.Document(infile)

    # Get document information
    doc_info = document.info

    # Display document information
    print(f"Author: {doc_info.author}")
    print(f"Creation Date: {doc_info.creation_date}")
    print(f"Keywords: {doc_info.keywords}")
    print(f"Modify Date: {doc_info.mod_date}")
    print(f"Subject: {doc_info.subject}")
    print(f"Title: {doc_info.title}")
```

## Atur Informasi File PDF

Aspose.PDF for Python via .NET memungkinkan Anda mengatur informasi spesifik file untuk PDF, informasi seperti penulis, tanggal pembuatan, subjek, dan judul. Untuk mengatur informasi ini:

1. Buka file PDF menggunakan kelas Document.
1. Buat sebuah [DocumentInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/documentinfo/) objek dan atur properti metadata yang diinginkan.
1. Simpan perubahan ke file PDF baru menggunakan metode save.

Cuplikan kode berikut menunjukkan cara mengatur informasi file PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_file_information(infile, outfile):

    # Open PDF document
    document = ap.Document(infile)

    # Specify document information
    doc_info = ap.DocumentInfo(document)
    doc_info.author = "Aspose"
    doc_info.creation_date = datetime.datetime.now()
    doc_info.keywords = "Aspose.Pdf, DOM, API"
    doc_info.mod_date = datetime.datetime.now()
    doc_info.subject = "PDF Information"
    doc_info.title = "Setting PDF Document Information"
    doc_info.producer = "Custom producer"
    doc_info.creator = "Custom creator"

    # Save PDF document
    document.save(outfile)
```

## Set Metadata XMP dalam File PDF

Potongan kode ini menunjukkan cara mengatur atau memperbarui metadata XMP secara programatis dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Dengan memodifikasi properti seperti xmp:CreateDate, xmp:Nickname, dan bidang yang didefinisikan secara khusus, Anda dapat menyematkan metadata standar ke dalam file PDF Anda. Pendekatan ini sangat berguna untuk meningkatkan organisasi dokumen, mempermudah pencarian, dan menyematkan informasi penting langsung ke dalam file.

Aspose.PDF memungkinkan Anda mengatur metadata dalam file PDF. Untuk mengatur metadata:

1. Buka file PDF menggunakan [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) kelas.
1. Modifikasi metadata XMP dengan menetapkan nilai ke kunci tertentu.
1. Simpan Dokumen PDF yang Diperbarui.

Potongan kode berikut menunjukkan cara mengatur metadata dalam file PDF.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_xmp_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Set XMP metadata properties
    document.metadata.add("xmp:CreateDate", datetime.datetime.now().isoformat())
    document.metadata.add("xmp:Nickname", "Nickname")
    document.metadata.add("xmp:CustomProperty", "Custom Value")

    # Save the updated PDF document
    document.save(outfile)
```

## Masukkan Metadata dengan Prefiks

Beberapa pengembang perlu membuat ruang nama metadata baru dengan prefiks. Potongan kode berikut menunjukkan cara menyisipkan metadata dengan prefiks.

```python
import aspose.pdf as ap
import datetime
import sys
from os import path

def set_prefix_metadata(infile, outfile):
    # Open PDF document
    document = ap.Document(infile)

    # Register a namespace URI for the 'xmp' prefix
    document.metadata.register_namespace_uri("xmp", "http://ns.adobe.com/xap/1.0/")

    # Set the metadata property using the registered prefix
    document.metadata.add(
        "xmp:ModifyDate", datetime.datetime.now().isoformat()
    )  # ISO 8601 format

    # Save the updated PDF document
    document.save(outfile)
```

## Topik Terkait

- [Operasi PDF lanjutan di Python](/pdf/id/python-net/advanced-operations/)
- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Bekerja dengan lampiran PDF di Python](/pdf/id/python-net/attachments/)
- [Bandingkan dokumen PDF dengan Python](/pdf/id/python-net/compare-pdf-documents/)
