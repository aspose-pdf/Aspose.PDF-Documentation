---
title: Extract Images from PDF Python
linktitle: Extract Images from PDF
type: docs
weight: 20
url: /python-net/extract-images-from-the-pdf-file/
description: How to extract a part of the image from PDF using Aspose.PDF for Python
lastmod: "2023-03-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Get Images from PDF using the Aspose.PDF for Python
Abstract: This article provides a Python code snippet for extracting embedded images from a PDF document using the Aspose.PDF library. The process involves three main steps - loading the PDF document, accessing the image resource, and saving the extracted image to a file. The script imports necessary modules, including Aspose.PDF and file handling libraries, to facilitate the image extraction. The code demonstrates how to specify the input and output file paths, load a PDF document, access an image from the document's resources, and save the image to a separate file for further analysis, editing, or reuse in other documents.
---

This code snippets extracts embedded images from a PDF document for separate analysis, editing, or reuse in other documents:

1. Load the PDF Document
1. Access the Image Resource
1. Save the Image to a File

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```
