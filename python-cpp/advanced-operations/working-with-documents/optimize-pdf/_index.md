---
title: Optimize, Compress or Reduce PDF Size in Python
linktitle: Optimize PDF
type: docs
weight: 30
url: /python-cpp/optimize-pdf/
description: Optimize PDF file, shrink all images, reduce size PDF, Unembed fonts, Remove unused objects with Python.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A PDF document may sometimes contain additional data. Reducing the size of a PDF file will help you optimize network transfer and storage. This is especially handy for publishing on web pages, sharing on social networks, sending by e-mail, or archiving in storage. We can use several techniques to optimize PDF:

- Optimize page content for online browsing
- Shrink or compress all images
- Enable reusing page content
- Merge duplicate streams
- Unembed fonts
- Remove unused objects
- Remove flattening form fields
- Remove or flatten annotations

{{% alert color="primary" %}}

 Detailed explanation of optimization methods can be found in the Optimization Methods Overview page.

{{% /alert %}}

## Optimize PDF Document for the Web

Optimization, or linearization for Web, refers to the process of making a PDF file suitable for online browsing using a web browser. To optimize a file for web display:


The following code snippet shows how to optimize a PDF document for the web.

```python

    import AsposePDFPythonWrappers as ap

    # The path to the documents directory.
    dataDir = "..."

    # Open document
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # Optimize for web
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # Save output document
    document.Save(dataDir)
```
