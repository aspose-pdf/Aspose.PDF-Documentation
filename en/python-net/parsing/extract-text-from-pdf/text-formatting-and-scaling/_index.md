---
title: Text Formatting and Scaling using Python
linktitle: Text Formatting and Scaling
type: docs
weight: 30
url: /python-net/text-formatting-and-scaling/
description: This section contains articles on Text formatting and scaling using Aspose.PDF in Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Reduce font size manually and then extract

Extraction accuracy in multi-column PDFs is achieved by first reducing the font size of all text fragments before extraction. The process helps prevent overlapping text issues that can occur in tightly formatted or multi-column layouts.
It helps for extracting text from complex layouts—such as magazines, academic papers, or brochures—where resizing text improves layout clarity and extraction results.

1. Load the PDF.
1. Reduce font size of existing text fragments, save and reopen document.
1. Use 'TextAbsorber' to extract text from pages.
1. Write out the extracted text.

```python

import io
import aspose.pdf as ap

def extract_text_reduce_font(infile, outfile, reduce_ratio=0.7):
    """
    Extract text from a multi-column PDF by first reducing font size of all text fragments.
    Args:
        infile (str): Path to input PDF.
        outfile (str): Output text file.
        reduce_ratio (float): Ratio to reduce font size (e.g., 0.7 = 70%).
    """
    doc = ap.Document(infile)
    try:
        frag_absorber = ap.text.TextFragmentAbsorber()
        doc.pages.accept(frag_absorber)
        for frag in frag_absorber.text_fragments:
            frag.text_state.font_size = frag.text_state.font_size * reduce_ratio
        # Save to memory stream and reopen (to apply changes)
        ms = io.BytesIO()
        doc.save(ms)
        ms.seek(0)
        doc2 = ap.Document(ms)
        text_absorber = ap.text.TextAbsorber()
        doc2.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```

## Extract text with scale factor

Extract text from PDFs with multi-column layouts by applying a scale factor to the document. Adjusting the scale factor ensures that the text fragments are interpreted correctly, reducing overlap or misalignment during extraction.
It's useful for PDFs with columns, tables, or dense layouts, where scaling helps maintain proper reading order and structure in the extracted text.

1. Load the PDF.
1. Configure 'TextExtractionOptions.ScaleFactor'.
1. Use 'TextAbsorber' to extract text from pages.
1. Write out the extracted text.

```python

import aspose.pdf as ap

def extract_text_with_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    try:
        text_absorber = ap.text.TextAbsorber()
        ext_opts = ap.text.TextExtractionOptions(ap.text.TextExtractionOptions.TextFormattingMode.PURE)
        ext_opts.scale_factor = scale_factor
        text_absorber.extraction_options = ext_opts
        doc.pages.accept(text_absorber)
        extracted_text = text_absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        doc.close()
```