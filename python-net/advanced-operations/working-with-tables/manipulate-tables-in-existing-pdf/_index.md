---
title: Manipulate Tables in existing PDF
linktitle: Manipulate Tables
type: docs
weight: 40
url: /python-net/manipulate-tables-in-existing-pdf/
description: Discover how to manipulate tables in an existing PDF document using Python .NET, simplifying your document editing tasks.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Tables in existing PDF",
    "alternativeHeadline": "How to update Tables content in existing PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, manipulate tables",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>

## Manipulate tables in existing PDF

One of the earliest features supported by Aspose.PDF for Python via .NET is its capabilities of Working with Tables and it provides great support for adding tables in PDF files being generated from scratch or any existing PDF files. In this new release, we have implemented new feature of searching and parsing simple tables that already exist on page of PDF document. A new class named [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) provides these capabilities. The usage of TableAbsorber is very much similar to existing [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) class. The following code snippet shows the steps to update contents in particular table cell.

```python

    import aspose.pdf as ap

    # Load existing PDF file
    pdf_document = ap.Document(input_file)
    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(pdf_document.pages[1])
    # Get access to first table on page, their first cell and text fragments in it
    fragment = absorber.table_list[0].row_list[0].cell_list[0].text_fragments[1]
    # Change text of the first text fragment in the cell
    fragment.text = "hi world"
    pdf_document.save(output_file)
```

## Replace old Table with a new one in PDF document

In case you need to find a particular table and replace it with the desired one, you can use [replace()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods) the method of [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) class in order to do that. Following example demonstrate the functionality to replace the table inside PDF document:

```python

    import aspose.pdf as ap

    # Load existing PDF document
    pdf_document = ap.Document(input_file)
    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(pdf_document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Create new table
    new_table = ap.Table()
    new_table.column_widths = "100 100 100"
    new_table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 1)

    row = new_table.rows.add()
    row.cells.add("Col 1")
    row.cells.add("Col 2")
    row.cells.add("Col 3")

    # Replace the table with new one
    absorber.replace(pdf_document.pages[1], table, new_table)
    # Save document
    pdf_document.save(output_file)
```

## How to determine if table will break in the current page

This code generates a PDF document containing a table, calculates the space available on the page, and checks if adding more rows to the table will lead to a page break based on space constraints. The result is saved to an output file.

```python

    import aspose.pdf as ap

    # Instantiate an object PDF class
    pdf = ap.Document()
    # Add the section to PDF document sections collection
    page = pdf.pages.add()
    # Instantiate a table object
    table1 = ap.Table()
    table1.margin.top = 300
    # Add the table in paragraphs collection of the desired section
    page.paragraphs.add(table1)
    # Set with column widths of the table
    table1.column_widths = "100 100 100"
    # Set default cell border using BorderInfo object
    table1.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL, 0.1)
    # Set table border using another customized BorderInfo object
    table1.border = ap.BorderInfo(ap.BorderSide.ALL, 1)
    # Create MarginInfo object and set its left, bottom, right and top margins
    margin = ap.MarginInfo()
    margin.top = 5
    margin.left = 5
    margin.right = 5
    margin.bottom = 5
    # Set the default cell padding to the MarginInfo object
    table1.default_cell_padding = margin
    # If you increase the counter to 17, table will break
    # Because it cannot be accommodated any more over this page
    for row_counter in range(0, 17):
        # Create rows in the table and then cells in the rows
        row1 = table1.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
    # Get the Page Height information
    page_height = pdf.page_info.height
    # Get the total height information of Page Top & Bottom margin,
    # Table Top margin and table height.
    total_objects_height = page.page_info.margin.top + page.page_info.margin.bottom + table1.margin.top + \
                           table1.get_height(None)
    # Display Page Height, Table Height, table Top margin and Page Top
    # And Bottom margin information
    print("PDF document Height = " + str(pdf.page_info.height) + "\nTop Margin Info = " + str(page.page_info.margin.top)
          + "\nBottom Margin Info = " + str(page.page_info.margin.bottom) + "\n\nTable-Top Margin Info = "
          + str(table1.margin.top) + "\nAverage Row Height = " + str(table1.rows[0].min_row_height) + " \nTable height "
          + str(table1.get_height(None)) + "\n ----------------------------------------" + "\nTotal Page Height ="
          + str(page_height) + "\nCummulative height including Table =" + str(total_objects_height))
    # Check if we deduct the sum of Page top margin + Page Bottom margin
    # + Table Top margin and table height from Page height and its less
    # Than 10 (an average row can be greater than 10)
    if (page_height - total_objects_height) <= 10:
        # If the value is less than 10, then display the message.
        # Which shows that another row can not be placed and if we add new
        # Row, table will break. It depends upon the row height value.
        print("Page Height - Objects Height < 10, so table will break")
    # Save the pdf document
    pdf.save(output_file)
```

## Add Repeating Column in Table

In the [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) class, you can set a [repeating_rows_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) that will repeat rows if the table is too long vertically and overflows to the next page. However, in some cases, tables are too wide to fit on a single page and needs to be continued to the next page. In order to serve the purpose, we have implemented [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) property in [Aspose.Pdf.Table](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) class. Setting this property will cause the table to break to next page column-wise and repeat given column count in the start of the next page. Following code snippet shows the usage of [repeating_columns_count](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/#properties) property:

```python

    import aspose.pdf as ap

    # Create a new document
    doc = ap.Document()
    page = doc.pages.add()
    # Instantiate an outer table that takes up the entire page
    outer_table = ap.Table()
    outer_table.column_widths = "100%"
    outer_table.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Instantiate a table object that will be nested inside outerTable that will break inside the same page
    my_table = ap.Table()
    my_table.broken = ap.TableBroken.VERTICAL_IN_SAME_PAGE
    my_table.column_adjustment = ap.ColumnAdjustment.AUTO_FIT_TO_CONTENT
    # Add the outerTable to the page paragraphs
    # Add my table to outerTable
    page.paragraphs.add(outer_table)
    body_row = outer_table.rows.add()
    body_cell = body_row.cells.add()
    body_cell.paragraphs.add(my_table)
    my_table.repeating_columns_count = 5
    page.paragraphs.add(my_table)
    # Add header Row
    row = my_table.rows.add()
    row.cells.add("header 1")
    row.cells.add("header 2")
    row.cells.add("header 3")
    row.cells.add("header 4")
    row.cells.add("header 5")
    row.cells.add("header 6")
    row.cells.add("header 7")
    row.cells.add("header 11")
    row.cells.add("header 12")
    row.cells.add("header 13")
    row.cells.add("header 14")
    row.cells.add("header 15")
    row.cells.add("header 16")
    row.cells.add("header 17")
    for row_counter in range(0, 6):
        # Create rows in the table and then cells in the rows
        row1 = my_table.rows.add()
        row1.cells.add("col " + str(row_counter) + ", 1")
        row1.cells.add("col " + str(row_counter) + ", 2")
        row1.cells.add("col " + str(row_counter) + ", 3")
        row1.cells.add("col " + str(row_counter) + ", 4")
        row1.cells.add("col " + str(row_counter) + ", 5")
        row1.cells.add("col " + str(row_counter) + ", 6")
        row1.cells.add("col " + str(row_counter) + ", 7")
        row1.cells.add("col " + str(row_counter) + ", 11")
        row1.cells.add("col " + str(row_counter) + ", 12")
        row1.cells.add("col " + str(row_counter) + ", 13")
        row1.cells.add("col " + str(row_counter) + ", 14")
        row1.cells.add("col " + str(row_counter) + ", 15")
        row1.cells.add("col " + str(row_counter) + ", 16")
        row1.cells.add("col " + str(row_counter) + ", 17")
    doc.save(output_file)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
