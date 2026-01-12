---
title: Replace Text - Facades
type: docs
weight: 40
url: /python-net/replace-text-facades/
description: This section explains how to work with Text - Facades using PdfContentEditor Class.
lastmod: "2025-11-24"
---

## Replace Text in an Existing PDF File

The Replace Text example demonstrates how to search for and replace text within a PDF document using Aspose.PDF for Python via .NET. This feature is useful when you need to update terminology, correct errors, or rebrand documents without manually editing the PDF content.

1. Create an instance of PdfContentEditor to manage text editing operations.
1. Attach the input PDF file with BindPdf().
1. Call ReplaceText(oldText, newText) to replace occurrences of the specified text.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text01():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Replace text: "Value" -> "Label"
    editor.ReplaceText("Value", "Label")

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo01_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully.")
```

Check how it's looks in the original document:

![Replace Text](replace_text1.png)

And check the result after replacing the text:

![Result of replacing Text](replace_text2.png)

In the second example, you will see how, in addition to replacing the text, you can also increase or decrease the font size:

Search for and replace text within a PDF document, while also specifying the font size for the replacement text. This feature is useful when you need not only to update content but also to ensure consistent formatting across the document.

1. Create an instance of PdfContentEditor to manage text editing operations.
1. Attach the input PDF file with BindPdf().
1. Call ReplaceText(oldText, newText, fontSize) to replace occurrences of the specified text.
1. Save the updated PDF.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text02():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Replace text: "Value" -> "Label" with font size 12
    editor.ReplaceText("Value", "Label", 12)

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo02_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully with new font size.")
```

For more advanced possibilities for working with our text, we will use the [TextState](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textstate) method. With this method, we can make text bold, italic, colored, and so on.

The Replace Text with Formatting example displays how to search for and replace text within a PDF document, while also applying custom formatting such as font size and color. This feature is useful when you need to update content and ensure that the replaced text matches your desired style.

1. Create an instance of PdfContentEditor to manage text editing operations.
1. Attach the input PDF file with BindPdf().
1. Define text formatting.
1. Replace text with formatting.
1. Save the updated PDF.

```python

import os
import clr

# Add references to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades
from Aspose.Pdf.Text import TextState
import Aspose.Pdf as pdf

def replace_text03():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Define text state with formatting
    text_state = TextState()
    text_state.ForegroundColor = pdf.Color.Red
    text_state.FontSize = 12

    # Replace text: "Value" -> "Label" with formatting
    editor.ReplaceText("Value", "Label", text_state)

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo03_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully with formatting applied.")
```

In case you need to replace all the specified text in the document, use the following code snippet. That is, the replacement of the text will take place wherever the text specified for replacement will be encountered, and it will also count the number of such replacements.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text04():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Replace all occurrences of "Value" with "Label"
    count = 0
    while editor.ReplaceText("Value", "Label"):
        count += 1

    print(f"{count} occurrences have been replaced.")

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo04_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replacement completed successfully.")
```

![Replace all Text](replace_text3.png)

The following code snippet shows how to make all the text replacements but on a specific page of your document.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text05():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor object
    editor = pdf_facades.PdfContentEditor()

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Replace all occurrences of "9999" with "ABCDE" using font size 2
    count = 0
    while editor.ReplaceText("9999", 2, "ABCDE"):
        count += 1

    print(f"{count} occurrences have been replaced.")

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo05_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replacement completed successfully.")
```

In the next code snippet, we will show how to replace, for example, a given number with the letters we need.

```python

import os
import clr

# Add reference to Aspose.PDF
clr.AddReference("Aspose.PDF")

import Aspose.Pdf.Facades as pdf_facades

def replace_text06():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Instantiate PdfContentEditor with ReplaceTextStrategy
    strategy = pdf_facades.ReplaceTextStrategy()
    strategy.IsRegularExpressionUsed = True
    strategy.ReplaceScope = pdf_facades.ReplaceTextStrategy.Scope.ReplaceAll

    editor = pdf_facades.PdfContentEditor()
    editor.ReplaceTextStrategy = strategy

    # Bind PDF document
    editor.BindPdf(os.path.join(data_dir, "sample.pdf"))

    # Replace all 4-digit numbers with "ABCDE"
    editor.ReplaceText(r"\d{4}", "ABCDE")

    # Save updated PDF document
    editor.Save(os.path.join(data_dir, "PdfContentEditorDemo06_out.pdf"))

    # Dispose resources
    editor.Dispose()

    print("Text replaced successfully using regex strategy.")
```
