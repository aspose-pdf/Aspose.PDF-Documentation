---
title: Convert PDF to TXT in Python
linktitle: Convert PDF to TXT
type: docs
weight: 20
url: /python-cpp/convert-pdf-to-txt/
lastmod: "2024-04-23"
description: Aspose.PDF for Python via C++ library allows you to convert PDF to TXT format using Python. 
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Convert PDF to TXT

Aspose.PDF for Python via C++ support converting PDF document to a Text file by following steps:

1. Creating the input, and output file path
1. Creating an instance of the PDF extractor facade with [extractor_create]
(https://reference.aspose.com/pdf/python-cpp/core/extractor_create/)
1. Binding the PDF file to the extractor with [extractor_bind_pdf](https://reference.aspose.com/pdf/python-cpp/core/extractor_bind_pdf/)
1. Extracting the text from the PDF file using [extractor_extract_text](https://reference.aspose.com/pdf/python-cpp/core/extractor_extract_text/)
1. Writing the extracted text to the output file
1. Save the output PDF with 'document.save' method.

The code snippet below shows how to convert JPG Image to PDF using Python via C++:

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Creating the data directory path
    dataDir = os.path.join(os.getcwd(), "samples")

    # Creating the input file path
    input_file = os.path.join(dataDir, "sample.pdf")

    # Creating the output file path
    output_file = os.path.join(dataDir, "results", "pdf-to-txt.txt")

    # Creating an instance of the PDF extractor facade
    extactor = apCore.facades_pdf_extractor_create()

    # Binding the PDF file to the extractor
    apCore.facades_facade_bind_pdf(extactor, input_file)

    # Extracting the text from the PDF file
    text = apCore.facades_pdf_extractor_extract_text(extactor)

    # Writing the extracted text to the output file
    with open(output_file, 'w') as f:
        f.write(text)
```


