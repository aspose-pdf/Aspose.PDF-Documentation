---
title: Split PDF
linktitle: Split PDF files
type: docs
weight: 60
url: /python-cpp/split-pdf-document/
keywords: split pdf into multiple files, split pdf into separate pdfs, split pdf python
description: This topic shows how to split PDF pages into individual PDF files in your Python applications.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Split PDF into multiple files or separate pdfs in Python

The following Python code snippet shows you how to split PDF pages into individual PDF files.

```python

import AsposePDFPythonWrappers as ap

# The path to the documents directory.
dataDir = "..."

# Open document
pdfDocument = ap.Document(dataDir + "SplitToPages.pdf")

pageCount = 1

# Loop through all the pages

for pdfPage in pdfDocument.pages:
    newDocument = ap.Document()
    newDocument.pages.add(pdfPage)
    newDocument.save(dataDir + "page_" + pageCount + "_out" + ".pdf")
    pageCount += 1

```
