---
title: Manipulate PDF Documents in Python
linktitle: Manipulate PDF Document
type: docs
weight: 20
url: /python-net/manipulate-pdf-document/
description: Learn how to validate, structure, and modify PDF documents in Python, including TOC management and PDF/A checks.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Guide on manipulating PDF documents using Python
Abstract: This article provides a comprehensive guide on manipulating PDF documents using Python, specifically with the Aspose.PDF library. It covers several functionalities, including validating PDF documents for PDF/A-1a and PDF/A-1b compliance using the `validate` method of the `Document` class. It also details how to add, customize, and manage a Table of Contents (TOC) in PDF files, such as setting different TabLeaderTypes, hiding page numbers, and customizing page numbering with a prefix. Additionally, the article explains how to set an expiration date for a PDF document by embedding JavaScript for access restriction and how to flatten fillable forms in a PDF to make them uneditable. Each section is accompanied by code snippets demonstrating the implementation of these features using Aspose.PDF in Python.
---

This page is useful when you need to validate PDF compliance, build or customize a table of contents, set document expiration behavior, or flatten fillable PDFs in Python workflows.

## Manipulate PDF Document in Python

## Validate PDF Document for PDF A Standard (A 1A and A 1B)

To validate a PDF document for PDF/A-1a or PDF/A-1b compatibility, use the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method. This method allows you to specify the name of the file in which the result is to be saved and the required validation type PdfFormat enumeration : PDF_A_1A or PDF_A_1B.

The following code snippet shows you how to validate PDF document for PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap

def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    _validate_pdfa_standard(input_pdf, output_pdf, ap.PdfFormat.PDF_A_1A)
```

The following code snippet shows you how to validate PDF document for PDF/A-1b.

```python
import sys
from os import path
import aspose.pdf as ap

def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    _validate_pdfa_standard(input_pdf, output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Working with TOC

### Add TOC to Existing PDF

TOC in PDF stands for "Table of Contents." It is a feature that allows users to quickly navigate through a document by providing an overview of its sections and headings. 

To add a TOC to an existing PDF file, use the Heading class in the [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace. The [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) namespace can both create new and manipulate existing PDF files. To add a TOC to an existing PDF, use the Aspose.Pdf namespace. The following code snippet shows how to create a table of contents inside an existing PDF file using Python via .NET.

```python
import sys
from os import path
import aspose.pdf as ap

def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Set different TabLeaderType for different TOC Levels

Aspose.PDF for Python also allows setting different TabLeaderType for different TOC levels. You need to set [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) property of [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap

def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Hide Page Numbers in TOC

In case if you do not want to display page numbers, along with the headings in TOC, you can use [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) property of [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Class as false. Please check following code snippet to hide page numbers in the table of contents:

```python
import sys
from os import path
import aspose.pdf as ap

def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Customize Page Numbers while adding TOC

It is common to customize the page numbering in the TOC while adding TOC in a PDF document. For example, we may need to add some prefix before page number like P1, P2, P3 and so on. In such a case, Aspose.PDF for Python provides [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) property of [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) class that can be used to customize page numbers as shown in the following code sample.

```python
import sys
from os import path
import aspose.pdf as ap

def customize_page_numbers_in_toc(input_pdf, output_pdf):  
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## How to set PDF expiry date

We apply access privileges on PDF files so that a certain group of users can access particular features/objects of PDF documents. In order to restrict the PDF file access, we usually apply encryption and we may have a requirement to set PDF file expiration, so that the user accessing/viewing the document gets a valid prompt regarding PDF file expiry.

```python
import sys
from os import path
import aspose.pdf as ap

def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Flatten Fillable PDF in Python

PDF documents often include forms with interactive fillable widgets such as radio buttons, checkboxes, text boxes, lists, etc. To make it uneditable for various application purposes, we need to flatten the PDF file.
Aspose.PDF provides the function to flatten your PDF in Python with just few line of code:

```python
import sys
from os import path
import aspose.pdf as ap

def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Related Document Topics

- [Work with PDF documents in Python](/pdf/python-net/working-with-documents/)
- [Format PDF documents in Python](/pdf/python-net/formatting-pdf-document/)
- [Create PDF files in Python](/pdf/python-net/create-pdf-document/)
- [Optimize PDF files in Python](/pdf/python-net/optimize-pdf/)
