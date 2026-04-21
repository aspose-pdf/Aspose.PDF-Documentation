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
    """Split a multi-page PDF document into separate single-page documents.

    Each page from the input PDF is saved as an individual PDF file in the
    specified output directory using the naming pattern ``Page_{n}.pdf``,
    where ``n`` is the 1-based page index.

    Args:
        infile (str): Path to the source multi-page PDF file to split.
        outdir (str): Directory where the single-page PDF files will be created.

    Returns:
        None

    Examples:
        Split ``sample_split.pdf`` into individual page files in the output directory:

        >>> from os import path
        >>> from examples.working_with_documents.example_split_pdf_document import split_documents
        >>> input_file = path.join("sample_data", "input", "sample_split.pdf")
        >>> output_dir = path.join("sample_data", "output")
        >>> split_documents(input_file, output_dir)
    """
    document = ap.Document(infile)
    page_count = 1
    for page in document.pages:
        with ap.Document(infile) as new_document:
            new_document.pages.add(page)
            new_document.save(path.join(outdir, f"Page_{page_count}.pdf"))
            page_count += 1
```

## Related Document Topics

- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Merge PDF files in Python](/pdf/python-net/merge-pdf-documents/)
- [Optimize PDF files in Python](/pdf/python-net/optimize-pdf/)
- [Manipulate PDF documents in Python](/pdf/python-net/manipulate-pdf-document/)

