---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 40
url: /python-net/manipulating-tables/
description: Learn how to work with tables in existing PDFs using Aspose.PDF for Python via .NET, providing flexibility in document modification.
lastmod: "2025-09-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipulate tables in existing PDF

Aspose.PDF for Python shows how to modify the content of a specific cell within a table in a PDF document. It uses the TableAbsorber class to locate tables on the first page, accesses a particular text fragment within the first cell of the first table, updates its text, and saves the modified PDF to a new file.

1. Open the PDF file using 'ap.Document()'.
1. Create a TableAbsorber object to detect tables in the PDF.
1. Calls absorber.visit() to find all tables on the first page.
1. Access a specific text fragment:
    - Retrieves the first table.
    - Gets the first row of the table.
    - Selects the second text fragment in the cell.
1. Modify the text.
1. Save the updated PDF.
1. Prints confirmation of the saved file.

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

## Replace old Table with a new one in PDF document

Aspose.PDF allows replacing an existing table in a PDF with a new table.  The code snippet opens a PDF, identifies the first table on the first page using TableAbsorber, creates a new table with custom column widths and content, and then replaces the original table with the new one. Finally, it saves the updated PDF to a new file.

It demonstrates how to modify table structure and content in a PDF without altering the rest of the document.

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