---
title: Add watermark to PDF using Python
linktitle: Add watermark
type: docs
weight: 40
url: /python-net/add-watermarks/
description: This article explains the features of working with artifacts and getting watermarks in PDFs using  programmatically the Python.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add watermark to PDF with Python
Abstract: The article discusses the use of Aspose.PDF for Python via .NET to add watermarks to PDF documents through the management of artifacts. It introduces the key classes for handling artifacts - `Artifact` and `ArtifactCollection`, and describes how to access them via the `Artifacts` property of the `Page` class. The article details the properties of the `Artifact` class, including attributes such as `contents`, `form`, `image`, `text`, `rectangle`, `rotation`, and `opacity`, which enable comprehensive manipulation of artifacts within PDF files. Additionally, a practical example is provided, demonstrating how to programmatically add a watermark to the first page of a PDF using Python. The code snippet illustrates the creation and configuration of a `WatermarkArtifact`, setting its text, alignment, rotation, and opacity, before appending it to a PDF document and saving the changes.
---

**Aspose.PDF for Python via .NET** allows adding watermarks to your PDF document using Artifacts. Please check this article to resolve your task.

In order to work with artifacts, Aspose.PDF has two classes: [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) and [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/).

In order to get all artifacts on a particular page, the [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) class has the Artifacts property. This topic explains how to work with artifact in PDF files.

## Working with Artifacts

The [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) class contains following properties:

**contents** – Gets a collection of artifact internal operators. Its supported type is System.Collections.ICollection.
**form** – Gets an artifact's XForm (if XForm is used). Watermarks, header, and footer artifacts contains XForm which shows all artifact contents.
**image** – Gets an artifact's image (if an image is presents, else null).
**text** – Gets an artifact's text.
**rectangle** – Gets an position of an artifact on the page.
**rotation** – Gets an artifact's rotation (in degrees, positive value indicates counter-clockwise rotation).
**opacity** – Gets an artifact's opacity. Possible values are in the range 0…1, where 1 is completely opaque.

## Programming Samples: How To Add Watermark On PDF Files

The following code snippet shows how to get each watermark on the first page of a PDF file with Python.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    artifact = ap.WatermarkArtifact()

    ts = ap.text.TextState()
    ts.font_size = 72
    ts.foreground_color = ap.Color.blue
    ts.font = ap.text.FontRepository.find_font("Courier")

    artifact.set_text_and_state("WATERMARK", ts)
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    artifact.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    artifact.rotation = 45
    artifact.opacity = 0.5
    artifact.is_background = True
    document.pages[1].artifacts.append(artifact)
    document.save(output_pdf)
```

