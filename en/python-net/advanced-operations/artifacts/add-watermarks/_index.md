---
title: Add Watermarks to PDF in Python
linktitle: Adding Watermark
type: docs
weight: 30
url: /python-net/add-watermarks/
description: Learn how to add watermark artifacts to PDF files in Python using Aspose.PDF for Python via .NET.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add watermark to PDF with Python
Abstract: The article discusses the use of Aspose.PDF for Python via .NET to add watermarks to PDF documents through the management of artifacts. It introduces the key classes for handling artifacts - `Artifact` and `ArtifactCollection`, and describes how to access them via the `Artifacts` property of the `Page` class. The article details the properties of the `Artifact` class, including attributes such as `contents`, `form`, `image`, `text`, `rectangle`, `rotation`, and `opacity`, which enable comprehensive manipulation of artifacts within PDF files. Additionally, a practical example is provided, demonstrating how to programmatically add a watermark to the first page of a PDF using Python. The code snippet illustrates the creation and configuration of a `WatermarkArtifact`, setting its text, alignment, rotation, and opacity, before appending it to a PDF document and saving the changes.
---

Add a watermark artifact to a PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using Aspose.PDF for Python via .NET. A watermark is a visual overlay applied to pages for branding, security, or informational purposes. The example shows how to configure [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) appearance, positioning with [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) and [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotation, and transparency before applying the watermark to a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## Extract Watermarks from PDF

1. Load the PDF document.
1. Access page artifacts.
1. Filter watermark artifacts.
1. Collect watermark elements.
1. Extract watermark properties.
1. Output watermark information.

```python
from os import path
import sys
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

## Add a Watermark to PDF

Add a text watermark to a PDF document using Aspose.PDF for Python:

1. Load the PDF document.
1. Create a text state.
1. Create a watermark artifact.
1. Set watermark text and style.
1. Configure positioning and rotation.
1. Set opacity and background behavior.
1. Attach the watermark to a page.
1. Save the updated document.

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## Remove Watermark Artifacts from PDF Page 

Remove watermark artifacts from a specific page in a PDF document using the Aspose.PDF for Python API. The approach targets watermark elements stored as page artifacts (specifically those classified as pagination watermark subtypes), iterates through them, and deletes them before saving the updated document.

1. Load the PDF document.
1. Access page artifacts.
1. Filter watermark artifacts.
1. Delete watermark artifacts.
1. Save the updated document.

```python
from os import path
import sys
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

- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
- [Add PDF backgrounds in Python](/pdf/python-net/add-backgrounds/)
- [Add Bates numbering to PDF in Python](/pdf/python-net/add-bates-numbering/)
- [Count artifact types in PDF files](/pdf/python-net/counting-artifacts/)