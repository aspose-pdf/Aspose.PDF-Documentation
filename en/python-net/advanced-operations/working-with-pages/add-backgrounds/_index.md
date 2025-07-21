---
title: Add background to PDF with Python
linktitle: Add backgrounds
type: docs
weight: 20
url: /python-net/add-backgrounds/
description: Add background image to the your PDF file with Python. Use the BackgroundArtifact class.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to add background to PDF with Python
Abstract: This article discusses the use of background images in PDF documents using Aspose.PDF for Python via .NET. It highlights the ability to add watermarks or subtle designs to documents by utilizing the `BackgroundArtifact` class, which allows for the incorporation of background images into individual page objects. The article provides a practical code example that demonstrates how to implement this feature. The process involves creating a new PDF document, adding a page, creating a `BackgroundArtifact` object, setting a background image, and appending the background artifact to the page's artifacts collection. Finally, the modified document is saved as a PDF file. This technique allows for enhanced visual presentation of PDF documents.
---

Background images can be used to add a watermark, or other subtle design, to documents. In Aspose.PDF for Python via .NET, each PDF document is a collection of pages and each page contains a collection of artifacts. The [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) class can be used to add a background image to a page object.

The following code snippet shows how to add a background image to PDF pages using the BackgroundArtifact object with Python.

```python

    import aspose.pdf as ap

    # Create a new Document object
    document = ap.Document()

    # Add a new page to document object
    page = document.pages.add()

    # Create Background Artifact object
    background = ap.BackgroundArtifact()

    # Specify the image for backgroundartifact object
    background.background_image = io.FileIO(input_image_file)

    # Add backgroundartifact to artifacts collection of page
    page.artifacts.append(background)

    # Save the document
    document.save(output_pdf)
```

