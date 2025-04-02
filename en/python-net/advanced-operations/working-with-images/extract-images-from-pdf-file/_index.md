---
title: Extract Images from PDF File using Python
linktitle: Extract Images
type: docs
weight: 30
url: /python-net/extract-images-from-pdf-file/
description: This section shows how to extract images from PDF file using Python library.
lastmod: "2025-02-27"
TechArticle: true 
AlternativeHeadline: Get images from PDF with Python
Abstract: This article discusses the process of extracting images from PDF files using Aspose.PDF for Python. It highlights the utility of separating images for purposes such as management, archiving, analysis, or sharing. The article explains that images within a PDF are stored in each page's resources collection, specifically within the XImage collection. To extract an image, users can access a particular page and retrieve the image using its index from the Images collection. The XImage object returned by the index provides a `save()` method to save the extracted image. A code snippet is provided to demonstrate the steps required to open a PDF document, extract a specific image from the second page using its index, and save it to a file.
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

