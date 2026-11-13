---
title: Count PDF Artifacts in Python
linktitle: Counting Artifacts
type: docs
weight: 40
url: /python-net/counting-artifacts/
description: Count watermarks, backgrounds, headers, and footers by pagination artifact subtype on a PDF page in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Counting Artifacts in PDF using Python
Abstract: Count pagination artifacts on a PDF page to check for watermarks, backgrounds, headers, and footers.
---

Count pagination artifacts on a PDF page to check for watermarks, backgrounds, headers, and footers.

## Counting Artifacts of a Particular Type

Filter the first page’s `artifacts` collection by the `PAGINATION` type, then tally the subtypes. The example prints zero when a subtype is absent.

```python
from collections import Counter
import aspose.pdf as ap

def count_pdf_artifacts(infile):
    """Count and display artifacts of different types on the first page."""
    with ap.Document(infile) as document:
        pagination_artifacts = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
        ]

        subtypes = [artifact.subtype for artifact in pagination_artifacts]
        counts = Counter(subtypes)

        print(f"Watermarks: {counts.get(ap.Artifact.ArtifactSubtype.WATERMARK, 0)}")
        print(f"Backgrounds: {counts.get(ap.Artifact.ArtifactSubtype.BACKGROUND, 0)}")
        print(f"Headers: {counts.get(ap.Artifact.ArtifactSubtype.HEADER, 0)}")
        print(f"Footers: {counts.get(ap.Artifact.ArtifactSubtype.FOOTER, 0)}")
```

## Related Artifact Topics

- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
- [Extract Watermark Details](/pdf/python-net/extract-watermarks/)
- [Remove Watermarks](/pdf/python-net/remove-watermarks/)
- [Remove Backgrounds](/pdf/python-net/remove-backgrounds/)
- [Remove Headers and Footers](/pdf/python-net/remove-headers-footers/)
