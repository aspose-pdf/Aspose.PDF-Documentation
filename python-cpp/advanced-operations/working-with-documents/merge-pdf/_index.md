---
title: How to Merge PDF using Python
linktitle: Merge PDF files
type: docs
weight: 50
url: /python-cpp/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf Python, combine multiple pdf into one Python, merge multiple pdf into one Python"
description: This page explain how to merge PDF documents into a single PDF file with Python.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Merge or combine multiple PDF into single PDF in Python

Merging PDF in Python is not straightforward task without using 3rd party library.
This article shows how to merge multiple PDF files into a single PDF document using Aspose.PDF for Python. PDF files are merged such that the first one is joined at the end of the other document.

## Merge PDF Files using Python and DOM

To concatenate two PDF files:

The following code snippet shows how to concatenate PDF files.

```python
import AsposePDFPythonWrappers as ap

# The path to the documents directory.
dataDir = ""

# Open first document
pdfDocument1 = ap.Document(dataDir + "sample.pdf")
pdfDocument2 = ap.Document(dataDir + "sample2.pdf")

# Add pages of second document to the first
pdfDocument1.pages.add(pdfDocument2.pages)

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf"
# Save concatenated output file
pdfDocument1.save(dataDir)
```

## Live Example

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) is an online free web application that allows you to investigate how presentation merging functionality works.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)
