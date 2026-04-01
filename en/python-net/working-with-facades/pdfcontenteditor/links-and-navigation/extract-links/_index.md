---
title: Extract Links
type: docs
weight: 70
url: /python-net/extract-links/
description: This example binds an input PDF, extracts all links, and prints their coordinates and URIs (if available).
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract Links from a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to extract all links from a PDF document using Aspose.PDF for Python via the Facades API. It shows how to identify and retrieve web links or other actionable links embedded in the PDF.     
---

PDF often contain interactive elements such as web links, document links, and custom actions. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can programmatically extract all link annotations from a PDF. This allows you to inspect or process links, for example, to validate URLs or analyze navigation patterns in a document.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Extract all links using 'extract_link()'.
1. Iterate through extracted links.
1. Check if a link is a LinkAnnotation and if its action is a GoToURIAction.
1. Print the rectangle coordinates and the URI.
1. Display a message if no links are found.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")                

    if count == 0:
        print("No links found")
```