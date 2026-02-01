---
title: Delete PDF pages
type: docs
weight: 70
url: /python-net/delete-pdf-pages/
description: This section explains how to delete PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

If you want to delete a number of pages from the PDF file which is residing on the disk then you can use the overload of the [delete](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method which takes following three parameters: intput file path, array of page numbers to be deleted, and output PDF file path. The second parameter is an integer array representing all of the pages which need to be deleted. The specified pages are removed from the intput file and the result is saved as output file. The following code snippet shows you how to delete PDF pages using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def delete_pages():
    # Path to the documents directory
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Pages to delete 
    pages_to_delete = [1, 2]

    # Delete pages
    pdf_editor.delete(
        data_dir + "DeletePagesInput.pdf",
        pages_to_delete,
        data_dir + "DeletePagesUsingFilePath_out.pdf"
    )
```

## Delete PDF Pages Using Streams

The [delete](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class also provides an overload which allows you to delete the pages from the input PDF file, while both the input and output files are in the streams. This overload takes following three parameters: intput stream, integer array of PDF pages to be deleted, and output stream.The following code snippet shows you how to delete PDF pages using streams.

```python

from aspose.pdf.facades import PdfFileEditor

def delete_pages_using_streams():
    data_dir = RunExamples.get_data_dir_aspose_pdf_facades_pages()

    pdf_editor = PdfFileEditor()
    pages_to_delete = [1, 2]  # 1-based page indexes

    with open(data_dir + "DeletePagesInput.pdf", "rb") as input_stream:
        with open(data_dir + "DeletePagesUsingStream_out.pdf", "wb") as output_stream:
            pdf_editor.delete(input_stream, pages_to_delete, output_stream)
```