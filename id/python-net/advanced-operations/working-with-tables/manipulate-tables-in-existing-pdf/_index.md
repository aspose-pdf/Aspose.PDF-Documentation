---
title: Memanipulasi Tabel dalam PDF yang ada
linktitle: Manipulasi Tabel
type: docs
weight: 40
url: /id/python-net/manipulating-tables/
description: Pelajari cara bekerja dengan tabel dalam PDF yang ada menggunakan Aspose.PDF untuk Python via .NET, memberikan fleksibilitas dalam modifikasi dokumen.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Memanipulasi Tabel dalam PDF yang ada

Aspose.PDF untuk Python menunjukkan cara memodifikasi konten sel tertentu dalam sebuah tabel pada dokumen PDF. Ini menggunakan kelas TableAbsorber untuk menemukan tabel pada halaman pertama, mengakses fragmen teks tertentu dalam sel pertama dari tabel pertama, memperbarui teksnya, dan menyimpan PDF yang telah dimodifikasi ke file baru.

1. Buka file PDF menggunakan 'ap.Document()'.
1. Buat objek TableAbsorber untuk mendeteksi tabel dalam PDF.
1. Panggil absorber.visit() untuk menemukan semua tabel pada halaman pertama.
1. Akses fragmen teks tertentu:
- Mengambil tabel pertama.
- Mendapatkan baris pertama tabel.
- Memilih fragmen teks kedua dalam sel.
1. Modifikasi teks.
1. Simpan PDF yang diperbarui.
1. Mencetak konfirmasi file yang disimpan.

```python

    import aspose.pdf as ap
    from os import path

    # Define file names and data directory
    data_dir = "."  # or specify your data directory
    infile = "input.pdf"   # replace with your input PDF file name
    outfile = "output.pdf" # replace with your desired output PDF file name

    # Open PDF document
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "hi world"

    # Save PDF document

    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```

## Ganti Tabel lama dengan yang baru dalam dokumen PDF

Aspose.PDF memungkinkan penggantian tabel yang ada dalam PDF dengan tabel baru. Potongan kode membuka PDF, mengidentifikasi tabel pertama pada halaman pertama menggunakan TableAbsorber, membuat tabel baru dengan lebar kolom dan konten khusus, kemudian mengganti tabel asli dengan tabel baru. Akhirnya, ia menyimpan PDF yang diperbarui ke file baru.

Ini menunjukkan cara memodifikasi struktur dan konten tabel dalam PDF tanpa mengubah bagian lain dari dokumen.

```python

    import aspose.pdf as ap
    from os import path

    # Open PDF document
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get first table on the page
    table = absorber.table_list[0]

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

    # Replace the table with new one
    absorber.replace(document.pages[1], table, new_table)

    # Save PDF document
    document.save(path_outfile)
    print(f"File saved at: {path_outfile}")
```
