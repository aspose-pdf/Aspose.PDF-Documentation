---
title: Add Text to PDF using Python
linktitle: Add Text to PDF
type: docs
weight: 10
url: /python-net/add-text-to-pdf-file/
description: This article describes various aspects of working with text in Aspose.PDF. Learn how to add text to PDF, add HTML fragments, or use custom OTF fonts.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Text to PDF using Python
Abstract: This article, authored, provides a comprehensive guide on adding text to PDF documents using Aspose.PDF for Python. It covers various techniques and functionalities available in the Aspose.PDF library to manipulate text in PDF files. The article includes detailed examples and code snippets for tasks such as adding text fragments, using custom fonts, and creating hyperlinks within PDFs. It also explores advanced features like using OTF fonts, embedding HTML content, and customizing footnotes and endnotes. The guide is designed for beginners in PDF document generation, offering step-by-step instructions and practical insights into the versatile capabilities of the Aspose.PDF library for Python via .NET. Additionally, the article addresses the creation of multi-column layouts, handling text and image inline paragraphs, and dynamically measuring text widths. The publication is by the Aspose.PDF Doc Team, and the software is available for download on multiple platforms, supporting Windows, MacOS, and Linux.
---

## Adding Text

1. Open the input PDF document using Aspose.PDF.
1. Select the particular page to which you want to add the text.
1. Create a TextFragment object. A text fragment is created with the content 'main text'. This fragment is positioned at coordinates (100, 600) on the page.
1. Setting Text Properties. Various properties of the text are set, such as font size, font type (Times New Roman), background color (light gray), and foreground color (red).
1. Create the TextBuilder Object. A TextBuilder object is instantiated with the selected page.
1. Append the Text Fragment. The text fragment created earlier is appended to the PDF page using the TextBuilder object.
1. Call [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method and save the output PDF file.

The following code snippet shows you how to add text in an existing PDF file:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get particular page
    page = document.pages[1]

    # Create text fragment
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextBuilder object
    builder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    builder.append_text(text_fragment)

    # Save resulting PDF document.
    document.save(output_pdf)             
```

## Loading Font from Stream

The following code snippet shows how to load Font from stream object when adding text to PDF document.

```python

    import aspose.pdf as ap

    # Load input PDF file
    document = ap.Document()
    document.pages.add()
    # Create text builder object for first page of document
    text_builder = ap.text.TextBuilder(document.pages[1])
    # Create text fragment with sample string
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # Load the TrueType font into stream object
        font_stream = open(input_ttf, "rb")
        # Set the font name for text string
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # Specify the position for Text Fragment
        text_fragment.position = ap.text.Position(10, 10)
        # Add the text to TextBuilder so that it can be placed over the PDF file
        text_builder.append_text(text_fragment)
        # Save resulting PDF document.
        document.save(output_pdf)
```

## Add Text using TextParagraph

The following code snippet shows you how to add text in PDF document using [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) class.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document()
    # Add page to pages collection of Document object
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # Create text paragraph
    paragraph = ap.text.TextParagraph()
    # Set subsequent lines indent
    paragraph.subsequent_lines_indent = 20
    # Specify the location to add TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # Specify word wraping mode
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # Create text fragment
    fragment1 = ap.text.TextFragment("the quick brown fox jumps over the lazy dog")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # Add fragment to paragraph
    paragraph.append_line(fragment1)
    # Add paragraph
    builder.append_paragraph(paragraph)

    # Save resulting PDF document.
    document.save(output_pdf)
```

## Add Hyperlink to TextSegment

This code demonstrates how to create dynamic and interactive content within a PDF document, including hyperlinks to external resources.

A PDF page may comprise of one or more TextFragment objects, where each TextFragment object can have one or more [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/) instance.

Please try using the following code snippet to accomplish this requirement:

```python

    import aspose.pdf as ap

    # Create document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page1 = document.pages.add()
    # Create TextFragment instance
    tf = ap.text.TextFragment("Sample Text Fragment")
    # Set horizontal alignment for TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # Create a textsegment with sample text
    segment = ap.text.TextSegment(" ... Text Segment 1...")
    # Add segment to segments collection of TextFragment
    tf.segments.append(segment)
    # Create a new TextSegment
    segment = ap.text.TextSegment("Link to Google")
    # Add segment to segments collection of TextFragment
    tf.segments.append(segment)
    # Set hyperlink for TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # Set forground color for text segment
    segment.text_state.foreground_color = ap.Color.blue
    # Set text formatting as italic
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # Create another TextSegment object
    segment = ap.text.TextSegment("TextSegment without hyperlink")
    # Add segment to segments collection of TextFragment
    tf.segments.append(segment)
    # Add TextFragment to paragraphs collection of page object
    page1.paragraphs.add(tf)
    # Save resulting PDF document.
    document.save(output_pdf)
```

## Use OTF Font

Aspose.PDF for Python via .NET offers the feature to use Custom/TrueType fonts while creating/manipulating PDF file contents so that file contents are displayed using contents other than default system fonts. 

```python

    import aspose.pdf as ap

    # Create new document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create TextFragment instnace with sample text
    fragment = ap.text.TextFragment("Sample Text in OTF font")
    # Or you can even specify the path of OTF font in system directory
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # Specify to emend font inside PDF file, so that its displayed properly,
    # Even if specific font is not installed/present over target machine
    fragment.text_state.font.is_embedded = True
    # Add TextFragment to paragraphs collection of Page instance
    page.paragraphs.add(fragment)
    # Save resulting PDF document.
    document.save(output_pdf)
```


## Add HTML String using DOM

The next Python code utilizes the Aspose.PDF library to create a PDF document with an HTML fragment. 

1. Instantiate Document. An instance of the Document class is created, representing the PDF document.
1. Add Page to the PDF document.
1. Instantiate an HtmlFragment object with HTML content
1. Set Margins for the HTML fragment. In this case, the bottom margin is set to 10 points and the top margin is set to 200 points.
1. Add HTML Fragment to Page.
1. Save PDF File.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add a page to pages collection of PDF file
    page = doc.pages.add()
    # Instantiate HtmlFragment with HTML contnets
    title = ap.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")
    # Set bottom margin information
    title.margin.bottom = 10
    # Set top margin information
    title.margin.top = 200
    # Add HTML Fragment to paragraphs collection of page
    page.paragraphs.add(title)
    # Save PDF file
    doc.save(output_pdf)
```

### Custom line style for FootNote

The following example demonstrates how to add Footnotes to the bottom of the Pdf page and define a custom line style.

```python

    import aspose.pdf as ap

    # Create Document instance
    doc = ap.Document()
    # Add page to pages collection of PDF
    page = doc.pages.add()
    # Create GraphInfo object
    graph = ap.GraphInfo()
    # Set line width as 2
    graph.line_width = 2
    # Set the color for graph object
    graph.color = ap.Color.red
    # Set dash array value as 3
    graph.dash_array = [3]
    # Set dash phase value as 1
    graph.dash_phase = 1
    # Set footnote line style for page as graph
    page.note_line_style = graph
    # Create TextFragment instance
    text = ap.text.TextFragment("Hello World")
    # Set FootNote value for TextFragment
    text.foot_note = ap.Note("foot note for test text 1")
    # Add TextFragment to paragraphs collection of first page of document
    page.paragraphs.add(text)
    # Create second TextFragment
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # Set FootNote for second text fragment
    text.foot_note = ap.Note("foot note for test text 2")
    # Add second text fragment to paragraphs collection of PDF file
    page.paragraphs.add(text)
    # Save resulting PDF document.
    doc.save(output_pdf)
```

### Customize Footnote label

The next code snippet shows how to create a PDF document with a text fragment containing a footnote.

By default, the FootNote number is incremental starting from 1. However, we may have a requirement to set a custom FootNote label. In order to accomplish this requirement, please try using the following code snippet

```python

    import aspose.pdf as ap

    # Create Document instance
    document = ap.Document()
    # Add page to pages collection of PDF
    page = document.pages.add()
    # Create GraphInfo object
    graph = ap.GraphInfo()
    # Set line width as 2
    graph.line_width = 2
    # Set the color for graph object
    graph.color = ap.Color.red
    # Set dash array value as 3
    graph.dash_array = [3]
    # Set dash phase value as 1
    graph.dash_phase = 1
    # Set footnote line style for page as graph
    page.note_line_style = graph
    # Create TextFragment instance
    text = ap.text.TextFragment("Hello World")
    # Set FootNote value for TextFragment
    text.foot_note = ap.Note("foot note for test text 1")
    # Specify custom label for FootNote
    text.foot_note.text = " Aspose"
    # Add TextFragment to paragraphs collection of first page of document
    page.paragraphs.add(text)
    # Save resulting PDF document.
    document.save(output_pdf)
```

## Adding Image and Table to Footnote

This code demonstrates how to create a PDF document with a text fragment containing a complex footnote that includes an image, text, and a table using Aspose.PDF for Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("footnote text")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Row 1 Cell 1"))
    text.foot_note.paragraphs.add(table)

    # Save resulting PDF document.
    document.save(output_pdf)
```

## How to Create EndNotes

An EndNote is a source citation that refers the readers to a specific place at the end of the paper where they can find out the source of the information or words quoted or mentioned in the paper. When using endnotes, your quoted or paraphrased sentence or summarized material is followed by a superscript number.

This code demonstrates how to add a text fragment with an endnote to a PDF document using Aspose.PDF for Python:

```python

    import aspose.pdf as ap

    # Create Document instance
    document = ap.Document()
    # Add page to pages collection of PDF
    page = document.pages.add()
    # Create TextFragment instance
    text = ap.text.TextFragment("Hello World")
    # Set EndNote value for TextFragment
    text.end_note = ap.Note("sample End note")
    # Specify custom label for FootNote
    text.end_note.text = " Aspose"
    # Add TextFragment to paragraphs collection of first page of document
    page.paragraphs.add(text)
    # Save resulting PDF document.
    document.save(output_pdf)
```

## Text and Image as InLine Paragraph

The default layout of the PDF file is flow layout (Top-Left to Bottom-Right). Therefore every new element being added to PDF file is added in the bottom right flow. However, we may have a requirement to display various page elements i.e. Image and Text at the same level (one after another). One approach can be to create a Table instance and add both elements to individual cell objects. However, another approach can be InLine paragraph. By setting IsInLineParagraph property of Image and Text as true, these paragraphs will appear as inline to other page elements.

The following code snippet shows you how to add text and Image as InLine paragraphs in PDF file.

```python

    import aspose.pdf as ap

    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of Document instance
    page = document.pages.add()
    # Create TextFragmnet
    text = ap.text.TextFragment("Hello World.. ")
    # Add text fragment to paragraphs collection of Page object
    page.paragraphs.add(text)
    # Create an image instance
    image = ap.Image()
    # Set image as inline paragraph so that it appears right after
    # The previous paragraph object (TextFragment)
    image.is_in_line_paragraph = True
    # Specify image file path
    image.file = input_jpg
    # Set image Height (optional)
    image.fix_height = 30
    # Set Image Width (optional)
    image.fix_width = 100
    # Add image to paragraphs collection of page object
    page.paragraphs.add(image)
    # Re-initialize TextFragment object with different contents
    text = ap.text.TextFragment(" Hello Again..")
    # Set TextFragment as inline paragraph
    text.is_in_line_paragraph = True
    # Add newly created TextFragment to paragraphs collection of page
    page.paragraphs.add(text)
    # Save resulting PDF document.
    document.save(output_pdf)
```

## Specify character Spacing when adding Text

The next code snippet shows how to generate a PDF document containing a text fragment with increased character Spacing. 

Text can be added inside a paragraph collection of PDF files using the TextFragment instance or by using the TextParagraph object and even you can stamp the text inside the PDF by using the TextStamp class. 

### Using TextBuilder and TextFragment

```python

    import aspose.pdf as ap

    # Create Document instance
    document = ap.Document()
    # Add page to pages collection of Document
    document.pages.add()
    # Create TextBuilder instance
    builder = ap.text.TextBuilder(document.pages[1])
    # Create text fragment instance with sample contents
    wide_fragment = ap.text.TextFragment("Text with increased character spacing")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # Specify character spacing for TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # Specify the position of TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # Append TextFragment to TextBuilder instance
    builder.append_text(wide_fragment)
    # Save resulting PDF document.
    document.save(output_pdf)
```

### Using TextParagraph

```python

    import aspose.pdf as ap

    # Create Document instance
    document = ap.Document()
    # Add page to pages collection of Document
    document.pages.add()
    # Create TextBuilder instance
    builder = ap.text.TextBuilder(document.pages[1])
    # Instantiate TextParagraph instance
    paragraph = ap.text.TextParagraph()
    # Create TextState instance to specify font name and size
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # Specify the character spacing
    state.character_spacing = 1.5
    # Append text to TextParagraph object
    tt = "This is paragraph with character spacing"
    paragraph.append_line(tt, state)
    # Specify the position for TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # Append TextParagraph to TextBuilder instance
    builder.append_paragraph(paragraph)
    # Save resulting PDF document.
    document.save(output_pdf)
```

### Using TextStamp

```python

    import aspose.pdf as ap

    # Create Document instance
    document = ap.Document()
    # Add page to pages collection of Document
    page = document.pages.add()
    # Instantiate TextStamp instance with sample text
    stamp = ap.TextStamp("This is text stamp with character spacing")
    # Specify font name for Stamp object
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # Specify Font size for TextStamp
    stamp.text_state.font_size = 12
    # Specify character specing as 1
    stamp.text_state.character_spacing = 1
    # Set the x_indent for Stamp
    stamp.x_indent = 100
    # Set the y_indent for Stamp
    stamp.y_indent = 500
    # Add textual stamp to page instance
    stamp.put(page)
    # Save resulting PDF document.
    document.save(output_pdf)
```

## Create Multi-Column PDF document

[Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/) also offers the feature to create multiple columns inside the pages of PDF documents. In order to create multi-column PDF file, we can make use of FloatingBox class as it provides column_info property to specify the number of columns inside FloatingBox and we can also specify the spacing between columns and columns widths using column_spacing and width  properties accordingly. 

Column spacing means the space between the columns and the default spacing between the columns is 1.25cm. If the column width is not specified, then [Aspose.PDF for Python via .NET](https://docs.aspose.com/pdf/python-net/) calculates width for each column automatically according to the page size and column spacing.

An example is given below to demonstrate the creation of two columns with Graphs objects (Line) and they are added to paragraphs collection of FloatingBox, which is then added paragraphs collection of Page instance.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # Specify the left margin info for the PDF file
    document.page_info.margin.left = 40
    # Specify the Right margin info for the PDF file
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # Add the line to paraphraphs collection of section object
    page.paragraphs.add(graph1)

    # Specify the coordinates for the line
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # Create string variables with text containing html tags
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> How to Steer Clear of money scams</<strong> "
        + "</font>"
    )
    # Create text paragraphs containing HTML text
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # Add four columns in the section
    box.column_info.column_count = 2
    # Set the spacing between the columns
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # Create a graphs object to draw a line
    graph2 = ap.drawing.Graph(50, 10)
    # Specify the coordinates for the line
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # Add the line to paragraphs collection of section object
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "Sed augue tortor, sodales id, luctus et, pulvinar ut, eros. Suspendisse vel dolor. Sed quam. Curabitur ut massa vitae eros euismod aliquam. Pellentesque sit amet elit. Vestibulum interdum pellentesque augue. Cras mollis arcu sit amet purus. Donec augue. Nam mollis tortor a elit. Nulla viverra nisl vel mauris. Vivamus sapien. nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et,nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim Nam justo lorem, aliquam luctus, sodales et, semper sed, enim nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales.nAenean posuere ante ut neque. Morbi sollicitudin congue felis. Praesent turpis diam, iaculis sed, pharetra non, mollis ac, mauris. Phasellus nisi ipsum, pretium vitae, tempor sed, molestie eu, dui. Duis lacus purus, tristique ut, iaculis cursus, tincidunt vitae, risus. Sed commodo. *** sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed urna. . Duis convallis ultrices nisi. Maecenas non ligula. Nunc nibh est, tincidunt in, placerat sit amet, vestibulum a, nulla. Praesent porttitor turpis eleifend ante. Morbi sodales."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # Save PDF file
    document.save(output_pdf)
```

## Working with custom Tab Stops

This Python code snippet shows how to create a PDF document containing text fragments arranged using tab stops to simulate a table structure.

Here is an example of how to set custom TAB stops.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "This is a example of forming table with TAB stops", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```

## How to Add Transparent Text in PDF

A PDF file contains Image, Text, Graph, attachment, Annotations objects and while creating TextFragment, you can set foreground, background-color information as well as text formatting. Aspose.PDF for Python via .NET supports the feature to add text with Alpha color channel. 

The following code snippet shows how to add text with transparent color.

```python

    import aspose.pdf as ap

    # Create Document instance
    document = ap.Document()
    # Create page to pages collection of PDF file
    page = document.pages.add()

    # Create TextFragment instance with sample value
    text = ap.text.TextFragment(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text "
    )
    # Create color object from Alpha channel
    color = ap.Color.from_argb(30, 0, 255, 0)
    # Set color information for text instance
    text.text_state.foreground_color = color
    # Add text to paragraphs collection of page instance
    page.paragraphs.add(text)

    document.save(output_pdf)
```

## Specify LineSpacing for Fonts

Every font has an abstract square, whose height is the intended distance between lines of type in the same type size. This square is called the em square and it is the design grid on which the glyph outlines are defined. Many letters of input font have points that are placed out of font's em square bounds, so to display the font correctly, usage of a special setting is needed.

The next code snippet loads a PDF, adds a text fragment with specific line spacing using a TrueType font, and saves the modified PDF document:

```python

    import aspose.pdf as ap

    # Load input PDF file
    document = ap.Document()
    # Create TextFormattingOptions with LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # Create text fragment with sample string
    text_fragment = ap.text.TextFragment("Hello world")

    # Load the TrueType font into stream object
    font_stream = open(input_ttf, "rb")
    # Set the font name for text string
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # Specify the position for Text Fragment
    text_fragment.position = ap.text.Position(100, 600)
    # Set TextFormattingOptions of current fragment to predefined(which points to LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # Save resulting PDF document
    document.save(output_pdf)
```

## Get Text Width Dynamically

This Python code snippet performs a comparison between the measurements of strings obtained from a font object and a text state object in Aspose.PDF:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

