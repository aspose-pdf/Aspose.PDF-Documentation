---
title: Ekstrak Tabel dari PDF dengan Python
linktitle: Ekstrak Tabel
type: docs
weight: 20
url: /id/python-net/extracting-table/
description: Pelajari cara mengekstrak data tabel dari dokumen PDF yang ada menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ekstrak data tabel dari file PDF dengan Python
Abstract: Artikel ini menjelaskan cara mengekstrak tabel dari dokumen PDF menggunakan Aspose.PDF for Python via .NET. Artikel ini menunjukkan cara menggunakan `TableAbsorber` untuk mendeteksi tabel per halaman, mengiterasi baris dan sel, serta mengambil teks sel untuk analisis dan pemrosesan data lanjutan.
---

## Ekstrak Tabel dari PDF

Mengekstrak tabel dari PDF berguna untuk pelaporan, migrasi data, dan alur kerja analitik. Dengan Aspose.PDF for Python via .NET, Anda dapat mendeteksi dan membaca konten tabel dari dokumen PDF yang ada secara efisien.

Potongan kode ini membuka file PDF yang sudah ada, memindai setiap halaman untuk tabel, dan mengekstrak konten teks sel. Ini menggunakan `TableAbsorber` untuk mendeteksi tabel dan kemudian mengiterasi baris serta sel untuk mencetak teks yang diekstrak.

1. Memuat PDF ke dalam objek ap.Document.
1. Loop melalui halaman.
1. Membuat objek TableAbsorber.
1. Iterasi melalui tabel.
1. Iterasi melalui baris dan sel.
1. Ekstrak dan cetak teks dari sel.

Contoh ini membaca PDF, menemukan semua tabel, dan mencetak isi selnya baris per baris.

```python
import aspose.pdf as ap
from os import path
import sys

def extract(infile: str) -> None:
    """Extract and print all tables from a PDF file."""
    document = ap.Document(infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row:")
                row_txt = ""
                for cell in row.cell_list:
                    cell_txt = ""
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        for seg in fragment.segments:
                            cell_txt += seg.text
                    row_txt += " | "
                    row_txt += cell_txt
                print(row_txt)
```

## Topik Tabel Terkait

- [Bekerja dengan tabel dalam PDF menggunakan Python](/pdf/id/python-net/working-with-tables/)
- [Tambahkan tabel ke PDF menggunakan Python](/pdf/id/python-net/adding-tables/)
- [Mengintegrasikan tabel PDF dengan sumber data](/pdf/id/python-net/integrate-table/)
- [Hapus tabel dari PDF yang ada](/pdf/id/python-net/removing-tables/)