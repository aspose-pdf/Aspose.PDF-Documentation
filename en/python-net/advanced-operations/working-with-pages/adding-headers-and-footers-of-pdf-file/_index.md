---
title: Adding Header and Footer to PDF using Python
linktitle: Adding Header and Footer to PDF
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET allows you to add headers and footers to your PDF file using TextStamp class.
lastmod: "2025-11-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Header and Footer to PDF using Python
Abstract: The article provides a comprehensive guide on using **Aspose.PDF for Python via .NET** to add headers and footers to PDF files, with the ability to incorporate text or images. It begins by detailing the use of the `TextStamp` class to insert text into the header of a PDF document. Key properties such as font size, style, and color are adjustable, and the method for adding text to the header is demonstrated with a Python code snippet. The article similarly explains how to add text to the footer, following the same procedural steps. For adding images, the `ImageStamp` class is employed, and the process is described for both headers and footers, again supported by Python code examples. Additionally, the article discusses adding multiple headers in a single PDF file. This includes creating multiple `TextStamp` objects, each with distinct formatting, and applying them to different pages. The explanation is complemented by a detailed code snippet demonstrating this functionality.
---

**Aspose.PDF for Python via .NET** allows you to add header and footer in your existing PDF file. You may add images or text to a PDF document. Also, try to add different headers in one PDF File with Python.

## Adding Headers and Footers as Text Fragments

Add simple text headers and footers to all pages in a PDF. It creates header and footer objects, inserts text fragments into them, sets margins for proper positioning, and attaches them to each page in the document. The result is a PDF where every page displays consistent header and footer text.

The following code snippet demonstrates how to add headers and footers as text fragments in a PDF using Python:  

1. Create text fragments for the header and footer.
1. Create HeaderFooter objects and add the text fragments to them.
1. Define margin settings to control the placement of the header and footer.
1. Load the PDF document from the input file.
1. Iterate through all pages in the document.
1. Assign the header and footer to each page.
1. Save the modified PDF to the output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_text(input_file, output_file):
    """
    Add simple text headers and footers to all pages of a PDF document.

    Creates basic text-based headers and footers that appear on every page
    of the PDF document. Headers show "header" text and footers show "footer" text.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Adds identical headers and footers to all pages
        - Sets margins of 50 units left and 20 units top
        - Uses simple TextFragment elements for content
        - Headers and footers are created separately for each page

    Example:
        >>> add_header_and_footer_as_text("input.pdf", "output.pdf")
        # Adds text headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

This method is useful for adding consistent titles, page indicators, or legal disclaimers at the top and bottom of each page. You can also extend it to include images or dynamic content, such as page numbers.

## Adding Headers and Footers for Page Numbering

Add automatic page numbering to the headers and footers of a PDF document using Aspose.PDF for Python. Using the built-in variables $p (current page number) and $P (total number of pages), the script dynamically inserts page numbering on every page. Headers display the format 'Page X from Y', while footers show 'Page X / Y'. The margins ensure proper placement on each page.

1. Create a TextFragment for the header using "Page $p from $P" to show current and total pages.
1. Create a HeaderFooter object and add the header text to it.
1. Create a TextFragment for the footer using "Page $p / $P" for an alternative numbering style.
1. Create a Footer object and add the footer text.
1. Define margin settings (left = 50, top = 20) and apply them to both header and footer.
1. Open the PDF document from the input file.
1. Loop through all pages and assign the header and footer to each page.
1. Save the updated PDF to the output path.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def using_header_and_footer_for_page_numbering(input_file, output_file):
    """
    Add page numbering headers and footers to all pages of a PDF document.

    Creates headers and footers with dynamic page numbering using special variables.
    The $p variable represents the current page number and $P represents the total
    number of pages in the document.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses $p for current page number and $P for total pages
        - Header shows "Page X from Y" format
        - Footer shows "Page X / Y" format
        - Variables are automatically replaced by Aspose.PDF
        - Sets margins of 50 units left and 20 units top
        - Page numbering updates dynamically for each page

    Example:
        >>> using_header_and_footer_for_page_numbering("input.pdf", "output.pdf")
        # Adds page numbering headers and footers to all pages
    """
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adding Headers and Footers as HTML Fragments

Apply HTML-formatted headers and footers to every page of a PDF document using Aspose.PDF for Python. By using HtmlFragment, the script allows rich text styling—such as bold and italic—to appear in the header and footer. Margins are applied for proper placement, and the same formatted elements are attached to each page in the document.

The following code snippet demonstrates how to add headers and footers as HTML fragments to a PDF using Python:

1. Create an HTML header snippet using HtmlFragment—including styled text such as '<strong>' for bold.
1. Create a HeaderFooter object and add the HTML header to it.
1. Create an HTML footer snippet using '<i>' for italic styling.
1. Create a Footer object and add the footer HTML to it.
1. Configure margins (left = 50, top = 20) and assign them to both header and footer.
1. Load the PDF document using 'ap.Document()'.
1. Loop through all pages and assign the header and footer to each one.
1. Save the modified PDF to the specified output path.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_html(input_file, output_file):
    """
    Add HTML-formatted headers and footers to all pages of a PDF document.

    Creates rich HTML-based headers and footers with formatting like bold
    and italic text. Demonstrates how to use HtmlFragment for styled content.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses HtmlFragment for rich text formatting
        - Header includes HTML with <strong> tag for bold text
        - Footer includes HTML with <i> tag for italic text
        - Sets margins of 50 units left and 20 units top
        - HTML tags are rendered properly in the PDF

    Example:
        >>> add_header_and_footer_as_html("input.pdf", "output.pdf")
        # Adds HTML-formatted headers and footers to all pages
    """
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Using HtmlFragment allows rich formatting with inline styles or HTML markup, giving you more design flexibility compared to plain text.

## Adding Headers and Footers as images

Add image-based headers and footers to each page of a PDF document using Aspose.PDF for Python. The same image file is used for both the header and footer on every page. Margins position the images, and the image automatically adjusts to fit within the header/footer area.

The following code snippet demonstrates how to add headers and footers as images to a PDF using Python:

1. Load the image into an 'ap.Image' object and prepare it for use as a header.
1. Create a HeaderFooter object and attach the header image to it.
1. Load the same image again for use as a footer.
1. Create a Footer object and add the footer image to it.
1. Load the input PDF document using 'ap.Document()'.
1. Iterate through all pages of the document.
1. Apply margins (left = 50) to position both header and footer.
1. Assign the header and footer to each page in the PDF.
1. Save the updated PDF to the specified output file.

This technique is ideal for branding documents with logos or watermarks in the header/footer area.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_image(input_file, image_file, output_file):
    """
    Add image-based headers and footers to all pages of a PDF document.

    Creates headers and footers using image files. The same image is used
    for both header and footer positioning on each page.

    Args:
        input_file (str): Path to the input PDF file.
        image_file (str): Path to the image file to use for headers and footers.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses the same image file for both header and footer
        - Creates separate Image objects for header and footer
        - Sets margin of 50 units left for positioning
        - Image files should be in supported formats (PNG, JPG, etc.)
        - Images are automatically sized to fit header/footer areas

    Example:
        >>> add_header_and_footer_as_image("input.pdf", "logo.png", "output.pdf")
        # Adds image headers and footers using logo.png
    """

    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adding Headers and Footers as Table

Add structured, table-based headers and footers to all pages of a PDF document using Aspose.PDF for Python. Tables provide better layout control, alignment, and consistent formatting for complex headers and footers. The header text is centered while the footer text is left-aligned, both using Arial 12pt font. Column widths are calculated dynamically based on page dimensions to ensure proper placement.

This code snippet adds headers and footers (using tables) to each page of a PDF document with Aspose.PDF for Python via .NET.

1. Define text styles using 'ap.text.TextState' for header and footer (font, size, alignment).
1. Create HeaderFooter objects for the header and footer.
1. Build the header table with a single row and a cell containing the header text.
1. Build the footer table with a single row and cell containing the footer text.
1. Add the tables to the corresponding 'HeaderFooter' objects.
1. Set footer margin for proper horizontal positioning.
1. Open the PDF document using 'ap.Document()'.
1. Iterate through all pages and assign the table-based header and footer to each page.
1. Save the modified PDF to the output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_table(input_file, output_file):
    """
    Add table-based headers and footers to all pages of a PDF document.

    Creates headers and footers using table structures for better layout
    control and alignment. Demonstrates advanced formatting with text states.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses Table objects for structured layout
        - Header table has centered Arial 12pt text
        - Footer table has left-aligned Arial 12pt text
        - Column width calculated based on page width minus margins
        - Provides more precise control over text positioning

    Example:
        >>> add_header_and_footer_as_table("input.pdf", "output.pdf")
        # Adds table-structured headers and footers to all pages
    """
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Adding Headers and Footers as LaTex

Add headers and footers containing LaTeX-formatted content to all pages of a PDF document using Aspose.PDF for Python. LaTeX allows rendering of mathematical symbols, dates, copyright marks, and other advanced formatting. The header includes a dynamic date, while the footer displays a copyright symbol along with the current page number and total page count.

The following code snippet shows how to use LaTeX fragments in headers and footers for a PDF using Aspose.PDF for Python via .NET.

1. Open the PDF document using 'ap.Document()'.
1. Determine total page count to use in dynamic footers.
1. Iterate through all pages of the document.
1. Create a HeaderFooter object for the header.
1. Create a TeXFragment for the header text containing LaTeX commands (e.g., \'today').
1. Create a HeaderFooter object for the footer.
1. Create a TeXFragment for the footer text including LaTeX symbols (e.g., \'copyright') and page numbering.
1. Add the TeXFragment to the corresponding header/footer object.
1. Bind the header and footer to the current page.
1. Save the modified PDF to the output file.

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def add_header_and_footer_as_latex(input_file, output_file):
    """
    Add LaTeX-formatted headers and footers to all pages of a PDF document.

    Creates headers and footers using LaTeX markup for mathematical expressions,
    symbols, and advanced formatting. Demonstrates TeXFragment usage.

    Args:
        input_file (str): Path to the input PDF file.
        output_file (str): Path where the modified PDF will be saved.

    Returns:
        None: The function modifies the PDF and saves it to the output path.

    Note:
        - Uses TeXFragment for LaTeX rendering
        - Header includes LaTeX date command (\\today\\)
        - Footer includes copyright symbol and page numbering
        - LaTeX commands are processed and rendered properly
        - Page count is dynamically calculated and inserted

    Example:
        >>> add_header_and_footer_as_latex("input.pdf", "output.pdf")
        # Adds LaTeX-formatted headers and footers with symbols and page numbers
    """
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTex Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```