---
title: Extract Text from PDF using Python
linktitle: Extract Text from PDF
type: docs
weight: 10
url: /python-net/extract-text-from-pdf/
description:  This section contains articles on text extraction from PDF documents using Aspose.PDF in Python.
lastmod: "2025-03-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Extract Text from PDF via Python
Abstract: The article provides a step-by-step guide on extracting text from PDF documents using two different methods. The first method involves converting the entire content of a PDF into plain text, which is useful for applications like text analysis, search indexing, or data extraction. This process includes loading the PDF, initializing a text absorber, extracting text from all pages, and writing the extracted text to a file. The second method focuses on extracting highlighted text from a PDF, which aids in reviewing key points or summarizing content. This involves identifying and printing text from highlight annotations found on specific pages of the document. Both methods utilize the Aspose.PDF library in Python to accomplish the tasks.
---

## Extract Text from PDF Document

This example converts PDF content into plain text, which can be used for further text analysis, search indexing, or data extraction.

1. Load the PDF Document
1. Initialize a Text Absorber
1. Extract Text from All Pages
1. Write the Extracted Text to a File

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    textAbsorber = apdf.text.TextAbsorber()
    document.pages.accept(textAbsorber)
    with open(path_outfile, "w", encoding="utf-8") as file:
        file.write(textAbsorber.text)
```

## Extract Highlighted Text from PDF Document

This code snippet extracts highlighted text from a PDF document, which can help review key points or summarize content:

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)

    document = apdf.Document(path_infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, apdf.annotations.HighlightAnnotation):
            highlight_annotation = cast(apdf.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```
