---
title: Formatting PDF Document using Python
linktitle: Formatting PDF Document
type: docs
weight: 11
url: /python-net/formatting-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for Python via .NET. Use the next code snippet to resolve your tasks.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Formatting PDF documents using Python
Abstract: The article provides a comprehensive guide on manipulating and formatting PDF documents using the Aspose.PDF library in Python. It covers various aspects of PDF customization, including setting document window and page display properties such as centering the window, reading direction, and hiding UI elements. The article explains how to retrieve and set these properties programmatically using the `Document` class. Additionally, it addresses font management, detailing how to embed Standard Type 1 fonts and other fonts into PDFs, ensuring document portability and visual consistency across systems. It also highlights techniques for setting a default font name, retrieving all fonts from a PDF, and enhancing font embedding using `FontSubsetStrategy`. Furthermore, the article elaborates on adjusting the zoom factor of PDF documents using the `GoToAction` class and configuring print dialog preset properties, including duplex printing options. Code snippets accompany each section, providing practical examples for implementing these features.
---

## Formatting PDF Document

### Get Document Window and Page Display Properties

This topic helps you understand how to get properties of the document window, viewer application, and how pages are displayed. To set these properties:

Open the PDF file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Now, you can set the Document object's properties, such as

- CenterWindow – Center the document window on the screen. Default: false.
- Direction – Reading order. This determines how pages are laid out when displayed side by side. Default: left to right.
- DisplayDocTitle – Display the document title in the document window title bar. Default: false (the title is displayed).
- HideMenuBar – Hide or display the document window's menu bar. Default: false (menu bar is displayed).
- HideToolBar – Hide or display the document window's toolbar. Default: false (toolbar is displayed).
- HideWindowUI – Hide or display document window elements like scroll bars. Default: false (UI elements are displayed).
- NonFullScreenPageMode – How the document when it's not displayed in full-page mode.
- PageLayout – The page layout.
- PageMode – How the document is displayed when first opened. The options are show thumbnails, full-screen, show attachment panel.

The following code snippet shows you how to get the properties using [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### Set Document Window and Page Display Properties

This topic explains how to set the properties of the document window, viewer application, and page display. To set these different properties:

1. Open the PDF file using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.
1. Set the Document object's properties.
1. Save the updated PDF file using the save method.

Properties available are:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Each is used and described in the code below. The following - code snippet shows you how to set the properties using the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### Embedding Standard Type 1 Fonts

Some PDF documents have fonts from a special Adobe font set. Fonts from this set are called “Standard Type 1 Fonts”. This set includes 14 fonts and embedding this type of fonts requires using of special flags i.e [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Following is the code snippet which can be used to get a document with all fonts embedded including Standard Type 1 Fonts:

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### Embedding Fonts while creating PDF

If you need to use any font other than the 14 core fonts supported by Adobe Reader, you must embed the font description while generating the PDF file. If font information is not embedded, Adobe Reader will take it from the Operating System if it's installed over the system, or it will construct a substitute font according to the font descriptor in the PDF.

>Please note the embedded font must be installed on the host machine i.e. in case of the following code ‘Univers Condensed’ font is installed over the system.

We use the property 'is_embedded' to embed the font information into PDF file. Setting the value of this property to 'True' will embed the complete font file into the PDF, knowing the fact that it will increase the PDF file size. Following is the code snippet that can be used to embed the font information into PDF.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### Set Default Font Name while Saving PDF

When a PDF document contains fonts, which are not available in the document itself and on the device, API replaces these fonts with the default font. If the font is available (installed on the device or embedded into the document), the output PDF should have the same font (should not be replaced with the default font). The value of the default font should contain the name of the font (not the path to the font files). We have implemented a feature to set default font name while saving a document as PDF. Following code snippet can be used to set default font:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### Get All Fonts from PDF Document

In case you want to get all fonts from a PDF document, you can use [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) method provided in [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Please check following code snippet in order to get all fonts from an existing PDF document:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### Improve Fonts Embedding using FontSubsetStrategy

Following code snippet shows how to set [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) used [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) property:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### Get-Set Zoom Factor of PDF File

Sometimes, you want to determine what a PDF document's current zoom factor is. With Aspose.Pdf, you can find out the current value as well as set one.

The [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) class Destination property allows you to get the zoom value associated with a PDF file. Similarly, it can be used to set a file's zoom factor.

#### Set Zoom factor

The following code snippet shows how to set the zoom factor of a PDF file.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### Get Zoom Factor

The following code snippet shows how to get a PDF file's zoom factor.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### Setting Print Dialog Preset Properties

Aspoose.PDF allows setting the [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) members of a PDF document. It allows you to change the DuplexMode property for a PDF document which is set to simplex by default. This can be achieved using two different methodologies as shown below.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### Setting Print Dialog Preset Properties using PDF Content Editor

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```

