---
title: Search and Extract PDF Text in Python
linktitle: Search and Get Text
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: Learn how to search, inspect, and extract text from PDF documents in Python.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Search and Get Text from Pages in PDF
Abstract: The article provides an in-depth exploration of text extraction and manipulation capabilities within PDF documents using the Aspose.PDF for Python via .NET library. It introduces the TextFragmentAbsorber class, which allows developers to search through an entire document or specific pages for designated phrases or regular expression patterns. The page outlines various practical scenarios—such as retrieving text content, determining its position (including coordinates and indent values), and extracting font properties like name, size, embed status, and color—from the matched text fragments. Detailed code examples demonstrate the process step-by-step, making it easier for developers to integrate text searching capabilities into their applications.
---

## Search Text from PDF

Search and extract text from a defined rectangular area in a PDF document using the TextAbsorber class. It employs pure text formatting mode for clean, unformatted text output, making it ideal for extracting content from structured regions like headers, footers, or table areas. By combining TextExtractionOptions and TextSearchOptions with rectangular constraints, this example gives you fine control over where and how text is extracted from the document.

Use this page when you need to audit PDF text content, extract text for analysis, or inspect positions and formatting of matched text fragments.

1. Load the PDF file using 'ap.Document'.
1. Configure Text Extraction Options.
1. Define Search Area with Rectangle Constraints.
1. Create and Configure TextAbsorber.
1. Process All Pages in the Document.
1. Retrieve and Display Extracted Text.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Search Text from a Specific PDF page

Search and extract text from a specific page and region in a PDF using Aspose.PDF’s TextAbsorber. It targets page 2 of the document and extracts only the text found within a defined rectangular area.
By combining TextExtractionOptions (for formatting control) and TextSearchOptions (for area limitation), you can perform precise, page-specific text extraction efficiently.

1. Load the PDF Document.
1. Set Up Text Extraction Options.
1. Restrict text extraction to a specific rectangular area on the page.
1. Create and Configure TextAbsorber.
1. Process a Specific Page.
1. Retrieve and Display Extracted Text.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## Analyze and Extract Detailed Text Fragment Properties from a PDF

Unlike TextAbsorber, which extracts raw text, TextFragmentAbsorber provides detailed, low-level information about each text fragment—such as its position, font attributes, color, and embedding details.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber.
1. Process All Pages in the Document.
1. Iterate Through Extracted Text Fragments.
1. Print Basic Text Information.
1. Print Font and Formatting Details.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## Search for a Specific Text Phrase on a Single PDF Page

Search for a specific text phrase within a page of a PDF document using TextFragmentAbsorber. Unlike searching the entire document, this approach limits the search to just one page, making it more efficient for confirming the presence and location of text in targeted areas like headers, footers, or specific content sections.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber with Search Phrase.
1. Apply Absorber to Specific Page.
1. Iterate Over Found Fragments.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Sequential Page-by-Page Text Search with Cumulative Results

Search text incrementally across multiple pages of a PDF document using Aspose.PDF’s TextFragmentAbsorber.
Unlike a single-page or document-wide search, this approach allows you to process pages sequentially, collect results progressively, and analyze text fragments with page-specific context. This method is ideal for large documents or progressive processing workflows.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber and Set Search Phrase.
1. Process First Page. Search only page 1. Prints text, page number, and position. Provide isolated page-specific results for clarity.
1. Process Next Page Sequentially. Move to page 2 and optionally continue through the rest of the document. The 'absorber.visit()' ensures the accumulation of results from all visited pages. Prints the cumulative search results, showing both text and location.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## Targeted Phrase Search within a Rectangular Area

Search for a specific phrase within a PDF while constraining the search to a specific rectangular area on a single page.
By combining phrase search with spatial constraints, you can locate content precisely in designated regions without scanning the entire page or document. This is particularly useful for forms, headers, footers, or structured reports where content appears in predictable locations.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber with Phrase and Rectangular Constraints
1. Apply Absorber to Page 2. Restricts processing to page 2, reducing unnecessary computation. Ensures search is page-specific.
1. Iterate Through Found Fragments and Print

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Text Pattern Search in PDF Using Regular Expressions

Search for text patterns in a PDF using regular expressions. By enabling regex mode in TextFragmentAbsorber, you can locate complex patterns such as numbers, dates, prices, coordinates, or custom text formats. The function limits the search to a specific page, making it efficient for targeted extraction of structured data.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber with Regex Pattern.
1. Apply Absorber to Page 2. Limits search to page 2 for efficiency and precision. Only text on this page is analyzed.
1. Iterate Through Found Fragments. Prints matching text fragments and their coordinates. Provides precise location information for extracted patterns.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## Convert Text Matches to Hyperlinks in PDF Using TextFragmentAbsorber

Search for specific text phrases in a PDF and convert them into clickable hyperlinks. Using TextFragmentAbsorber with regex patterns, it locates target words and applies visual styling (color and underline) along with interactive links.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber with Regex Pattern.
1. Apply Absorber to Page 1.
1. Style and Add Hyperlinks to Matches.
1. Save Modified PDF.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## Search and Identify Styled Text in PDF Using TextFragmentAbsorber

Search for text fragments in a PDF based on their formatting properties rather than their content. Using TextFragmentAbsorber, it identifies text with specific styles, such as bold text.

1. Load the PDF Document.
1. Initialize TextFragmentAbsorber.
1. Apply Absorber to Page 1.
1. Inspect Text Fragments Based on Formatting. Checks font style for bold formatting.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## Visual Text Highlighting in PDF Pages

This function combines text recognition and rendering into a single workflow. It not only extracts text but also visualizes it by highlighting fragments, segments, and characters in color-coded rectangles on PNG images of each page.

Our example performs advanced text visualization on a PDF by:

- searching for all visible text fragments using regular expressions
- rendering each PDF page into a high-resolution PNG image
- drawing colored rectangles around text fragments, text segments, and individual characters

1. Set Output Image Resolution. Each PDF page is converted into a 150 DPI PNG image.
1. Open the PDF and Initialize Text Absorber.
1. Process Each Page. Apply the absorber to every page. Collect all detected text fragments and their geometrical positions.
1. Convert Page to PNG Stream.
1. Prepare Graphics Object for Drawing.
1. Apply Coordinate Transformation. Convert PDF coordinates to image pixels.
1. Draw Rectangles for Text Elements.
1. Save the Result.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## Related Text Topics

- [Work with text in PDF using Python](/pdf/python-net/working-with-text/)
- [Replace text in PDF via Python](/pdf/python-net/replace-text-in-pdf/)
- [Add tooltips to PDF text in Python](/pdf/python-net/pdf-tooltip/)
- [Adding text to PDF](/pdf/python-net/add-text-to-pdf-file/)