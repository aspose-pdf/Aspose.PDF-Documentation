---
title: Create Rubber Stamp With Appearance Stream
type: docs
weight: 30
url: /python-net/create-rubber-stamp-with-appearance-stream/
description: This example loads a PDF, creates a rubber stamp on page 1 using an image file for its appearance, and saves the modified document. ✨
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create a Rubber Stamp with Custom Image Appearance Using PdfContentEditor in Python
Abstract: This example shows how to create a rubber stamp annotation with a custom image appearance in a PDF using Aspose.PDF for Python via the Facades API. This approach lets you apply branded or visually rich stamps such as logos, seals, or signatures.    
---

Rubber stamp annotations can be customized using an external image file. Instead of relying only on text-based stamps, you can define a visual appearance (for example, a company logo or approval badge) and place it on a page.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Define a rectangle for the stamp location.
1. Use an image file as the stamp appearance.
1. Apply text and color settings.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def create_rubber_stamp_with_appearance_file(infile, image_file, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# Create rubber stamp using appearance_file overload (image path)
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(100, 400, 200, 60),
		"Stamp with custom appearance",
		apd.Color.dark_green,
		image_file,
	)
	# Save updated document
	content_editor.save(outfile)
```    