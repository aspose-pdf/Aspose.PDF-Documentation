---
title: Extract PDF pages
type: docs
weight: 40
url: /python-net/extract-pdf-pages/
description: This section explains how to extract PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Extract PDF Pages between Two Numbers Using File Paths

The [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to extract specified range of pages from a PDF file. This overload allows you to extract pages while manipulating the PDF files from the disk. This overload requires following parameters: intput file path, start page, end page, and output file path. The pages from the start page to end page will be extracted and output will be saved on the disk.The following code snippet shows you how to extract PDF pages between two numbers using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def extract_pdf_pages_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Extract pages (from page 1 to page 3, inclusive)
    pdf_editor.extract(
        data_dir + "MultiplePages.pdf",
        1,
        3,
        data_dir + "ExtractPagesBetweenNumbers_out.pdf"
    )
```

## Extract Array of PDF Pages Using File Paths

If you do not want to extract a range of pages, rather a set of particular pages, [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method allows you to do that as well. You first need to create an integer array with all the page numbers which need to be extracted. This overload of [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method takes following parameters: input PDF file, integer array of pages to be extracted, and output PDF file. The following code snippet shows you how to extract PDF pages using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def extract_pdf_pages_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Extract pages using streams (1-based page numbers)
    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream:
        with open(data_dir + "ExtractPagesBetweenTwoNumbers_out.pdf", "wb") as output_stream:
            pdf_editor.extract(input_stream, 1, 3, output_stream)
```

## Extract PDF Pages between Two Numbers Using Streams

The [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to extract a range of pages using streams. You need to pass the following paramteres to this overload: intput stream, start page, end page, and output stream. The pages specified by the range between start page and end page will be extracted from the intput stream and saved to the output stream.The following code snippet shows you how to extract PDF pages between two numbers using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def extract_array_pdf_pages_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to extract (1-based indexes)
    pages_to_extract = [1, 2]

    # Extract pages
    pdf_editor.extract(
        data_dir + "Extract.pdf",
        pages_to_extract,
        data_dir + "ExtractArrayOfPages_out.pdf"
    )
```

## Extract Array of PDF Pages Using Streams

An array of pages can be extracted from the PDF stream and saved in the output stream using appropriate overload of [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method. If you do not want to extract a range of pages, rather a set of particular pages, [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method allows you to do that as well. You first need to create an integer array with all the page numbers which need to be extracted. This overload of [extract](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method takes following parameters: input stream, integer array of pages to be extracted and output stream.
The following code snippet shows you how to extract PDF pages using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def extract_array_pdf_pages_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()
    pages_to_extract = [1, 2]  # 1-based page numbers

    # Extract pages using streams
    with open(data_dir + "MultiplePages.pdf", "rb") as input_stream:
        with open(data_dir + "ExtractArrayOfPagesUsingStreams_out.pdf", "wb") as output_stream:
            pdf_editor.extract(input_stream, pages_to_extract, output_stream)
```
