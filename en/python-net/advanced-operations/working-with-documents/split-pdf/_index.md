---
title: Split PDF Files in Python
linktitle: Split PDF files
type: docs
weight: 60
url: /python-net/split-pdf-document/
description: Learn how to split PDF pages into separate PDF files in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Splitting PDF pages using Python
Abstract: The article discusses the process of splitting PDF pages into individual files using Python, highlighting the utility of such a feature for managing large PDF documents. It references the Aspose.PDF Splitter, an online tool designed to demonstrate PDF splitting functionality. The article provides a detailed method for achieving this in Python applications, involving iterating through a PDF document's pages via the `Document` object's `PageCollection`. For each page, a new `Document` object is created, the page is added to it, and the new PDF file is saved using the `save()` method. An accompanying Python code snippet illustrates this process, showcasing the steps necessary to split a PDF document into separate files by iterating through its pages and saving each as an individual PDF.
---

Splitting PDF pages can be a useful feature for those who want to split a large file into separate pages or groups of pages.

Use this workflow when you need to break large PDFs into single-page files or smaller document sets for distribution, review, or downstream processing.

## Live Example

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) is an online free web application that allows you to investigate how presentation splitting functionality works.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

This topic shows how to split PDF pages into individual PDF files in your Python applications. To split PDF pages into single page PDF files using Python, the following steps can be followed:

1. Loop through the pages of PDF document through the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) collection
1. For each iteration, create a new Document object and add the individual [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) object into the empty document
1. Save the new PDF using [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method

## Split PDF into multiple files or separate pdfs in Python

The following Python code snippet shows you how to split PDF pages into individual PDF files.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents(infile, outdir):
    document = ap.Document(infile)
    for page_num in range(1, len(document.pages) + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num}.pdf"))
```

## Split a PDF into Two Equal Parts

1. Load the PDF document.
1. Determine total number of pages.
1. Calculate the midpoint.
1. Create the first output document.
1. Remove second-half pages from the first document.
1. Save the first part.
1. Create the second output document.
1. Remove first-half pages from the second document.
1. Save the second part.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_two_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    mid_point = total_pages // 2

    # First part
    with ap.Document(infile) as first_document:
        first_part_range = range(mid_point + 1, total_pages + 1)
        first_document.pages.delete(first_part_range)
        first_document.save(path.join(outdir, "Part_1.pdf"))

    # Second part
    with ap.Document(infile) as second_document:
        second_part_range = range(1, mid_point + 1)
        second_document.pages.delete(second_part_range)
        second_document.save(path.join(outdir, "Part_2.pdf"))
```

## Split a PDF into Multiple Files Every N Pages

Split a PDF document into multiple smaller files based on a fixed number of pages using Aspose.PDF for Python.

1. Load the PDF document.
1. Determine total number of pages.
1. Define pages per part.
1. Iterate through the document in chunks.
1. Calculate the page range for each part.
1. Create a new document for each part.
1. Copy pages into the new document.
1. Save the split document.
1. Repeat until all pages are processed.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_every_n_pages(infile, outdir, pages_per_part=3):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    part_index = 1
    for start_page in range(1, total_pages + 1, pages_per_part):
        end_page = min(start_page + pages_per_part - 1, total_pages)

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(
                path.join(outdir, f"Every_{pages_per_part}_Part_{part_index}.pdf")
            )

        part_index += 1
```

## Split a PDF by Custom Page Ranges

Split a PDF document into multiple files based on custom-defined page ranges using Aspose.PDF for Python.

1. Load the PDF document.
1. Determine total number of pages.
1. Create a list of tuples representing (start_page, end_page) ranges.
1. Iterate through defined ranges.
1. Validate the start page.
1. Adjust the end page.
1. Validate the effective range.
1. Create a new document for each range.
1. Copy pages into the new document.
1. Save each split document.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_by_page_ranges(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    # Define ranges as (start_page, end_page). Use None to indicate last page.
    ranges = [(1, 3), (4, 6), (7, None)]

    for index, (start_page, end_page) in enumerate(ranges, start=1):
        if start_page > total_pages:
            continue

        effective_end = total_pages if end_page is None else min(end_page, total_pages)
        if start_page > effective_end:
            continue

        with ap.Document() as range_document:
            for page_num in range(start_page, effective_end + 1):
                range_document.pages.add(document.pages[page_num])
            range_document.save(
                path.join(outdir, f"Range_{index}_{start_page}_to_{effective_end}.pdf")
            )
```

## Split a PDF into First Page and Remaining Pages

Separate the first page of a PDF document from the rest of the pages using Aspose.PDF for Python.

1. Load the PDF document.
1. Determine total number of pages.
1. Check if the document is empty.
1. Create a document for the first page.
1. Add the first page.
1. Save the first page document.
1. Check if there are additional pages.
1. Create a document for remaining pages.
1. Copy remaining pages.
1. Save the remaining pages document.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_first_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as first_page_document:
        first_page_document.pages.add(document.pages[1])
        first_page_document.save(path.join(outdir, "First_Page.pdf"))

    if total_pages == 1:
        return

    with ap.Document() as remaining_pages_document:
        for page_num in range(2, total_pages + 1):
            remaining_pages_document.pages.add(document.pages[page_num])
        remaining_pages_document.save(path.join(outdir, "Remaining_Pages.pdf"))
```

## Split a PDF into Last Page and Previous Pages

Extract the last page of a PDF document and separate it from the remaining pages using Aspose.PDF for Python.

1. Load the PDF document.
1. Determine total number of pages.
1. Check if the document is empty.
1. Create a document for the last page.
1. Add the last page.
1. Save the last page document.
1. Check for single-page documents.
1. Remove the last page from the original document.
1. Save the remaining pages.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_last_page_and_rest(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    with ap.Document() as last_page_document:
        last_page_document.pages.add(document.pages[total_pages])
        last_page_document.save(path.join(outdir, "Last_Page.pdf"))

    if total_pages == 1:
        return

    document.pages.delete(total_pages)  # Remove last page from original document
    document.save(path.join(outdir, "Previous_Pages.pdf"))
```

## Split a PDF into Three Parts

Split a PDF document into three separate parts using Aspose.PDF for Python.

1. Load the PDF document.
1. Determine total number of pages.
1. Check if the document is empty.
1. Calculate part size.
1. Iterate through three parts.
1. Determine page range for each part.
1. Validate the page range.
1. Create a new document for each part.
1. Copy pages into the part document.
1. Save each part.

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_into_three_parts(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    if total_pages == 0:
        return

    part_size = max(1, (total_pages + 2) // 3)

    for part_index in range(3):
        start_page = part_index * part_size + 1
        end_page = min((part_index + 1) * part_size, total_pages)

        if start_page > total_pages:
            break

        with ap.Document() as part_document:
            for page_num in range(start_page, end_page + 1):
                part_document.pages.add(document.pages[page_num])
            part_document.save(path.join(outdir, f"Three_Parts_{part_index + 1}.pdf"))
```

```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_custom_page_groups(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)
    groups = [
        [1, 2, 5],
        [3, 4, 6, 7],
    ]

    for group_index, group in enumerate(groups, start=1):
        valid_pages = [page_num for page_num in group if 1 <= page_num <= total_pages]
        if not valid_pages:
            continue

        with ap.Document() as group_document:
            for page_num in valid_pages:
                group_document.pages.add(document.pages[page_num])
            group_document.save(path.join(outdir, f"Custom_Group_{group_index}.pdf"))
```


```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_with_stable_filenames(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    for page_num in range(1, total_pages + 1):
        with ap.Document() as new_document:
            new_document.pages.add(document.pages[page_num])
            new_document.save(path.join(outdir, f"Page_{page_num:03d}.pdf"))
```



```python
import sys
import aspose.pdf as ap
from os import path


def split_documents_odd_even_pages(infile, outdir):
    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Odd pages document
    with ap.Document(infile) as document:
        with ap.Document() as odd_document:
            for page_num in range(1, total_pages + 1, 2):
                odd_document.pages.add(document.pages[page_num])
            odd_document.save(path.join(outdir, "Odd_Pages.pdf"))

        with ap.Document() as even_document:
            for page_num in range(2, total_pages + 1, 2):
                even_document.pages.add(document.pages[page_num])
            even_document.save(path.join(outdir, "Even_Pages.pdf"))
```

## Related Document Topics

- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Merge PDF files in Python](/pdf/python-net/merge-pdf-documents/)
- [Optimize PDF files in Python](/pdf/python-net/optimize-pdf/)
- [Manipulate PDF documents in Python](/pdf/python-net/manipulate-pdf-document/)

