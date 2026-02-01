---
title: Insert PDF pages
type: docs
weight: 50
url: /python-net/insert-pdf-pages/
description: This section explains how to insert PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Insert PDF Pages Between Two Numbers Using File Paths

A particular range of pages can be inserted from one PDF into another using [insert](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class. In order to do that, you need an input PDF file in which you want to insert the pages, a port file from which the pages need to be taken for insertion, a location where the pages are to be inserted, and a range of pages of the port file which have to be inserted in the input PDF file. This range is specified with start page and end page parameters. Finally, the output PDF file is saved with the specified range of pages inserted in the input file. The following code snippet shows you how to insert PDF pages between two numbers using file streams.

```python

from aspose.pdf.facades import PdfFileEditor

def insert_pdf_pages_between_two_numbers_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Insert pages:
    # - Insert pages 2–5 from InsertPages.pdf
    # - Into MultiplePages.pdf after page 1
    pdf_editor.insert(
        data_dir + "MultiplePages.pdf",  # destination PDF
        1,                               # position to insert after
        data_dir + "InsertPages.pdf",    # source PDF
        2,                               # start page
        5,                               # end page
        data_dir + "InsertPagesBetweenNumbers_out.pdf"
    )
```

## Insert Array of PDF Pages Using File Paths

If you want to insert some specified pages into another PDF file, then you can use an overload of the [insert](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method which requires an integer array of pages. In this array, you can specify which particular pages you want to insert in the input PDF file. In order to do that, you need an input PDF file in which you want to insert the pages, a port file from which the pages need to be taken for insertion, a location where the pages are to be inserted, and integer array of the pages from port file which have to be inserted in the input PDF file. This array contains a list of particular pages which you’re interested to insert in the input PDF file. Finally, the output PDF file is saved with the specified array of pages inserted in the input file.
The following code snippet shows you how to insert array of PDF pages using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def insert_array_of_pdf_pages_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to insert (1-based page numbers)
    pages_to_insert = [2, 3]

    # Insert selected pages into destination PDF
    pdf_editor.insert(
        data_dir + "MultiplePages.pdf",  # destination PDF
        1,                               # insert after page 1
        data_dir + "InsertPages.pdf",    # source PDF
        pages_to_insert,                 # pages to insert
        data_dir + "InsertArrayOfPages_out.pdf"
    )
```

## Insert PDF Pages between Two Numbers Using Streams

If you want to insert the range of pages using streams, you only need to use the appropriate overload of the [insert](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class. In order to do that, you need an input PDF stream in which you want to insert the pages, a port stream from which the pages need to be taken for insertion, a location where the pages are to be inserted, and a range of pages of the port stream which have to be inserted in the input PDF stream. This range is specified with start page and end page parameters. Finally, the output PDF stream is saved with the specified range of pages inserted in the input stream. The following code snippet shows you how to insert PDF pages between two numbers using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def insert_pdf_pages_between_two_numbers_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream, \
         open(data_dir + "InsertPages.pdf", "rb") as port_stream, \
         open(data_dir + "InsertPagesBetweenNumbersUsingStreams_out.pdf", "wb") as output_stream:

        # Insert pages:
        # Insert pages 1–4 from InsertPages.pdf into MultiplePages.pdf after page 1
        pdf_editor.insert(
            input_stream,
            1,
            port_stream,
            1,
            4,
            output_stream
        )
```

## Insert Array of PDF Pages Using Streams

This example demonstrates how to insert specific pages from one PDF document into another PDF using file streams. It shows how to select individual pages by their numbers and insert them at a specified position in the destination document, enabling in-memory PDF manipulation without relying on file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def insert_array_of_pdf_pages_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to insert (1-based page numbers)
    pages_to_insert = [2, 3]

    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream, \
         open(data_dir + "InsertPages.pdf", "rb") as port_stream, \
         open(data_dir + "InsertPagesUsingStreams_out.pdf", "wb") as output_stream:

        # Insert selected pages into destination PDF
        pdf_editor.insert(
            input_stream,        # destination stream
            1,                   # insert after page 1
            port_stream,         # source stream
            pages_to_insert,     # pages to insert
            output_stream        # output stream
        )
```