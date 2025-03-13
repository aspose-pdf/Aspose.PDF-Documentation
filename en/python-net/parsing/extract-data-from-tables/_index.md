---
title: Extract Data from Table in PDF with Python
linktitle: Extract Data from Table
type: docs
weight: 40
url: /python-net/extract-data-from-table-in-pdf/
description: Learn how to extract tabular from PDF using Aspose.PDF for Python
lastmod: "2025-03-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get Data from Table using the Aspose.PDF for Python
Abstract: The article discusses methods for extracting tables from PDF documents programmatically using the Aspose.PDF library in Python. It presents three code snippets, each demonstrating a specific technique for handling tabular data within PDFs.
---

## Extract Tables from PDF programmatically

This code extracts PDF tables and converts tabular data from a PDF file into a readable and structured format for further processing or analysis.

1. Opening the PDF Document
1. Iterating through PDF Pages
1. Extracting Table Data

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Iterate through each page in the document
    for page in document.pages:
        absorber = apdf.text.TableAbsorber()
        absorber.visit(page)

        for table in absorber.table_list:
            print("Table")
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extract table in specific area of PDF page

This code snippet extracts tabular data from specific marked regions in a PDF, such as data within a highlighted box or a specific annotation.

1. Open PDF document
1. Get the first page
1. Find the first square annotation
1. Initialize the TableAbsorber
1. Iterate through tables on the page
1. Check if the table is inside the annotation region

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    # Get the first page (index starts from 1 in Aspose.PDF)
    page = document.pages[1]

    # Find the first square annotation
    square_annotation = next(
        (
            ann
            for ann in page.annotations
            if ann.annotation_type == apdf.annotations.AnnotationType.SQUARE
        ),
        None,
    )

    if square_annotation is None:
        print("No square annotation found.")
        return

    # Initialize the TableAbsorber
    absorber = apdf.text.TableAbsorber()
    absorber.visit(page)

    # Iterate through tables on the page
    for table in absorber.table_list:
        table_rect = table.rectangle
        annotation_rect = square_annotation.rect

        # Check if the table is inside the annotation region
        is_in_region = (
            annotation_rect.llx < table_rect.llx
            and annotation_rect.lly < table_rect.lly
            and annotation_rect.urx > table_rect.urx
            and annotation_rect.ury > table_rect.ury
        )

        if is_in_region:
            for row in table.row_list:
                row_text = []
                for cell in row.cell_list:
                    cell_text = []
                    for fragment in cell.text_fragments:
                        cell_text.append(
                            "".join(seg.text for seg in fragment.segments)
                        )
                    row_text.append("|".join(cell_text))
                print("|".join(row_text))
```

## Extract Table Data from PDF and store it in Excel file

This following code snippet extracts tabular data from a PDF and exports it as a CSV file for further analysis or manipulation in spreadsheet applications like Excel or Google Sheets.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    excel_save = apdf.ExcelSaveOptions()
    excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
    document.save(path_outfile, excel_save)
```
