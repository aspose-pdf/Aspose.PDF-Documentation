---
title: Extract Images from PDF using Python
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
AlternativeHeadline: How to Extract Images from PDF via Python
Abstract: This article provides a concise guide on extracting embedded images from a PDF document using Python. The process involves three main steps - loading the PDF document, accessing the image resource, and saving the image to a file. The code snippet utilizes the Aspose.PDF library to facilitate these operations. Initially, the PDF document is loaded from a specified path, and the desired image is accessed from the resources of the first page. Finally, the image is saved to a specified output file using a file I/O operation, allowing for further analysis, editing, or reuse in other documents.
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
