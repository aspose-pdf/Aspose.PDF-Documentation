---
title: Extract Table from PDF Document
linktitle: Extract Table
type: docs
weight: 20
url: /python-net/extract-table-from-existing-pdf-document/
description: Aspose.PDF for Python via .NET makes it possible to carry out various manipulations with the tables contained in your pdf document.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to extract Table from PDF Document
Abstract: The article "Extract Table from PDF Document" discusses using the Aspose.PDF for Python via .NET Library to extract tables from PDF documents. This process is valuable for data extraction and analysis tasks. The article provides a Python code snippet demonstrating how to load a PDF document and use the `TableAbsorber` to iterate through pages and extract text from table cells. This approach is particularly useful for beginners seeking to manipulate PDF content programmatically. The Aspose.PDF library, which supports various operating systems and offers comprehensive PDF manipulation capabilities, serves as a robust tool for these tasks.
---

## Extract Table from PDF

Extracting tables from PDFs using Python can be incredibly useful for data extraction and analysis. With the Aspose.PDF for Python via .NET Library, you can efficiently work with tables embedded in PDF documents for various data-related tasks.

```python

    import aspose.pdf as ap

    # Load source PDF document
    pdf_document = ap.Document(input_file)
    for page in pdf_document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            for row in table.row_list:
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)

```

