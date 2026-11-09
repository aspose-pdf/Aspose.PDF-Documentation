---
title: Extract PDF Watermark Details in Python
linktitle: Extract Watermark Details
type: docs
weight: 50
url: /python-net/extract-watermarks/
description: Read the text and bounding rectangle of watermark artifacts on the first page of a PDF in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract Watermark Details in a PDF with Python
Abstract: Read the text and bounding rectangle of watermark artifacts on the first page of a PDF in Python.
---

Read the text and bounding rectangle of watermark artifacts on the first page of a PDF in Python.

## Read watermark text and bounds

Print the text and bounding rectangle of each pagination artifact with the `WATERMARK` subtype.

```python
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## Related Artifact Topics

- [Add Watermarks](/pdf/python-net/add-watermarks/)
- [Remove Watermarks](/pdf/python-net/remove-watermarks/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
