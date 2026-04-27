---
title: Manipulate Tables in Existing PDF
linktitle: Manipulate Tables
type: docs
weight: 40
url: /python-net/manipulating-tables/
description: Learn how to inspect and modify tables in existing PDF documents using Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modify existing PDF tables with Python
Abstract: This article explains how to manipulate tables already present in PDF documents using Aspose.PDF for Python via .NET. Learn how to locate tables with TableAbsorber, access specific rows and cells, update table text content, and save the modified PDF in Python.
---

Aspose.PDF for Python shows how to modify the content of a specific cell within a table in a PDF document. It uses the TableAbsorber class to locate tables on the first page, accesses a particular text fragment within the first cell of the first table, updates its text, and saves the modified PDF to a new file.

## Find and Replace Text Inside PDF Table Cells

Locate and modify text inside PDF table cells using Python and Aspose.PDF. It uses TableAbsorber to detect tables on a page, accesses specific cell text fragments, and updates their content without recreating the table.

```python
import aspose.pdf as ap
from os import path
import sys

def replace_cells(infile: str, outfile: str) -> None:
    """Replace text in table cells."""
    # Open PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()

    # Visit first page with absorber
    absorber.visit(document.pages[1])

    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]

    # Change text of the first text fragment in the cell
    fragment.text = "New Value"

    # Save PDF document
    document.save(outfile)
```

## Replace old Table with a new one in PDF document

Aspose.PDF allows replacing an existing table in a PDF with a new table.  The code snippet opens a PDF, identifies the first table on the first page using TableAbsorber, creates a new table with custom column widths and content, and then replaces the original table with the new one. Finally, it saves the updated PDF to a new file.

It demonstrates how to modify table structure and content in a PDF without altering the rest of the document.

```python
import aspose.pdf as ap
from os import path
import sys

def replace_table(infile: str, outfile: str) -> None:
    """Replace an entire table with a new one."""
    # Open PDF document
    document = ap.Document(infile)

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
    document.save(outfile)
```

## Related Table Topics

- [Work with tables in PDF using Python](/pdf/python-net/working-with-tables/)
- [Add tables to PDF using Python](/pdf/python-net/adding-tables/)
- [Extract tables from PDF documents](/pdf/python-net/extracting-table/)
- [Remove tables from existing PDFs](/pdf/python-net/removing-tables/)