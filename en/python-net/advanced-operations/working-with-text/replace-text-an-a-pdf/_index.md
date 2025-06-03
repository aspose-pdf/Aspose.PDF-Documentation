---
title: Replace Text in PDF via Python
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /python-net/replace-text-in-pdf/
description: Learn more about various ways of replacing and removing text from Aspose.PDF for Python via .NET library.
lastmod: "2025-05-27"
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

In order to replace text in all the pages of a PDF document, you first need to use [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) to find the particular phrase you want to replace. After that, you need to go through all the TextFragments to replace the text and change any other attributes. Once you have done that, you only need to save the output PDF using the Save method of the Document object. The following code snippet shows you how to replace text in all pages of PDF document.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all instances of the input search phrase
        absorber = ap.text.TextFragmentAbsorber("text")
        # Accept the absorber for all the pages
        document.pages.accept(absorber)

        # Get the extracted text fragments
        collection = absorber.text_fragments

        # Loop through the fragments
        for text_fragment in collection:
            # Update text and other properties
            text_fragment.text = "TEXT"
            text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            text_fragment.text_state.font_size = 22
            text_fragment.text_state.foreground_color = ap.Color.from_rgb(drawing.Color.blue)
            text_fragment.text_state.background_color = ap.Color.from_rgb(drawing.Color.green)

        # Save the document
        document.save(path_outfile)
```

## Replace Text in particular page region

In order to replace text in a particular page region, first, we need to instantiate TextFragmentAbsorber object, specify page region using 'text_search_options.rectangle' property and then iterate through all the TextFragments to replace the text. Once these operations are completed, we only need to save the output PDF using the 'save' method of the Document object.

The following code snippet shows you how to replace text in all pages of PDF document:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # instantiate TextFragment Absorber object
        absorber = ap.text.TextFragmentAbsorber()

        # search text within page bound
        absorber.text_search_options.limit_to_page_bounds = True

        # specify the page region for TextSearch Options
        absorber.text_search_options.rectangle = ap.Rectangle(100, 100, 500, 500, False)

        # search text from first page of PDF file
        document.pages[1].accept(absorber)

        # iterate through individual TextFragment
        for text_fragment in absorber.text_fragments:
            # update text to blank characters
            text_fragment.text = ""

        # Save the document
        document.save(path_outfile)
```

## Replace Text Based on a Regular Expression

If you want to replace some phrases based on regular expression, you first need to find all the phrases matching that particular regular expression using TextFragmentAbsorber. This class is employed to search for text fragments that match a specific pattern or phrase. By setting text_search_options with TextSearchOptions(True), the absorber interprets the input string as a regular expression.

The following code snippet shows you how to replace text based on a regular expression.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber("\\d{4}-\\d{4}") # Like 1999-2000

        # Set text search option to specify regular expression usage
        absorber.text_search_options = ap.text.TextSearchOptions(True)

        # Accept the absorber for a single page
        document.pages[1].accept(absorber)

        # Loop through the fragments
        for text_fragment in absorber.text_fragments:
            # Update text and other properties
            text_fragment.text = "New Phrase"
            # Set to an instance of an object.
            text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            text_fragment.text_state.font_size = 22
            text_fragment.text_state.foreground_color = ap.Color.from_rgb(drawing.Color.blue)
            text_fragment.text_state.background_color = ap.Color.from_rgb(drawing.Color.green)

        # Save the document
        document.save(path_outfile)
```

## Replace fonts in existing PDF file

Aspose.PDF for Python via .NET supports the capability to replace text in PDF document. However, sometimes you have a requirement to only replace the font being used inside PDF document.

TextFragmentAbsorber class is used to search and manipulate text fragments within a PDF. By initializing it with the specified TextEditOptions, it can process all text segments in the document accordingly.

The following code snippet shows how to replace the font inside PDF document.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create text edit options
        options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)
        # Search text fragments and set edit option as remove unused fonts
        absorber = ap.text.TextFragmentAbsorber(options)
        # Accept the absorber for all the pages
        document.pages.accept(absorber)
        # Traverse through all the text_fragments
        for text_fragment in absorber.text_fragments:
            # If the font name is ArialMT, replace font name with Arial
            if text_fragment.text_state.font.font_name == "Arial,Bold":
                text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Save the document
        document.save(path_outfile)
```

## Text Replacement should automatically re-arrange Page Contents

Aspose.PDF for Python via .NET supports the feature to search and replace text inside the PDF file. However recently some customers encountered issues during text replace when particular TextFragment is replaced with smaller contents and some extra spaces are displayed in resultant PDF or in case the TextFragment is replaced with some longer string, then words overlap existing page contents. So the requirement was to introduce a mechanism that once the text inside a PDF document is replaced, the contents should be re-arranged.

In order to cater above-stated scenarios, Aspose.PDF for Python via .NET has been enhanced so that no such issues appear when replacing text inside PDF file. The following code snippet shows how to replace text inside PDF file and the page contents should be re-arranged automatically.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create TextFragment Absorber object with regular expression
        absorber = ap.text.TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]")
        document.pages.accept(absorber)
        # Replace each TextFragment
        for text_fragment in absorber.text_fragments:
            # Set font of text fragment being replaced
            text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
            # Set font size
            text_fragment.text_state.font_size = 12
            text_fragment.text_state.foreground_color = ap.Color.navy
            # Replace the text with larger string than placeholder
            text_fragment.text = "This is a Larger String for the Testing of this issue"
        # Save PDF document
        document.save(path_outfile)
```

## Rendering Replaceable Symbols during PDF creation

Replaceable symbols are special symbols in a text string that can be replaced with corresponding content at run time.

- create a TextParagraph object. It will add text with line splitting;
- add the TextFragment with 'paragraph.append_line';
- add the TextParagraph with 'text_builder.append_paragraph'.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        page = document.pages.add()

        # Initialize new TextFragment with text containing required newline markers
        text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

        # Set text fragment properties if necessary
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment.text_state.background_color = ap.Color.light_gray
        text_fragment.text_state.foreground_color = ap.Color.red

        # Create TextParagraph object
        paragraph = ap.text.TextParagraph()

        # Add new TextFragment to paragraph
        paragraph.append_line(text_fragment)

        # Set paragraph position
        paragraph.position = ap.text.Position(100, 600)

        # Create TextBuilder object
        text_builder = ap.text.TextBuilder(page)
        # Add the TextParagraph using TextBuilder
        text_builder.append_paragraph(paragraph)
        # Save the document
        document.save(path_outfile)
```

## Replaceable symbols in Header/Footer area

Replaceable symbols can also be placed inside the Header/Footer section of PDF file. 
Please take a look over the following code snippet for details on how to add replaceable symbol in the footer section.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        page = document.pages.add()
        margin_info = ap.MarginInfo()
        margin_info.top = 90
        margin_info.bottom = 50
        margin_info.left = 50
        margin_info.right = 50
        # Assign the marginInfo instance to Margin property of sec1.PageInfo
        page.page_info.margin = margin_info

        header_footer_first = ap.HeaderFooter()
        page.header = header_footer_first
        header_footer_first.margin.left = 50
        header_footer_first.margin.right = 50

        # Instantiate a Text paragraph that will store the content to show as header
        fragment_1 = ap.text.TextFragment("report title")
        fragment_1.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment_1.text_state.font_size = 16
        fragment_1.text_state.foreground_color = ap.Color.black
        fragment_1.text_state.font_style = ap.text.FontStyles.BOLD
        fragment_1.text_state.horizontal_alignment = ap.HorizontalAlignment.CENTER
        fragment_1.text_state.line_spacing = 5
        header_footer_first.paragraphs.add(fragment_1)

        fragment_2 = ap.text.TextFragment("Report_Name")
        fragment_2.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment_2.text_state.foreground_color = ap.Color.black
        fragment_2.text_state.horizontal_alignment = ap.HorizontalAlignment.CENTER
        fragment_2.text_state.line_spacing = 5
        fragment_2.text_state.font_size = 12
        header_footer_first.paragraphs.add(fragment_2)

        # Create a HeaderFooter object for the section
        header_footer_foot = ap.HeaderFooter()
        # Set the HeaderFooter object to odd & even footer
        page.footer = header_footer_foot
        header_footer_foot.margin.left = 50
        header_footer_foot.margin.right = 50

        # Add a text paragraph containing current page number of total number of pages
        fragment_3 = ap.text.TextFragment("Generated on test date")
        fragment_4 = ap.text.TextFragment("report name ")
        fragment_5 = ap.text.TextFragment("Page $p of $P")

        # Instantiate a table object
        table2 = ap.Table()

        # Add the table in paragraphs collection of the desired section
        header_footer_foot.paragraphs.add(table2)

        # Set with column widths of the table
        table2.column_widths = "165 172 165"

        # Create rows in the table and then cells in the rows
        row3 = table2.rows.add()

        row3.cells.add()
        row3.cells.add()
        row3.cells.add()

        # Set the vertical alignment of the text as center aligned
        row3.cells[0].alignment = ap.HorizontalAlignment.LEFT
        row3.cells[1].alignment = ap.HorizontalAlignment.CENTER
        row3.cells[2].alignment = ap.HorizontalAlignment.RIGHT

        row3.cells[0].paragraphs.add(fragment_3)
        row3.cells[1].paragraphs.add(fragment_4)
        row3.cells[2].paragraphs.add(fragment_5)

        # Instantiate a table object
        table = ap.Table()

        table.column_widths = "33% 33% 34%"
        table.default_cell_padding = ap.MarginInfo()
        table.default_cell_padding.top = 10
        table.default_cell_padding.bottom = 10

        # Add the table in paragraphs collection of the desired section
        page.paragraphs.add(table)

        # Set default cell border using BorderInfo object
        table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)

        # Set table border using another customized BorderInfo object
        table.border = ap.BorderInfo(ap.BorderSide.ALL, 1)

        table.repeating_rows_count = 1

        # Create rows in the table and then cells in the rows
        row1 = table.rows.add()

        row1.cells.add("col1")
        row1.cells.add("col2")
        row1.cells.add("col3")
        CRLF = "\r\n"
        for i in range(10):
            row = table.rows.add()
            row.is_row_broken = True
            for c in range(3):
                if c == 2:
                    c1 = row.cells.add(
                        "Aspose.Total for Java is a compilation of every Java component offered by Aspose. It is compiled on a"
                        + CRLF
                        + "daily basis to ensure it contains the most up to date versions of each of our Java components. "
                        + CRLF
                        + "daily basis to ensure it contains the most up to date versions of each of our Java components. "
                        + CRLF
                        + "Using Aspose.Total for Java developers can create a wide range of applications."
                    )
                else:
                    c1 = row.cells.add("item1" + str(c))
                c1.margin = ap.MarginInfo()
                c1.margin.left = 30
                c1.margin.top = 10
                c1.margin.bottom = 10

        # Save the document
        document.save(path_outfile)
```

## Remove Unused Fonts from PDF File

Aspose.PDF for Python via .NET supports the feature to embed fonts while creating a PDF document, as well as the capability to embed fonts in existing PDF files. From Aspose.PDF for Python via .NET, it also lets you remove duplicate or unused fonts from PDF documents.

To replace fonts, use the following approach:

1. Call the [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) class.
1. Call the TextFragmentAbsorber class TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS parameter. (This removes fonts that have become unused during font replacement).
1. Set font individually for each text fragment.

The following code snippet replaces font for all text fragments of all document pages and removes unused fonts.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        options = ap.text.TextEditOptions(ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS)
        absorber = ap.text.TextFragmentAbsorber(options)
        document.pages.accept(absorber)

        # Iterate through all the text_fragments
        for text_fragment in absorber.text_fragments:
            text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial, Bold")

        # Save the document
        document.save(path_outfile)
```

## Remove All Text from PDF Document

### Remove All Text using Operators

In some text operation, you need to remove all text from PDF document and for that, you need to set found text as empty string value usually. The point is that changing the text for multitude text fragments invokes a number of checking and text position adjustment operations. They are essential in the text editing scenarios. The difficulty is that you cannot determine how many text fragments will be removed in the scenario where they are processed in a loop.

Therefore, we recommend using another approach for the scenario of removing all text from PDF pages. Please consider the following code snippet that works very fast.

1. Import the Library. The script imports aspose.pdf, a powerful library for handling PDF files programmatically.
1. Open the PDF Document. The Document(path_infile) method loads the PDF file specified by path_infile.
1. Iterate Through Pages. A loop runs from 1 to len(document.pages), meaning it processes all pages except the first one (since indexing starts at 1 here, this could be unintentional if the user wants to process the first page).
1. Select Text Operators. The OperatorSelector is used with TextShowOperator(), which identifies all text elements on a page.
1. Delete Text. The page.contents.delete(operator_selector.selected) command removes all identified text from the page.
1. Save the Modified PDF. The processed document is saved using document.save(path_outfile).

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Loop through all pages of PDF Document
        for i in range(1, len(document.pages)):
            page = document.pages[i]
            operator_selector = ap.OperatorSelector(ap.operators.TextShowOperator())
            # Select all text on the page
            page.contents.accept(operator_selector)
            # Delete all text
            page.contents.delete(operator_selector.selected)

        # Save the document
        document.save(path_outfile)
```

