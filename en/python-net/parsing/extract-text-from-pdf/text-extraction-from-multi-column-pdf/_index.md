---
title: Improving Text Extraction from Multi‑Column PDFs
linktitle: Text Extraction from Multi‑Column PDFs
type: docs
weight: 30
url: /python-net/text-extraction-from-multi-column-pdf/
description: Learn techniques for improving text extraction from multi-column PDF layouts with Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Reduce font size manually and then extract

In some multi-column layouts, reducing the font size of text fragments before extraction can improve reading order and reduce overlap issues. This technique can help with tightly formatted documents such as magazines, research papers, brochures, or reports with dense text columns.

1. Load the PDF.
1. Use [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) to collect the text fragments.
1. Reduce the font size of each fragment, then save and reopen the document.
1. Use [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) to extract the text.
1. Write the extracted text to an output file.

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
```

## Extract text with scale factor

Another option for multi-column extraction is to configure [TextExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textextractionoptions/) with a scale factor. Adjusting the scale factor can improve interpretation of tightly packed fragments and help preserve a more accurate reading order in dense layouts, tables, or column-based documents.

1. Load the PDF.
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/).
1. Configure `TextExtractionOptions.scale_factor`.
1. Assign the extraction options to the absorber.
1. Extract the page text and write the result to an output file.

```python
import aspose.pdf as ap


def extract_text_scale_factor(infile, outfile, scale_factor=0.5):
    """
    Extract text from a PDF with multi-column layout using scale factor.
    Args:
        infile (str): Input PDF path.
        outfile (str): Output text file path.
        scale_factor (float): Scale factor between 0.1 and 1.0 or 0 for auto-scaling.
    """
    doc = ap.Document(infile)
    text_absorber = ap.text.TextAbsorber()
    ext_opts = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    ext_opts.scale_factor = scale_factor
    text_absorber.extraction_options = ext_opts
    doc.pages.accept(text_absorber)
    extracted_text = text_absorber.text
    with open(outfile, "w", encoding="utf-8") as tw:
        tw.write(extracted_text)
```
