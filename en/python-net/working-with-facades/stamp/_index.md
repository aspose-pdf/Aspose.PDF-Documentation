---
title: Add PDF Stamps in Python
type: docs
weight: 150
url: /python-net/stamp-class/
description: Learn how to add image, PDF, and text stamps to PDF files in Python with Aspose.PDF for Python via .NET using the Stamp class.
lastmod: "2026-04-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Work with image, text, and PDF page stamps in Python
Abstract: This article explains how to use the Stamp class in Aspose.PDF for Python via .NET to apply reusable image, text, and PDF-based stamps to PDF documents. Learn how to position stamps, style text-based stamps, apply stamps to selected pages, and create background watermark-style effects.
---

Aspose.PDF for Python via .NET provides the [Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) class for placing reusable visual content on PDF pages. A stamp can be based on text, an image, or even a page from another PDF, and it can be positioned, rotated, styled, and limited to specific pages.

Use `Stamp` when you need to define the visual content and placement of a reusable stamp. In typical workflows, you create and configure a `Stamp` object first, then apply it to a document with [PdfFileStamp](/pdf/python-net/pdffilestamp-class/) or navigate back to the broader [PDF Facades overview](/pdf/python-net/working-with-facades/) for related facade classes.

This article demonstrates several common stamp workflows:

1. Create reusable text resources for text-based stamps.
1. Add image and PDF-page stamps.
1. Add styled text stamps.
1. Limit a stamp to selected pages.
1. Configure a background image stamp.

The example uses two helper functions: one creates formatted text for text-based stamps, and the other creates a `TextState` object used to style text stamps.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def _create_text_logo(text: str) -> pdf_facades.FormattedText:
    """Create formatted text for text stamp examples."""
    return pdf_facades.FormattedText(
        text,
        drawing.Color.blue,
        drawing.Color.light_gray,
        pdf_facades.FontStyle.HELVETICA_BOLD,
        pdf_facades.EncodingType.WINANSI,
        True,
        14,
    )


def _create_text_state() -> ap.text.TextState:
    """Create a text state used to style text stamps."""
    text_state = ap.text.TextState()
    text_state.foreground_color = ap.Color.dark_blue
    text_state.font_size = 16
    text_state.font_style = ap.text.FontStyles.BOLD
    return text_state
```

## Add an image stamp

Use `bind_image()` when the stamp should display an image such as a logo, badge, or icon. After binding the image, you can set the stamp ID and origin before adding it to the document.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp to the PDF."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.stamp_id = 1
        stamp.set_origin(36, 520)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add a PDF page as a stamp

Use `bind_pdf()` when you want to use a page from another PDF file as the stamp content. This is useful for overlays such as approvals, templates, or prebuilt visual elements stored in a separate document.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_pdf_page_as_stamp(infile: str, stamp_pdf: str, outfile: str) -> None:
    """Add the first page of another PDF as a stamp."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_pdf(stamp_pdf, 1)
        stamp.page_number = 1
        stamp.set_origin(36, 250)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add a text stamp with text state

Use `bind_logo()` together with `bind_text_state()` when you want to create a text-based stamp with custom font styling. This approach is useful for approval marks, labels, and workflow-specific annotations.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_text_stamp_with_text_state(infile: str, outfile: str) -> None:
    """Add a text stamp and style it with a TextState object."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_logo(_create_text_logo("Approved by signing workflow"))
        stamp.bind_text_state(_create_text_state())
        stamp.set_origin(36, 700)
        stamp.rotation = 15.0

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add a stamp to specific pages

If the stamp should not appear on every page, assign the target page numbers to the `pages` property. This example adds an image stamp only to the first page.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_stamp_to_specific_pages(infile: str, image_file: str, outfile: str) -> None:
    """Add an image stamp only to the selected pages."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.pages = [1]
        stamp.set_origin(400, 40)
        stamp.set_image_size(120, 60)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Add a background image stamp

Use a background stamp when the image should appear behind the page content. You can also control the stamp opacity, rotation, quality, size, and position to create watermark-style effects.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as drawing

from config import initialize_data_dir, set_license


def add_background_image_stamp(infile: str, image_file: str, outfile: str) -> None:
    """Add a rotated background image stamp with opacity and quality settings."""
    pdf_stamper = pdf_facades.PdfFileStamp()
    try:
        pdf_stamper.bind_pdf(infile)

        stamp = pdf_facades.Stamp()
        stamp.bind_image(image_file)
        stamp.is_background = True
        stamp.opacity = 0.35
        stamp.quality = 90
        stamp.rotation = 45.0
        stamp.set_image_size(160, 80)
        stamp.set_origin(200, 300)

        pdf_stamper.add_stamp(stamp)
        pdf_stamper.save(outfile)
    finally:
        pdf_stamper.close()
```

## Related Facades Topics

- [Working with PDF Facades in Python](/pdf/python-net/working-with-facades/)
- [Add headers, footers, and stamps with PdfFileStamp](/pdf/python-net/pdffilestamp-class/)
- [Add a page stamp to PDF files in Python](/pdf/python-net/add-stamp/)
