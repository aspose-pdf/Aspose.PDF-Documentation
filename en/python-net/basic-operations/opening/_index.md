---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /python-net/open-pdf-document/
description: Learn how to open a PDF file in Python Aspose.PDF for Python via .NET library. You can open existing PDF, document from stream, and encrypted PDF document.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Open existing PDF document

There are several ways to open a document. The easiest is to specify a file name.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    print("Pages: " + str(len(document.pages)))
```

## Open existing PDF document from stream

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    stream = io.FileIO(input_pdf, 'r')
    # Open document
    document = ap.Document(stream)
    print("Pages: " + str(len(document.pages)))
```

## Open encrypted PDF document

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf, password)
    print("Pages: " + str(len(document.pages)))
```
