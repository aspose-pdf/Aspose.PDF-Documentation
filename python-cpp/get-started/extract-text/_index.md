---
title: Extract Text from PDF using Python
linktitle: Extract Text from PDF
type: docs
weight: 10
url: /python-cpp/extract-text/
description: This section describes how to extract text from PDF document using Python library.
lastmod: "2023-07-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Text From all the Pages of PDF Document

Extracting text from PDF isn’t easy. Not many PDF readers can extract text from PDF images or scanned PDFs. But **Aspose.PDF for Python via C++** tool allows you to easily extract text from all PDF file. 

Check the code snippet  and follow the steps to extract text from your PDF:

1. Import the Aspose.PDF library for Python
1. Create a new extractor object, which is used to extract text and images from PDF documents.
1. Bind the extractor object to a PDF file, which is the source of the extraction.
1. Extract all the text from the PDF document and put it in some variable.
1. Do whatever, print the extracted text to the console, make search some frgaments etc

```python
from AsposePdfPython import *

extactor = Extract()
extractor_bind_pdf(extactor,"blank_pdf_document.pdf")
text = extractor_extract_text(extactor)

print(text)
```
