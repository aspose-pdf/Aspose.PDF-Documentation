---
title: Extract Text From Stamps using Python
type: docs
weight: 60
url: /python-net/extract-text-from-stamps/
description: Learn how to use special feature of Aspose.PDF for Python - text exstraction from stamp annotations
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get text from stamp annotations using the Aspose.PDF for Python
Abstract: The article introduces a method for extracting text from stamp annotations in PDF documents using the Aspose.PDF library for Python. It outlines a step-by-step process to achieve this task - loading the PDF document, accessing its first page, iterating through annotations to identify stamp annotations, initializing a text absorber, extracting appearance information, and finally extracting text from the appearance stream to print it. The article provides a Python code snippet that demonstrates how to implement these steps, showcasing the use of Aspose.PDF's functionalities to handle and extract data from stamp annotations effectively.
---

## Extract Text from Stamp Annotations

Aspose.PDF for Python lets you extract text from stamp annotations. In order to extract text from Stamp Annotations in a PDF, the following steps can be used:

1. Load the PDF Document
1. Access the First Page
1. Iterate Through Annotations
1. Check for Stamp Annotations
1. Initialize a Text Absorber
1. Extract Appearance Information
1. Extract Text from the Appearance Stream
1. Print the Extracted Text

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    document = apdf.Document(path_infile)
    page = document.pages[1]
    # Get the annotation from the first page (index 0-based in Python)
    for annotation in page.annotations:
        if annotation.annotation_type == apdf.annotations.AnnotationType.STAMP:
            absorber = apdf.text.TextAbsorber()
            xforms = []
            # Get the appearance of the annotation
            if (annotation.appearance.try_get_value('N', xforms)):
                # Extract text from the appearance
                absorber.visit(xforms[0])

                # Print extracted text
                print(absorber.text)
```
