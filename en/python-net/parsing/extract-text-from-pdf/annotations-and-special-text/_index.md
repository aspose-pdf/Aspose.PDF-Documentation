---
title: Annotations and Special Text using Python
linktitle: Annotations and Special Text
type: docs
weight: 40
url: /python-net/annotation-and-special-text/
description: Learn how to extract text from stamp annotations, highlighted text, and superscript/subscript content in PDF documents using Aspose.PDF for Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extract Text from Stamp Annotations

Use [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) to extract text embedded in a [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) appearance stream. This is useful when stamp content is rendered as a form XObject rather than stored as plain text.

1. Open the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Access the target annotation from `page.annotations`.
1. Verify it is a `StampAnnotation`, then retrieve its normal appearance XForm.
1. Pass the XForm to `TextAbsorber.visit()` to extract the embedded text.

```python
import os
import aspose.pdf as ap


def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## Extract Highlighted Text

Iterate over a page's annotations and use [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) to read the text spans covered by each highlight. The page annotation collection is 1-based.

1. Open the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) and select the target page.
1. Loop through `page.annotations`.
1. Use `is_assignable` to filter for [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) instances.
1. Cast the annotation and call `get_marked_text()` to retrieve the highlighted content.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## Extract Superscript and Subscript Text

Superscripts and subscripts appear frequently in formulas, mathematical expressions, and chemical compound names. Aspose.PDF for Python via .NET supports extracting this content through [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), which detects character-level positioning metadata.

1. Open the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Create a `TextFragmentAbsorber` instance.
1. Call `document.pages[page_number].accept(absorber)` to scan the target page.
1. Retrieve the full extracted text from `absorber.text`.
1. Write the result to a file and close the document.

```python
import os
import aspose.pdf as ap


def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterate through Text Fragments to Detect Superscript/Subscript

For per-fragment inspection, iterate over `absorber.text_fragments` and read the `text_state.superscript` and `text_state.subscript` boolean flags on each [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Open the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) and create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Accept the absorber on the target page to populate `absorber.text_fragments`.
1. For each fragment, read `fragment.text`, `fragment.text_state.superscript`, and `fragment.text_state.subscript`.
1. Write the results to the output file and close the document.

```python
import os
import aspose.pdf as ap


def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
