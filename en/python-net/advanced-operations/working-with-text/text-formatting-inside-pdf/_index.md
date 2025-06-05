---
title: Text Formatting inside PDF using Python
linktitle: Text Formatting inside PDF
type: docs
weight: 30
url: /python-net/text-formatting-inside-pdf/
description: Explore text formatting options within PDF files in Python using Aspose.PDF for customized document styling.
lastmod: "2025-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to edit Text in PDF with Python
Abstract: The article provides a comprehensive guide on various text formatting techniques in PDF documents using Aspose.PDF for Python via .NET. It covers a range of functionalities including adding line indent, creating text borders, underlining text, and adding strikeout text, among others.
---

## Text Formatting inside PDF

This example demonstrates how to create and format a PDF document. It establishes a single-page PDF that includes lengthy, repetitive text with a specially formatted paragraph, configured so that any wrapped lines appear with an indent of 20 units. In addition, several separate lines of text are added as individual paragraphs below the main block. Finally, the modified PDF is saved to a designated output path. This approach is useful for creating documents with complex text layouts and formatting, ensuring that text appearance (like indented wrapped lines) is controlled programmatically.

1. Create a New PDF Document.
1. Adding a Page and Creating a Long Text Fragment.
1. Applying Text Formatting Options.
1. Adding the Text Fragments to the Page.
1. Saving the PDF Document.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        text_fragment = "".join(["A quick brown fox jumped over the lazy dog. "] * 10)

        text = ap.text.TextFragment(text_fragment)

        # Initialize TextFormattingOptions for the text fragment and specify subsequent_lines_indent value
        text.text_state.formatting_options = ap.text.TextFormattingOptions()
        text.text_state.formatting_options.subsequent_lines_indent = 20

        page.paragraphs.add(text)

        text = ap.text.TextFragment("Line2")
        page.paragraphs.add(text)

        text = ap.text.TextFragment("Line3")
        page.paragraphs.add(text)

        text = ap.text.TextFragment("Line4")
        page.paragraphs.add(text)

        text = ap.text.TextFragment("Line5")
        page.paragraphs.add(text)

        document.save(path_outfile)
```

## How to add Text Border

The following code snippet shows, how to add a border to a text using TextBuilder and setting DrawTextRectangleBorder property of TextState:

1. Create a New PDF Document.
1. Add a Page to the Document.
1. Create a Text Fragment.
1. Set the Position of the Text Fragment.
1. Customize Text Appearance.
1. Set Border (Stroking) Properties.
1. Append the Text Fragment to the PDF Page.
1. Save the PDF Document.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
    # Add page to pages collection of PDF
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set stroking_color property for drawing border (stroking) around text rectangle
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Set draw_text_rectangle_border property value to true
    text_fragment.text_state.draw_text_rectangle_border = True
    tb = ap.text.TextBuilder(page)
    tb.append_text(text_fragment)
    # Save the document
    document.save(path_outfile)
```

## How to add Underline Text

The following code snippet shows you how to add Underline text while creating a new PDF file.

1. Create a New PDF Document.
1. Add a New Page.
1. Initialize a TextBuilder.
1. Create and Configure a Text Fragment.
1. Append the Text Fragment to the Page.
1. Save the Document.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create TextBuilder for first page
        tb = ap.text.TextBuilder(page)
        # Create text fragment with sample text
        fragment = ap.text.TextFragment("Test message")
        # Set the font for TextFragment
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 10
        # Set the formatting of text as underline
        fragment.text_state.underline = True
        # Specify the position where TextFragment needs to be placed
        fragment.position = ap.text.Position(10, 800)
        # Append TextFragment to PDF file
        tb.append_text(fragment)
        # Save the document
        document.save(path_outfile)
```

## How to add Border Around Added Text

You have control over the look and feel of the text you add. The example below shows how to add a border around a piece of text that you have added by drawing a rectangle around it. Find out more about the [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor) class.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    with ap.facades.PdfContentEditor() as editor:
        # Bind PDF document
        editor.bind_pdf(path_infile)
        line_info = ap.facades.LineInfo()
        line_info.line_width = 2
        line_info.vertice_coordinate = [0, 0, 100, 100, 50, 100]
        line_info.visibility = True
        editor.create_polygon(line_info, 1, drawing.Rectangle(0, 0, 0, 0), "")

        # Save resulting PDF document.
        editor.save(path_outfile)
```

## How to add NewLine feed

TextFragment doesn’t support line feed inside the text. However in order to add text with line feed, please use TextFragment with TextParagraph:

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
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

## How to add StrikeOut Text

The TextState class provides the capabilities to set formatting for TextFragments being placed inside PDF document.

1. Create a New PDF Document.
1. Add a Page to the Document.
1. Create and Position a Text Fragment.
1. Set Text Styling Properties.
1. Append the Text Fragment to the Page.
1. Save the PDF Document.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()
        # Create text fragment
        text_fragment = ap.text.TextFragment("main text")
        text_fragment.position = ap.text.Position(100, 600)

        # Set text properties
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
        text_fragment.text_state.background_color = ap.Color.light_gray
        text_fragment.text_state.foreground_color = ap.Color.red
        # Set StrikeOut property
        text_fragment.text_state.strike_out = True
        # Mark text as Bold
        text_fragment.text_state.font_style = ap.text.FontStyles.BOLD

        # Create TextBuilder object
        builder = ap.text.TextBuilder(page)
        # Append the text fragment to the PDF page
        builder.append_text(text_fragment)

        # Save the document
        document.save(path_outfile)
```

## Apply Gradient Shading to the Text

The next example illustrates how Aspose.PDF can be used for precise text formatting and placement in PDF generation, which is useful for creating documents with complex text layouts and visual styles.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        absorber = ap.text.TextFragmentAbsorber("Lorem ipsum")
        document.pages.accept(absorber)

        text_fragment = absorber.text_fragments[1]

        # Create new color with pattern colorspace
        color = ap.Color()
        color.pattern_color_space = ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
        text_fragment.text_state.foreground_color = color
        text_fragment.text_state.underline = True

        # Save the document
        document.save(path_outfile)
```

## How to align text to float content

Aspose.PDF supports setting text alignment for contents inside a FloatingBox element.
This example demonstrates how to create a PDF document using Aspose.PDF and dynamically add multiple floating boxes to a page. Each floating box is configured with a fixed width and height and is aligned to different vertical positions (bottom, center, and top) while maintaining right horizontal alignment. Inside each floating box, a text fragment is inserted to indicate its position, and a blue border is applied to visually demarcate each box. Finally, all the content is saved into a PDF, showcasing how to programmatically control layout elements like floating boxes for customized PDF document design.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        # Add page to pages collection of PDF
        page = document.pages.add()

        # Create float box
        float_box = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box.vertical_alignment = ap.VerticalAlignment.BOTTOM
        float_box.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box.paragraphs.add(ap.text.TextFragment("FloatingBox_bottom"))
        float_box.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box)

        # Create float box
        float_box_2 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_2.vertical_alignment = ap.VerticalAlignment.CENTER
        float_box_2.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_2.paragraphs.add(ap.text.TextFragment("FloatingBox_center"))
        float_box_2.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_2)

        # Create float box
        float_box_3 = ap.FloatingBox(100, 100)
        # Set settings to float box
        float_box_3.vertical_alignment = ap.VerticalAlignment.TOP
        float_box_3.horizontal_alignment = ap.HorizontalAlignment.RIGHT
        float_box_3.paragraphs.add(ap.text.TextFragment("FloatingBox_top"))
        float_box_3.border = ap.BorderInfo(ap.BorderSide.ALL, ap.Color.blue)
        # Add float box
        page.paragraphs.add(float_box_3)

        # Save the document
        document.save(path_outfile)
```

## Remove Hidden text

The next code snippet demonstrates how to remove hidden (invisible) text from a PDF document using the Aspose.PDF for Python library. It does so by:

1. Opening an existing PDF document.
1. Employing a TextFragmentAbsorber (with text replacement options set to avoid shifting visible content) to collect all text fragments.
1. Iterating through the text fragments and clearing the text from any fragment that is marked as invisible.
1. Saving the updated document to a new file.

```python

    import aspose.pdf as ap
    
    # Open PDF document
    with ap.Document(path_infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(ap.text.TextReplaceOptions.ReplaceAdjustment.NONE)
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(path_outfile)
```