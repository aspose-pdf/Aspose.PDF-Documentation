---
title: Add Rubber Stamp
type: docs
weight: 10
url: /python-net/add-rubber-stamp/
description: This example binds an input PDF, adds a green “Approved” rubber stamp to the first four pages, and saves the modified document.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a Rubber Stamp Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to add a rubber stamp annotation to a PDF document using Aspose.PDF for Python via the Facades API. Rubber stamps allow you to visually mark pages with approvals, reviews, or custom labels.   
---

Rubber stamp annotations are commonly used in PDFs to indicate approval, review status, or other notes. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a rectangle for the stamp, set its text and comments, choose a color, and apply it to multiple pages of a document.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Loop through pages 1–4.
1. Add a rubber stamp annotation with custom text, comments, and color.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def add_rubber_stamp(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)
	
	for i in range(1, 5):
		content_editor.create_rubber_stamp(
			i,
			apd.Rectangle(120, 450, 180, 60),
			"Approved",
			"Approved by reviewer",
			apd.Color.green,
		)
	# Save updated document
	content_editor.save(outfile)
```