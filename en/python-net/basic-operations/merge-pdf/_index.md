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

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is an online free web application that allows you to investigate how presentation merging functionality works.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

