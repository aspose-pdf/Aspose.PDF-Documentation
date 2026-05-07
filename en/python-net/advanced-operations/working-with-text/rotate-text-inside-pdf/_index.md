---
title: Rotate PDF Text in Python
linktitle: Rotate Text Inside PDF
type: docs
weight: 50
url: /python-net/rotate-text-inside-pdf/
description: Learn how to rotate text fragments and paragraphs inside PDF documents in Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotate text fragments and paragraphs in PDF documents with Python
Abstract: This article explains how to rotate text in PDF documents using Aspose.PDF for Python via .NET. It shows how to set the `rotation` property on `TextFragment`, build rotated content with `TextBuilder` and `TextParagraph`, and add rotated text directly to page paragraphs for different layout scenarios.
---

Rotate text fragments in a PDF document using Aspose.PDF for Python via .NET. This page shows how to control the position and rotation of text by using `TextFragment`, `TextState`, and `TextBuilder`. By adjusting rotation angles, you can create layouts such as diagonal headers, vertical labels, and rotated annotations.

## Rotate Text Fragments Using TextBuilder in PDF

Creates a PDF file named `rotated_fragments.pdf` containing three text fragments aligned horizontally:

- the first text is unrotated
- the second is rotated 45°
- the third is rotated 90°

1. Create a new PDF document.
1. Insert a new page to host the rotated text.
1. Create the first text fragment (no rotation).
1. Create the second text fragment (45° rotation).
1. Create the third text fragment (90° rotation).
1. Add text fragments using `TextBuilder`.
1. Save the document.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_1(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        text_fragment_1.position = ap.text.Position(100, 600)
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create rotated text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        text_fragment_2.position = ap.text.Position(200, 600)
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        text_fragment_2.text_state.rotation = 45
        # Create rotated text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        text_fragment_3.position = ap.text.Position(300, 600)
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

Creates a PDF named `rotated_paragraph_fragments.pdf` containing a paragraph with three lines of text, each line rotated differently:

- the first line is rotated 45°
- the second line remains horizontal (0°)
- the third line is rotated -45°

1. Create a new PDF document.
1. Add a blank page where the rotated text will appear.
1. Create a `TextParagraph`.
1. Create and configure the first text fragment (+45° rotation).
1. Create the second text fragment (no rotation).
1. Create the third text fragment (-45° rotation).
1. Append text fragments to the paragraph.
1. Add the paragraph to the page using `TextBuilder`.
1. Save the document.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_2(outfile):
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
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_1.text_state.rotation = 45
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("another rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
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

This section demonstrates a simplified method for rotating text within a PDF using Aspose.PDF for Python via .NET.
Unlike lower-level approaches with `TextBuilder` or `TextParagraph`, this method adds rotated text fragments directly to the page’s paragraph collection (`page.paragraphs`). It is ideal when you need basic text rotation but do not require precise positioning or paragraph structuring.

Generates a file named `simple_rotated_text.pdf` containing:

- a main horizontal text fragment 0° rotation
- 315° rotated fragment
- 270° rotated fragment

1. Initialize a new PDF document.
1. Create a page where the rotated text will be placed.
1. Create the first text fragment (no rotation).
1. Create the second text fragment (315° rotation).
1. Create the third text fragment (270° rotation).
1. Add text fragments directly to page paragraphs.
1. Save the PDF document.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_3(outfile):
    # Create PDF document
    with ap.Document() as document:
        # Get particular page
        page = document.pages.add()
        # Create text fragment
        text_fragment_1 = ap.text.TextFragment("main text")
        # Set text properties
        text_fragment_1.text_state.font_size = 12
        text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Create text fragment
        text_fragment_2 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_2.text_state.font_size = 12
        text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_2.text_state.rotation = 315
        # Create text fragment
        text_fragment_3 = ap.text.TextFragment("rotated text")
        # Set text properties
        text_fragment_3.text_state.font_size = 12
        text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )
        # Set rotation
        text_fragment_3.text_state.rotation = 270
        page.paragraphs.add(text_fragment_1)
        page.paragraphs.add(text_fragment_2)
        page.paragraphs.add(text_fragment_3)

        # Save the document
        document.save(outfile)
```

## Rotate Entire Paragraphs in a PDF

This example demonstrates advanced paragraph-level text rotation in a PDF. Unlike fragment-level rotation (where each text piece is rotated individually), this method rotates entire paragraphs as unified blocks at different angles.
Each paragraph contains multiple styled text fragments, and the full paragraph is rotated at specific angles — allowing for complex, consistent layout transformations.
This is ideal for artistic layouts, watermarks, or design-heavy PDFs where entire text sections need to be oriented in various directions.

Creates `rotated_paragraphs.pdf`, containing four fully styled and rotated paragraphs:

- each rotated at a unique angle (45°, 135°, 225°, and 315°)
- each paragraph has three lines of text with colored backgrounds, underlining, and consistent styling

1. Create a new PDF document.
1. Add a blank page to hold the rotated paragraphs.
1. Iterate to create multiple paragraphs.
1. Create and position the paragraph.
1. Create text fragments with formatting.
1. Apply text formatting.
1. Add text fragments to the paragraph.
1. Append the paragraph to the page using `TextBuilder`.
1. Repeat for all four rotations.
1. Save the PDF document.

```python
import aspose.pdf as ap

def rotate_text_inside_pdf_4(outfile):
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
            text_fragment_1.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_1.text_state.background_color = ap.Color.light_gray
            text_fragment_1.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_2 = ap.text.TextFragment("Second line of text")
            # Set text properties
            text_fragment_2.text_state.font_size = 12
            text_fragment_2.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
            text_fragment_2.text_state.background_color = ap.Color.light_gray
            text_fragment_2.text_state.foreground_color = ap.Color.blue
            # Create text fragment
            text_fragment_3 = ap.text.TextFragment("And some more text...")
            # Set text properties
            text_fragment_3.text_state.font_size = 12
            text_fragment_3.text_state.font = ap.text.FontRepository.find_font(
                "TimesNewRoman"
            )
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

## Related Text Topics

- [Work with text in PDF using Python](/pdf/python-net/working-with-text/)
- [Adding text to PDF](/pdf/python-net/add-text-to-pdf-file/)
- [Format PDF text in Python](/pdf/python-net/text-formatting-inside-pdf/)
- [Replace text in PDF with Python](/pdf/python-net/replace-text-in-pdf/)