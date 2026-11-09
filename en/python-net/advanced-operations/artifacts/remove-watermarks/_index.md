---
title: Remove PDF Watermarks in Python
linktitle: Remove Watermarks
type: docs
weight: 90
url: /python-net/remove-watermarks/
description: Remove watermark artifacts from the first page of a PDF in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Watermarks in a PDF with Python
Abstract: Remove watermark artifacts from the first page of a PDF in Python.
---

Remove watermark artifacts from the first page of a PDF in Python.

## Remove watermark artifacts

The example removes only artifacts with the `PAGINATION` type and the `WATERMARK` subtype from the first page. Visible watermarks stored as regular page text, images, or annotations remain in the PDF.

```python
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## Related Artifact Topics

- [Add Watermarks](/pdf/python-net/add-watermarks/)
- [Extract Watermark Details](/pdf/python-net/extract-watermarks/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
