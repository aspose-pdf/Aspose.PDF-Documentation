---
title: Extract Tables from PDF in Python
linktitle: Extract Table
type: docs
weight: 20
url: /python-net/extracting-table/
description: Learn how to extract table data from existing PDF documents in Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract table data from PDF files with Python
Abstract: This article explains how to extract tables from PDF documents using Aspose.PDF for Python via .NET. It shows how to use `TableAbsorber` to detect tables by page, iterate rows and cells, and retrieve cell text for analysis and downstream data processing.
---

## Extract Table from PDF

Extracting tables from PDFs is useful for reporting, data migration, and analytics workflows. With Aspose.PDF for Python via .NET, you can detect and read table content from existing PDF documents efficiently.

This code snippet opens an existing PDF file, scans each page for tables, and extracts cell text content. It uses `TableAbsorber` to detect tables and then iterates through rows and cells to print the extracted text.

1. Loads the PDF into an ap.Document object.
1. Loop through pages.
1. Creates a TableAbsorber object.
1. Iterate through tables.
1. Iterate through rows and cells.
1. Extract and print text from cells.

This example reads a PDF, finds all tables, and prints out their cell contents row by row.

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

## Related Table Topics

- [Work with tables in PDF using Python](/pdf/python-net/working-with-tables/)
- [Add tables to PDF using Python](/pdf/python-net/adding-tables/)
- [Integrate PDF tables with data sources](/pdf/python-net/integrate-table/)
- [Remove tables from existing PDFs](/pdf/python-net/removing-tables/)