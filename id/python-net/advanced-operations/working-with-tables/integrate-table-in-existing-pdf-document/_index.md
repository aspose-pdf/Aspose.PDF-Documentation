---
title: Mengintegrasikan Tabel dengan Sumber Data PDF
linktitle: Integrasikan Tabel
type: docs
weight: 30
url: /id/python-net/integrate-table/
description: Artikel ini menunjukkan cara mengintegrasikan tabel PDF. Mengintegrasikan Tabel dengan Database dan menentukan apakah tabel akan terpisah pada halaman saat ini.
lastmod: "2025-09-17"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Buat PDF dari DataFrame

Fungsi 'create_pdf_from_dataframe' mengambil DataFrame dan mengubahnya menjadi tabel dalam PDF baru. Fungsi ini membuat dokumen PDF baru, menambahkan halaman, menghasilkan tabel dari DataFrame (menggunakan metode bantuan), dan menyimpan hasilnya ke jalur file yang diberikan. Dan ini tidak hanya mungkin tetapi sangat mudah.

1. Menginisialisasi dokumen PDF kosong dengan 'ap.Document()'.
1. Fungsi 'self.create_table_from_dataframe(df, max_rows)' mengubah DataFrame menjadi objek tabel Aspose.PDF.
1. Menyisipkan tabel ke halaman PDF. Menambahkan tabel yang dihasilkan ke konten halaman pertama (page.paragraphs.add(table)).
1. Menyimpan dokumen PDF.

```python

from os import path
import pandas as pd
import aspose.pdf as ap

# Example DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Paris", "London"]
})

max_rows = 3  # Number of rows to include in the table
path_outfile = "output.pdf"

# Define the function to create a table from DataFrame
def create_table_from_dataframe(df, max_rows):
    table = ap.Table()
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )
    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray
    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))
    return table

# Load source PDF document
document = ap.Document()
page = document.pages.add()

table = create_table_from_dataframe(df, max_rows)

# Add table object to first page of input document
page.paragraphs.add(table)
document.save(path_outfile)
```

## Buat Tabel dari DataFrame

Kode ini mengonversi DataFrame menjadi objek Tabel Aspose.PDF. Ini menyiapkan batas tabel, menambahkan baris header dengan nama kolom, dan mengisi tabel dengan baris pertama sebanyak max_rows dari DataFrame. Tabel yang dihasilkan kemudian dapat ditambahkan ke dokumen PDF.

1. Membuat objek 'ap.Table()' kosong.
1. Mengatur batas tabel.
1. Mengatur batas sel default.
1. Menambahkan baris header.
1. Menambahkan baris data.
1. Mengembalikan tabel.

```python

    from os import path
    import pandas as pd
    import aspose.pdf as ap

    
    table = ap.Table()  # Initializes a new instance of the Table
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = (
        False  # Prevent header row from being split across pages
    )
    for column_name in df.columns:
        cell = header_row.cells.add(str(column_name))
        cell.background_color = ap.Color.light_gray

    # Add data rows
    for row_data in df.head(max_rows).itertuples(index=False):
        row = table.rows.add()
        for value in row_data:
            row.cells.add(str(value))

    return table
```
