---
title: Annotation and Special Text using Python
linktitle: Annotation and Special Text
type: docs
weight: 40
url: /python-net/annotation-and-special-text/
description: This section contains articles on annotation and special Text extraction from PDF documents using Aspose.PDF in Python.
lastmod: "2025-11-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract Text from Stamp Annotations

Aspose.PDF for Python library allows you to extract text from a stamp annotation (specifically a StampAnnotation) on a PDF page.

1. Open the document.
1. Access the stamp annotation from the page's annotations collection.
1. Get the appearance stream of the stamp (XForm).
1. Use a 'TextAbsorber' to extract the embedded text from that appearance.

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

## Extract SuperScripts and SubScripts Text

**SubScripts and SuperScripts** are most often used in formulas, mathematical expressions, and specifications of chemical compounds. It is tough to edit them when there can be many of them in the same passage of text.
In one of the latest releases, the **Aspose.PDF for Python via .NET** library added support for extracting SuperScripts and SubScripts text from PDF. Extract all text (including superscripts and subscripts) from a specific page of a PDF document using 'TextFragmentAbsorber'.

1. Load the PDF document.
1. Instantiate a 'TextFragmentAbsorber()', which supports detection of superscript/subscript text as per version capabilities.
1. Call 'document.pages[page_number].accept(absorber)' to scan only the given page.
1. Retrieve the extracted text via 'absorber.text'.
1. Write the text into the output file using standard file I/O.
1. Close the document to release resources.

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
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Iterate through TextFragments to Detect Superscript/Subscript

Loop through each text fragment in a page, check whether it is superscript or subscript, and process accordingly.

1. Load the PDF document.
1. Create 'TextFragmentAbsorber()' and accept it on the chosen page.
1. Access 'absorber.text_fragments', which returns a collection of fragments found on that page.
1. For each fragment:
    - Retrieve 'fragment.text'.
    - Check 'fragment.text_state.superscript' and 'fragment.text_state.subscript'.
    - Write a line to the output file with fragment text and flags.
1. Close the file and document.

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
        
        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```