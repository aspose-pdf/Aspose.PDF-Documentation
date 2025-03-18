---
title: Creating a complex PDF
linktitle: Creating a complex PDF
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET allows you to create more complex documents that contain images, text fragments, and tables in one document.
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Generate complex PDF with Aspose.PDF for Python
Abstract: This article provides a comprehensive guide to creating a complex PDF document using Python and the Aspose.PDF library. The example centers around a fictitious company offering passenger ferry services, illustrating the process of document creation from scratch. The document includes an image, a header, a descriptive paragraph, and a table. The steps involved include instantiating a `Document` object, adding a `Page`, inserting an `Image`, and creating `TextFragment` objects for both the header and description. The header uses Arial font at a size of 24pt and is center-aligned, while the description uses Times New Roman at 14pt with left alignment. A table is also created with specific properties and added to the page. The article includes a Python code snippet that demonstrates these steps, ensuring the document is saved as "Complex.pdf." The code illustrates the use of Aspose.PDF classes and methods to manage text, images, and table elements within a PDF document.
---

The [Hello, World](/pdf/python-net/hello-world-example/) example showed simple steps to create a PDF document using Python and Aspose.PDF. In this article, we will take a look at creating a more complex document with Aspose.PDF for Python. As an example, we'll take a document from a fictitious company that operates passenger ferry services. Our document will contain a image, two text fragments (header and paragraph), and a table. 

If we create a document from scratch we need to follow certain steps:

1. Instantiate a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object. In this step we will create an empty PDF document with some metadata but without pages.
1. Add a [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) to the document object. So, now our document will have one page.
1. Add a [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) to the Page.
1. Create a [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) for header. For the header we will use Arial font with font size 24pt and center alignment.
1. Add header to the page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Create a [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) for description. For the description we will use Arial font with font size 24pt and center alignment.
1. Add (description) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (table) to the page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Save a document "Complex.pdf".

```python

    from datetime import timedelta
    import aspose.pdf as apdf

    # Initialize document object
    document = apdf.Document()
    # Add page
    page = document.pages.add()

    # Add image
    imageFileName = self.dataDir + "logo.png"
    page.add_image(imageFileName, apdf.Rectangle(20, 730, 120, 830))

    # Add Header
    header = apdf.TextFragment("New ferry routes in Fall 2020")
    header.TextState.Font = apdf.text.FontRepository.find_font("Arial")
    header.TextState.FontSize = 24
    header.HorizontalAlignment = apdf.HorizontalAlignment.CENTER
    header.Position = apdf.Position(130, 720)
    page.Paragraphs.Add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = apdf.TextFragment(descriptionText)
    description.TextState.Font = apdf.text.FontRepository.find_font(
        "Times New Roman"
    )
    description.TextState.FontSize = 14
    description.HorizontalAlignment = apdf.HorizontalAlignment.LEFT
    page.Paragraphs.Add(description)

    # Add table
    table = apdf.Table()

    # Add table
    table = apdf.Table()

    table.column_widths = "200"
    table.border = apdf.BorderInfo(
        apdf.BorderSide.BOX, 1.0, apdf.Color.dark_slate_gray
    )
    table.default_cell_border = apdf.BorderInfo(
        apdf.BorderSide.BOX, 0.5, apdf.Color.black
    )
    table.default_cell_padding = apdf.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = apdf.text.FontRepository.find_font(
        "Helvetica"
    )

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = apdf.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = (
            apdf.Color.white_smoke
        )
        i += 1

    time = timedelta(hours=6, minutes=0)
    incTime = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        dataRow = table.rows.add()
        dataRow.cells.add(str(time))
        time = time.__add__(incTime)
        dataRow.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.dataDir + "Complex.pdf")
```
