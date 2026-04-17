---
title: Creating a complex PDF
linktitle: Creating a complex PDF
type: docs
weight: 30
url: /python-net/complex-pdf-example/
description: Learn how to build a richer PDF layout in Python by combining images, styled text, and tables with Aspose.PDF for Python via .NET.
lastmod: "2026-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create a complex PDF using Python
Abstract: This tutorial extends the Hello World workflow by creating a more detailed PDF layout. The sample document includes a logo image, a heading, descriptive paragraph text, and a styled table with schedule data. It demonstrates how to combine common PDF building blocks in a single Python script using Aspose.PDF for Python via .NET.
---

The [Hello, World](/pdf/python-net/hello-world-example/) tutorial covers the basic PDF creation flow. This guide builds on that foundation and shows how to compose a more realistic document layout with multiple content types.

In this example, you create a PDF for a fictional passenger ferry service. The output includes:

- A logo image
- A title text fragment
- A descriptive paragraph
- A styled table with departure times

When creating this document from scratch, follow these steps:

1. Create a [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Add a [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) to the document.
1. Insert an [Image](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/) on the page.
1. Create a header [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) with custom font and alignment.
1. Add the header to page [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties).
1. Create a second [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) for the description text.
1. Add the description to page paragraphs.
1. Create and style a table (columns, borders, padding, and font).
1. Populate table rows and add the table to page paragraphs.
1. Save the output as `Complex.pdf`.

```python
from datetime import timedelta
import aspose.pdf as ap


def run_complex(self):

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()

    # Add image
    image_file_name = self.data_dir + "logo.png"
    page.add_image(image_file_name, ap.Rectangle(20, 730, 120, 830, True))

    # Add Header
    header = ap.text.TextFragment("New ferry routes in Fall 2029")
    header.text_state.font = ap.text.FontRepository.find_font("Arial")
    header.text_state.font_size = 24
    header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    header.position = ap.text.Position(130, 720)
    page.paragraphs.add(header)

    # Add description
    description_text = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
    Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
    description = ap.text.TextFragment(description_text)
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

    header_row = table.rows.add()
    header_row.cells.add("Departs City")
    header_row.cells.add("Departs Island")

    i = 0
    while i < header_row.cells.count:
        header_row.cells[i].background_color = ap.Color.gray
        header_row.cells[
            i
        ].default_cell_text_state.foreground_color = ap.Color.white_smoke
        i += 1

    time = timedelta(hours=6, minutes=0)
    inc_time = timedelta(hours=0, minutes=30)

    i = 0
    while i < 10:
        data_row = table.rows.add()
        data_row.cells.add(str(time))
        time = time.__add__(inc_time)
        data_row.cells.add(str(time))
        i += 1

    page.paragraphs.add(table)

    document.save(self.data_dir + "Complex.pdf")
```
