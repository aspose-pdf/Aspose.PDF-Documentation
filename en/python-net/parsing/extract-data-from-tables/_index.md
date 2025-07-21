---
title: Extract Data from Table in PDF with Python
linktitle: Extract Data from Table
type: docs
weight: 40
url: /python-net/extract-data-from-table-in-pdf/
description: Learn how to extract tabular from PDF using Aspose.PDF for Python
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from Table in PDF via Python
Abstract: This article provides a comprehensive guide on programmatically extracting and processing tables from PDF documents using Aspose.PDF, a Python library. The article presents a Python script that opens a PDF document, iterates through each page, and extracts tables by utilizing the `TableAbsorber` class. The extracted table data is then structured and printed for further analysis.This section describes how to extract tables from specific marked regions within a PDF, such as areas enclosed by square annotations. The script identifies these annotations, initializes the `TableAbsorber`, and checks if the tables fall within the annotated regions before extracting and printing the data. The final section details a method to convert extracted tabular data from a PDF into a CSV file format.
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
