---
title: Add PDF Backgrounds in Python
linktitle: Adding backgrounds
type: docs
weight: 20
url: /python-net/add-backgrounds/
description: Learn how to add a background image to PDF pages in Python using the BackgroundArtifact class in Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add background to PDF with Python
Abstract: This article discusses the use of background images in PDF documents using Aspose.PDF for Python via .NET. It highlights the ability to add watermarks or subtle designs to documents by utilizing the `BackgroundArtifact` class, which allows for the incorporation of background images into individual page objects. The article provides a practical code example that demonstrates how to implement this feature. The process involves creating a new PDF document, adding a page, creating a `BackgroundArtifact` object, setting a background image, and appending the background artifact to the page's artifacts collection. Finally, the modified document is saved as a PDF file. This technique allows for enhanced visual presentation of PDF documents.
---

## Add a Background Image to a PDF

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Python via .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) class can be used to add a background image to a page object.

This approach is useful when you need to place a decorative image behind the main PDF content without turning it into searchable document text.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object with Python.

1. Load the PDF document.
1. Create a background artifact.
1. Load the image file.
1. Attach the artifact to a page.
1. Save the updated document.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Add a Background Image with Opacity to a PDF

Add a semi-transparent background image to a PDF page using Aspose.PDF for Python.

By applying opacity, the background image becomes partially transparent, allowing the original page content (text, images, etc.) to remain clearly visible. This is especially useful for:

- Watermarks
- Branding overlays
- Subtle design enhancements

The background is added as an artifact, ensuring it stays behind all page content.

1. Load the PDF document.
1. Create a background artifact.
1. Load the image file.
1. Set the opacity level.
1. Attach the artifact to a page.
1. Save the updated document.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Add a Background Color to a PDF

Apply a solid background color to a PDF page using Aspose.PDF for Python.

1. Load the PDF document.
1. Create a background artifact.
1. Set the background color.
1. Attach the artifact to a page.
1. Save the updated document.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## Remove Background from a PDF

Remove background artifacts from a PDF page using Aspose.PDF for Python.
Backgrounds in PDFs are often stored as artifacts, and this method selectively identifies and removes only those artifacts that are classified as background elements.

1. Load the PDF document.
1. Access page artifacts.
1. Filter background artifacts.
1. Collect background elements.
1. Delete background artifacts.
1. Save the updated document.

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

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

- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
- [Add watermarks to PDF in Python](/pdf/python-net/add-watermarks/)
- [Add Bates numbering to PDF in Python](/pdf/python-net/add-bates-numbering/)
- [Count artifact types in PDF files](/pdf/python-net/counting-artifacts/)