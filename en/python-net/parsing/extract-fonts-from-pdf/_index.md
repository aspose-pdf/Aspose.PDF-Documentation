---
title: Extract Fonts from PDF via Python
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /python-net/extract-fonts-from-pdf/
description: Use the Aspose.PDF for Python library to extract all embedded fonts from your PDF document.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Fonts from PDF using Python
Abstract: This article explains how to inspect the fonts used in a PDF document with Aspose.PDF for Python. It shows how to open a PDF with the Document class, call font_utilities.get_all_fonts() to retrieve the available font objects, and iterate through the results to read font names for analysis, auditing, or document processing workflows.
---

Use [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to open the PDF and call `font_utilities.get_all_fonts()` to retrieve all available [Font](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/font/) objects referenced by the document. This is useful when auditing embedded fonts, checking font availability before conversion, or analyzing document resources.

1. Open the source PDF as a `Document`.
1. Call `document.font_utilities.get_all_fonts()` to get the font collection.
1. Iterate through the returned `Font` objects.
1. Read and print each `font.font_name` value.

```python

    import aspose.pdf as apdf
    from os import path

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
