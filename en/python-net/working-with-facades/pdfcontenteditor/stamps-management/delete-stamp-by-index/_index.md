---
title: Move Stamp By Index
type: docs
weight: 50
url: /python-net/move-stamp-by-index/
description: This example creates two rubber stamps on page 2. After that, a stamp can be moved by specifying its index and new coordinates.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Move a Rubber Stamp by Index in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to reposition a rubber stamp annotation in a PDF using its index with Aspose.PDF for Python via the Facades API. It shows how to add multiple stamps and then move one of them based on its order on the page.
---

When multiple rubber stamps exist on a page, you can move a specific one using its index. The move_stamp() method allows repositioning annotations according to their sequence, which is useful when you don’t track stamp IDs but know their order.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Add two rubber stamp annotations on the same page.
1. Demonstrate how to move a stamp using its index.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def move_stamp_by_index(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	content_editor.create_rubber_stamp(
		2,
		apd.Rectangle(200, 380, 180, 60),
		"Draft",
		"Draft stamp for ID-based operations",
		apd.Color.orange,
	)

	content_editor.create_rubber_stamp(
		2,
		apd.Rectangle(200, 480, 180, 60),
		"Draft",
		"Draft stamp for ID-based operations",
		apd.Color.orange,
	)
	content_editor.save(outfile)

	# Move first stamp on page 1 by index
	# content_editor.move_stamp(1, 1, 10, 10)
	# Save updated document
	content_editor.save(outfile)
```