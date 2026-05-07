---
title: Extract Data from Table in PDF with Python
linktitle: Extract Data from Table
type: docs
weight: 40
url: /python-net/extract-data-from-table-in-pdf/
description: Learn how to extract table data from PDF files with Aspose.PDF for Python and export the results for further processing.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from Table in PDF via Python
Abstract: This article explains how to extract and process table data from PDF documents with Aspose.PDF for Python. It shows how to scan each page with TableAbsorber, read rows and cells from detected tables, limit extraction to a specific annotated region, and export PDF content to CSV format for use in spreadsheet tools and downstream processing.
---

## Extract Tables from PDF programmatically

Use [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) to detect tables on each page of a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). After visiting a page, iterate through `table_list`, then walk through each row and cell to reconstruct the table content in a readable text format.

1. Open the PDF as a `Document`.
1. Iterate through the pages in `document.pages`.
1. Create a `TableAbsorber` for each page and call `visit(page)`.
1. Loop through the detected tables, rows, and cells.
1. Read text fragments from each cell and assemble the extracted row output.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Extract table in specific area of PDF page

If you need to extract only tables located inside a marked region, combine [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) with a [SquareAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/squareannotation/). In this example, the annotation rectangle is used as a boundary, and only tables fully contained within that region are processed.

1. Open the PDF as a `Document`.
1. Select the target page.
1. Find the square annotation that marks the region of interest.
1. Create a `TableAbsorber` and visit the page.
1. Compare each detected table rectangle with the annotation rectangle.
1. Process only the tables that fall completely inside the marked area.

```python
import aspose.pdf as apdf
from os import path

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
                    cell_text.append("".join(seg.text for seg in fragment.segments))
                row_text.append("|".join(cell_text))
            print("|".join(row_text))
```

## Export Table Data from PDF to CSV

When you need the extracted data in a spreadsheet-friendly format, save the PDF using [ExcelSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/excelsaveoptions/) and set the output format to CSV. The resulting file can be opened in Excel, Google Sheets, or imported into analytics workflows.

1. Open the source PDF as a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create an `ExcelSaveOptions` instance.
1. Set `excel_save.format` to `ExcelSaveOptions.ExcelFormat.CSV`.
1. Save the document to the target CSV path.

```python
import aspose.pdf as apdf
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

document = apdf.Document(path_infile)
excel_save = apdf.ExcelSaveOptions()
excel_save.format = apdf.ExcelSaveOptions.ExcelFormat.CSV
document.save(path_outfile, excel_save)
```
