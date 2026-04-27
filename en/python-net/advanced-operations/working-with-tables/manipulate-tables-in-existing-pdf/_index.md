---
title: Manipulate Tables in Existing PDF
linktitle: Manipulate Tables
type: docs
weight: 40
url: /python-net/manipulating-tables/
description: Learn how to inspect and modify tables in existing PDF documents using Python.
lastmod: "2026-04-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Modify existing PDF tables with Python
Abstract: This article explains how to manipulate tables already present in PDF documents using Aspose.PDF for Python via .NET. Learn how to locate tables with TableAbsorber, access specific rows and cells, update table text content, and save the modified PDF in Python.
---

## Manipulate Tables in Existing PDF

Aspose.PDF for Python via .NET lets you update tables that already exist in a PDF document. You can use the [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) class to find tables on a page, access rows and cells, change text content, and save the updated file.

Use this page when you need to update existing table content in PDFs without recreating the whole document layout.

## Find and Replace Text in PDF Table Cells

This example finds the first table on page 1, accesses the first cell, replaces its text, and saves the output PDF.

1. Open the input PDF.
1. Create a TableAbsorber and visit page 1.
1. Ensure at least one table is detected.
1. Access the first cell in the first row of the first table.
1. Ensure the cell contains text fragments, then update the first fragment.
1. Save the modified PDF.

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

## Replace an Existing Table with a New Table

You can also replace a detected table with a newly created one. This approach is useful when both structure and content must change.

The code below opens a PDF, finds the first table on page 1, creates a replacement table, swaps the old table with the new one, and saves the result.

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

## Related Table Topics

- [Work with tables in PDF using Python](/pdf/python-net/working-with-tables/)
- [Add tables to PDF using Python](/pdf/python-net/adding-tables/)
- [Extract tables from PDF documents](/pdf/python-net/extracting-table/)
- [Remove tables from existing PDFs](/pdf/python-net/removing-tables/)
