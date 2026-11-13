---
title: Add PDF Backgrounds in Python
linktitle: Add Backgrounds
type: docs
weight: 20
url: /python-net/add-backgrounds/
description: Add image and solid-color backgrounds to PDF pages in Python and adjust background image opacity.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Backgrounds in a PDF with Python
Abstract: Add image and solid-color backgrounds to PDF pages in Python and adjust background image opacity.
---

Use `BackgroundArtifact` to place an image or solid color behind the content of a PDF page. These examples modify the first page.

## Add a Background Image to a PDF

Set `background_image` from an image stream and append the artifact to the page.

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Add a Background Image with Opacity to a PDF

Pass an opacity between 0 and 1 to the same function. Use `0.5` for a semi-transparent image.

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## Add a Background Color to a PDF

Set `background_color` on the artifact to apply a solid color.

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Related Artifact Topics

- [Remove Backgrounds](/pdf/python-net/remove-backgrounds/)
- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
