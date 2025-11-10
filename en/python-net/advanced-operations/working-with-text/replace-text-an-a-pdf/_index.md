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

These examples demonstrate how to **modify or remove text in an existing PDF**.

## Replace existing text

### Replace Text in all pages of PDF document

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

    Searches for a specific text phrase throughout all pages of a PDF document
    and replaces all occurrences with a new phrase. This function demonstrates
    global text replacement using TextFragmentAbsorber.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "Black cat" with "White dog" as demonstration
        - Searches across all pages in the document
        - Preserves original formatting and layout
        - Uses TextFragmentAbsorber for efficient text search

    Example:
        >>> replace_text_on_all_pages("input.pdf", "output.pdf")
        # Replaces all instances of "Black cat" with "White dog"
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

### Replace Text in particular page region

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

    Performs targeted text replacement within a specific rectangular region
    on the first page of a PDF document. This allows for precise control
    over which text gets replaced based on its location.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Replaces "doc" with "DOC" within the specified region
        - Only affects text within coordinates (300, 442, 500, 742)
        - Uses limit_to_page_bounds for precise region control
        - Only processes the first page (pages[1])

    Example:
        >>> replace_text_in_particular_page_region("input.pdf", "output.pdf")
        # Replaces "doc" with "DOC" only in the specified rectangular area
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

### Resize and Shift Text Without Changing Font Size

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
    Resize and shift text without changing the font size.

    Demonstrates how to replace text content while adjusting its position
    and width within a modified rectangular area. The font size remains
    unchanged, but spacing is adjusted to fit the new content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Targets the second text fragment on the first page
        - Narrows the text rectangle by 50 units on each side
        - Duplicates the original text content
        - Uses ADJUST_SPACE_WIDTH for proper spacing
        - Maintains original font size and style

    Example:
        >>> replace_text_and_resize_and_shift_without_changing_font_size("input.pdf", "output.pdf")
        # Duplicates text in a narrower space with adjusted spacing
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

### Resize and Shift a Paragraph in PDF

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

    Demonstrates paragraph-level text replacement with automatic resizing
    to fit within the page's media box boundaries. Adjusts the text area
    to provide margins while duplicating content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses page media box as base rectangle
        - Adds 20-unit margins on left, right, and top
        - Targets the second text fragment on the first page
        - Duplicates original text content
        - Automatically adjusts space width for proper fit

    Example:
        >>> replace_text_and_resize_and_shift_paragraph("input.pdf", "output.pdf")
        # Resizes paragraph to fit within page margins with duplicated text
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

### Replace Text and Automatically Expand Font to Fill Target Area

Replace text in a PDF while automatically resizing and expanding the font to fill a specific rectangular area. Using the Aspose.PDF for Python via .NET library, the code dynamically adjusts the font size and spacing so that the new text content perfectly fits within a defined bounding box — without manual font calculations.

1. Load the PDF.
1. Capture Text Fragments.
1. Select a Specific Fragment.
1. Define Target Rectangle.
1. Enable Text Adjustment Options.
1. Replace Text.
1. Save the Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_resize_and_expand_font(infile, outfile):
    """
    Resize and expand font to fill target area.

    Demonstrates automatic font scaling to fill a specified rectangular area.
    The font size is dynamically adjusted to make the text content fit
    perfectly within the defined target rectangle.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Defines target rectangle at coordinates (100, 300, 512, 692)
        - Uses SCALE_TO_FILL for automatic font size adjustment
        - Duplicates original text content
        - Adjusts space width for optimal text distribution
        - Font size scales up or down to fill the entire rectangle

    Example:
        >>> replace_text_and_resize_and_expand_font("input.pdf", "output.pdf")
        # Scales font to completely fill the specified rectangular area
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

### Replace Text and Fit It into a Rectangle

Replace text in a PDF document while ensuring the new content fits within the original text’s rectangular area by automatically reducing the font size when needed.

Using the Aspose.PDF for Python via .NET library, this function adjusts both the text layout and font size dynamically, preserving document structure while preventing overflow.

1. Create a TextFragmentAbsorber object to extract all text fragments from the first page.
1. Access a Specific Text Fragment.
1. Set the Replacement Area.
1. Configure Text Adjustment Options. Set two key replacement options:
    - Font size adjustment - 'SHRINK_TO_FIT' automatically reduces font size if the new text is too long.
    - Spacing adjustment - 'ADJUST_SPACE_WIDTH' keeps spacing proportional.
1. Replace the Text.
1. Save the Modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    """
    Fit text into a rectangle by adjusting font size.

    Demonstrates how to ensure text content fits within its original
    rectangle by automatically shrinking the font size when the new
    content is longer than the original.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses original text fragment rectangle as target area
        - Employs SHRINK_TO_FIT to reduce font size if needed
        - Duplicates original text content (making it longer)
        - Adjusts space width for proper text distribution
        - Prevents text overflow by automatic font scaling

    Example:
        >>> replace_text_and_fit_text_into_rectangle("input.pdf", "output.pdf")
        # Shrinks font size to fit doubled text content in original space
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

### Automatically Replace Placeholder Text and Rearrange PDF Layout

Replace placeholder text inside a PDF (e.g., templates or forms) with actual data such as names or company information.
It automatically adjusts the page layout to fit new text while applying custom formatting (font, color, size).

1. Import and Load the PDF.
1. Create a Text Absorber for the Placeholder.
1. Apply the Absorber to All Pages.
1. Loop Through Found Text Fragments.
1. Apply Custom Text Formatting.
1. Save the Updated Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def automatically_rearrange_page_contents(input_file, output_file):
    """
    Replace placeholder text in PDF with actual content.

    Demonstrates how to replace long placeholder text with actual content
    and automatically rearrange page layout. Shows dynamic content replacement
    with custom formatting applied to the new text.

    Args:
        input_file (str): Path to the input PDF file containing placeholders.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for "[Long_placeholder_Long_placeholder]" placeholders
        - Replaces with either "John Smith" or extended version with studio info
        - Applies Calibri font, size 12, navy blue color
        - Automatically adjusts page layout to accommodate content changes
        - Demonstrates real-world template filling scenarios

    Example:
        >>> automatically_rearrange_page_contents("template.pdf", "filled.pdf")
        # Replaces placeholders with formatted actual content
    """
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Replace Text Based on a Regular Expression

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

    Demonstrates pattern-based text replacement using regular expressions
    to find and replace text that matches specific formats. Also shows
    how to apply formatting changes to the replaced text.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses regex pattern r"\\d{4}-\\d{4}" to find 4-digit-4-digit patterns
        - Replaces matched patterns with "ABC1-2XZY"
        - Applies custom formatting: Verdana font, size 12, blue text
        - Sets light green background color for replaced text
        - Enables regex mode with TextSearchOptions(True)

    Example:
        >>> replace_text_based_on_regex("input.pdf", "output.pdf")
        # Replaces patterns like "1234-5678" with formatted "ABC1-2XZY"
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

## Replace fonts or remove unused fonts

### Replace fonts in existing PDF file

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

    Demonstrates how to find and replace specific fonts throughout a PDF
    document. Searches for text using a particular font and changes it
    to a different font while preserving the text content.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Searches for text using "Arial-BoldMT" font
        - Replaces font with "Verdana" while keeping text content
        - Processes all text fragments across all pages
        - Maintains original text size and formatting properties
        - Useful for font standardization across documents

    Example:
        >>> replace_fonts("input.pdf", "output.pdf")
        # Changes all Arial-BoldMT text to use Verdana font instead
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Remove unused fonts

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

    Optimizes PDF file size by removing fonts that are embedded but not
    actually used in the document. Also demonstrates how to standardize
    all text to use a specific font family.

    Args:
        input_file (str): Path to the input PDF file to optimize.
        output_file (str): Path where the optimized PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses REMOVE_UNUSED_FONTS option for optimization
        - Changes all text to use TimesNewRoman font
        - Processes all text fragments across the document
        - Reduces file size by eliminating unnecessary font data
        - Useful for PDF optimization and standardization

    Example:
        >>> remove_unused_fonts("input.pdf", "optimized.pdf")
        # Removes unused fonts and standardizes text to TimesNewRoman
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

## Remove all Text

### Remove Text from PDF

Remove all text content from a PDF file while keeping images, shapes, and layout structures intact.
By using TextFragmentAbsorber, the code efficiently scans the entire document and deletes every text fragment found on each page.

1. Load the PDF Document.
1. A TextFragmentAbsorber object is created to detect and handle text fragments in the PDF.
1. Remove All Text Content. The method 'absorber.remove_all_text()' removes every text element from the loaded document, leaving non-text components untouched.
1. Save the Updated Document.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber1(infile, outfile):
    """
    Remove all text from a PDF using TextFragmentAbsorber.

    Demonstrates complete text removal from an entire PDF document,
    leaving only non-text elements like images, shapes, and layout
    structures intact.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the text-free PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes all text content from the entire document
        - Preserves images, graphics, and page structure
        - Uses document-level text removal for complete cleanup
        - Useful for creating templates or removing sensitive text
        - Maintains page layout and non-text elements

    Example:
        >>> remove_all_text_using_absorber1("input.pdf", "no_text.pdf")
        # Creates a PDF with all text removed but graphics preserved
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Remove all Text from a Specific Page

Remove all text from a single page of a PDF document using the TextFragmentAbsorber class in Aspose.PDF.
Unlike full-document removal, this method performs page-level text cleanup, deleting text only from the chosen page while leaving all other pages untouched.

1. Load the PDF File.
1. Create a TextFragmentAbsorber Instance.
1. Remove All Text from the First Page.
1. Save the Modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber2(infile, outfile):
    """
    Remove all text from page using TextFragmentAbsorber.

    Demonstrates text removal from a specific page while leaving text
    on other pages intact. Useful for selective text cleanup or
    creating mixed-content documents.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only from the first page (pages[1])
        - Preserves text content on all other pages
        - Maintains page structure and non-text elements
        - Useful for page-specific text removal operations
        - Images and graphics on the target page remain intact

    Example:
        >>> remove_all_text_using_absorber2("input.pdf", "first_page_clean.pdf")
        # Removes all text from first page only
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Remove all Text from particular area on PDF page

Remove all text from a specific rectangular region on a page using Aspose.PDF’s TextFragmentAbsorber.
Instead of clearing an entire page, this method performs targeted text removal, allowing precise control over which part of the page is affected.

1. Load the PDF Document.
1. Create a TextFragmentAbsorber.
1. Define the Target Area (Rectangle).
1. Remove Text from the Specified Region.
1. Preserve the Rest of the Document.
1. Save the Modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_all_text_using_absorber3(infile, outfile):
    """
    Remove all text from particular area on PDF page using TextFragmentAbsorber.

    Demonstrates precise text removal from a specific rectangular region
    on a page. Allows for surgical text removal while preserving text
    outside the target area.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Removes text only within rectangle (10, 200, 120, 600)
        - Targets the first page only (pages[1])
        - Preserves text outside the specified rectangle
        - Maintains all non-text elements in the region
        - Useful for removing watermarks, headers, or specific sections

    Example:
        >>> remove_all_text_using_absorber3("input.pdf", "region_clean.pdf")
        # Removes text only from the specified rectangular area
    """
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1], ap.Rectangle(10, 200, 120, 600))
        document.save(outfile)
```

### Remove all hidden Text from a PDF document

Remove all text from a specific rectangular region on a page using Aspose.PDF’s TextFragmentAbsorber.
Instead of clearing an entire page, this method performs targeted text removal, allowing precise control over which part of the page is affected.

1. Load the PDF Document.
1. Create a TextFragmentAbsorber.
1. Define the Target Area (Rectangle).
1. Remove Text from the Specified Region.
1. Preserve the Rest of the Document.
1. Save the Modified PDF.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def remove_hidden_text(infile, outfile):
    """
    Remove all hidden (invisible) text from a PDF document.

    Identifies and removes text that has been marked as invisible while
    preserving all visible text content. Useful for cleaning documents
    that may contain hidden tracking text or metadata.

    Args:
        infile (str): Path to the input PDF file to process.
        outfile (str): Path where the cleaned PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Detects text fragments with invisible text state
        - Replaces hidden text with empty strings
        - Uses NONE replacement adjustment to prevent layout shifts
        - Preserves all visible text and document structure
        - Useful for privacy and security document cleanup

    Example:
        >>> remove_hidden_text("input.pdf", "no_hidden_text.pdf")
        # Removes all invisible text while keeping visible content intact
    """
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```