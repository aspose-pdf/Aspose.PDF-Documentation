---
title: Working with Operators using Python
linktitle: Working with Operators
type: docs
weight: 90
url: /python-net/working-with-operators/
description: This topic explains how to use operators with Aspose.PDF for Python via .NET. The operator classes provide great features for PDF manipulation.
lastmod: "2025-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Using Operators in PDF with Aspose.PDF for Python via .NET
Abstract: The article provides an in-depth exploration of PDF operators and their applications in manipulating PDF content streams. Operators are specialized keywords in PDF that direct particular actions, such as rendering graphical elements on a page, and are only valid within content streams. The article details a method to exert precise control over image placement in PDFs by directly manipulating content streams using low-level graphics operators. This approach is beneficial for tasks requiring exact image positioning, such as adding watermarks, aligning overlays, and creating custom layouts. Specific operators like GSave, ConcatenateMatrix, Do, and GRestore are emphasized for their roles in managing graphical states and transformations, ensuring accurate rendering without affecting other page content.
---

## Introduction to the PDF Operators and Their Usage

An operator is a PDF keyword specifying some action that shall be performed, such as painting a graphical shape on the page. An operator keyword is distinguished from a named object by the absence of an initial solidus character (2Fh). Operators are meaningful only inside the content stream.

A content stream is a PDF stream object whose data consists of instructions describing the graphical elements to be painted on a page. More details about PDF operators can be found in the [PDF specification](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Implementation details

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

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## Draw XForm on Page using Operators

This example used the power of XForms and graphics operators to efficiently reuse graphical content within a PDF. By encapsulating the image in an XForm, it can be drawn multiple times without duplicating the image data, leading to smaller file sizes and improved performance. This approach is particularly beneficial when:

- the same image or graphic needs to appear multiple times in a document.

- precise control over the placement and transformation of graphics is required.

- optimizing the PDF for performance and size is a priority.

By managing the graphics state with GSave and GRestore, and using transformation matrices with ConcatenateMatrix, this technique ensures that each graphic is rendered correctly and independently.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## Remove Graphics Objects using Operator Classes

The following code snippet shows how to remove graphics. Please note that if the PDF file contains text labels for the graphics, they might persist in the PDF file, using this approach. Therefore search the graphic operators for an alternate method to delete such images.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```

