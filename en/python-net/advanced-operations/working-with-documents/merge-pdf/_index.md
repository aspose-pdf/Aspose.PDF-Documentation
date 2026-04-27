---
title: Merge PDF Files in Python
linktitle: Merge PDF files
type: docs
weight: 50
url: /python-net/merge-pdf-documents/
description: Learn how to merge multiple PDF files into a single document in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Combine PDF pages using Python
Abstract: This article addresses the common need to merge multiple PDF files into a single document, a process valuable for organizing and optimizing storage and sharing of PDF content. It explores the use of Aspose.PDF for Python via .NET to efficiently combine PDF files, acknowledging that merging PDFs in Python can be challenging without third-party libraries. The article provides a step-by-step guide to concatenating PDF files - creating a new document, merging the files, and saving the merged document. A code snippet demonstrates the implementation using Aspose.PDF, highlighting the library's capability to streamline the merging process. Additionally, it introduces the Aspose.PDF Merger, an online tool for merging PDFs, enabling users to explore the functionality in a web-based environment.
---

## Merge or combine multiple PDF into single PDF in Python

Combining PDF files is a very popular query among users This can be useful when you have several PDF files that you want to share or store together as one document.

Merging PDF files can help you organize your documents, make room for storage on your PC, and share several PDF files with others by combining them into one document.

Merging PDF in Python via .NET is not straightforward task without using 3rd party library.
This article shows how to merge multiple PDF files into a single PDF document using Aspose.PDF for Python via .NET. 

## Merge PDF Files using Python and DOM

To concatenate two PDF files:

1. Create a New Document.
1. Merge the PDF Files
1. Save the Merged Document

Combining multiple PDF documents into a single file:

```python
import sys
import aspose.pdf as ap
from os import path


def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Append a Page Range from One PDF to Another

Copy and append a specific range of pages from a source PDF document to a destination PDF document using Aspose.PDF for Python.

1. Open the PDF files using the Document class.
1. Check if the source document has pages.
1. Validate the page range.
1. Skip the operation if the start page is greater than the end page.
1. Iterate through the page range.
1. Append pages to the destination document.

```python
import sys
import aspose.pdf as ap
from os import path


def _append_page_range(source_document, destination_document, start_page, end_page):
    total_pages = len(source_document.pages)
    if total_pages == 0:
        return

    start = max(1, start_page)
    end = min(end_page, total_pages)
    if start > end:
        return

    for page_number in range(start, end + 1):
        destination_document.pages.add(source_document.pages[page_number])
```

## Merge Multiple PDF Documents into One

This code snippet explains how to merge multiple PDF files into a single document:

1. Create an empty output document.
1. Iterate through input files.
1. Load each source document.
1. Determine page range.
1. Append pages to the output document.
1. Repeat for all documents.
1. Save the merged PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_multiple_documents(input_files, outfile):
    output_document = ap.Document()

    for input_file in input_files:
        source_document = ap.Document(input_file)
        _append_page_range(
            source_document, output_document, 1, len(source_document.pages)
        )

    output_document.save(outfile)
```

## Merge Selected Page Ranges from Multiple PDF

1. Load the source PDF documents.
1. Create an output document.
1. Define page ranges for each document.
1. Append pages from the first document.
1. Append pages from the second document.
1. Combine pages in desired order.
1. Save the merged PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_selected_page_ranges(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    _append_page_range(document1, output_document, 1, 2)
    _append_page_range(document2, output_document, 2, 3)

    output_document.save(outfile)
```

## Insert One PDF into Another at a Specific Position

1. Load the base and insert documents.
1. Create an output document.
1. Determine total pages in the base document.
1. Validate the insertion index.
1. Append pages before the insertion point.
1. Append all pages from the insert document.
1. Append remaining pages from the base document.
1. Save the resulting PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_insert_document_at_position(infile1, infile2, insert_after_page, outfile):
    base_document = ap.Document(infile1)
    insert_document = ap.Document(infile2)
    output_document = ap.Document()

    base_total_pages = len(base_document.pages)
    insert_index = max(0, min(insert_after_page, base_total_pages))

    _append_page_range(base_document, output_document, 1, insert_index)
    _append_page_range(insert_document, output_document, 1, len(insert_document.pages))
    _append_page_range(
        base_document, output_document, insert_index + 1, base_total_pages
    )

    output_document.save(outfile)
```

## Merge PDFs by Alternating Pages

This example demonstrates how to merge two PDF documents by alternating their pages using Aspose.PDF for Python.

1. Load the input PDF documents.
1. Create an output document.
1. Get the number of pages in each document.
1. Calculate the maximum page count.
1. Iterate through page numbers.
1. Append pages alternately.
1. Handle unequal page counts.
1. Save the merged PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_alternating_pages(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    output_document = ap.Document()

    document1_pages = len(document1.pages)
    document2_pages = len(document2.pages)
    max_pages = max(document1_pages, document2_pages)

    for page_number in range(1, max_pages + 1):
        if page_number <= document1_pages:
            output_document.pages.add(document1.pages[page_number])
        if page_number <= document2_pages:
            output_document.pages.add(document2.pages[page_number])

    output_document.save(outfile)
```

## Merge PDFs with Section Separators and Bookmarks

Merge multiple PDF documents into a single file with structured sections and navigation bookmarks using Aspose.PDF for Python.

1. Create an output document.
1. Iterate through input files.
1. Load the source document.
1. Add a separator page.
1. Create a section bookmark.
1. Append source document pages.
1. Track the first content page.
1. Add a nested content bookmark (optional).
1. Repeat for all documents.
1. Save the merged PDF.

```python
import sys
import aspose.pdf as ap
from os import path


def merge_with_section_separators_and_bookmarks(input_files, outfile):
    output_document = ap.Document()

    for section_index, input_file in enumerate(input_files, start=1):
        source_document = ap.Document(input_file)
        source_page_count = len(source_document.pages)

        separator_page = output_document.pages.add()
        separator_page.paragraphs.add(
            ap.text.TextFragment(
                f"Section {section_index}: {path.basename(input_file)}"
            )
        )

        section_bookmark = ap.OutlineItemCollection(output_document.outlines)
        section_bookmark.title = f"Section {section_index}"
        section_bookmark.action = ap.annotations.GoToAction(separator_page)
        output_document.outlines.append(section_bookmark)

        first_content_page_number = len(output_document.pages) + 1
        _append_page_range(source_document, output_document, 1, source_page_count)

        if source_page_count > 0 and first_content_page_number <= len(
            output_document.pages
        ):
            content_bookmark = ap.OutlineItemCollection(output_document.outlines)
            content_bookmark.title = f"Section {section_index} Content"
            content_bookmark.action = ap.annotations.GoToAction(
                output_document.pages[first_content_page_number]
            )
            section_bookmark.append(content_bookmark)

    output_document.save(outfile)
```

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is an online free web application that allows you to investigate how presentation merging functionality works.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Related Document Topics

- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Split PDF files in Python](/pdf/python-net/split-document/)
- [Optimize PDF files in Python](/pdf/python-net/optimize-pdf/)
- [Manipulate PDF documents in Python](/pdf/python-net/manipulate-pdf-document/)

