---
title: Remove Tables from Existing PDF Documents
linktitle: Remove Tables
description: Learn how to remove one or more tables from existing PDF documents in Python.
lastmod: "2026-05-05"
type: docs
weight: 50
url: /python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete one or multiple tables from PDF files with Python
Abstract: This article explains how to remove tables from existing PDF documents using Aspose.PDF for Python via .NET. It introduces `TableAbsorber` for locating tables and demonstrates how to delete a single table or remove all detected tables from a page.
---

## Remove Table from PDF document

Aspose.PDF for Python lets you remove a table from a PDF. It opens an existing PDF, detects the first table on the first page with `TableAbsorber`, deletes that table using `remove()`, and saves the updated PDF to a new file.

Use this page when you need to clean up table-heavy PDFs, remove outdated tabular content, or simplify documents before redistribution.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Remove all Tables from PDF document

With our library, you can remove all tables from a specific page in a PDF. The code opens an existing PDF, detects all tables on the second page with TableAbsorber, iterates through the detected tables, removes each one, and then saves the modified PDF to a new file. It is useful when you need to bulk-remove tables from a page while leaving the rest of the PDF content intact.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Related Table Topics

- [Work with tables in PDF using Python](/pdf/python-net/working-with-tables/)
- [Add tables to PDF using Python](/pdf/python-net/adding-tables/)
- [Extract tables from PDF documents](/pdf/python-net/extracting-table/)
- [Manipulate tables in existing PDFs](/pdf/python-net/manipulating-tables/)