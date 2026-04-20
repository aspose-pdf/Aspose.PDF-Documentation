---
title: Add Sound Annotation
type: docs
weight: 20
url: /python-net/add-sound-annotation/
description: This example binds an input PDF, adds a sound annotation on page 1, and saves the modified PDF.
lastmod: "2026-03-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add a Sound Annotation to a PDF Using PdfContentEditor in Python
Abstract: This example demonstrates how to embed audio into a PDF document using Aspose.PDF for Python via the Facades API. It shows how to add a clickable sound annotation that plays an audio file directly within the PDF.
---

Sound annotations in PDFs enable you to add audio content such as voice notes, music, or sound effects to your documents. Using [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/), you can define a small clickable rectangle on a page that plays a specified audio file when activated.

1. Create a PdfContentEditor instance.
1. Bind the input PDF document.
1. Define a rectangle for the sound annotation.
1. Specifie the audio file, annotation name, page number, and sampling rate.
1. Save the updated PDF document.

```python
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd
import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def add_sound_annotation(infile, sound_file, outfile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Add sound annotation to page 1
    content_editor.create_sound(
        apd.Rectangle(80, 450, 30, 30), sound_file, "Speaker", 1, "8000"
    )
    # Save updated document
    content_editor.save(outfile)
```
