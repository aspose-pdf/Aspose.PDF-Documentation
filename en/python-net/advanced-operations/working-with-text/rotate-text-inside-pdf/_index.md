---
title: Rotate Text Inside PDF using Python
linktitle: Rotate Text Inside PDF
type: docs
weight: 50
url: /python-net/rotate-text-inside-pdf/
description: Explore how to rotate text inside a PDF document in Python for flexible document formatting with Aspose.PDF for Python.
lastmod: "2025-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to rotate Text in PDF with Python
Abstract: The article provides a detailed guide on how to rotate text within a PDF document using the Aspose.PDF library for Python via .NET. It describes the utilization of the `Rotation` property of the `TextFragment` class to achieve text rotation at various angles, which is useful in multiple document generation scenarios. Demonstrates creating text fragments with specified rotation angles and adding them to a PDF page using a `TextBuilder'. Illustrates how to append rotated text fragments to a `TextParagraph` and then add the paragraph to a PDF page. Shows how to add rotated text fragments directly to the page's paragraph collection.Explains rotating an entire paragraph with multiple text fragments.
---

Rotate text fragments in a PDF document using Aspose.PDF for Python via .NET. It shows how to precisely control the position and rotation of individual text elements by combining the 'TextFragment', 'TextState', and 'TextBuilder' classes. By adjusting the rotation angle for each text fragment, you can create visually dynamic layouts, such as diagonal headers, vertical labels, or rotated annotations.

## Rotate Text Fragments Using TextBuilder in PDF

Creates a PDF file named rotated_fragments.pdf containing three text fragments aligned horizontally:

 - the first text is unrotated
 - the second is rotated 45°
 - the third is rotated 90°

1. Create a New PDF Document.
1. Insert a new page to host the rotated text.
1. Create the First Text Fragment - No Rotation.
1. Create the Second Text Fragment - 45° Rotation.
1. Create the Third Text Fragment - 90° Rotation.
1. Add Text Fragments Using TextBuilder.
1. Save the Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_1(outfile):
    """
    Implement text rotation using TextFragment and TextBuilder.

    Demonstrates basic text rotation techniques by creating multiple text
    fragments with different rotation angles. Shows how to position and
    rotate individual text elements using TextBuilder for precise control.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text fragments.

    Note:
        - Creates three text fragments with 0°, 45°, and 90° rotations
        - Uses Position class for precise text placement
        - Applies TimesNewRoman font with 12pt size
        - TextBuilder provides low-level control over text placement
        - Demonstrates individual fragment rotation capabilities

    Example:
        >>> rotate_text_inside_pdf_1("rotated_fragments.pdf")
        # Creates a PDF with text fragments at different rotation angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment_3.text_state.rotation = 90
        # create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment_1)
        builder.append_text(text_fragment_2)
        builder.append_text(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotate Individual Text Fragments Inside a Paragraph in PDF

Rotate individual text fragments within a paragraph. It shows how to build a multi-line paragraph (TextParagraph) containing multiple fragments (TextFragment), each with its own rotation angle. This technique is useful for creating visually rich documents that combine horizontally and diagonally oriented text — for example, stylized headers, diagrams, or annotated labels.

Creates a PDF named rotated_paragraph_fragments.pdf containing a paragraph with three lines of text, each line rotated differently:

 - the first line is rotated 45°
 - the second line remains horizontal (0°)
 - the third line is rotated -45°

1. Create a New PDF Document.
1. Add a blank page where the rotated text will appear.
1. Create a TextParagraph.
1. Create and Configure the First Text Fragment - 45° Rotation.
1. Create the Second Text Fragment - No Rotation.
1. Create the Third Text Fragment - 45° Rotation.
1. Append Text Fragments to the Paragraph.
1. Add the Paragraph to the Page Using TextBuilder.
1. Save the Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_2(outfile):
    """
    Implement text rotation using TextParagraph and TextBuilder with rotated fragments.

    Demonstrates how to create multi-line paragraphs containing individually
    rotated text fragments. Shows the combination of paragraph structure
    with fragment-level rotation control.

    Args:
        outfile (str): Path where the PDF with rotated paragraph fragments will be saved.

    Returns:
        None: The function creates and saves a PDF file with a paragraph containing rotated fragments.

    Note:
        - Creates a TextParagraph containing multiple text fragments
        - Individual fragments have different rotations: 45°, 0°, and -45°
        - Uses append_line to structure fragments within the paragraph
        - Demonstrates mixed rotation within a single paragraph
        - TextBuilder handles paragraph-level placement and rendering

    Example:
        >>> rotate_text_inside_pdf_2("rotated_paragraph_fragments.pdf")
        # Creates a PDF with a paragraph containing individually rotated text fragments
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        paragraph = ap.text.TextParagraph()
        paragraph.position = ap.text.Position(200, 600)
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = -45
        # Append the text fragments to the paragraph
        paragraph.append_line(text_fragment_1)
        paragraph.append_line(text_fragment_2)
        paragraph.append_line(text_fragment_3)
        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Append the text paragraph to the PDF page
        text_builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```

## Rotate Text Using Page Paragraphs in PDF

Simplified method for rotating text within a PDF using Aspose.PDF for Python via .NET.
Unlike lower-level approaches with TextBuilder or TextParagraph, this method adds rotated text fragments directly to the page’s paragraph collection (page.paragraphs). It's ideal for cases where you need basic text rotation but don’t require precise positioning or paragraph structuring. This approach simplifies layout creation, automatically handling text placement on the page while still allowing for individual text rotation control.

Generates a file named 'simple_rotated_text.pdf' containing:

 - a main horizontal text fragment 0° rotation
 - 315° rotated fragment
 - 270° rotated fragment

1. Initialize a new PDF document.
1. Create a page where the rotated text will be placed.
1. Create the First Text Fragment - No Rotation.
1. Create the Second Text Fragment - 315° Rotation.
1. Create the Third Text Fragment - 270° Rotation.
1. Add Text Fragments Directly to Page Paragraphs.
1. Save the PDF Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_3(outfile):
    """
    Implement text rotation using TextFragment and Page.Paragraphs.

    Demonstrates a simplified approach to text rotation by adding rotated
    text fragments directly to the page's paragraph collection. Shows
    high-level text placement without TextBuilder complexity.

    Args:
        outfile (str): Path where the PDF with rotated text will be saved.

    Returns:
        None: The function creates and saves a PDF file with rotated text using page paragraphs.

    Note:
        - Uses Page.Paragraphs for direct text fragment addition
        - Creates fragments with 0°, 315°, and 270° rotations
        - Simpler approach compared to TextBuilder method
        - Demonstrates automatic layout with rotated text elements
        - Good for basic rotation without precise positioning needs

    Example:
        >>> rotate_text_inside_pdf_3("simple_rotated_text.pdf")
        # Creates a PDF with rotated text using the simplified page paragraphs approach
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotate Entire Paragraphs in a PDF

Our library shows advanced paragraph-level text rotation in a PDF. Unlike fragment-level rotation (where each text piece is rotated individually), this method rotates entire paragraphs as unified blocks at different angles.
Each paragraph contains multiple styled text fragments, and the full paragraph is rotated at specific angles — allowing for complex, consistent layout transformations.
This is ideal for artistic layouts, watermarks, or design-heavy PDFs where entire text sections need to be oriented in various directions.

Creates 'rotated_paragraphs.pdf', containing four fully styled and rotated paragraphs:

 - each rotated at a unique angle (45°, 135°, 225°, and 315°)
 - each paragraph has three lines of text with colored backgrounds, underlining, and consistent styling

1. Create a New PDF Document.
1. Add a blank page to hold the rotated paragraphs.
1. Iterate to Create Multiple Paragraphs.
1. Create and Position the Paragraph.
1. Create Text Fragments with Formatting.
1. Apply Text Formatting.
1. Add Text Fragments to the Paragraph.
1. Append Paragraph to the Page Using TextBuilder.
1. Repeat for All Four Rotations.
1. Save the PDF Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def rotate_text_inside_pdf_4(outfile):
    """
    Implement whole paragraph rotation using TextParagraph and TextBuilder.

    Demonstrates advanced text rotation by rotating entire paragraphs at
    different angles. Creates multiple styled paragraphs with comprehensive
    formatting and rotates each paragraph as a complete unit.

    Args:
        outfile (str): Path where the PDF with rotated paragraphs will be saved.

    Returns:
        None: The function creates and saves a PDF file with fully rotated paragraphs.

    Note:
        - Creates 4 paragraphs rotated at 45°, 135°, 225°, and 315°
        - Each paragraph contains multiple formatted text fragments
        - Applies comprehensive styling: colors, backgrounds, underlines
        - Demonstrates paragraph-level rotation vs. fragment-level rotation
        - Shows complex multi-line content with consistent rotation
        - Uses loop to create systematic rotation pattern

    Example:
        >>> rotate_text_inside_pdf_4("rotated_paragraphs.pdf")
        # Creates a PDF with complete paragraphs rotated at different angles
    """

    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        for i in range(4):
            paragraph = ap.text.TextParagraph()
            paragraph.position = ap.text.Position(200, 600)
            # Specify rotation
            paragraph.rotation = i * 90 + 45
            # Create text fragment
            text_fragment_1 = ap.text.TextFragment("Paragraph Text")
            # Create text fragment
            text_fragment_1.text_state.font_size = 12
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
            text_fragment_3.text_state.background_color = ap.Color.light_gray
            text_fragment_3.text_state.foreground_color = ap.Color.blue
            text_fragment_3.text_state.underline = True
            paragraph.append_line(text_fragment_1)
            paragraph.append_line(text_fragment_2)
            paragraph.append_line(text_fragment_3)
            # Create TextBuilder object
            builder = ap.text.TextBuilder(page)
            # Append the text fragment to the PDF page
            builder.append_paragraph(paragraph)

        # Save the document
        document.save(outfile)
```