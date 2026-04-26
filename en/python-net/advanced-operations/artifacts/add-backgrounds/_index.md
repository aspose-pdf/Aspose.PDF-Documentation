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

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Python via .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) class can be used to add a background image to a page object.

This approach is useful when you need to place a decorative image behind the main PDF content without turning it into searchable document text.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object with Python.

```python
import aspose.pdf as ap
import io


def add_background_image(input_image_file, output_pdf):
    # Create a new PDF document
    document = ap.Document()

    # Add a blank page to the document
    page = document.pages.add()

    # Create a BackgroundArtifact object
    background = ap.BackgroundArtifact()

    # Load the image as a binary stream
    with open(input_image_file, "rb") as image_stream:
        background.background_image = image_stream

        # Add the background artifact to the page
        page.artifacts.append(background)

    # Save the resulting PDF
    document.save(output_pdf)
```

## Related Artifact Topics

- [Work with PDF artifacts in Python](/pdf/python-net/artifacts/)
- [Add watermarks to PDF in Python](/pdf/python-net/add-watermarks/)
- [Add Bates numbering to PDF in Python](/pdf/python-net/add-bates-numbering/)
- [Count artifact types in PDF files](/pdf/python-net/counting-artifacts/)

