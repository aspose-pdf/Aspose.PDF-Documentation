---
title: Extract SuperScripts and SubScripts text from PDF
linktitle: Extract SuperScripts and SubScripts 
type: docs
weight: 30
url: /python-net/extract-superscripts-subscripts-from-pdf/
description: This article describes various ways to extract SuperScripts and SubScripts text from PDF using Aspose.PDF in Python. 
lastmod: "2025-11-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract SuperScripts and SubScripts Text

**SubScripts and SuperScripts** are most often used in formulas, mathematical expressions, and specifications of chemical compounds. It is tough to edit them when there can be many of them in the same passage of text.
In one of the latest releases, the **Aspose.PDF for Python via .NET** library added support for extracting SuperScripts and SubScripts text from PDF.

### Simple Text Extraction

Extract all text (including superscripts and subscripts) from a specific page of a PDF document using 'TextFragmentAbsorber'.

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

### Iterate through TextFragments to Detect Superscript/Subscript

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