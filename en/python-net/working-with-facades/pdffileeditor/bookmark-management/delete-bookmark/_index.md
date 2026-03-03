---
title: 
type: docs
weight: 100
url: /python-net//
description: 
lastmod: "2026-02-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline:
Abstract:      
---

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def delete_bookmark():
        # Initialize the data directory
        data_dir = initialize_data_dir()

        # Set the license
        set_license()

        # Open document
        with FileIO(path.join(data_dir, "input.pdf"), "r") as input_stream:
            document = ap.Document(input_stream)

            # Create PdfBookmarkEditor object
            bookmark_editor = pdf_facades.PdfBookmarkEditor()

            # Bind the PDF document to PdfBookmarkEditor
            bookmark_editor.bind_pdf(document)

            # Delete bookmark by title
            bookmark_editor.delete_bookmark("Bookmark Title")

            # Save updated PDF document
            bookmark_editor.save(path.join(data_dir, "output.pdf"))
```
