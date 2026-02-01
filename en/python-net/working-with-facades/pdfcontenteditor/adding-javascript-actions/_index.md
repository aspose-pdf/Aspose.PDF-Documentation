---
title: Adding Javascript actions PDF 
type: docs
weight: 10
url: /python-net/adding-javascript-actions/
description: Discover how to add JavaScript actions, such as button clicks or form submissions, to PDFs in Python using Aspose.PDF.
lastmod: "2025-11-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Aspose.PDF for Python via .NET allows developers to embed JavaScript actions into PDF documents programmatically. JavaScript inside PDF files can be used for a variety of purposes, such as displaying alerts, validating form fields, opening web links, or automating user interactions.

This example displays how to add a JavaScript link annotation to a PDF page using the PdfContentEditor class from the Aspose.Pdf.Facades namespace. When the user clicks the defined area in the PDF, the embedded JavaScript code will execute.

1. Instantiate PdfContentEditor to manage annotations and actions.
1. Attach the input PDF file with BindPdf().
1. Create a Rectangle object to specify the region where the JavaScript action will be triggered.
1. Write JavaScript code.
1. Create JavaScript link annotation.
1. Save the updated PDF.

```python

import os
import clr

# Add references to Aspose.PDF and System.Drawing
clr.AddReference("Aspose.PDF")
clr.AddReference("System.Drawing")

import Aspose.Pdf.Facades as pdf_facades
from System.Drawing import Rectangle, Color

def add_javascript_action():
    # Path to documents directory
    data_dir = "/path/to/documents/"  # <-- update to your actual path

    # Create PdfContentEditor
    editor = pdf_facades.PdfContentEditor()

    # Bind input PDF
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Define rectangle area for JavaScript link (x, y, width, height)
    rect = Rectangle(50, 750, 150, 30)

    # JavaScript code to execute
    code = "app.alert('Welcome to Aspose!');"

    # Create JavaScript link annotation on page 1
    editor.CreateJavaScriptLink(code, rect, 1, Color.Green)

    # Save updated PDF
    editor.Save(os.path.join(data_dir, "JavaScriptAdded_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("JavaScript action added successfully.")
```
