---
title: Adding Annotations to existing PDF file
type: docs
weight: 80
url: /python-net/adding-annotations-to-existing-pdf-file/
description: Explore how to add annotations like comments or highlights to existing PDF documents in Python using Aspose.PDF.
lastmod: "2025-11-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Add Free Text Annotation in an Existing PDF File (facades)

The Add Free Text Annotation example shows how to insert a free‑text annotation into a PDF document using Python. Free‑text annotations are a powerful way to overlay custom text directly on top of PDF content, making them useful for notes, labels, or reviewer comments without altering the underlying document text.

This sample allows for locating existing text fragments, calculating a position relative to them, and then overlaying a free‑text annotation at the desired location.

1. Open the PDF document.
1. Initialize the content editor.
1. Locate target text.
1. Define annotation position.
1. Create the free text annotation.
1. Save the updated PDF.

The following code snippet shows you how to add free text annotation in a PDF file.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")  # Needed for Rectangle

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Text import TextFragmentAbsorber
from System.Drawing import Rectangle

def add_free_text_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Search for the text "PDF" on the first page
    tfa = TextFragmentAbsorber("PDF")
    tfa.Visit(document.Pages[1])

    # Define rectangle above the found text fragment
    rect = Rectangle(
        int(tfa.TextFragments[1].Rectangle.LLX),
        int(tfa.TextFragments[1].Rectangle.URY) + 5,
        100,   # Width
        18     # Height
    )

    # Add free text annotation on page 1
    editor.CreateFreeText(rect, "Free Text Demo", 1)

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "AddFreeTextAnnotation_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Free text annotation added successfully.")
```

## Add Text Annotation in an Existing PDF File (facades)

Insert a text annotation into a PDF document. Text annotations are commonly used for adding reviewer notes, comments, or explanations that appear as sticky notes in the PDF. Our Python library shows how to locate existing text fragments, calculate a position relative to them, and then overlay a text annotation at the desired location.

1. Load the input PDF using the Document class.
1. Create an instance of PdfContentEditor to manage annotations.
1. Locate target text.
    - Use TextFragmentAbsorber to search for the word "PDF" on the first page.
    - Call Visit() on the page to absorb matching text fragments.
1. Define annotation position.
1. Create the text annotation. Call CreateText(rect, author, contents, open, subject, pageNumber) to add the annotation.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")  # Needed for Rectangle

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Text import TextFragmentAbsorber
from System.Drawing import Rectangle

def add_text_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Search for the text "PDF" on the first page
    tfa = TextFragmentAbsorber("PDF")
    tfa.Visit(document.Pages[1])

    # Define rectangle above the found text fragment
    rect = Rectangle(
        int(tfa.TextFragments[1].Rectangle.LLX),
        int(tfa.TextFragments[1].Rectangle.URY) + 5,
        100,   # Width
        18     # Height
    )

    # Add text annotation on page 1
    editor.CreateText(
        rect,
        "Aspose User",  # Author
        "PDF is a better format for modern documents",  # Contents
        False,          # Open status
        "Key",          # Subject
        1               # Page number
    )

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "AddTextAnnotation_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Text annotation added successfully.")
```

## Add Line Annotation in an Existing PDF File (facades)

Insert a line annotation into a PDF document. Line annotations are graphical elements that allow you to draw lines with customizable styles, colors, and endings. They are often used to highlight relationships, point to specific content, or visually mark areas in a PDF.

1. Load the input PDF using the Document class.
1. Create an instance of PdfContentEditor to manage annotations.
1. Define annotation properties.
    - Specify a bounding rectangle for the annotation.
    - Provide start and end coordinates for the line.
    - Set border styles, line color, and dash pattern.
    - Define line ending styles (e.g., "Open").
1. Create the line annotation.
1. Save the updated PDF.

```python

import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf as pdf
import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Rectangle, Color

def add_line_annotation():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open PDF document
    document = pdf.Document(os.path.join(data_dir, "input.pdf"))

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor(document)

    # Create Line Annotation
    editor.CreateLine(
        Rectangle(550, 93, 562, 439),   # Bounding rectangle
        "Test",                         # Title
        556, 99,                        # Starting coordinates (X1, Y1)
        556, 443,                       # Ending coordinates (X2, Y2)
        1,                              # Starting border style
        2,                              # Ending border style
        Color.Red,                      # Line color
        "dash",                         # Line style
        [1, 0, 3],                      # Dash pattern
        ["Open", "Open"]                # Line ending styles
    )

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "AddLineAnnotation_out.pdf"))

    # Dispose resources
    editor.Dispose()
    document.Dispose()

    print("Line annotation added successfully.")
```
