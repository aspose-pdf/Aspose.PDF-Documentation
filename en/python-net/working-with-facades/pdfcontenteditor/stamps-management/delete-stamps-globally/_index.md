---
title: Delete Stamps Globally
type: docs
weight: 60
url: /python-net/delete-stamps-globally/
description: This example demonstrates how to delete rubber stamp annotations globally across all pages in a PDF using Aspose.PDF for Python via the Facades API. It shows how to remove stamps by ID without specifying individual pages.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Rubber Stamps Globally in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to delete rubber stamp annotations globally across all pages in a PDF using Aspose.PDF for Python via the Facades API. It shows how to remove stamps by ID without specifying individual pages.    
---

When working with multiple pages, you may need to remove certain stamps throughout the entire document. The 'delete_stamp_by_id()' and 'delete_stamp_by_ids()' methods allow you to delete stamps globally by their identifiers, eliminating the need to iterate through each page manually.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Add rubber stamps to multiple pages.
1. Delete stamps globally using their IDs.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def delete_stamps_globally(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	# Add stamps across multiple pages so global deletion is meaningful
	for page in range(1, 5):
		content_editor.create_rubber_stamp(
			page,
			apd.Rectangle(120, 500, 180, 60),
			"Draft",
			"Stamp for global deletion",
			apd.Color.gray,
		)

	# delete_stamp_by_id without page number removes stamp ID from all pages
	content_editor.delete_stamp_by_id(1)
	# delete_stamp_by_ids without page number removes a list of IDs from all pages
	content_editor.delete_stamp_by_ids([2, 3])

	# Save updated document
	content_editor.save(outfile)
```