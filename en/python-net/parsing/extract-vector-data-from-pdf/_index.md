---
title: Extract Vector Data from a PDF file using Python
linktitle: Extract Vector Data from PDF
type: docs
weight: 80
url: /python-net/extract-vector-data-from-pdf/
description: Aspose.PDF makes it easy to extract vector data from a PDF file. You can get the vector data (path, polygon, polyline), such as position, color, linewidth, etc.
lastmod: "2026-04-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Access Vector Data from a PDF Document

Use [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) to inspect vector graphic elements on a page of a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). After visiting the target page, iterate through the extracted elements to examine properties such as rectangle bounds, positions, and drawing operators.

1. Open the source PDF as a `Document`.
1. Create a `GraphicsAbsorber` instance.
1. Call `gr_absorber.visit(page)` on the target page.
1. Read the extracted items from `gr_absorber.elements`.
1. Iterate through the elements and write their properties to an output file.

```python
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
                f.write(
                    f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n"
                )
    finally:
        document.close()
```

## Save Vector Graphics from a Page to an SVG File

Export vector graphics from a PDF page to SVG to preserve scalable paths and shapes outside the original PDF. This method is useful for reusing vector artwork in web, design, or publishing workflows.

1. Load the PDF document.
1. Access the target page.
1. Call `page.try_save_vector_graphics()` to export the page's vector paths to SVG.
1. Close the document.

```python
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

When a page contains multiple independent vector paths, use [SvgExtractionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractionoptions/) with [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) to write each sub-path to a separate SVG file.

1. Load the PDF.
1. Create `SvgExtractionOptions` and set `extract_every_subpath_to_svg`.
1. Access the first page of the document.
1. Instantiate `SvgExtractor` with the options.
1. Call `extractor.extract()` to write separate SVG files for each vector sub-path.
1. Close the document.

```python
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

        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### Extract a List of Elements to a Single Image

Extract multiple vector elements from a PDF page and save them as a single combined SVG image. This is useful when you want to preserve the visual relationship between grouped shapes, diagrams, or drawing fragments.

1. Open the PDF using [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Select a page and prepare a list of vector elements.
1. Use [SvgExtractor](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/svgextractor/) to combine those elements into one SVG.
1. Save the output file.

```python
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

Extract one specific vector element from a PDF and save it as an individual SVG file. This is useful for isolating logos, icons, or standalone shapes from more complex vector-based pages.

1. Create a [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) to capture vector data.
1. Visit a specific page to collect its vector elements.
1. Select a target element, such as an [XFormPlacement](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/xformplacement/).
1. Save that single element to an SVG file.

```python
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
