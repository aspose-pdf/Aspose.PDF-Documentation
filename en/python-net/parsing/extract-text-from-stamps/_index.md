---
title: Extract Text From Stamps using Python
type: docs
weight: 60
url: /python-net/extract-text-from-stamps/
description: Learn how to use special feature of Aspose.PDF for Python via .NET - text extraction from stamp annotations
lastmod: "2025-10-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Text from Stamp Annotations

Aspose.PDF for Python library allows you to extract text from a stamp annotation (specifically a StampAnnotation) on a PDF page.

1. Open the document.
1. Access the stamp annotation from the page's annotations collection.
1. Get the appearance stream of the stamp (XForm).
1. Use a 'TextAbsorber' to extract the embedded text from that appearance.

```python

import os
import aspose.pdf as ap

def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```
