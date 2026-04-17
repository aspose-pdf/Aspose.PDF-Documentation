---
title: Region-Based Extraction using Python
linktitle: Region-Based Extraction
type: docs
weight: 20
url: /python-net/region-based-extraction/
description: Learn how to extract text from a specific page region or paragraph structure in PDF documents with Aspose.PDF for Python.
lastmod: "2026-04-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract text from a specific region of a page

Use [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) together with a [Rectangle](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) to limit extraction to a specific area of a page. This approach is useful for zone-based extraction from headers, footers, table cells, form fields, invoices, or other fixed-layout regions where the text position is known in advance.

1. Open the source PDF as a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create a `TextAbsorber` instance.
1. Configure `text_search_options` to limit extraction to a rectangle.
1. Accept the absorber on the target page.
1. Write the extracted text to an output file.

```python
import aspose.pdf as ap


def extract_text_from_region(infile, page_number, rect_coords, outfile):
    """
    Extract text from a specified rectangular region on a given page.
    Args:
        infile (str): Path to input PDF file.
        page_number (int): 1-based index of the page.
        rect_coords (tuple): (llx, lly, urx, ury) coordinates of the rectangle.
        outfile (str): Output text file path.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextAbsorber()
        # Set options to restrict search to the rectangle
        absorber.text_search_options.limit_to_page_bounds = True
        llx, lly, urx, ury = rect_coords
        absorber.text_search_options.rectangle = ap.Rectangle(llx, lly, urx, ury, True)
        # Accept on the specific page
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as tw:
            tw.write(extracted_text)
    finally:
        document.close()
```

## Extract Paragraphs by iterating through them

Use [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) when you need paragraph-aware extraction instead of plain page text. Unlike [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber/) or [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/), this API organizes output by page, section, and paragraph, which is useful for text analysis, structured export, and layout-sensitive processing.

1. Open the source PDF as a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create a `ParagraphAbsorber` instance.
1. Call `absorber.visit(document)` to analyze all pages.
1. Iterate through `page_markups`, then through each section and paragraph.
1. Read the text fragments from each paragraph and write the result to a file.

```python
import aspose.pdf as ap


def extract_paragraphs_from_pdf(infile, outfile):
    """
    Extract all paragraphs from a PDF document, and write each paragraph’s text into an output file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document)

        with open(outfile, "w", encoding="utf-8") as tw:
            for page_markup in absorber.page_markups:
                for sec_idx, section in enumerate(page_markup.sections, start=1):
                    for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                        # Concatenate all fragments/lines in the paragraph
                        parts = []
                        for line in paragraph.lines:
                            for fragment in line:
                                parts.append(fragment.text)
                            parts.append("\r\n")
                        paragraph_text = "".join(parts)
                        tw.write(
                            f"Page {page_markup.number}, Section {sec_idx}, Paragraph {para_idx}:\n"
                        )
                        tw.write(paragraph_text + "\n")
    finally:
        document.close()
```

## Extract Paragraphs with bounding polygon rendering

You can also use [ParagraphAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/paragraphabsorber/) to inspect paragraph geometry. In addition to extracting text, this approach records each section rectangle and paragraph polygon, which is useful for layout mapping, document analysis, accessibility tooling, or region-aware post-processing.

1. Open the source PDF as a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Create a `ParagraphAbsorber` instance.
1. Visit the target page.
1. Read the page markup from `absorber.page_markups`.
1. Iterate through sections and paragraphs to capture geometry and text.
1. Write the rectangle, polygon, and text data to the output file.

```python
import aspose.pdf as ap


def extract_paragraphs_with_geometry(infile, outfile):
    """
    Extract paragraphs and record geometry info (rectangle / polygon) for each paragraph in a PDF.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.ParagraphAbsorber()
        absorber.visit(document.pages[1])  # Visit page 2 (pages are 1-indexed)

        page_markup = absorber.page_markups[0]
        with open(outfile, "w", encoding="utf-8") as tw:
            for sec_idx, section in enumerate(page_markup.sections, start=1):
                tw.write(f"Section {sec_idx}: rectangle = {section.rectangle}\n")
                for para_idx, paragraph in enumerate(section.paragraphs, start=1):
                    tw.write(f"  Paragraph {para_idx}: polygon = {paragraph.points}\n")
                    # Concatenate paragraph text
                    parts = []
                    for line in paragraph.lines:
                        for fragment in line:
                            parts.append(fragment.text)
                        parts.append("\r\n")
                    tw.write("    Text: " + "".join(parts) + "\n\n")
    finally:
        document.close()
```
