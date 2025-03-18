---
title: Add background to PDF with Python
linktitle: Add backgrounds
type: docs
weight: 20
url: /python-net/add-backgrounds/
description: Add background image to the your PDF file with Python. Use the BackgroundArtifact class.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add background to PDF with Python
Abstract: The article titled "Add background to PDF with Python" provides a guide for beginners on how to add background images to PDF files using the Aspose.PDF library for Python via .NET. It explains that background images can serve as watermarks or subtle design elements in documents. The article details the process of utilizing the `BackgroundArtifact` class to add a background image to PDF pages. It includes a concise code snippet demonstrating how to create a new document, add pages, and apply a background image using the Aspose.PDF library. The publisher of the article, Aspose.PDF, offers this software library for manipulating PDF documents across different operating systems, including Windows, MacOS, and Linux. The article emphasizes the practical application of the Aspose.PDF library in enhancing PDF document aesthetics and provides contact information for further inquiries.
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

