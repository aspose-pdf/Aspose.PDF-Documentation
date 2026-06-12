---
title: Gabungkan File PDF di Python
linktitle: Gabungkan file PDF
type: docs
weight: 50
url: /id/python-net/merge-pdf-documents/
description: Pelajari cara menggabungkan beberapa file PDF menjadi satu dokumen dalam Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gabungkan halaman PDF menggunakan Python
Abstract: Artikel ini membahas kebutuhan umum untuk menggabungkan beberapa file PDF menjadi satu dokumen, proses yang berharga untuk mengatur dan mengoptimalkan penyimpanan serta berbagi konten PDF. Artikel ini mengeksplorasi penggunaan Aspose.PDF for Python via .NET untuk secara efisien menggabungkan file PDF, dengan mengakui bahwa menggabungkan PDF di Python dapat menjadi tantangan tanpa perpustakaan pihak ketiga. Artikel ini menyediakan panduan langkah demi langkah untuk mengkonkatenasi file PDF - membuat dokumen baru, menggabungkan file, dan menyimpan dokumen yang telah digabungkan. Sebuah cuplikan kode menunjukkan implementasi menggunakan Aspose.PDF, menyoroti kemampuan perpustakaan untuk menyederhanakan proses penggabungan. Selain itu, diperkenalkan Aspose.PDF Merger, sebuah alat daring untuk menggabungkan PDF, memungkinkan pengguna menjelajahi fungsionalitasnya dalam lingkungan berbasis web.
---

## Gabungkan atau satukan beberapa PDF menjadi satu PDF dalam Python

Menggabungkan file PDF adalah kueri yang sangat populer di antara pengguna. Ini dapat berguna ketika Anda memiliki beberapa file PDF yang ingin Anda bagikan atau simpan bersama sebagai satu dokumen.

Menggabungkan file PDF dapat membantu Anda mengatur dokumen, memberi ruang penyimpanan di PC Anda, dan berbagi beberapa file PDF dengan orang lain dengan menggabungkannya menjadi satu dokumen.

Menggabungkan PDF dalam Python via .NET bukanlah tugas yang mudah tanpa menggunakan pustaka pihak ketiga.
Artikel ini menunjukkan cara menggabungkan beberapa file PDF menjadi satu dokumen PDF menggunakan Aspose.PDF for Python via .NET. 

## Gabungkan File PDF menggunakan Python dan DOM

Untuk menggabungkan dua file PDF:

1. Buat Dokumen Baru.
1. Gabungkan File PDF
1. Simpan Dokumen Gabungan

Menggabungkan beberapa dokumen PDF menjadi satu file:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Tambahkan Rentang Halaman dari Satu PDF ke PDF Lain

Salin dan tambahkan rentang halaman tertentu dari dokumen PDF sumber ke dokumen PDF tujuan menggunakan Aspose.PDF untuk Python.

1. Buka file PDF menggunakan kelas Document.
1. Periksa apakah dokumen sumber memiliki halaman.
1. Validasi rentang halaman.
1. Lewati operasi jika halaman awal lebih besar dari halaman akhir.
1. Iterasikan rentang halaman.
1. Tambahkan halaman ke dokumen tujuan.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## Gabungkan Beberapa Dokumen PDF Menjadi Satu

Potongan kode ini menjelaskan cara menggabungkan beberapa file PDF menjadi satu dokumen:

1. Buat dokumen output kosong.
1. Iterasi melalui file input.
1. Muat setiap dokumen sumber.
1. Tentukan rentang halaman.
1. Tambahkan halaman ke dokumen output.
1. Ulangi untuk semua dokumen.
1. Simpan PDF yang digabungkan.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## Gabungkan Rentang Halaman yang Dipilih dari Beberapa PDF

1. Muat dokumen PDF sumber.
1. Buat dokumen keluaran.
1. Tentukan rentang halaman untuk setiap dokumen.
1. Tambahkan halaman dari dokumen pertama.
1. Tambahkan halaman dari dokumen kedua.
1. Gabungkan halaman dalam urutan yang diinginkan.
1. Simpan PDF yang digabungkan.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## Masukkan Satu PDF ke PDF Lain pada Posisi Tertentu

1. Muat basis dan sisipkan dokumen.
1. Buat dokumen keluaran.
1. Tentukan total halaman dalam dokumen dasar.
1. Validasi indeks penyisipan.
1. Tambahkan halaman sebelum titik sisipan.
1. Tambahkan semua halaman dari dokumen sisipan.
1. Tambahkan halaman yang tersisa dari dokumen dasar.
1. Simpan PDF yang dihasilkan.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## Gabungkan PDF dengan Halaman Bergantian

Contoh ini menunjukkan cara menggabungkan dua dokumen PDF dengan cara mengatur halaman mereka secara bergantian menggunakan Aspose.PDF for Python.

1. Muat dokumen PDF input.
1. Buat dokumen keluaran.
1. Dapatkan jumlah halaman di setiap dokumen.
1. Hitung jumlah halaman maksimum.
1. Iterasi melalui nomor halaman.
1. Tambahkan halaman secara bergantian.
1. Tangani jumlah halaman yang tidak sama.
1. Simpan PDF yang digabungkan.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## Gabungkan PDF dengan Pemisah Bagian dan Penanda Buku

Gabungkan beberapa dokumen PDF menjadi satu file dengan bagian terstruktur dan bookmark navigasi menggunakan Aspose.PDF for Python.

1. Buat dokumen keluaran.
1. Iterasi melalui file input.
1. Muat dokumen sumber.
1. Tambahkan halaman pemisah.
1. Buat penanda bagian.
1. Tambahkan halaman dokumen sumber.
1. Lacak halaman konten pertama.
1. Tambahkan bookmark konten bersarang (opsional).
1. Ulangi untuk semua dokumen.
1. Simpan PDF yang digabungkan.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## Contoh Langsung

[Penggabung Aspose.PDF](https://products.aspose.app/pdf/merger) adalah aplikasi web gratis daring yang memungkinkan Anda menyelidiki cara kerja fungsi penggabungan presentasi.

[![Penggabung Aspose.PDF](merger.png)](https://products.aspose.app/pdf/merger)

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Membagi file PDF dengan Python](/pdf/id/python-net/split-document/)
- [Optimalkan file PDF dalam Python](/pdf/id/python-net/optimize-pdf/)
- [Manipulasi dokumen PDF dalam Python](/pdf/id/python-net/manipulate-pdf-document/)

