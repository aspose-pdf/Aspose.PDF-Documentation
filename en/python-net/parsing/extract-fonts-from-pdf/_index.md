---
title: Extract Fonts from PDF Python
linktitle: Extract Fonts from PDF
type: docs
weight: 30
url: /python-net/extract-fonts-from-pdf/
description: Use the Aspose.PDF for Python library to extract all embedded fonts from your PDF document.
lastmod: "2025-03-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get Fonts from PDF using the Aspose.PDF for Python
Abstract: This article provides a guide on extracting all fonts from a PDF document using the `get_all_fonts()` method available in the `Document` class of the `aspose.pdf` library. The article includes a Python code snippet that demonstrates the process. It begins by importing required modules and setting up the input file path. The `Document` object is created to open the specified PDF file. Subsequently, the `get_all_fonts()` method is invoked to retrieve all fonts used in the document. Each font's name is then printed, illustrating how to access font details from a PDF.
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
