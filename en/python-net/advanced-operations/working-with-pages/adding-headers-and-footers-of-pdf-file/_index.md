---
title: Add PDF Headers and Footers in Python
linktitle: Adding Header and Footer to PDF
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Learn how to add headers and footers to PDF files in Python using text, images, and structured content.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add headers and footers to PDF files with Python
Abstract: This article shows how to add headers and footers to PDF documents with Aspose.PDF for Python via .NET. It covers text, page numbering, HTML, image, table, and LaTeX-based header and footer content.
---

Use this page to add consistent header and footer content across PDF pages with **Aspose.PDF for Python via .NET**.

You can build headers and footers with [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), and [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objects, then apply them through [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) on each page.

## Adding Headers and Footers as Text Fragments

Add simple text headers and footers to all pages in a PDF. It creates [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objects, inserts [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) elements into them, sets [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) for proper positioning, and attaches them to each page in the document. The result is a PDF where every page displays consistent header and footer text.

The following code snippet demonstrates how to add headers and footers as text fragments in a PDF using Python:

1. Create text fragments for the header and footer.
1. Create HeaderFooter objects and add the text fragments to them.
1. Define margin settings to control the placement of the header and footer.
1. Load the PDF document from the input file.
1. Iterate through all pages in the document.
1. Assign the header and footer to each page.
1. Save the modified PDF to the output file.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
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

Add automatic page numbering to the headers and footers of a PDF document using Aspose.PDF for Python. Using the built-in variables $p (current page number) and $P (total number of pages), the script dynamically inserts page numbering on every page. Headers display the format 'Page X from Y', while footers show 'Page X / Y'. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) ensures proper placement on each page.

1. Create a TextFragment for the header using "Page $p from $P" to show current and total pages.
1. Create a HeaderFooter object and add the header text to it.
1. Create a TextFragment for the footer using "Page $p / $P" for an alternative numbering style.
1. Create a Footer object and add the footer text.
1. Define margin settings (left = 50, top = 20) and apply them to both header and footer.
1. Open the PDF document from the input file.
1. Loop through all pages and assign the header and footer to each page.
1. Save the updated PDF to the output path.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
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

Apply HTML-formatted headers and footers to every page of a PDF document using Aspose.PDF for Python. By using [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), the script allows rich text styling—such as bold and italic—to appear in the header and footer. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) is applied for proper placement, and the same formatted elements are attached to each page in the document.

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
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
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

## Adding Headers and Footers as Images

Add image-based headers and footers to each page of a PDF document using Aspose.PDF for Python. The same image file is used for both the header and footer on every page. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) positions the images, and the image automatically adjusts to fit within the header/footer area.

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
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
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

Add structured, table-based headers and footers to all pages of a PDF document using Aspose.PDF for Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objects provide better layout control, alignment, and consistent formatting for complex headers and footers. The header text is centered while the footer text is left-aligned, both using Arial 12pt font. Column widths are calculated dynamically based on page dimensions to ensure proper placement.

This code snippet adds headers and footers (using tables) to each page of a PDF document with Aspose.PDF for Python via .NET.

1. Define text styles using [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) for header and footer (font, size, alignment).
1. Create [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objects for the header and footer.
1. Build the header [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) with a single row and a cell containing the header text.
1. Build the footer [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) with a single row and cell containing the footer text.
1. Add the tables to the corresponding [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objects.
1. Set footer [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) for proper horizontal positioning.
1. Open the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using appropriate methods.
1. Iterate through all pages and assign the table-based header and footer to each page.
1. Save the modified [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to the output file.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
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

## Adding Headers and Footers as LaTeX

Add headers and footers containing LaTeX-formatted content to all pages of a PDF document using Aspose.PDF for Python. LaTeX allows rendering of mathematical symbols, dates, copyright marks, and other advanced formatting. The header includes a dynamic date, while the footer displays a copyright symbol along with the current page number and total page count.

The following code snippet shows how to use [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) in headers and footers for a PDF using Aspose.PDF for Python via .NET.

1. Open the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) using appropriate methods.
1. Determine total page count to use in dynamic footers.
1. Iterate through all pages of the document.
1. Create a [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) object for the header.
1. Create a [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) for the header text containing LaTeX commands (e.g., `\\today\\`).
1. Create a [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) object for the footer.
1. Create a [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) for the footer text including LaTeX symbols and page numbering.
1. Add the [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) to the corresponding header/footer object.
1. Bind the header and footer to the current page.
1. Save the modified [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) to the output file.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Related Page Topics

- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Add page numbers to PDF in Python](/pdf/python-net/add-page-number/)
- [Stamp PDF pages in Python](/pdf/python-net/stamping/)
- [Format PDF documents in Python](/pdf/python-net/formatting-pdf-document/)