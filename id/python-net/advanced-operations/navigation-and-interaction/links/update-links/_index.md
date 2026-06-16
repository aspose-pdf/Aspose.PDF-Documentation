---
title: Perbarui Tautan PDF di Python
linktitle: Perbarui Tautan
type: docs
weight: 20
url: /id/python-net/update-links/
description: Pelajari cara memperbarui tampilan dan tujuan tautan PDF di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cara memperbarui Tautan di PDF
Abstract: Panduan Aspose.PDF for Python via .NET tentang memperbarui tautan memandu pengembang melalui proses memodifikasi perilaku hyperlink dalam dokumen PDF menggunakan Python. Panduan ini menjelaskan cara mengubah tujuan tautan agar mengarah ke halaman tertentu, situs web eksternal, atau bahkan file PDF lain. Dokumentasi juga mencakup cara menyesuaikan tampilan anotasi tautan, termasuk warna teks, dan menyediakan contoh kode praktis untuk setiap skenario. Baik Anda memperbaiki URL yang kedaluwarsa maupun meningkatkan navigasi, sumber daya ini menawarkan pendekatan yang jelas dan efisien untuk mengelola tautan secara programatik.
---

## Perbarui Warna Teks LinkAnnotation

Contoh ini menunjukkan cara mendeteksi semua anotasi tautan pada halaman pertama PDF menggunakan Aspose.PDF for Python, kemudian menyorot teks di dekat setiap tautan dengan mengubah warna fontnya menjadi merah. Ini menggunakan TextFragmentAbsorber dengan area yang sedikit diperluas di sekitar setiap persegi panjang tautan untuk menemukan dan memodifikasi teks di sekitarnya.

Ini dapat digunakan untuk:

- Menandai tautan secara visual dalam dokumen
- Meningkatkan aksesibilitas dengan menekankan konten yang terhubung
- Pra-pemrosesan file PDF sebelum peninjauan atau ekspor

Untuk setiap anotasi tautan ini, skrip mengambil batas persegi panjangnya dan sedikit memperluas wilayah tersebut untuk menyertakan teks di sekitarnya, memungkinkan identifikasi visual yang lebih luas. Kemudian skrip menerapkan TextFragmentAbsorber pada area yang diperluas ini untuk mengekstrak semua fragmen teks yang berada di dalamnya. Fragmen yang ditangkap tersebut diubah dengan mengubah warna font menjadi merah, secara efektif menandai teks di sekitarnya untuk penekanan dan peninjauan. Setelah semua pembaruan ini diterapkan, dokumen yang dimodifikasi disimpan ke jalur output, mempertahankan anotasi yang disorot serta teks yang terkait.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## Perbarui Bingkai

Skrip ini berfokus pada halaman pertama dokumen dan menyaring semua anotasi, memilih hanya yang berjenis LINK—biasanya ini mewakili elemen interaktif, seperti tautan hiperteks atau pemicu navigasi. Untuk setiap anotasi tautan ini, kode mengubahnya menjadi tipe LinkAnnotation dan memperbarui properti warna mereka menjadi merah, menyorotnya secara visual agar menonjol dari konten lainnya. Setelah semua anotasi tautan dimodifikasi, dokumen yang diperbarui disimpan ke lokasi output yang telah ditentukan, menjaga gaya baru tersebut.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Perbarui Tujuan Web

Setelah jalur-jalur berada di tempatnya, dokumen asli dimuat menggunakan perpustakaan Aspose.PDF, membuat isinya dapat diakses untuk dimodifikasi. Skrip kemudian memfokuskan pada halaman pertama dokumen, menyaring semua anotasi dan memilih hanya yang berjenis tautan, biasanya mewakili area yang dapat diklik atau hyperlink. Untuk menghindari kesalahan tipe dan memastikan penanganan yang aman, setiap anotasi diperiksa dengan is_assignable dan kemudian di‑cast ke tipe LinkAnnotation yang sesuai. Jika tautan terkait dengan GoToURIAction, artinya menunjuk ke alamat web, skrip memperbarui URI tersebut untuk mengarahkan pengguna ke "https://www.aspose.com". Akhirnya, setelah semua perubahan yang diinginkan diterapkan, dokumen yang dimodifikasi disimpan ke jalur output yang ditentukan.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## Topik Tautan Terkait

- [Bekerja dengan tautan PDF di Python](/pdf/id/python-net/links/)
- [Buat tautan PDF dalam Python](/pdf/id/python-net/create-links/)
- [Ekstrak tautan PDF di Python](/pdf/id/python-net/extract-links/)