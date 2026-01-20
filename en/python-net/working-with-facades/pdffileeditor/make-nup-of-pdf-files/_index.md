---
title: Make NUp of PDF files
type: docs
weight: 90
url: /net/make-nup-of-pdf-files/
description: This article shows how to make NUp of PDF files work with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Make NUp of PDF Using File Paths

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF file and save it to the output PDF file. This overload allows you to make NUp using file paths.The following code snippet shows you how to make NUP using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def make_nup_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_nup(
        data_dir + "MakeNupInput.pdf",
        data_dir + "MakeNupInput2.pdf",
        data_dir + "MakeNUpUsingPaths_out.pdf"
    )
```

## Make NUp Using Page Size and File Paths

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF file and save it to the output PDF file. This overload allows you to make NUp using file paths. You can also set the page size of the output PDF file using this overload.The following code snippet shows you how to make NUp using page size and file paths.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_nup_with_page_size_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_nup(
        data_dir + "MakeNupMultiplePagesInput.pdf",
        data_dir + "MakeNUpUsingPageSizeAndPaths_out.pdf",
        page_size=PageSize.A5
    )
```

## Make NUp of PDF Using Page Size, Horizontal and Vertical Values, and File Paths

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF file and save it to the output PDF file. This overload allows you to make NUp using file paths. You can also set the page size of the output PDF file and horizontal and vertical number of pages on each output page using this overload. The following code snippet shows you how to make NUp using page size, horizontal and vertical values, and file paths.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_nup_page_size_horizontal_vertical_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.make_nup(
        data_dir + "MakeNupInput.pdf",
        data_dir + "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf",
        page_size=PageSize.A5,
        horizontal_pages=2,
        vertical_pages=3
    )
```

## Make NUp of PDF Using Array Of PDF Files and File Paths

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of an array of input PDF files and save them to a single output PDF file. This overload allows you to make NUp using file paths.The following code snippet shows you how make NUp using array of PDF files and file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def make_nup_array_of_files_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    files = [
        data_dir + "MakeNupInput.pdf",
        data_dir + "MakeNupInput2.pdf"
    ]

    pdf_editor.make_nup(
        files,
        data_dir + "MakeNUpUsingArrayOfFilesAndPaths_out.pdf",
        is_sidewise=True
    )
```

## Make NUp of PDF Using Streams

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF stream and save it to the output PDF stream. This overload allows you to make NUp using streams instead of file paths. The following code snippet shows you how to make NUp using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def make_nup_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MakeNupInput.pdf", "rb") as in1, \
         open(data_dir + "MakeNupInput2.pdf", "rb") as in2, \
         open(data_dir + "MakeNUpUsingStreams_out.pdf", "wb") as outp:

        pdf_editor.make_nup(in1, in2, outp)
```

## Make NUp of PDF Using Page Size and Streams

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF stream and save it to the output PDF stream. This overload allows you to make NUp using streams instead of file paths. You can also set the page size of the output PDF stream using this overload. The following code snippet shows you how to make NUp using page size and streams.

```python

from aspose.pdf.facades import PdfFileEditor, PageSize

def make_nup_page_size_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MakeNupInput.pdf", "rb") as inp, \
         open(data_dir + "MakeNUpUsingPageSizeAndStreams_out.pdf", "wb") as outp:

        pdf_editor.make_nup(inp, outp, 2, 3, page_size=PageSize.A5)
```

## Make NUp of PDF Using Page Size, Horizontal and Vertical Values, and Streams

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF stream and save it to the output PDF stream. This overload allows you to make NUp using streams instead of file paths. You can also set the page size of the output PDF stream and horizontal and vertical number of pages on each output page using this overload. The following code snippet shows you how to make NUp using page size, horizontal and vertical values, and streams.

```python

from aspose.pdf.facades import PdfFileEditor

def make_nup_page_size_horizontal_vertical_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MakeNupInput.pdf", "rb") as inp, \
         open(data_dir + "MakeNUpUsingPageSizeHorizontalVerticalValuesAndStreams_out.pdf", "wb") as outp:

        pdf_editor.make_nup(inp, outp, 2, 3)
```

## Make NUp of PDF Using Array Of PDF Files and Streams

The [make_n_up](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of an array of input PDF streams and save them to a single output PDF stream. This overload allows you to make NUp using streams instead of file paths. The following code snippet shows you how to make NUp using array of PDF files using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def make_nup_array_of_files_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MakeNupInput.pdf", "rb") as s1, \
         open(data_dir + "MakeNupInput2.pdf", "rb") as s2, \
         open(data_dir + "MakeNUpUsingArrayOfFilesAndStreams_out.pdf", "wb") as outp:

        streams = [s1, s2]
        pdf_editor.make_nup(streams, outp, is_sidewise=True)
```