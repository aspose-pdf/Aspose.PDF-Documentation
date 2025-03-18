---
title: Extract Images from PDF File using Python
linktitle: Extract Images
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: This section shows how to extract images from PDF file using Python library.
lastmod: "2025-02-27"
TechArticle: true 
AlternativeHeadline: How to Extract Images from PDF File using Python
Abstract: The article titled "Extract Images from PDF File with Python", published by the Aspose.PDF Doc Team, provides a guide for beginners on how to extract images from PDF files using the Aspose.PDF library for Python. This tutorial explains the process of accessing images stored in a PDF's resources collection, specifically within the XImage collection of each page. The article includes a Python code snippet demonstrating how to open a PDF document, access a specific image by its index, and save it using the `save()` method of the XImage object. The Aspose.PDF library is highlighted as a powerful tool for managing, archiving, analyzing, or sharing images extracted from PDF files. The article is aimed at simplifying the image extraction process for users, enhancing document management and accessibility.
---

Do you need to separate images from your PDF files? For simplified management, archiving, analysis, or sharing images of your documents, use **Aspose.PDF for Python** and extract images from PDF files.

Images are held in each page's [resources](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) collection's [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximagecollection/) collection. To extract a particular page, then get the image from the Images collection using the particular index of the image.

The image's index returns an [XImage](https://reference.aspose.com/pdf/python-net/aspose.pdf/ximage/) object. This object provides a [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method which can be used to save the extracted image. The following code snippet shows how to extract images from a PDF file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_file)

    # Extract a particular image
    xImage = document.pages[2].resources.images[1]
    outputImage = io.FileIO(output_image, "w")

    # Save output image
    xImage.save(outputImage)
    outputImage.close()
```

