---
title: Replace Text in PDF via Python
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /python-net/replace-text-in-pdf/
description: Learn more about various ways of replacing and removing text from Aspose.PDF for Python via .NET library.
lastmod: "2025-10-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true 
AlternativeHeadline: How to replace Text in PDF using Python
Abstract: The article provides a comprehensive guide on various text manipulation techniques within PDF documents using Aspose.PDF for Python via .NET. It covers several text replacement strategies, including replacing text across all pages, within specific page regions, and using regular expressions. The article also explains how to replace fonts within PDFs, ensuring that unused fonts are removed, and how to manage text replacement to automatically rearrange page content. Additionally, it delves into rendering replaceable symbols during PDF creation, including their use in header/footer areas, to enhance document customization. Finally, it details methods to remove all text from a PDF document, optimizing operations for scenarios where complete text removal is necessary. Each section is supplemented with code snippets in Python and other supported languages to demonstrate practical implementation.
---

## Replace Text in all pages of PDF document

{{% alert color="primary" %}}

You can try to find in replace the text in the document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Text replacement is a common requirement when updating or correcting content in existing PDF documents — for instance, changing product names, fixing typos, or updating terminology across multiple pages.

Aspose.PDF for Python via .NET offers a powerful and efficient method for searching and replacing text programmatically through the [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) class.

This example demonstrates how to find all occurrences of a specific phrase (in this case, "Black cat") and replace them with a new phrase ("White dog") throughout an entire PDF document.

1. Specify Search and Replacement Phrases. Set the text you want to find and the text you want it replaced with.
1. Load the PDF Document.
1. Create a Text Absorber. A TextFragmentAbsorber is initialized with the search phrase. It scans the document for all instances of the given phrase.
1. Apply the Absorber to All Pages. This iterates through all pages and collects text fragments matching the phrase.
1. Replace each found fragment. Every instance of "Black cat" should be changed to "White dog".
1. Save the Updated PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_on_all_pages(infile, outfile):
    """
    Replace text on all pages of a PDF document.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    search_phrase = "Black cat"
    replace_phrase = "White dog"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

## Replace Text in particular page region

Sometimes, you may need to replace text only within a specific area of a PDF page instead of searching the entire document — for example, updating a header, footer, or a table cell within a known position.

The Aspose.PDF for Python via .NET library enables this functionality by utilizing the [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) in conjunction with region-based text searching.

This example demonstrates how to find and replace all occurrences of a target phrase within a defined rectangular region on a specific page.

1. Specify Search and Replacement Phrases.
1. Load the PDF Document.
1. Create a Text Absorber for Searching. Initialize a TextFragmentAbsorber to find the desired text.
1. Restrict the Search Area. The rectangle specifies the x- and y-coordinate limits on the page.
1. Apply the Absorber to a Specific Page. This performs the search and collects matching text fragments within the specified area.
1. Replace the Found Text. Every occurrence of 'doc' in the defined region becomes 'DOC'.
1. Save the Updated PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_in_particular_page_region(infile, outfile):
    """
    Replace text in a particular region of a page.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

## Replace Text Based on a Regular Expression

When working with PDF documents, you may need to replace text that follows a pattern rather than a specific phrase — for example, phone numbers, codes, or date-like formats.

Aspose.PDF for Python via .NET allows you to perform such replacements using regular expressions (regex) with the TextFragmentAbsorber class.

This example demonstrates how to find text patterns (in this case, any text matching the format ####-####, such as 1234-5678) and replace them with a formatted string 'ABC1-2XZY'. It also shows how to customize the font, color, and size of the replaced text.

The following code snippet shows you how to replace text based on a regular expression.

1. Load the PDF Document.
1. Create a Regex-Based Text Absorber. Initialize the TextFragmentAbsorber with a regular expression pattern.
1. Enable Regular Expression Mode. The 'True' parameter activates regular expression search mode.
1. Apply the Absorber to a Page. This scans the page for all text fragments that match the defined regex pattern.
1. Replace each match with new text and apply custom styling.
1. Save the Modified Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_based_on_regex(infile, outfile):
    """
    Replace text based on a regular expression pattern.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Replace fonts in existing PDF file

On occasion, you need to standardize or update fonts across a PDF — for instance, replacing an outdated or proprietary font with a more accessible one. The Aspose.PDF for Python via .NET library allows you to detect and replace fonts programmatically, ensuring consistent typography and document compatibility.

This example demonstrates how to replace all instances of a specific font (e.g., 'Arial-BoldMT') with another font (e.g., 'Verdana') throughout a PDF document.

The following code snippet shows how to replace the font inside PDF document:

1. Open the PDF Document.
1. Initialize a TextFragmentAbsorber.
1. Use the Absorber to extract text fragments from every page in the document.
1. Identify and Replace Fonts. The script checks if a fragment’s current font is 'Arial-BoldMT'. If true, it replaces it with the 'Verdana' font using the FontRepository.find_font() method.
1. Save the Modified Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_fonts(infile, outfile):
    """
    Replace specific fonts in a PDF document.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

## Remove unused fonts

Over time, PDF documents can accumulate unused or embedded fonts that increase file size and slow down processing. These unused fonts often remain even after text edits or replacements, especially when working with large or complex PDFs.

The Aspose.PDF for Python via .NET library provides an efficient way to remove such redundant fonts using the TextEditOptions class. This not only optimizes your document but also ensures it uses only the fonts actually applied to visible text.

The 'remove_unused_fonts()' method is a simple but powerful way to optimize PDF files by removing redundant font data.

This example demonstrates how to:

- Scan a PDF for unused fonts.
- Remove them safely.
- Reassign active text fragments to a consistent font (e.g., Times New Roman).

1. Open the PDF Document.
1. Configure Text Editing Options. This instructs the engine to eliminate any embedded fonts not currently used in the visible text.
1. Create a Text Absorber with Options. A TextFragmentAbsorber extracts text fragments from the document for editing.
1. Reassign a Standard Font. Once the absorber has collected all fragments, iterate through them and apply a consistent font.
1. Save the Cleaned PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_unused_fonts(input_file, output_file):
    """
    Remove unused fonts from a PDF document.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """

    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")

    # Save the updated PDF document
    document.save(output_file)
```

## Remove Text from PDF

There are times when you need to remove text from a PDF document — for example, redacting confidential data, cleaning placeholders, or preparing a layout for new content.
The Aspose.PDF for Python via .NET library provides a powerful tool for this purpose: the TextFragmentAbsorber class.

Our library supports three approaches to removing text from a PDF:

- From the entire document. This version removes all text across all pages of a PDF.
- From a specific page. This method targets a single page, allowing precise control when editing multipage PDFs.
- From a specific rectangular region of a page. This approach limits text removal to a rectangular area within a specific page, defined by coordinates.

Each approach uses the absorber’s 'remove_all_text()' method but applies it at different scopes.

The next example demonstrates removing text from a specific page.

1. Load the PDF Document.
1. Create an instance of TextFragmentAbsorber, which is designed to capture and manipulate text fragments within a document.
1. Remove All Text from One Page. The 'absorber.remove_all_text()' method removes all text fragments found on that page, effectively clearing the text layer while leaving images, lines, or vector graphics untouched.
1. Save the Updated Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

## Replace Text and Fitting It into a Rectangle

Sometimes, when updating or replacing text in a PDF, the new text may not naturally fit within the original layout boundaries.
Aspose.PDF for Python provides options to automatically adjust font size and spacing so that the replaced text fits neatly within a defined rectangle, preserving the page layout.

1. Load the PDF Document.
1. Use a 'TextFragmentAbsorber' to collect all text fragments on the page.
1. Select the Fragment to Replace.
1. Set Rectangle Bounds for Replacement. This ensures the new text stays within the original text fragment’s layout area.
1. Enable Font Size Adjustment. Automatically shrink the font if the new text is too long.
1. Adjust Spacing if Needed. Optionally, adjust the spacing between words or letters to fit longer text.
1. Replace the fragment text.
1. Save the Updated Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH

        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

## Resize and Shift Text Without Changing Font Size

When replacing text in a PDF, sometimes you want to fit or reposition the new text within a specific area without modifying the font size.
Aspose.PDF for Python via .NET provides options to adjust text layout and spacing while keeping the original font size intact.

1. Load the PDF Document.
1. Collect all text fragments on the page using a 'TextFragmentAbsorber'.
1. Select the Fragment to Modify.
1. Shift and resize the text rectangle.
1. Adjust Text Spacing. Enable spacing adjustment to fit the text within the modified rectangle.
1. Replace the fragment text.
1. Save the Updated PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    """
    Resize and shift text without changing the font.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

## Resize and Shift a Paragraph in PDF

When working with PDFs, sometimes you need to replace or expand a paragraph while keeping it visually aligned with the page layout. Aspose.PDF allows you to resize the paragraph’s bounding rectangle and adjust spacing to fit new text, all without changing the font size.

1. Load the PDF Document.
1. Use 'TextFragmentAbsorber' to collect all text fragments on the page.
1. Select the Fragment to Modify.
1. Resize and Shift the Paragraph. Use the page's media box to determine bounds and adjust the rectangle.
1. Adjust Spacing. This modifies the spacing between words/letters instead of changing font size.
1. Replace the fragment text.
1. Save the Modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    """
    Resize and shift a paragraph in the document.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

## Replace Text and Expand Font to Fill a Target Area

When replacing text in a PDF, you want the new content to fill a specific area for better visual impact or alignment. Our library allows you to automatically scale the font size so the text fits a designated rectangle, while also optionally adjusting spacing between words.

1. Load the PDF Document.
1. Use 'TextFragmentAbsorber' to collect all text fragments on the page.
1. Select the Fragment to Replace.
1. Set the Target Rectangle. This rectangle determines the area the text will occupy on the page.
1. Enable Font Scaling. Automatically scale the font size to fill the rectangle.
1. Adjust Spacing Between Words. This ensures that longer text can fit the rectangle without shrinking the font unnecessarily.
1. Replace the fragment text.
1. Save the Modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Parameters:
    - infile (str): Path to input PDF file.
    - outfile (str): Path to output PDF file.
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
             ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```