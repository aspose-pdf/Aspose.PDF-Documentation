---
title: Convert Image to PDF in Python
linktitle: Convert Image to PDF file
type: docs
weight: 10
url: /python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: This topic show you how to convert Image to PDF using Aspose.PDF for Python via C++ library.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Our library demonstrates code snippets for converting the most popular image formats - JPEG. You can very easy convert a JPG images to PDF with Aspose.PDF for Python via C++ by following steps:

## Convert Image to PDF

You can very easy convert a JPG images to PDF with Aspose.PDF for C++ by following steps:

1. Open the input image file using PIL library
1. Get the width and height of the image
1. Create a new Document instance using AsposePDFPythonWrappers library
1. Set the fixed height and width of the image 
1. Add a new page to the document
1. Add the image to the page
1. Save the output PDF with 'document.save' method.

The code snippet below shows how to convert JPG Image to PDF using Python via C++:

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Set the directory path for the data files
dataDir = os.path.join(os.getcwd(), "samples")

# Set the input file path
input_file = os.path.join(dataDir, "sample.jpg")

# Set the output file path
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Open the input image file using PIL library
pil_img = Image.open(input_file)

# Get the width and height of the image
width, height = pil_img.size

# Create a new Document instance using AsposePDFPythonWrappers library
document = apw.Document()

# Create a new Image instance using AsposePDFPythonWrappers library
image = apw.Image()

# Set the file path of the image
image.file = input_file

# Set the fixed height and width of the image
image.fix_height = height
image.fix_width = width

# Add a new page to the document
page = document.pages.add()

# Add the image to the page
page.paragraphs.add(image)

# Save the document to the output file path
document.save(output_file)
```


