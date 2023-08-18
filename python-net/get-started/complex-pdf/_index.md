---
title: Creating a complex PDF
linktitle: Creating a complex PDF
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Aspose.PDF for Python via .NET allows you to create more complex documents that contain images, text fragments, and tables in one document.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
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

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2020")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(descriptionText)
    description.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    description.text_state.font_size = 14
    description.horizontal_alignment = ap.HorizontalAlignment.LEFT
    page.paragraphs.add(description)

    # Add table
    table = ap.Table()

    table.column_widths = "200"
    table.border = ap.BorderInfo(ap.BorderSide.BOX, 1.0, ap.Color.dark_slate_gray)
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.BOX, 0.5, ap.Color.black)
    table.default_cell_padding = ap.MarginInfo(4.5, 4.5, 4.5, 4.5)
    table.margin.bottom = 10
    table.default_cell_text_state.font = ap.text.FontRepository.find_font("Helvetica")

    headerRow = table.rows.add()
    headerRow.cells.add("Departs City")
    headerRow.cells.add("Departs Island")

    i = 0
    while i < headerRow.cells.count:
        headerRow.cells[i].background_color = ap.Color.gray
        headerRow.cells[i].default_cell_text_state.foreground_color = ap.Color.white_smoke
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

    document.save(output_pdf)
```
