---
title: Adding Page Stamps to PDF with Python
linktitle: Adding Page Stamps
type: docs
weight: 30
url: /python-net/page-stamps-in-the-pdf-file/
description: Aspose.PDF for Python via .NET allows you to add Page Stamp to your PDF file.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add Page Stamps to PDF using Python
Abstract: This article explains how to add a page stamp to a PDF document using Aspose.PDF for Python. A page stamp allows you to overlay or underlay content—such as logos, watermarks, or annotations—onto a specific page in a PDF. The example shows how to open an existing PDF, create a PdfPageStamp object from another PDF page, configure it as a background stamp, and apply it to a particular page. The stamped PDF is then saved as a new document. This technique is useful for branding, watermarking, or emphasizing page-level content in automated PDF workflows.
---

Aspose.PDF for Python via .NET shows how to apply a page stamp (watermark or overlay) to a specific page in a PDF document using Aspose.PDF for Python. The page stamp can be an existing PDF page used as a background or foreground layer. This is useful for adding logos, watermarks, or other repetitive page content.

1. Open the PDF document using 'ap.Document()'.
1. Create a 'PdfPageStamp' object using the PDF page or file to use as the stamp.
1. Set the stamp properties, e.g., 'background = True' to place it behind the content.
1. Add the stamp to a specific page using 'document.pages[page_number].add_stamp(page_stamp)'.
1. Save the modified PDF to the specified output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_page_stamp(input_file_name, page_stamp_name, output_file_name):
    # Open PDF document
    document = ap.Document(input_file_name)

    page_stamp = ap.PdfPageStamp(page_stamp_name, 1)
    page_stamp.background = True

    # Add stamp to particular page
    document.pages[1].add_stamp(page_stamp)

    document.save(output_file_name)
```
