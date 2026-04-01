---
title: List Stamps
type: docs
weight: 70
url: /python-net/list-stamps/
description: This example loads a PDF, retrieves all stamps from page 1, prints them, and displays a message if no stamps are found.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: List Rubber Stamp Annotations in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to retrieve and list rubber stamp annotations from a PDF document using Aspose.PDF for Python via the Facades API. It shows how to access stamps on a specific page and display their details.    
---

When working with annotated PDFs, you may need to inspect existing rubber stamps before modifying or removing them. The 'get_stamps()' method allows you to retrieve all stamps placed on a particular page. You can then iterate through the results and process them programmatically.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Retrieve all stamps from page 1.
1. Iterate through the stamp collection.
1. Print each stamp.
1. Display a message if no stamps exist.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def list_stamps(infile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	# List all stamps on page 1
	stamps = content_editor.get_stamps(1)

	count = 0
	for stamp in stamps:
		count += 1
		print(f"Stamp {count}: {stamp}")

	if count == 0:
		print("No stamps found")
```