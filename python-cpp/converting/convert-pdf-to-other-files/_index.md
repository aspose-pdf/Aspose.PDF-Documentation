---
title: Convert PDF to Text in Python
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /python-cpp/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: convert, PDF, EPUB, LaText, Text, XPS, Python
description: This topic shows you how to convert PDF file to other file formats like Text using Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF to Text

**Aspose.PDF for Python** support converting whole PDF document and single page to a Text file.

### Convert PDF document to Text file

You can convert PDF document to TXT file using 'TextDevice' class.

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

{{% alert color="success" %}}
**Try to convert Convert PDF to Text online**

Aspose.PDF for Python presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}
