---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /python-net/open-pdf-document/
description: Learn how to open a PDF file in Python Aspose.PDF for Python via .NET library. You can open existing PDF, document from stream, and encrypted PDF document.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Opening PDF documents using the Aspose.PDF library in Python
Abstract: This article provides a guide on opening existing PDF documents using the Aspose.PDF library in Python. It outlines three methods to achieve this - opening a PDF by specifying the file name, opening a PDF from a stream, and opening an encrypted PDF by providing a password. Each method includes a code snippet demonstrating how to utilize the Aspose.PDF library to access the PDF and print the number of pages it contains. These examples illustrate the flexibility and functionality of Aspose.PDF for handling different PDF file access scenarios.
---

## Open existing PDF document

There are several ways to open a document. The easiest is to specify a file name.

```python
import aspose.pdf as ap
import io
import sys
from os import path

def open_document_from_file(infile):

    # Open document
    document = ap.Document(infile)
    print("Pages: " + str(len(document.pages)))
```

## Open existing PDF document from stream

```python
import aspose.pdf as ap
import io
import sys
from os import path

def open_document_from_stream(infile):
    with io.FileIO(infile, "r") as stream:
        # Open document
        document = ap.Document(stream)
        print("Pages: " + str(len(document.pages)))
```

## Open encrypted PDF document

```python
import aspose.pdf as ap
import io
import sys
from os import path

def open_document_encrypted(infile):
    password = "P@ssw0rd"
    # Open document
    document = ap.Document(infile, password)
    print("Pages: " + str(len(document.pages)))
```
