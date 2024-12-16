---
title: Convert PDF to Text in Python
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
description: This topic shows you how to convert PDF file to other file formats like Text using Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF to Text

**Aspose.PDF for Python** support converting whole PDF document and single page to a Text file.

### Convert PDF document to Text file

You can convert PDF document to TXT file using 'TextDevice' class.

1. Creating the input, and output file path
1. Creating an instance of the PDF extractor facade with [extractor_create]
(https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Binding the PDF file to the extractor with [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Extracting the text from the PDF file using [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Writing the extracted text to the output file
1. Save the output PDF with 'document.save' method.

The following code snippet explains how to extract the texts from the all pages.

```python

    from AsposePdfPython import *

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"

    extactor = extractor_create()
    extractor_bind_pdf(extactor,input_pdf)
    text = extractor_extract_text(extactor)

    with open(output_pdf, 'w') as f:
        f.write(text)
```


