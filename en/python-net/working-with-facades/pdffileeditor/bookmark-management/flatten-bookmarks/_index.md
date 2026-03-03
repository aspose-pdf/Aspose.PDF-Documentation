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
---

```python

    from io import FileIO
    import sys
    from os import path
    import aspose.pdf as ap
    import aspose.pdf.facades as pdf_facades

    sys.path.append(path.join(path.dirname(__file__), ".."))

    from config import set_license, initialize_data_dir

    def flatten_bookmarks():
        # Initialize the data directory
        data_dir = initialize_data_dir()

        # Set the license
        set_license()

        # Open document
        with FileIO(path.join(data_dir, "input.pdf"), "r") as input_stream:
            document = ap.Document(input_stream)

            # Create PdfBookmarkEditor object
            bookmark_editor = pdf_facades.PdfBookmarkEditor(document)

            # Flatten bookmarks
            bookmark_editor.flatten_bookmarks()

            # Save output document
            with FileIO(path.join(data_dir, "output.pdf"), "w") as output_stream:
                document.save(output_stream)
```                