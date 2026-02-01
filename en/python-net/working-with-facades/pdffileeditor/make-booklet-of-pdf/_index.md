---
title: Make Booklet of PDF
type: docs
weight: 80
url: /python-net/make-booklet-of-pdf/
description: This section explains how to make booklet of PDF with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Make Booklet of PDF Using File Paths

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF file and save it to the output PDF file. This overload allows you to make booklet using file paths. The following code snippet shows you how to make booklet using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def make_booklet_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_booklet(
        data_dir + "MakeBookletInput.pdf",
        data_dir + "MakeBookletUsingPaths_out.pdf"
    )
```

## Make Booklet of PDF Using Page Size and File Paths

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF file and save it to the output PDF file. This overload allows you to make booklet using file paths. You can also set the page size of the output PDF file with this overlaod. The following code snippet shows you how to make booklet using page size and file paths.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_booklet_with_page_size_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_booklet(
        data_dir + "MakeBookletInput.pdf",
        data_dir + "MakeBookletUsingPageSizeAndPaths_out.pdf",
        PageSize.A5
    )
```

## Make Booklet of PDF Using Page Size, Specified Left and Right Pages, and File Paths

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF file and save it to the output PDF file. This overload allows you to make booklet using file paths. You can also set the page size of the output PDF file and specify particular pages for the left and right sides of the output PDF file with this overlaod. The following code snippet shows you how to make booklet using page size, specified left and right pages and file paths.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_booklet_with_size_and_left_right_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    left_pages = [1, 5]
    right_pages = [2, 3]

    pdf_editor.make_booklet(
        data_dir + "MakeBookletMultiplePagesInput.pdf",
        data_dir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf",
        PageSize.A5,
        left_pages,
        right_pages
    )
```

## Make Booklet of PDF Using Specified Left and Right Pages, and File Paths

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF file and save it to the output PDF file. This overload allows you to make booklet using file paths. You can also specify particular pages for the left and right sides of the output PDF file with this overload.color:#000000}The following code snippet shows you how to make booklet using specified left and right pages and file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def make_booklet_left_right_only_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    left_pages = [1, 5]
    right_pages = [2, 3]

    pdf_editor.make_booklet(
        data_dir + "MakeBookletMultiplePagesInput.pdf",
        data_dir + "MakeBookletUsingLeftRightPagesAndPaths_out.pdf",
        left_pages,
        right_pages
    )
```

## Make Booklet of PDF Using Streams

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF stream and save it to the output PDF streams. This overload allows you to make booklet using streams instead of file paths. The following code snippet shows you how to make booklet using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def make_booklet_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()

    with open(data_dir + "MakeBookletInput.pdf", "rb") as inp, \
         open(data_dir + "MakeBookletUsingStreams_out.pdf", "wb") as outp:
        pdf_editor.make_booklet(inp, outp)
```

## Make Booklet of PDF Using Page Size and Streams

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF stream and save it to the output PDF stream. This overload allows you to make booklet using streams instead of file paths. You can also set the page size of the output PDF stream with this overload. The following code snippet shows you how to make booklet using page size and streams.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_booklet_page_size_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()

    with open(data_dir + "MakeBookletInput.pdf", "rb") as inp, \
         open(data_dir + "MakeBookletUsingPageSizeAndStreams_out.pdf", "wb") as outp:
        pdf_editor.make_booklet(inp, outp, PageSize.A5)
```

## Make Booklet of PDF Using Page Size, Specified Left and Right Pages, and Streams

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF stream and save it to the output PDF stream. This overload allows you to make booklet using streams instead of file paths. You can also set the page size of the output PDF file and specify particular pages for the left and right sides of the output PDF stream with this overload. The following code snippet shows you how to make booklet using page size, specified left and right pages, and streams.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_booklet_size_and_left_right_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    left_pages = [1, 5]
    right_pages = [2, 3]

    with open(data_dir + "MakeBookletMultiplePagesInput.pdf", "rb") as inp, \
         open(data_dir + "MakeBookletUsingPageSizeLeftRightPagesAndStreams_out.pdf", "wb") as outp:

        pdf_editor.make_booklet(inp, outp, PageSize.A5, left_pages, right_pages)
```

## Make Booklet of PDF Using Specified Left and Right Pages, and Streams

The [make_booklet](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to make booklet of the input PDF stream and save it to the output PDF stream. This overload allows you to make booklet using streams instead of file paths. You can also specify particular pages for the left and right sides of the output PDF stream with this overlaod. The following code snippet shows you how to make booklet using specified left and right pages and streams.

```python

from aspose.pdf.facades import PdfFileEditor

def make_booklet_left_right_only_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    left_pages = [1, 5]
    right_pages = [2, 3]

    with open(data_dir + "MakeBookletMultiplePagesInput.pdf", "rb") as inp, \
         open(data_dir + "MakeBookletUsingLeftRightPagesAndStreams_out.pdf", "wb") as outp:

        pdf_editor.make_booklet(inp, outp, left_pages, right_pages)
```