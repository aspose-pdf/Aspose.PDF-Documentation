---
title: Extract Fonts from PDF via Python
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /python-net/extract-fonts-from-pdf/
description: Use the Aspose.PDF for Python library to extract all embedded fonts from your PDF document.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Fonts from PDF using Python
Abstract: This article provides guidance on extracting all fonts from a PDF document using a specific method from the Aspose.PDF library. It introduces the `font_utilities.get_all_fonts()` method available in the `Document` class, which facilitates the retrieval of font information. The article includes a Python code snippet demonstrating the process, which involves importing necessary modules, opening the PDF document, and iterating through the fonts to print each font's name. This approach is useful for developers needing to analyze or manipulate font data within PDF files.
---

In case you want to get all fonts from a PDF document, you can use 'font_utilities.get_all_fonts()' method provided in Document class. Please check following code snippet in order to get all fonts from an existing PDF document:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    # Open PDF document
    document = apdf.Document(path_infile)

    fonts = document.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```
