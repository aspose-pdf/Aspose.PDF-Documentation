---
title: Manipulasi Tabel dalam Dokumen PDF yang Ada
linktitle: Manipulasi Tabel
type: docs
weight: 40
url: /id/python-net/manipulating-tables/
description: Pelajari cara memeriksa dan memodifikasi tabel dalam dokumen PDF yang ada menggunakan Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Periksa dan modifikasi tabel PDF yang ada dengan Python
Abstract: Artikel ini menjelaskan cara memanipulasi tabel yang sudah ada dalam dokumen PDF menggunakan Aspose.PDF for Python via .NET. Pelajari cara menemukan tabel dengan TableAbsorber, mengakses baris dan sel tertentu, memperbarui konten teks tabel, dan menyimpan PDF yang telah dimodifikasi menggunakan Python.
---

## Manipulasi Tabel dalam PDF yang Ada

Aspose.PDF for Python via .NET memungkinkan Anda memperbarui tabel yang sudah ada dalam dokumen PDF. Anda dapat menggunakan [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) kelas untuk menemukan tabel pada halaman, mengakses baris dan sel, mengubah konten teks, dan menyimpan file yang telah diperbarui.

Gunakan halaman ini ketika Anda perlu memperbarui konten tabel yang ada dalam PDF tanpa membuat ulang tata letak dokumen secara keseluruhan.

## Temukan dan Ganti Teks dalam Sel Tabel PDF

Contoh ini menemukan tabel pertama pada halaman 1, mengakses sel pertama, mengganti teksnya, dan menyimpan PDF output.

1. Buka PDF input.
1. Buat TableAbsorber dan kunjungi halaman 1.
1. Pastikan setidaknya satu tabel terdeteksi.
1. Akses sel pertama pada baris pertama dari tabel pertama.
1. Pastikan sel berisi fragmen teks, kemudian perbarui fragmen pertama.
1. Simpan PDF yang telah dimodifikasi.

```python
import aspose.pdf as ap

def replace_cell_text(infile: str, outfile: str) -> None:
    """Replace text in the first cell of the first detected table."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    first_cell = absorber.table_list[0].row_list[0].cell_list[0]
    if len(first_cell.text_fragments) == 0:
        raise ValueError("The target cell has no text fragments.")

    # Change text of the first text fragment in the cell
    first_cell.text_fragments[0].text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Ganti Tabel yang Ada dengan Tabel Baru

Anda juga dapat mengganti tabel yang terdeteksi dengan yang baru dibuat. Pendekatan ini berguna ketika struktur dan konten keduanya harus diubah.

Kode di bawah ini membuka PDF, menemukan tabel pertama pada halaman 1, membuat tabel pengganti, menukar tabel lama dengan yang baru, dan menyimpan hasilnya.

```python
import aspose.pdf as ap

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    if len(absorber.table_list) == 0:
        raise ValueError("No tables were found on page 1.")

    # Get first table on the page
    old_table = absorber.table_list[0]

    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1.0)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")
    row = new_table.rows.add()
    row.cells.add("Col 12")
    row.cells.add("Col 22")
    row.cells.add("Col 32")

    # Replace the old table with the new one
    absorber.replace(document.pages[1], old_table, new_table)

    # Save PDF document
    document.save(outfile)
```

## Topik Tabel Terkait

- [Bekerja dengan tabel di PDF menggunakan Python](/pdf/id/python-net/working-with-tables/)
- [Tambahkan tabel ke PDF menggunakan Python](/pdf/id/python-net/adding-tables/)
- [Ekstrak tabel dari dokumen PDF](/pdf/id/python-net/extracting-table/)
- [Hapus tabel dari PDF yang sudah ada](/pdf/id/python-net/removing-tables/)
