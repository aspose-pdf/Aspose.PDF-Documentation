---
title: Integrate Table with Data Sources PDF
linktitle: Integrate Table
type: docs
weight: 30
url: /python-net/integrate-table/
description: This article shows how to integrate PDF tables. Integrate Table with Database and determine if the table will split on the current page.
lastmod: "2025-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Create PDF from DataFrame

The function 'create_pdf_from_dataframe' takes a  DataFrame and converts it into a table inside a new PDF. It creates a fresh PDF document, adds a page, generates a table from the DataFrame (using a helper method), and saves the result to the given file path. And it's not only possible but it's very easy.

1. Initializes an empty PDF document with 'ap.Document()'.
1. The 'self.create_table_from_dataframe(df, max_rows)' function transforms the DataFrame into an Aspose.PDF table object.
1. Insert table into PDF page. Adds the generated table to the first page’s content (page.paragraphs.add(table)).
1. Save PDF document.

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

## Create Table from DataFrame

This code converts DataFrame into an Aspose.PDF Table object. It sets up table borders, adds a header row with column names, and fills the table with the first max_rows rows from the DataFrame. The resulting Table can then be added to a PDF document.

1. Creates an empty 'ap.Table()' object.
1. Set table border.
1. Set default cell border.
1. Add header row.
1. Add data rows.
1. Return the table.

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