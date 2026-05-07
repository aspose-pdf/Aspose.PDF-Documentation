---
title: Integrate PDF Tables with Data Sources in Python
linktitle: Integrate Table
type: docs
weight: 30
url: /python-net/integrate-table/
description: Learn how to integrate PDF tables with data sources such as databases and pandas DataFrames in Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Integrate PDF tables with databases and DataFrames using Python
Abstract: This article explains how to integrate PDF tables with external data sources using Aspose.PDF for Python via .NET. Learn how to build PDF tables from pandas DataFrames and other structured sources, insert them into documents, and control table flow when rendering across PDF pages in Python.
---

## Create PDF from DataFrame

The `create_pdf_from_dataframe` function builds a new PDF and inserts a table generated from a pandas DataFrame. This approach is useful for reporting workflows where your data already exists in tabular form.

The function performs the following steps:

1. Create an empty PDF document with `ap.Document()`.
1. Add a page to the document.
1. Convert the DataFrame into an Aspose.PDF table by calling `create_table_from_dataframe(df, max_rows)`.
1. Add the table to the page with `page.paragraphs.add(table)`.
1. Save the PDF to the output path.

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

## Create Table from DataFrame

The `create_table_from_dataframe` function converts a DataFrame into an Aspose.PDF `Table` object that you can add to any page.

It does the following:

1. Create an empty `ap.Table()` instance.
1. Set table and cell borders for consistent formatting.
1. Add a header row using DataFrame column names.
1. Add data rows from `df.head(max_rows)`.
1. Return the populated table object.

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

## Related Table Topics

- [Work with tables in PDF using Python](/pdf/python-net/working-with-tables/)
- [Add tables to PDF using Python](/pdf/python-net/adding-tables/)
- [Extract tables from PDF documents](/pdf/python-net/extracting-table/)
- [Manipulate tables in existing PDFs](/pdf/python-net/manipulating-tables/)