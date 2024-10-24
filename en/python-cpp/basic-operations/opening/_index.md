---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /python-cpp/open-pdf-document/
description: Learn how to open a PDF file in Python Aspose.PDF for Python via C++ library. You can open existing PDF, document from stream, and encrypted PDF document.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Open existing PDF document

There are several ways to open a document. The easiest is to specify a file name.

```python

    import AsposePDFPythonWrappers as ap
    # Open document
    document = ap.Document("sample.pdf")
    count = document.pages.count()
    print("Pages: " + str(count))
```

## Open encrypted PDF document

```python

    import AsposePDFPythonWrappers as ap
    # Open document
    document = ap.Document("sample.pdf","password")
    count = document.pages.count()
    print("Pages: " + str(count))
```
