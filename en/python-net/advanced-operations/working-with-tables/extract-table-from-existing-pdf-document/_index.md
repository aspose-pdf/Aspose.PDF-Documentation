---
title: Extract Table from PDF Document
linktitle: Extract Table
type: docs
weight: 20
url: /python-net/extracting-table/
description: Aspose.PDF for Python via .NET makes it possible to carry out various manipulations with the tables contained in your pdf document.
lastmod: "2025-09-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to extract Table from PDF using Python
Abstract: This article discusses the process of extracting tables from PDF documents using Python, specifically leveraging the Aspose.PDF for Python via .NET Library. It provides a code example demonstrating how to load a PDF document, iterate through its pages, and utilize the `TableAbsorber` class to identify and extract table data. The code iterates through each table, row, and cell, collecting text fragments and printing the extracted text. This method is highlighted as a powerful tool for data extraction and analysis tasks involving tabular data within PDFs.
---

## Extract Table from PDF

Extracting tables from PDFs using Python can be incredibly useful for data extraction and analysis. With the Aspose.PDF for Python via .NET Library, you can efficiently work with tables embedded in PDF documents for various data-related tasks.

This code snippet opens an existing PDF file, scans each page for tables, and extracts their cell text content. It uses the 'TableAbsorber' to detect tables and then iterates through rows and cells to print out the text inside.

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

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```

