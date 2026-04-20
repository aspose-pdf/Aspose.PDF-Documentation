---
title: Format PDF Documents in Python
linktitle: Formatting PDF Document
type: docs
weight: 11
url: /python-net/formatting-pdf-document/
description: Learn how to format PDF documents, embed fonts, control viewer settings, and adjust display options in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Formatting PDF documents using Python
Abstract: The article provides a comprehensive guide on manipulating and formatting PDF documents using the Aspose.PDF library in Python. It covers various aspects of PDF customization, including setting document window and page display properties such as centering the window, reading direction, and hiding UI elements. The article explains how to retrieve and set these properties programmatically using the `Document` class. Additionally, it addresses font management, detailing how to embed Standard Type 1 fonts and other fonts into PDFs, ensuring document portability and visual consistency across systems. It also highlights techniques for setting a default font name, retrieving all fonts from a PDF, and enhancing font embedding using `FontSubsetStrategy`. Furthermore, the article elaborates on adjusting the zoom factor of PDF documents using the `GoToAction` class and configuring print dialog preset properties, including duplex printing options. Code snippets accompany each section, providing practical examples for implementing these features.
---

This guide is useful when you need to control PDF viewer behavior, font embedding, default display settings, or print preferences in Python-generated documents.

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

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
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

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### Embedding Standard Type 1 Fonts

Some PDF documents have fonts from a special Adobe font set. Fonts from this set are called “Standard Type 1 Fonts”. This set includes 14 fonts and embedding this type of fonts requires using of special flags i.e [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). Following is the code snippet which can be used to get a document with all fonts embedded including Standard Type 1 Fonts:

```python
import aspose.pdf as ap

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
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

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### Set Default Font Name while Saving PDF

When a PDF document contains fonts, which are not available in the document itself and on the device, API replaces these fonts with the default font. If the font is available (installed on the device or embedded into the document), the output PDF should have the same font (should not be replaced with the default font). The value of the default font should contain the name of the font (not the path to the font files). We have implemented a feature to set default font name while saving a document as PDF. Following code snippet can be used to set default font:

```python
import aspose.pdf as ap

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### Get All Fonts from PDF Document

In case you want to get all fonts from a PDF document, you can use [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) method provided in [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Please check following code snippet in order to get all fonts from an existing PDF document:

```python
import aspose.pdf as ap

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### Improve Fonts Embedding using FontSubsetStrategy

Following code snippet shows how to set [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) used [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) property:

```python
import aspose.pdf as ap

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)

    document.save(output_pdf)
```

### Get-Set Zoom Factor of PDF File

Sometimes, you want to determine what a PDF document's current zoom factor is. With Aspose.Pdf, you can find out the current value as well as set one.

The [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) class Destination property allows you to get the zoom value associated with a PDF file. Similarly, it can be used to set a file's zoom factor.

#### Set Zoom factor

The following code snippet shows how to set the zoom factor of a PDF file.

```python
import aspose.pdf as ap

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    document.open_action = action
    document.save(output_pdf)
```

#### Get Zoom Factor

The following code snippet shows how to get a PDF file's zoom factor.

```python
import aspose.pdf as ap

import sys
from os import path
import aspose.pdf as ap

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir  # noqa: E402

def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## Related Document Topics

- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Create PDF files in Python](/pdf/python-net/create-pdf-document/)
- [Manipulate PDF documents in Python](/pdf/python-net/manipulate-pdf-document/)
- [Optimize PDF files in Python](/pdf/python-net/optimize-pdf/)

