---
title: Add Text stamps in PDF via Python
linktitle: Text stamps in PDF File
type: docs
weight: 20
url: /python-net/text-stamps-in-the-pdf-file/
description: Add a text stamp to a PDF document using the TextStamp class with  Aspose.PDF for Python library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Text stamps in PDF using Python
Abstract: This article provides a comprehensive guide on adding text stamps to PDF files using the Aspose.PDF library for Python. It outlines the use of the `TextStamp` class to create customizable text stamps with properties such as font size, style, color, and alignment. The article includes code snippets demonstrating how to add a simple text stamp, configure text alignment, and apply advanced rendering modes like fill stroke text. The first section explains the creation of a `Document` and `TextStamp` object, setting text properties, and adding the stamp to a specific page. The second section introduces the `text_alignment` property to align text horizontally and vertically, providing a code example of centering text on a PDF page. The final section discusses rendering modes, demonstrating how to add fill stroke text using a `TextState` object to set stroke color and rendering mode before binding to a stamp. Each section is accompanied by practical examples to facilitate understanding and implementation.
---

## Add Text Stamp with Python

You can use [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class to add a text stamp in a PDF file. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class provides properties necessary to create a text based stamp like font size, font style, and font color etc. In order to add text stamp, you need to create a Document object and a TextStamp object using required properties. After that, you can call [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) method of the Page to add the stamp in the PDF. The following code snippet shows you how to add text stamp in the PDF file.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.aqua
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    # Save output document
    document.save(output_pdf)
```

## Define alignment for TextStamp object

Adding watermarks to PDF documents is one of the frequent demanded features and Aspose.PDF for Python is fully capable of adding Image as well as Text watermarks. We have a class named [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) which provides the feature to add text stamps over the PDF file. Recently there has been a requirement to support the feature to specify the alignment of text when using TextStamp object. So in order to fulfill this requirement, we have introduced [text_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) property in [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) class. Using this property, we can specify the [horizontal_alignment](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/#properties) text alignment.

The following code snippets shows an example on how to load an existing PDF document and add TextStamp over it.

```python

    import aspose.pdf as ap

    # Instantiate Document object with input file
    doc = ap.Document(input_pdf)
    # Instantiate FormattedText object with sample string
    text = ap.facades.FormattedText("This")
    # Add new text line to FormattedText
    text.add_new_line_text("is sample")
    text.add_new_line_text("Center Aligned")
    text.add_new_line_text("TextStamp")
    text.add_new_line_text("Object")
    # Create TextStamp object using FormattedText
    stamp = ap.TextStamp(text)
    # Specify the Horizontal Alignment of text stamp as Center aligned
    stamp.horizontal_alignment = ap.HorizontalAlignment.CENTER
    # Specify the Vertical Alignment of text stamp as Center aligned
    stamp.vertical_alignment = ap.VerticalAlignment.CENTER
    # Specify the Text Horizontal Alignment of TextStamp as Center aligned
    stamp.text_alignment = ap.HorizontalAlignment.CENTER
    # Set top margin for stamp object
    stamp.top_margin = 20
    # Add the stamp object over first page of document
    doc.pages[1].add_stamp(stamp)

    # Save the udpated document
    doc.save(output_pdf)
```

## Fill Stroke Text as Stamp in PDF File

We have implemented setting of rendering mode for text adding and editing scenarios. To render stroke text please create TextState object to transfer advanced properties. Set color for stroke. After, set text rendering mode, Next step is bind TextState, and adding Stamp.

Following code snippet demonstrates adding Fill Stroke Text:

```python

    import aspose.pdf as ap

    # Create TextState object to transfer advanced properties
    ts = ap.text.TextState()
    # Set color for stroke
    ts.stroking_color = ap.Color.gray
    # Set text rendering mode
    ts.rendering_mode = ap.text.TextRenderingMode.STROKE_TEXT
    # Load an input PDF document
    file_stamp = ap.facades.PdfFileStamp(ap.Document(input_pdf))

    stamp = ap.facades.Stamp()
    stamp.bind_logo(
        ap.facades.FormattedText(
            "PAID IN FULL",
            ap.facades.FontColor(100, 100, 100),
            ap.facades.FontStyle.TIMES_ROMAN,
            ap.facades.EncodingType.WINANSI,
            True,
            78.0,
        )
    )

    # Bind TextState
    stamp.bind_text_state(ts)
    # Set X,Y origin
    stamp.set_origin(100, 100)
    stamp.opacity = 5
    stamp.blending_space = ap.facades.BlendingColorSpace.DEVICE_RGB
    stamp.rotation = 45.0
    stamp.is_background = False
    # Add Stamp
    file_stamp.add_stamp(stamp)
    file_stamp.save(output_pdf)
    file_stamp.close()
```

