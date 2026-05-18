---
title: Delete Stamp By Index
type: docs
weight: 50
url: /python-net/delete-stamp-by-index/
description: This example creates two rubber stamps on page 2. After that, a stamp can be deleted by specifying its index.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete a Rubber Stamp by Index in a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to delete a rubber stamp annotation in a PDF using its index with Aspose.PDF for Python via the Facades API. It shows how to add multiple stamps and then delete one of them based on its order on the page.
---

When multiple rubber stamps exist on a page, you can delete a specific one using its index. The delete_stamp() method allows removing annotations according to their sequence, which is useful when you don’t track stamp IDs but know their order.

1. Create a [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/) instance.
1. Bind the input PDF document.
1. Bind the input PDF file to the PdfContentEditor instance using bind_pdf(infile).
1. Call 'delete_stamp(1, [2, 3])' to remove the stamp with index 1 from pages 2 and 3.
1. Save the modified PDF document to the output file using save(outfile).

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
from io import BytesIO
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def delete_stamp_by_index(infile, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    content_editor.delete_stamp(1, [2, 3])
    # Save updated document
    content_editor.save(outfile)
```
