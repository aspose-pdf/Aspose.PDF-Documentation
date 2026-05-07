---
title: Work with PDF Operators in Python
linktitle: Working with Operators
type: docs
weight: 90
url: /python-net/working-with-operators/
description: Learn how to use low-level PDF operators in Python for precise content stream manipulation and graphics control.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Use low-level PDF operators for content stream control in Python
Abstract: This article explains how to work with low-level PDF operators in Aspose.PDF for Python via .NET. Learn how to manipulate content streams directly, position graphics precisely with operator classes, and remove drawn objects from PDF pages in Python workflows.
---

## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

Use this page when you need direct control over PDF content streams in Python, such as placing graphics at exact coordinates, wrapping graphics state changes, or removing specific drawing operators from a page.

## Add Images with Operator Classes

Use low-level operator classes when you need to place image content very precisely in a PDF page stream without relying on higher-level layout abstractions.

This method provides fine-grained control over image placement within a PDF by directly manipulating the content stream with low-level graphics operators. It is particularly useful when precise positioning and transformation of images are required, such as:

- adding watermarks or logos at specific locations.
- overlaying images onto existing content with exact alignment.
- implementing custom layouts that are not achievable with higher-level abstractions.

By using operators like GSave, ConcatenateMatrix, Do, and GRestore, developers can ensure that images are rendered accurately and without unintended side effects on other page content.

- The [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) operator saves the PDF's current graphical state.
- The [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (concatenate matrix) operator is used to define how an image should be placed on the PDF page.
- The [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) operator draws the image on the page.
- The [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) operator restores the graphical state.

To add an image into a PDF file:

1. Open the PDF Document
1. Define Image Placement Coordinates
1. Access the Target Page
1. Load the Image into a Stream
1. Save the Current Graphics State
1. Create a Rectangle and Transformation Matrix
1. Apply the Transformation Matrix
1. Draw the Image
1. Restore the Previous Graphics State
1. Save the Modified PDF Document

The following code snippet shows how to use PDF operators:

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Draw XForm on Page using Operators

This example used the power of XForms and graphics operators to efficiently reuse graphical content within a PDF. By encapsulating the image in an XForm, it can be drawn multiple times without duplicating the image data, leading to smaller file sizes and improved performance. This approach is particularly beneficial when:

- the same image or graphic needs to appear multiple times in a document.

- precise control over the placement and transformation of graphics is required.

- optimizing the PDF for performance and size is a priority.

By managing the graphics state with GSave and GRestore, and using transformation matrices with ConcatenateMatrix, this technique ensures that each graphic is rendered correctly and independently.

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## Remove Graphics Objects using Operator Classes

The following code snippet shows how to remove graphics. Please note that if the PDF file contains text labels for the graphics, they might persist in the PDF file, using this approach. Therefore search the graphic operators for an alternate method to delete such images.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## Related Topics

- [Advanced PDF operations in Python](/pdf/python-net/advanced-operations/)
- [Work with PDF pages in Python](/pdf/python-net/working-with-pages/)
- [Work with images in PDF using Python](/pdf/python-net/working-with-images/)
- [Work with PDF graphs in Python](/pdf/python-net/working-with-graphs/)
