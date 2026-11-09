---
title: Remove PDF Backgrounds in Python
linktitle: Remove Backgrounds
type: docs
weight: 80
url: /python-net/remove-backgrounds/
description: Remove background artifacts from the first page of a PDF in Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Backgrounds in a PDF with Python
Abstract: Remove background artifacts from the first page of a PDF in Python.
---

Remove background artifacts from the first page of a PDF in Python.

## Remove background artifacts

Collect pagination artifacts with the `BACKGROUND` subtype before deleting them.

```python
import aspose.pdf as ap

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## Related Artifact Topics

- [Add Backgrounds](/pdf/python-net/add-backgrounds/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
