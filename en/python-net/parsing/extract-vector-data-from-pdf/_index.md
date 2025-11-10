---
title:  Extract Vector Data from a PDF file using Python
linktitle:  Extract Vector Data from PDF
type: docs
weight: 80
url: /python-net/extract-vector-data-from-pdf/
description: Aspose.PDF makes it easy to extract vector data from a PDF file. You can get the vector data (path, polygon, polyline), such as position, color, linewidth, etc.
lastmod: "2025-11-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Access to Vector Data from PDF document

The following code snippet uses the GraphicsAbsorber class to show how to extract vector graphic elements from a specific page of a PDF document and examine properties such as rectangle bounds, operators, and positions.

1. Load the PDF document using 'ap.Document'.
1. Initialize a 'GraphicsAbsorber' instance.
1. Call 'gr_absorber.visit()' to inspect the second page.
1. Retrieve the extracted elements via 'gr_absorber.elements'.
1. Iterate through each element and log properties - rectangle, position, and number of operators.
1. Write the information to a text output file.
1. Close the document to free resources.

```python

import os
import aspose.pdf as ap

def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])
        
        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## Save Vector Graphics from a Page to an SVG File

Export vector graphics from a PDF page into an SVG file, preserving vector shapes and paths:

1. Load the PDF document.
1. Access the target page().
1. Call 'page.try_save_vector_graphics()' which exports the page's vector paths into an SVG file.
1. Close the document.

```python

import os
import aspose.pdf as ap

def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### Extract Each Sub-path to a Separate SVG

Extract every sub-path (component) of vector graphics into separate SVG files by using an extraction options object.

1. Load the PDF.
1. Create 'SvgExtractionOptions' and set 'extract_every_subpath_to_svg'.
1. Access the first page of the document.
1. Instantiate 'SvgExtractor' with the options.
1. Call 'extractor.extract()' to output separate SVG files for each vector sub-path.
1. Close the document.

```python

import os
import aspose.pdf as ap

def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True
        
        page = document.pages[0]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### Extract list of elements to single image

Extract multiple vector elements from a PDF page and save them as a single combined SVG image using Aspose.PDF for Python.
This is useful when you want to preserve the visual structure of grouped shapes or drawings, such as diagrams or CAD exports.

1. Open the PDF using 'Document'.
1. Select a page and prepare a list of vector elements.
1. Use 'SvgExtractor' to combine those elements into one SVG.
1. Save the output file.

```python

import os
import aspose.pdf as ap

def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### Extract single element

Extract one specific vector element from a PDF and save it as an individual SVG file.
It is beneficial for isolating and exporting logos, icons, or standalone shapes from complex vector-based PDFs.

1. Create a 'GraphicsAbsorber' to capture vector data.
1. Visit a specific page to collect its vector elements.
1. Select a target element (e.g., an 'XFormPlacement').
1. Save that single element to an SVG file.

```python

import os
import aspose.pdf as ap

def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```