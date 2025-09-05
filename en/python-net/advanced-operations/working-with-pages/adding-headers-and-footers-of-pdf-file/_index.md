---
title: Add Header and Footer to PDF using Python
linktitle: Add Header and Footer to PDF
type: docs
weight: 50
url: /python-net/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Python via .NET allows you to add headers and footers to your PDF file using TextStamp class.
lastmod: "2025-06-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Header and Footer to PDF using Python
Abstract: The article provides a comprehensive guide on using **Aspose.PDF for Python via .NET** to add headers and footers to PDF files, with the ability to incorporate text or images. It begins by detailing the use of the `TextStamp` class to insert text into the header of a PDF document. Key properties such as font size, style, and color are adjustable, and the method for adding text to the header is demonstrated with a Python code snippet. The article similarly explains how to add text to the footer, following the same procedural steps. For adding images, the `ImageStamp` class is employed, and the process is described for both headers and footers, again supported by Python code examples. Additionally, the article discusses adding multiple headers in a single PDF file. This includes creating multiple `TextStamp` objects, each with distinct formatting, and applying them to different pages. The explanation is complemented by a detailed code snippet demonstrating this functionality.
---

**Aspose.PDF for Python via .NET** allows you to add header and footer in your existing PDF file. You may add images or text to a PDF document. Also, try to add different headers in one PDF File with Python.

## Adding Headers and Footers as Text Fragments

The following code snippet demonstrates how to add headers and footers as text fragments in a PDF using Python:  

1. Open the existing PDF file.
1. Loop through all pages.
1. Create and customize HeaderFooter objects with TextFragment for both the header and the footer.
1. Apply margin settings for positioning.
1. Assign the header and footer to each page.
1. Save the modified PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        for i in range(1, len(document.pages) + 1):
            # Create header text
            header_text = ap.text.TextFragment("header")
            # Create header
            header = ap.HeaderFooter();
            header.paragraphs.add(header_text)
                
            # Create footer text
            footer_text = ap.text.TextFragment("footer")
        
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
                
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(path_outfile)
```

This method is useful for adding consistent titles, page indicators, or legal disclaimers at the top and bottom of each page. You can also extend it to include images or dynamic content, such as page numbers.

## Adding Headers and Footers as HTML Fragments

The following code snippet demonstrates how to add headers and footers as HTML fragments to a PDF using Python:

1. Open the target PDF file.
1. Create HtmlFragment elements for both header and footer.
1. Wrap them in HeaderFooter objects and assign margins.
1. Attach them to each page in the PDF.
1. Save the updated file.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        for i in range(1, len(document.pages) + 1):
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
                
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(path_outfile)
```

Using HtmlFragment allows rich formatting with inline styles or HTML markup, giving you more design flexibility compared to plain text.

## Adding Headers and Footers as images

The following code snippet demonstrates how to add headers and footers as images to a PDF using Python:

1. Load the PDF file.
1. For each page, create an Image object and assign the image path.
1. Embed the image inside HeaderFooter objects.
1. Apply margins using MarginInfo for positioning.
1. Attach the header and footer to every page.

This technique is ideal for branding documents with logos or watermarks in the header/footer area.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_imagefile = self.data_dir + imagefile
    path_outfile = self.data_dir + outfile
    
    # Open PDF document
    with ap.Document(path_infile) as document:
        for i in range(1, len(document.pages) + 1):
            # Create header image
            header_image = ap.Image()
            header_image.file = path_imagefile
            # Create header
            header = ap.HeaderFooter()
            header.paragraphs.add(header_image)
                
            # Create footer image
            footer_image = ap.Image()
            footer_image.file = path_imagefile
        
            # Create footer 
            footer = ap.HeaderFooter()
            footer.paragraphs.add(footer_image)
        
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
        document.save(path_outfile)
```

## Adding Headers and Footers as Table

This code snippet adds headers and footers (using tables) to each page of a PDF document with Aspose.PDF for Python via .NET.

1. Open the PDF document.
1. Loop through all pages.
1. Create text states for header and footer.
1. Create header and footer objects.
1. Build header table.
1. Build footer table.
1. Add tables to header and footer.
1. Set footer margin.
1. Bind header and footer to the page.
1. Save the updated PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        for i in range(1, len(document.pages) + 1):
            text_state_top_header = ap.text.TextState()
            text_state_top_header.font = ap.text.FontRepository.find_font("Arial")
            text_state_top_header.font_size = 12
            text_state_top_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
            text_state_info_footer = ap.text.TextState()
            text_state_info_footer.font = ap.text.FontRepository.find_font("Arial")
            text_state_info_footer.font_size = 12
            text_state_info_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
            # Create header
            header = ap.HeaderFooter()
            # Create footer
            footer = ap.HeaderFooter()
            # Create header Table
            table_header = ap.Table()
            table_header.column_widths = str(594 - header.margin.left - header.margin.right)
            table_header.rows.add().cells.add("This is a Table Header", text_state_top_header)
            # Create footer Table
            table = ap.Table()
            table.column_widths = str(594 - footer.margin.left - footer.margin.right)
            table.rows.add().cells.add("Powered by Aspose.PDF", text_state_info_footer)
            header.paragraphs.add(table_header)
            footer.paragraphs.add(table)
            # Set margin
            margin = ap.MarginInfo()
            margin.left = 50
            # Set footer margin
            footer.margin = margin
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

            # Save PDF document
        document.save(path_outfile)
```

## Adding Headers and Footers as LaTex

The following code snippet shows how to use LaTeX fragments in headers and footers for a PDF using Aspose.PDF for Python via .NET.

1. Open the PDF document.
1. Get the number of pages.
1. Iterate over all pages.
1. Create a header with LaTeX text.
1. Create a footer with LaTeX text.
1. Assign header and footer to the page.
1. Save the modified PDF.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
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
        document.save(path_outfile)
```