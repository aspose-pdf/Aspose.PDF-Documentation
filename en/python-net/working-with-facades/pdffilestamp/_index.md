---
title: PdfFileStamp Class
type: docs
weight: 155
url: /python-net/pdffilestamp-class/
description: This section explains how you can use PdfFileStamp Class by Aspose.PDF Facades in working with PDF.
lastmod: "2026-01-05"
---

## Add Text Footer

```python


```

## Add Header with Margins

```python


```

### Add Page Numbers with Default Position

```python

import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

CURRENT_DIR = path.dirname(__file__)
EXAMPLES_DIR = path.abspath(path.join(CURRENT_DIR, "..", ".."))
if EXAMPLES_DIR not in sys.path:
    sys.path.insert(0, EXAMPLES_DIR)

from config import initialize_data_dir, set_license

def add_page_numbers_default(infile: str, outfile: str) -> None:
    """Add centered page numbers to the bottom of each page."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)
        pdf_stamper.add_page_number("Page #")
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()


```

### Add Page Numbers with Custom Position

```python


```

### Add Page Numbers with Margins

```python


```

## Add Stamp to PDF

```python


```