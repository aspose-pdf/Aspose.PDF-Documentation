---
title: Ekstrak Tautan PDF dalam Python
linktitle: Ekstrak Tautan
type: docs
weight: 30
url: /id/python-net/extract-links/
description: Pelajari cara mengekstrak anotasi tautan dan hyperlink dari dokumen PDF dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara mengekstrak Tautan dari PDF
Abstract: Panduan Aspose.PDF for Python via .NET tentang mengekstrak tautan menjelaskan cara secara programatik mengambil anotasi hyperlink dari dokumen PDF menggunakan Python. Dokumentasi mencakup contoh kode praktis dan menyoroti bagaimana fungsi ini dapat digunakan untuk tugas seperti audit tautan, analisis navigasi, atau membangun fitur dokumen interaktif. Baik Anda bekerja dengan PDF satu halaman atau memproses batch besar, panduan ini menawarkan pendekatan yang jelas dan efisien untuk ekstraksi hyperlink.
---

## Ekstrak Tautan dari File PDF

Contoh ini menunjukkan cara mengiterasi semua anotasi tautan pada halaman pertama PDF menggunakan Aspose.PDF for Python. Ia menyaring anotasi untuk mengidentifikasi yang bertipe LinkAnnotation, melakukan casting secara aman, dan kemudian mencetak indeks halaman serta posisi persegi panjangnya pada halaman.

Ini dapat digunakan untuk debugging, analitik, atau pembaruan otomatis pada anotasi tautan yang ada dalam PDF.

1. Muat dokumen PDF. Gunakan ap.Document(path_infile) untuk membuka file.
1. Akses anotasi dari halaman pertama. Gunakan document.pages[1].annotations untuk mengambil semua anotasi.
1. Saring hanya tipe LinkAnnotation. Periksa annotation_type setiap anotasi.
1. Lakukan casting dan proses LinkAnnotations. Gunakan is_assignable() dan cast() untuk memastikan akses yang aman ke properti LinkAnnotation.
1. Cetak detail anotasi. Keluarkan indeks halaman dan persegi panjang (lokasi) dari setiap tautan.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## Ekstrak HyperLink dari File PDF

Kode ini menunjukkan cara mengekstrak semua objek LinkAnnotation dari halaman pertama dokumen PDF menggunakan Aspose.PDF for Python, dan kemudian mengidentifikasi yang mengandung GoToURIAction. Untuk setiap tautan semacam itu, ia mencetak indeks halaman dan URI target.

Ini berguna untuk tugas seperti:

- Mengaudit tautan eksternal dalam PDF
- Mengekstrak URL dokumentasi atau dukungan
- Mendeteksi hyperlink yang rusak atau kedaluwarsa

1. Muat dokumen PDF. Buka file menggunakan ap.Document.
1. Dapatkan semua anotasi tautan dari halaman pertama. Saring anotasi untuk hanya menyertakan yang berjenis AnnotationType.LINK.
1. Periksa tipe dan lakukan casting ke LinkAnnotation. Pastikan setiap anotasi memang merupakan LinkAnnotation sebelum mengakses propertinya.
1. Periksa tipe aksi tautan. Saring tautan yang menggunakan GoToURIAction (yaitu, tautan ke URL web).
1. Ekstrak dan cetak URI serta indeks halaman. Gunakan .uri untuk mendapatkan tautan eksternal dan .page_index untuk konteks.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## Topik Tautan Terkait

- [Bekerja dengan tautan PDF di Python](/pdf/id/python-net/links/)
- [Buat tautan PDF dalam Python](/pdf/id/python-net/create-links/)
- [Perbarui tautan dalam PDF menggunakan Python](/pdf/id/python-net/update-links/)