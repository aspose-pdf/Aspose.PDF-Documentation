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
    """Merge two PDF documents into a single output document.

    This operation opens two input PDF files, appends all pages from the
    second document to the first, and saves the merged result to the
    specified output file.

    Args:
        infile1 (str): Path to the first input PDF document. Pages from
            this document will appear first in the merged output.
        infile2 (str): Path to the second input PDF document. All pages
            from this document are appended to ``infile1``.
        outfile (str): Path where the merged PDF document will be saved.

    Returns:
        None

    Examples:
        Merge two sample documents and save the result::

            from os import path
            from working_with_documents.example_merge_pdf_document import merge_two_documents

            input_dir = "sample_data/input"
            output_dir = "sample_data/output"

            infile1 = path.join(input_dir, "sample1.pdf")
            infile2 = path.join(input_dir, "sample3.pdf")
            outfile = path.join(output_dir, "sample_merge.pdf")

            merge_two_documents(infile1, infile2, outfile)
    """
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is an online free web application that allows you to investigate how presentation merging functionality works.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## Related Document Topics

- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Split PDF files in Python](/pdf/python-net/split-document/)
- [Optimize PDF files in Python](/pdf/python-net/optimize-pdf/)
- [Manipulate PDF documents in Python](/pdf/python-net/manipulate-pdf-document/)

