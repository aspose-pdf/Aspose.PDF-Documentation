---
title: Hapus Tabel dari Dokumen PDF yang Ada
linktitle: Hapus Tabel
description: Pelajari cara menghapus satu atau lebih tabel dari dokumen PDF yang ada menggunakan Python.
lastmod: "2026-06-12"
type: docs
weight: 50
url: /id/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hapus satu atau beberapa tabel dari file PDF dengan Python
Abstract: Artikel ini menjelaskan cara menghapus tabel dari dokumen PDF yang ada menggunakan Aspose.PDF for Python via .NET. Ini memperkenalkan `TableAbsorber` untuk menemukan tabel dan menunjukkan cara menghapus satu tabel atau menghapus semua tabel yang terdeteksi dari sebuah halaman.
---

## Hapus Tabel dari Dokumen PDF

Aspose.PDF for Python memungkinkan Anda menghapus tabel dari PDF. Ia membuka PDF yang ada, mendeteksi tabel pertama pada halaman pertama dengan `TableAbsorber`, menghapus tabel itu menggunakan `remove()`, dan menyimpan PDF yang diperbarui ke file baru.

Gunakan halaman ini ketika Anda perlu membersihkan PDF yang banyak berisi tabel, menghapus konten tabular yang sudah usang, atau menyederhanakan dokumen sebelum didistribusikan kembali.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Hapus semua Tabel dari dokumen PDF

Dengan perpustakaan kami, Anda dapat menghapus semua tabel dari halaman tertentu dalam PDF. Kode membuka PDF yang ada, mendeteksi semua tabel pada halaman kedua dengan TableAbsorber, iterasi melalui tabel yang terdeteksi, menghapus masing‑masing, dan kemudian menyimpan PDF yang telah dimodifikasi ke file baru. Ini berguna ketika Anda perlu menghapus banyak tabel dari sebuah halaman sambil membiarkan konten PDF lainnya tetap utuh.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Topik Tabel Terkait

- [Bekerja dengan tabel dalam PDF menggunakan Python](/pdf/id/python-net/working-with-tables/)
- [Tambahkan tabel ke PDF menggunakan Python](/pdf/id/python-net/adding-tables/)
- [Ekstrak tabel dari dokumen PDF](/pdf/id/python-net/extracting-table/)
- [Manipulasi tabel dalam PDF yang ada](/pdf/id/python-net/manipulating-tables/)