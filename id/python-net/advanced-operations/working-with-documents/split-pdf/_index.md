---
title: Membagi File PDF dengan Python
linktitle: Membagi file PDF
type: docs
weight: 60
url: /id/python-net/split-pdf-document/
description: Pelajari cara membagi file PDF di Python menjadi halaman individual, bagian yang sama, grup berukuran tetap, rentang halaman khusus, serta halaman ganjil atau genap.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Bagi PDF menjadi halaman dan rentang halaman menggunakan Python
Abstract: Artikel ini menunjukkan cara memisahkan file PDF dengan Aspose.PDF for Python via .NET. Ini mencakup pemisahan PDF menjadi halaman individual, dua bagian yang sama, grup halaman berukuran tetap, rentang halaman khusus, grup halaman bernama, nama file yang stabil, serta file halaman ganjil atau genap.
---

Halaman ini menunjukkan cara **memisahkan file PDF di Python** menggunakan Aspose.PDF for Python via .NET.

Gunakan contoh-contoh ini saat Anda perlu memecah PDF besar menjadi file satu halaman, bagian-bagian yang sama, grup berukuran tetap, rentang halaman khusus, atau set halaman ganjil dan genap untuk distribusi, peninjauan, atau pemrosesan lanjutan.

## Contoh Membagi PDF Online

[Pemecah Aspose.PDF](https://products.aspose.app/pdf/splitter) adalah aplikasi web daring yang memungkinkan Anda menguji fungsi pemisahan PDF.

[![Aspose Pisah PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Untuk membagi halaman PDF menjadi file PDF satu halaman dalam Python, ikuti langkah-langkah berikut:

1. Lakukan perulangan pada halaman dokumen PDF melalui [Dokumen](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objek [Koleksi Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) koleksi
1. Untuk setiap iterasi, buat objek Document baru dan tambahkan yang individual [Halaman](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) objek ke dalam dokumen kosong
1. Simpan PDF baru menggunakan [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) metode

## Membagi PDF menjadi Beberapa File dalam Python

Potongan kode Python berikut menunjukkan cara memisahkan halaman PDF menjadi file PDF individu.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Bagi PDF menjadi Dua Bagian yang Setara

1. Muat dokumen PDF.
1. Tentukan total jumlah halaman.
1. Hitung titik tengah.
1. Buat dokumen output pertama.
1. Hapus halaman paruh kedua dari dokumen pertama.
1. Simpan bagian pertama.
1. Buat dokumen output kedua.
1. Hapus halaman setengah pertama dari dokumen kedua.
1. Simpan bagian kedua.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## Membagi PDF menjadi Beberapa File Setiap N Halaman

Pisahkan dokumen PDF menjadi beberapa file kecil berdasarkan jumlah halaman tetap menggunakan Aspose.PDF for Python.

1. Muat dokumen PDF.
1. Tentukan total jumlah halaman.
1. Tentukan halaman per bagian.
1. Iterasi melalui dokumen dalam potongan.
1. Hitung rentang halaman untuk setiap bagian.
1. Buat dokumen baru untuk setiap bagian.
1. Salin halaman ke dalam dokumen baru.
1. Simpan dokumen yang dipisah.
1. Ulangi hingga semua halaman diproses.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## Membagi PDF berdasarkan Rentang Halaman Kustom

Pisahkan dokumen PDF menjadi beberapa file berdasarkan rentang halaman yang ditentukan secara khusus menggunakan Aspose.PDF for Python.

1. Muat dokumen PDF.
1. Tentukan total jumlah halaman.
1. Buat daftar tuple yang mewakili rentang (start_page, end_page).
1. Iterasi melalui rentang yang ditentukan.
1. Validasi halaman awal.
1. Sesuaikan halaman akhir.
1. Validasi rentang efektif.
1. Buat dokumen baru untuk setiap rentang.
1. Salin halaman ke dalam dokumen baru.
1. Simpan setiap dokumen yang dipisah.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## Membagi PDF menjadi Halaman Pertama dan Halaman yang Tersisa

Pisahkan halaman pertama dari dokumen PDF dari sisa halaman menggunakan Aspose.PDF for Python.

1. Muat dokumen PDF.
1. Tentukan total jumlah halaman.
1. Periksa apakah dokumen kosong.
1. Buat dokumen untuk halaman pertama.
1. Tambahkan halaman pertama.
1. Simpan dokumen halaman pertama.
1. Periksa apakah ada halaman tambahan.
1. Buat dokumen untuk halaman yang tersisa.
1. Salin halaman yang tersisa.
1. Simpan dokumen halaman yang tersisa.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Pisahkan PDF menjadi Halaman Terakhir dan Halaman Sebelumnya

Ekstrak halaman terakhir dari dokumen PDF dan pisahkan dari halaman‑halaman yang tersisa menggunakan Aspose.PDF for Python.

1. Muat dokumen PDF.
1. Tentukan total jumlah halaman.
1. Periksa apakah dokumen kosong.
1. Buat dokumen untuk halaman terakhir.
1. Tambahkan halaman terakhir.
1. Simpan dokumen halaman terakhir.
1. Periksa dokumen satu halaman.
1. Hapus halaman terakhir dari dokumen asli.
1. Simpan halaman yang tersisa.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Pisahkan PDF menjadi Tiga Bagian

Pisahkan dokumen PDF menjadi tiga bagian terpisah menggunakan Aspose.PDF untuk Python.

1. Muat dokumen PDF.
1. Tentukan total jumlah halaman.
1. Periksa apakah dokumen kosong.
1. Hitung ukuran bagian.
1. Iterasi melalui tiga bagian.
1. Tentukan rentang halaman untuk setiap bagian.
1. Validasi rentang halaman.
1. Buat dokumen baru untuk setiap bagian.
1. Salin halaman ke dalam dokumen bagian.
1. Simpan setiap bagian.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

## Pemecah Halaman PDF Kustom

Membagi dokumen PDF menjadi beberapa file berdasarkan kelompok halaman yang didefinisikan secara khusus menggunakan Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```

## Pisahkan PDF menjadi Halaman Individual dengan Nama File Stabil

Pisahkan dokumen PDF menjadi halaman-halaman terpisah dan simpan dengan nama file yang stabil menggunakan Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```

## Pisahkan PDF menjadi Halaman Ganjil dan Genap

Pisahkan dokumen PDF menjadi dua file terpisah yang masing-masing berisi halaman ganjil dan genap menggunakan Aspose.PDF for Python.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Topik Dokumen Terkait

- [Bekerja dengan dokumen PDF di Python](/pdf/id/python-net/working-with-documents/)
- [Gabungkan file PDF di Python](/pdf/id/python-net/merge-pdf-documents/)
- [Optimalkan file PDF di Python](/pdf/id/python-net/optimize-pdf/)
- [Memanipulasi dokumen PDF dalam Python](/pdf/id/python-net/manipulate-pdf-document/)
