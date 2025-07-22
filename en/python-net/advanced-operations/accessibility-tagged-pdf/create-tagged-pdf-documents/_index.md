---
title: Create Tagged PDF using Python
linktitle: Create Tagged PDF
type: docs
weight: 10
url: /python-net/create-tagged-pdf/
description: This article explains how to create structure's elements for Tagged PDF document programmatically using Aspose.PDF for Python via .NET.
lastmod: "2025-06-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Creating a Tagged PDF means adding (or creating) certain elements to the document that will enable the document to be validated in accordance with PDF/UA requirements. These elements are called often Structure Elements.

## Creating Tagged PDF (Simple Scenario)

In order to create structure elements in a Tagged PDF Document, Aspose.PDF offers methods to create structure elements using the [ITaggedContent](https://reference.aspose.com/pdf/python-net/aspose.pdf.tagged/itaggedcontent/) interface. This example creates a Tagged PDF document — a PDF with semantic structure, making it more accessible and compliant with standards like PDF/UA.
Following code snippet shows how to create Tagged PDF which contains 2 elements: header and paragraph.

```python

    import aspose.pdf as ap

    # Create PDF Document
    document = ap.Document()

    # Get Content for working with TaggedPdf
    tagged_content = document.tagged_content
    root_element = tagged_content.root_element

    # Set Title and Language for Document
    tagged_content.set_title("Tagged Pdf Document")
    tagged_content.set_language("en-US")
    main_header = tagged_content.create_header_element()
    main_header.set_text("Main Header")
    paragraph_element = tagged_content.create_paragraph_element()
    paragraph_element.set_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
                                "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
                                "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
                                "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
                                "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
                                "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
                                "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
                                "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
                                "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.")
    root_element.append_child(main_header, True)
    root_element.append_child(paragraph_element, True)

    # Save Tagged PDF Document
    document.save(path_outfile)
```

```python

    import aspose.pdf as ap

    # Create PDF Document
    document = ap.Document()

    # Get Content for working with TaggedPdf
    tagged_content = document.tagged_content
    root_element = tagged_content.root_element

    # Set Title and Language for Document
    tagged_content.set_title("Tagged Pdf Document")
    tagged_content.set_language("en-US")

    # Create Header Level 1
    header1 = tagged_content.create_header_element(1)
    header1.set_text("Header Level 1")

    # Create Paragraph with Quotes
    paragraph_with_quotes = tagged_content.create_paragraph_element()
    paragraph_with_quotes.structure_text_state.font = ap.text.FontRepository.find_font("Calibri")
    position_settings = ap.tagged.PositionSettings()
    position_settings.margin = ap.MarginInfo(10, 5, 10, 5)
    paragraph_with_quotes.adjust_position(position_settings)

    # Create Span Element
    span_element1 = tagged_content.create_span_element()
    span_element1.set_text(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. "
        "Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, "
        "luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada "
        "fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus "
        "condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae "
        "lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non "
        "lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit.")

    # Create Quote Element
    quote_element = tagged_content.create_quote_element()
    quote_element.set_text(
        "Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.")
    quote_element.structure_text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC

    # Create Another Span Element
    span_element2 = tagged_content.create_span_element()
    span_element2.set_text(" Sed non consectetur elit.")

    # Append Children to Paragraph
    paragraph_with_quotes.append_child(span_element1, True)
    paragraph_with_quotes.append_child(quote_element, True)
    paragraph_with_quotes.append_child(span_element2, True)

    # Append Header and Paragraph to Root Element
    root_element.append_child(header1, True)
    root_element.append_child(paragraph_with_quotes, True)

    # Save Tagged PDF Document
    document.save(path_outfile)
```

We will get the following document after creation:

![Tagged PDF document with 2 elements - Header and Paragraph](taggedpdf-01.png)

## Styling Text Structure

Tagged PDFs are structured documents that provide accessibility features and semantic meaning to the content.

The example creates a PDF document with accessibility features by using a tagged content structure. It demonstrates how to make a paragraph element with custom styling and proper document metadata.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        paragraph_element = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph_element, True)

        paragraph_element.structure_text_state.font_size = 18.0
        paragraph_element.structure_text_state.foreground_color = ap.Color.red
        paragraph_element.structure_text_state.font_style = ap.text.FontStyles.ITALIC

        paragraph_element.set_text("Red italic text.")

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Illustrating Structure Elements

Tagged PDFs are essential for accessibility compliance and provide structured content that can be properly interpreted by screen readers and other assistive technologies. Following code snippet shows how to create a tagged PDF document with an embedded image:

1. Create tagged PDF with image.
1. Configure document.
1. Create and configure figure.
1. Set positioning.
1. Save document.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")
        figure1 = tagged_content.create_figure_element()
        tagged_content.root_element.append_child(figure1, True)
        figure1.alternative_text = "Figure One"
        figure1.title = "Image 1"
        figure1.set_tag("Fig1")
        figure1.set_image(path_imagefile, 300)
        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 50
        margin_info.top = 20
        position_settings.margin = margin_info
        figure1.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Validate Tagged PDF

Aspose.PDF for Python via .NET provides the ability to validate a PDF/UA Tagged PDF Document. The 'validate_tagged_pdf' method validates PDF documents against the PDF/UA-1 standard, which is part of the ISO 14289 specification for accessible PDF documents. This ensures that PDFs are accessible to users with disabilities and assistive technologies.

- Document Structure. Proper semantic tagging and logical structure.
- Alternative Text. Alt text for images and non-text elements.
- Reading Order. Logical sequence for screen readers.
- Color and Contrast. Sufficient contrast ratios.
- Forms. Accessible form fields and labels.
- Navigation. Proper bookmarks and navigation structure.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        is_valid = document.validate(path_logfile, ap.PdfFormat.PDF_UA_1)
```

## Adjust position of Text Structure

The following code snippet shows how to adjust Text Structure position in the Tagged PDF document:

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document() as document:
        # Get Content for work with TaggedPdf
        tagged_content = document.tagged_content

        # Set Title and Language for Document
        tagged_content.set_title("Tagged Pdf Document")
        tagged_content.set_language("en-US")

        # Create paragraph
        paragraph = tagged_content.create_paragraph_element()
        tagged_content.root_element.append_child(paragraph, True)
        paragraph.set_text("Text.")

        # Adjust position
        position_settings = ap.tagged.PositionSettings()
        margin_info = ap.MarginInfo()
        margin_info.left = 300
        margin_info.top = 20
        margin_info.right = 0
        margin_info.bottom = 0
        position_settings.margin = margin_info
        position_settings.horizontal_alignment = ap.HorizontalAlignment.NONE
        position_settings.vertical_alignment = ap.VerticalAlignment.NONE
        position_settings.is_first_paragraph_in_column = False
        position_settings.is_kept_with_next = False
        position_settings.is_in_new_page = False
        position_settings.is_in_line_paragraph = False
        paragraph.adjust_position(position_settings)

        # Save Tagged PDF Document
        document.save(path_outfile)
```

## Creating Tagged PDF automatically with PDF/UA-1 conversion

Aspose.PDF enables the automatic generation of basic logical structure markup when converting a document to PDF/UA-1. Users may then manually improve upon this basic logical structure, providing additional insights regarding the document contents.

The code snippet converts an existing PDF document to PDF/UA-1 format, which is an ISO standard (ISO 14289-1) that ensures PDF documents are accessible to users with disabilities. The conversion includes automatic tagging of document elements to create a logical structure.

```python

    import aspose.pdf as ap

    # Create PDF Document
    with ap.Document(path_infile) as document:
        # Create conversion options
        options = ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_UA_1, ap.ConvertErrorAction.DELETE)
        # Create auto-tagging settings
        # aspose.pdf.AutoTaggingSettings.default may be used to set the same settings as given below
        auto_tagging_settings = ap.AutoTaggingSettings()
        # Enable auto-tagging during the conversion process
        auto_tagging_settings.enable_auto_tagging = True
        # Use the heading recognition strategy that's optimal for the given document structure
        auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO
        # Assign auto-tagging settings to be used during the conversion process
        options.auto_tagging_settings = auto_tagging_settings
        # During the conversion, the document logical structure will be automatically created
        document.convert(options)
        # Save PDF document
        document.save(path_outfile)
```