---
title: Add Movie Annotation
type: docs
weight: 10
url: /python-net/add-movie-annotation/
description: This example binds an input PDF, adds a movie annotation on page 1, and saves the updated PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a Movie Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to embed a movie (video) into a PDF document using Aspose.PDF for Python via the Facades API. It shows how to add a clickable annotation that plays a video directly within the PDF.
---

Movie annotations in PDFs allow you to embed multimedia content, such as videos, into your documents. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a rectangle on a page where the video will appear. When clicked, the video can be played directly from the PDF, making your documents more interactive and engaging.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the movie annotation.
1. Specifie the video file to embed.
1. Assign the page number for the annotation.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_movie_annotation(infile, movie_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add movie annotation to page 1
    content_editor.create_movie(apd.Rectangle(80, 500, 220, 120), movie_file, 1)
    # Save updated document
    content_editor.save(outfile)
```
