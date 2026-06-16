---
title: Mengintegrasikan Tabel PDF dengan Sumber Data di Python
linktitle: Integrasikan Tabel
type: docs
weight: 30
url: /id/python-net/integrate-table/
description: Pelajari cara mengintegrasikan tabel PDF dengan sumber data seperti basis data dan DataFrames pandas di Python.
lastmod: "2026-06-12"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Integrasikan tabel PDF dengan basis data dan DataFrames menggunakan Python
Abstract: Artikel ini menjelaskan cara mengintegrasikan tabel PDF dengan sumber data eksternal menggunakan Aspose.PDF for Python via .NET. Pelajari cara membuat tabel PDF dari DataFrames pandas dan sumber terstruktur lainnya, menyisipkannya ke dalam dokumen, dan mengontrol alur tabel saat merender melintasi halaman PDF di Python.
---

## Buat PDF dari DataFrame

The `create_pdf_from_dataframe` fungsi membuat PDF baru dan menyisipkan tabel yang dihasilkan dari pandas DataFrame. Pendekatan ini berguna untuk alur kerja pelaporan di mana data Anda sudah ada dalam bentuk tabel.

Fungsi ini melakukan langkah-langkah berikut:

1. Buat dokumen PDF kosong dengan `ap.Document()`.
1. Tambahkan halaman ke dokumen.
1. Ubah DataFrame menjadi tabel Aspose.PDF dengan memanggil `create_table_from_dataframe(df, max_rows)`.
1. Tambahkan tabel ke halaman dengan `page.paragraphs.add(table)`.
1. Simpan PDF ke path output.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_pdf_from_dataframe(
    outfile: str, df: pd.DataFrame, max_rows: int = 20
) -> None:
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    table = create_table_from_dataframe(df, max_rows)

    # Add table object to first page of input document
    page.paragraphs.add(table)
    document.save(outfile)
```

## Buat Tabel dari DataFrame

The `create_table_from_dataframe` fungsi mengonversi DataFrame menjadi Aspose.PDF `Table` objek yang dapat Anda tambahkan ke halaman mana pun.

Berikut ini yang dilakukan:

1. Buat yang kosong `ap.Table()` instance.
1. Atur batas tabel dan sel untuk format yang konsisten.
1. Tambahkan baris header menggunakan nama kolom DataFrame.
1. Tambahkan baris data dari `df.head(max_rows)`.
1. Kembalikan objek tabel yang telah terisi.

```python
from os import path
import sys

import pandas as pd
import aspose.pdf as ap
from config import set_license, initialize_data_dir

def create_table_from_dataframe(df: pd.DataFrame, max_rows: int = 20) -> ap.Table:
    """Create an Aspose.PDF table from a pandas DataFrame."""
    # Initializes a new instance of the Table
    table = ap.Table()
    # Set the table border color as LightGray
    table.border = ap.BorderInfo(ap.BorderSide.ALL, 1, ap.Color.light_gray)
    # Set the border for table cells
    table.default_cell_border = ap.BorderInfo(
        ap.BorderSide.BOTTOM, 1, ap.Color.light_gray
    )

    # Add header row with column names
    header_row = table.rows.add()
    header_row.is_row_broken = False  # Prevent header row from being split across pages
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

## Topik Tabel Terkait

- [Bekerja dengan tabel dalam PDF menggunakan Python](/pdf/id/python-net/working-with-tables/)
- [Tambahkan tabel ke PDF menggunakan Python](/pdf/id/python-net/adding-tables/)
- [Ekstrak tabel dari dokumen PDF](/pdf/id/python-net/extracting-table/)
- [Manipulasi tabel dalam PDF yang ada](/pdf/id/python-net/manipulating-tables/)