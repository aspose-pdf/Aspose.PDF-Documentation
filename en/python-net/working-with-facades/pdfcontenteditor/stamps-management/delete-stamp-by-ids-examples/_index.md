---
title: Delete Stamp By ID
type: docs
weight: 85
url: /python-net/delete-stamp-by-ids-examples/
description: 
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete Rubber Stamps by Single or Multiple IDs in a PDF Using PdfContentEditor
Abstract: This example demonstrates how to remove rubber stamp annotations from a PDF based on their unique IDs using Aspose.PDF for Python via the Facades API. It covers both single-ID deletion and multiple-ID deletion.   
---

When working with PDFs containing multiple stamps, it is often necessary to remove specific stamps without affecting others. Using ID-based deletion, you can precisely control which stamps to remove:

- 'delete_stamp_by_id(stamp_id, page_number)' – deletes a single stamp by its ID on a specific page
- 'delete_stamp_by_ids(page_number, stamp_ids)' – deletes multiple stamps by their IDs on a given page

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Add two rubber stamps with distinct IDs.
1. Delete stamps using both single-ID and multiple-ID deletion methods.
1. Save the updated PDF.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def delete_stamp_by_ids_examples(infile, outfile):
	# Create PdfContentEditor object
	content_editor = pdf_facades.PdfContentEditor()
	# Bind document to PdfContentEditor
	content_editor.bind_pdf(infile)

	# Create two stamps on page 1 so they can be deleted by ID
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(120, 320, 180, 60),
		"Draft",
		"Delete by single ID",
		apd.Color.orange,
	)
	content_editor.create_rubber_stamp(
		1,
		apd.Rectangle(120, 250, 180, 60),
		"Draft",
		"Delete by multiple IDs",
		apd.Color.orange,
	)

	# Delete by single ID overload and by IDs overload
	content_editor.delete_stamp_by_id(1, 1)
	content_editor.delete_stamp_by_ids(1, [2])

	# Save updated document
	content_editor.save(outfile)
```

