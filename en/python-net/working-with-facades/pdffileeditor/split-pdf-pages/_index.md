---
title: Split PDF pages
type: docs
weight: 60
url: /python-net/split-pdf-pages/
description: This section explains how to split PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Split PDF Pages from First Using File Paths

The [split_from_first](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file starting from the first page and ending at the specified page number. If you want to manipulate the PDF files from the disk, you can pass the file paths of the intput and output PDF files to this method. The following code snippet shows you how to split PDF pages from first using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_from_first_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.split_from_first(
        data_dir + "MultiplePages.pdf",
        3,
        data_dir + "SplitPagesUsingPaths_out.pdf"
    )
```

## Split PDF Pages from First Using File Streams

The [split_from_first](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods)  method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file starting from the first page and ending at the specified page number. If you want to manipulate the PDF files from the streams, you can pass the input and output PDF streams to this method. The following code snippet shows you how to split PDF pages from first using file streams.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_from_first_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MultiplePages.pdf", "rb") as inp, \
         open(data_dir + "SplitPagesUsingStreams_out.pdf", "wb") as outp:

        pdf_editor.split_from_first(inp, 3, outp)
```

## Split PDF Pages to Bulk Using File Paths

The [split_to_bulks](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file into multiple sets of pages. In this example, we require two sets of pages (1, 2) and (5, 6). If you want to access the PDF file from the disk, you need to pass the input PDF as file path. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_bulk_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    page_ranges = [[1, 2], [3, 4]]

    out_streams = pdf_editor.split_to_bulks(
        data_dir + "MultiplePages.pdf",
        page_ranges
    )

    index = 1
    for stream in out_streams:
        with open(f"{data_dir}File_{index}_out.pdf", "wb") as outp:
            stream.write_to(outp)
        index += 1
```

## Split PDF Pages to Bulk Using Streams

The [split_to_bulks](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file into multiple sets of pages. In this example, we require two sets of pages (1, 2) and (5, 6). You can pass a stream to this method instead of accessing the file from the disk. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_bulk_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    ranges = [[1, 2], [3, 4]]

    with open(data_dir + "MultiplePages.pdf", "rb") as inp:
        out_streams = pdf_editor.split_to_bulks(inp, ranges)

        i = 1
        for s in out_streams:
            with open(f"{data_dir}File_{i}_out.pdf", "wb") as outp:
                s.write_to(outp)
            i += 1
```

## Split PDF Pages to End Using File Paths

The [split_to_end](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/methods/) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF from the specified page number to the end of the PDF file and save it as a new PDF. In order to do this, using file paths, you need to pass input and output file paths and the page number from where the split needs to be started. The output PDF will be saved to the disk. The following code snippet shows you how to split PDF pages to end using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_end_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pdf_editor.split_to_end(
        data_dir + "MultiplePages.pdf",
        3,
        data_dir + "SplitPagesToEndUsingPaths_out.pdf"
    )
```

## Split PDF Pages to End Using Streams

The [split_to_end](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/methods/) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF from the specified page number to the end of the PDF file and save it as a new PDF. In order to do this, using streams, you need to pass input and output streams and the page number from where the split needs to be started. The output PDF will be saved to the output stream. The following code snippet shows you how to split PDF pages to end using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_pages_to_end_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "MultiplePages.pdf", "rb") as inp, \
         open(data_dir + "SplitPagesToEndUsingStreams_out.pdf", "wb") as outp:

        pdf_editor.split_to_end(inp, 3, outp)
```

## Split PDF to Individual Pages Using File Paths

{{% alert color="primary" %}}

You can try to split PDF document and view the results online at this link:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

In order to split PDF file to individual pages, you need to pass the PDF as file path to the [split_to_pages](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/methods/) method. This method will return an array of MemoryStream containing individual pages of the PDF file. You can loop through this array of MemoryStream and save individual pages as individual PDF files on the disk. The following code snippet shows you how to split PDF to individual pages using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_to_individual_pages_using_file_paths():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    out_buffers = pdf_editor.split_to_pages(data_dir + "splitPdfToIndividualPagesInput.pdf")

    count = 1
    for buf in out_buffers:
        with open(f"{data_dir}File_{count}_out.pdf", "wb") as outp:
            buf.write_to(outp)
        count += 1
```

## Split PDF to Individual Pages Using Streams

In order to split PDF file to individual pages, you need to pass the PDF as stream to the [split_to_pages](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/methods/) method. This method will return an array of MemoryStream containing individual pages of the PDF file. You can loop through this array of MemoryStream and save individual pages as individual PDF files on the disk, or you can keep these individual pages in the memory stream for later use in your application. The following code snippet shows you how to split PDF to individual pages using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def split_pdf_to_individual_pages_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    with open(data_dir + "splitPdfToIndividualPagesInput.pdf", "rb") as inp:
        buffers = pdf_editor.split_to_pages(inp)

        i = 1
        for b in buffers:
            with open(f"{data_dir}File_{i}_out.pdf", "wb") as outp:
                b.write_to(outp)
            i += 1
```