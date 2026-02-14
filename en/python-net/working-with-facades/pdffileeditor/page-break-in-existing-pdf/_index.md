---
title: Page Break in existing PDF
type: docs
weight: 30
url: /python-net/page-break-in-existing-pdf/
description: Discover how to insert page breaks in an existing PDF file in Python using Aspose.PDF for better page management.
lastmod: "2026-01-05"
---

The [add_page_break](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method lets you insert page breaks into an existing PDF document at specified positions. It's useful when you want to split content within a single page at a given vertical position, effectively pushing later content to a new page.

The method can be called using:

1. Document objects
1. File paths
1. Streams

## Add Page Break Using Document Objects

```python

from aspose.pdf import Document
from aspose.pdf.facades import PdfFileEditor

def add_page_break_example01():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_page_break()

    # Open source PDF
    with Document(data_dir + "PageBreak.pdf") as src:
        # Create an empty destination PDF
        with Document() as dest:
            file_editor = PdfFileEditor()

            # Define page break: insert at page 1, position 450 units down
            page_break = PdfFileEditor.PageBreak(1, 450)

            # Add the page break
            file_editor.add_page_break(src, dest, [page_break])

            # Save the modified PDF
            dest.save(data_dir + "PageBreak_out.pdf")
```

## Add Page Break Using File Paths

```python

from aspose.pdf.facades import PdfFileEditor

def add_page_break_example02():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_page_break()

    file_editor = PdfFileEditor()

    # Insert page break into a PDF via file paths
    page_break = PdfFileEditor.PageBreak(1, 450)

    file_editor.add_page_break(
        data_dir + "PageBreak.pdf",
        data_dir + "PageBreakWithDestPath_out.pdf",
        [page_break]
    )
```

## Add Page Break Using Streams

```python

from aspose.pdf.facades import PdfFileEditor

def add_page_break_example03():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_page_break()

    file_editor = PdfFileEditor()
    page_break = PdfFileEditor.PageBreak(1, 450)

    with open(data_dir + "PageBreak.pdf", "rb") as src_stream, \
         open(data_dir + "PageBreakWithStream_out.pdf", "wb") as dest_stream:

        file_editor.add_page_break(src_stream, dest_stream, [page_break])
```
