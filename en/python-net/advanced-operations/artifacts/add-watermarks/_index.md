---
title: Adding Watermark to PDF using Python
linktitle: Adding Watermark
type: docs
weight: 30
url: /python-net/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the Python.
lastmod: "2025-11-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add watermark to PDF with Python
Abstract: The article discusses the use of Aspose.PDF for Python via .NET to add watermarks to PDF documents through the management of artifacts. It introduces the key classes for handling artifacts - `Artifact` and `ArtifactCollection`, and describes how to access them via the `Artifacts` property of the `Page` class. The article details the properties of the `Artifact` class, including attributes such as `contents`, `form`, `image`, `text`, `rectangle`, `rotation`, and `opacity`, which enable comprehensive manipulation of artifacts within PDF files. Additionally, a practical example is provided, demonstrating how to programmatically add a watermark to the first page of a PDF using Python. The code snippet illustrates the creation and configuration of a `WatermarkArtifact`, setting its text, alignment, rotation, and opacity, before appending it to a PDF document and saving the changes.
---

## Programming Samples: How To Add Watermark On PDF Files

Add a watermark artifact to a PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using Aspose.PDF for Python via .NET. A watermark is a visual overlay applied to pages for branding, security, or informational purposes. The example shows how to configure [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) appearance, positioning with [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) and [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/), rotation, and transparency before applying the watermark to a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

1. Create a watermark artifact (see [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)).
1. Configure text state (see [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)).
1. Bind text to the watermark.
1. Define positioning and style using [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) and [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/).
1. Attach watermark to a [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) via the page's [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection (see [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)).
1. Save the updated [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```

