---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /python-cpp/save-pdf-document/
description: Learn how to save PDF file in Python Aspose.PDF for Python via C++ library. Save PDF document to file system, to stream, and in Web applications.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Save PDF document to file system

```python

    import AsposePDFPythonWrappers as ap

    document = ap.Document("sample.pdf")
    document.pages.add()
    document.save("sample_mod.pdf")
```
