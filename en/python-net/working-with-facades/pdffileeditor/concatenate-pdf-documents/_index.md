---
title: Concatenate PDF documents in Python
linktitle: Concatenate PDF documents
type: docs
weight: 20
url: /python-net/concatenate-pdf-documents/
description: This section explains how to concatenate PDF documents with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

## Concatenate PDF files using file paths

[PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) is the class in [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) which allows you to concatenate multiple PDF files. You can not only concatenate files using FileStreams but also using MemoryStreams as well. In this article, the process of concatenating the files using MemoryStreams will be explained and then shown using the code snippet.

[Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class can be used to concatenate two PDF files. The [Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method allows you to pass three parameters: first input PDF, second input PDF, and output PDF. The final output PDF contains both the input PDF files.

The following Python code snippet shows you how to concatenate PDF files using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_files_using_file_paths():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Concatenate PDF files
    pdf_editor.concatenate(
        data_dir + "ConcatenatePdfFilesUsingFilePaths1.pdf",
        data_dir + "ConcatenatePdfFilesUsingFilePaths2.pdf",
        data_dir + "ConcatenateUsingPath_out.pdf"
    )
```

In some cases, when there are a lot of outlines, users may disable them with setting CopyOutlines to false and improve performance of concatenation.

```python

from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_files_using_file_paths_copy_outlines_disabled():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Disable copying of outlines (bookmarks)
    pdf_editor.copy_outlines = False

    # Concatenate PDF files
    pdf_editor.concatenate(
        data_dir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled1.pdf",
        data_dir + "ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled2.pdf",
        data_dir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf"
    )
```

## Concatenate multiple PDF files using MemoryStreams

[Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class takes the source PDF files and the destination PDF file as parameters. These parameters can be either paths to the PDF files on the disk or they could be MemoryStreams. Now, for this example, we’ll first create two files streams to read the PDF files from the disk. Then we’ll convert these files into byte arrays. These byte arrays of the PDF files will be converted to MemoryStreams. Once we get the MemoryStreams out of PDF files, we’ll be able to pass them on to the concatenate method and merge into a single output file.

The following Python code snippet shows you how to concatenate multiple PDF files using MemoryStreams:

```python

from aspose.pdf.facades import PdfFileEditor
from io import BytesIO

def concatenate_multiple_pdf_files_using_memory_streams():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()
    
    document1_path = data_dir + "ConcatenateMultiplePdfFilesUsingMemoryStreams1.pdf"
    document2_path = data_dir + "ConcatenateMultiplePdfFilesUsingMemoryStreams2.pdf"
    result_pdf_path = data_dir + "concatenated_out.pdf"

    # Read PDF files into memory
    with open(document1_path, "rb") as f1, open(document2_path, "rb") as f2:
        buffer1 = f1.read()
        buffer2 = f2.read()

    # Convert byte arrays into memory streams
    with BytesIO(buffer1) as stream1, BytesIO(buffer2) as stream2, BytesIO() as output_stream:
        # Create PdfFileEditor object
        pdf_editor = PdfFileEditor()

        # Concatenate both input streams and save to output stream
        pdf_editor.concatenate(stream1, stream2, output_stream)

        # Write the output stream to a file
        with open(result_pdf_path, "wb") as out_file:
            out_file.write(output_stream.getvalue())
```

## Concatenate Array of PDF Files Using File Paths

If you want to concatenate multiple PDF files, you can use the overload of the [Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method, which allows you to pass an array of PDF files. The final output is saved as a merged file created from all the files in the array.The following Python code snippet shows you how to concatenate array of PDF files using file paths.

```python

from aspose.pdf.facades import PdfFileEditor

def concatenate_array_of_pdf_files_using_file_paths():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # List of PDF files to concatenate
    files_array = [
        data_dir + "Concatenate1.pdf",
        data_dir + "Concatenate2.pdf"
    ]

    # Concatenate the array of PDF files
    pdf_editor.concatenate(files_array, data_dir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf")
```

## Concatenate Array of PDF Files Using Streams

Concatenating an array of PDF files is not limited to only files residing on the disk. You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the [Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method. First, you need to create an array of input streams and one stream for output PDF and then call the [Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) method. The output will be saved in the output stream.The following Python code snippet shows you how to concatenate array of PDF files using streams.

```python

from aspose.pdf.facades import PdfFileEditor
from io import BytesIO

def concatenate_array_of_pdf_files_using_streams():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()
    
    document1_path = data_dir + "Concatenate1.pdf"
    document2_path = data_dir + "Concatenate2.pdf"
    result_pdf_path = data_dir + "ConcatenateArrayOfPdfUsingStreams_out.pdf"

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Open PDF files as byte streams
    with open(document1_path, "rb") as f1, open(document2_path, "rb") as f2:
        stream1 = BytesIO(f1.read())
        stream2 = BytesIO(f2.read())

        # Array (list) of input streams
        input_streams = [stream1, stream2]

        # Output stream
        with BytesIO() as output_stream:
            # Concatenate the input streams
            pdf_editor.concatenate(input_streams, output_stream)

            # Save the output stream to a file
            with open(result_pdf_path, "wb") as out_file:
                out_file.write(output_stream.getvalue())
```

## Concatenating all Pdf files in Particular folder

You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following Python code snippet to achieve this functionality.

```python

import os
from aspose.pdf.facades import PdfFileEditor

def concatenating_all_pdf_files_in_particular_folder():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Retrieve all PDF files in the directory
    file_entries = [
        os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.lower().endswith(".pdf")
    ]

    result_pdf_path = os.path.join(data_dir, "ConcatenatingAllPdfFilesInParticularFolder_out.pdf")

    # Instantiate PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Concatenate all input files into a single output file
    pdf_editor.concatenate(file_entries, result_pdf_path)
```

## Concatenate PDF Forms and keep fields names unique

[PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class in [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/) offers the capability to concatenate the PDF files. Now, if the Pdf files which are to be concatenated have form fields with similar field names, Aspose.PDF provides the feature to keep the fields in the resultant Pdf file as unique and also you can specify the suffix to make the field names unique. [keep_fields_unique](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#properties) property of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) as true will make field names unique when Pdf forms are concatenated. Also, [unique_suffix](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#properties) property of PdfFileEditor can be used to specify the user defined format of the suffix which is added to field name to make it unique when forms are concatenated. This string must contain `%NUM%` substring which will be replaced with numbers in the resultant file.

Please see the following simple code snippet to achieve this functionality.

```python

from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_forms_and_keep_fields_unique():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Set input and output file paths
    input_file1 = data_dir + "ConcatenatePdfFormsAndKeepFieldsUnique1.pdf"
    input_file2 = data_dir + "ConcatenatePdfFormsAndKeepFieldsUnique2.pdf"
    out_file = data_dir + "ConcatenatePDFForms_out.pdf"

    # Create PdfFileEditor object
    file_editor = PdfFileEditor()

    # Ensure unique field IDs for all form fields
    file_editor.keep_fields_unique = True

    # Format of the suffix added to field names to make them unique
    file_editor.unique_suffix = "_%NUM%"

    # Concatenate the PDF forms into a single output file
    file_editor.concatenate(input_file1, input_file2, out_file)
```

## Concatenate PDF files and create Table Of Contents

## Concatenate PDF files

Please take a look over following code snippet for information on how to merge the PDF files.

```python

from aspose.pdf.facades import PdfFileEditor
from io import BytesIO

def concatenate_pdf_files():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Set input and output file paths
    input_file1 = data_dir + "ConcatenateInput1.pdf"
    input_file2 = data_dir + "ConcatenateInput2.pdf"
    out_file = data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Open PDF files as byte streams
    with open(input_file1, "rb") as f1, open(input_file2, "rb") as f2:
        stream1 = BytesIO(f1.read())
        stream2 = BytesIO(f2.read())

        # Concatenate streams into an output stream
        with BytesIO() as output_stream:
            pdf_editor.concatenate(stream1, stream2, output_stream)

            # Save the output stream to a file
            with open(out_file, "wb") as out_file_stream:
                out_file_stream.write(output_stream.getvalue())
```

### Insert blank page

Once the PDF files have been merged, we can insert a blank page at the beginning of document on which can can create Table Of contents. In order to accomplish this requirement, we can load the merged file into **Document** object and we need to call Page.insert(...) method to insert a blank page.

```python

import aspose.pdf as pdf

def insert_blank_page():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Open the PDF document
    doc = pdf.Document(data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf")

    # Insert a blank page at the beginning (page index 1)
    doc.pages.insert(1, pdf.Page(doc))

    # Save changes
    doc.save(data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf")
```

### Add Text Stamps

In order to create a Table of Contents, we need to add Text stamps on first page using [PdfFileStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/) objects. Stamp class provides [bind_logo()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/stamp/#methods) method to add [FormattedText](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formattedtext) and we can also specify the location to add these text stamps using `SetOrigin(..)` method. In this article, we are concatenating two PDF files, so we need to create two text stamp objects pointing to these individual documents.

```python

from aspose.pdf.facades import Stamp, FormattedText, PdfFileInfo, FontStyle, EncodingType
from aspose.pdf.facades import Color

def add_text_stamp_for_table_of_contents():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()
    input_pdf_file = data_dir + "ConcatenateInput1.pdf"

    # Create a Stamp object
    stamp = Stamp()

    # Bind text to the stamp
    formatted_text = FormattedText(
        "Table Of Contents",      # Text to display
        Color.maroon,             # Text color
        Color.transparent,        # Background color
        FontStyle.Helvetica,      # Font
        EncodingType.Winansi,     # Encoding type
        True,                     # Bold
        18                        # Font size
    )
    stamp.bind_logo(formatted_text)

    # Specify the origin of the stamp
    page_width = PdfFileInfo(input_pdf_file).get_page_width(1)
    stamp.set_origin(page_width / 3, 700)

    # Apply stamp to specific pages
    stamp.pages = [1]
```

### Create local links

Now we need to add links towards the pages inside the concatenated file. In order to accomplish this requirement, we can use [create_local_link()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/#methods) method of [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor) class. In following code snippet, we have passed Transparent as 4th argument so that the rectangle around link is not visible.

```python

from aspose.pdf.facades import PdfContentEditor
from aspose.pdf.facades import Color
from aspose.pdf import Rectangle

def create_local_links():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Create PdfContentEditor object
    content_editor = PdfContentEditor()

    # Bind the PDF document
    content_editor.bind_pdf(
        data_dir + "ConcatenatePdfFilesAndCreateTOC_out.pdf"
    )

    # Create a local link for the first document
    content_editor.create_local_link(
        Rectangle(150, 650, 100, 20),  # Link rectangle (x, y, width, height)
        2,                             # Destination page number
        1,                             # Source page number
        Color.transparent              # Border color
    )
```

### Complete code

```python

from aspose.pdf.facades import ()
from aspose.pdf import Document, Rectangle
from io import BytesIO

def complete_code():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    input_file1 = data_dir + "ConcatenateInput1.pdf"
    input_file2 = data_dir + "ConcatenateInput2.pdf"
    output_file = data_dir + "Concatenated_Table_Of_Contents_out.pdf"

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Hold the concatenated PDF in memory
    with BytesIO() as concatenated_stream:
        # Open input PDFs as streams
        with open(input_file1, "rb") as f1, open(input_file2, "rb") as f2:
            pdf_editor.concatenate(f1, f2, concatenated_stream)

        # Load concatenated PDF into Document
        concatenated_stream.seek(0)
        document = Document(concatenated_stream)

        # Insert a blank page at the beginning for TOC
        document.pages.insert(1)

        # Save document with blank page to memory
        with BytesIO() as document_with_blank_page:
            document.save(document_with_blank_page)
            document_with_blank_page.seek(0)

            # Add TOC heading and items using stamps
            with BytesIO() as document_with_toc_heading:
                file_stamp = PdfFileStamp()
                file_stamp.bind_pdf(document_with_blank_page)

                # ---- TOC Title ----
                toc_title = Stamp()
                toc_title.bind_logo(
                    FormattedText(
                        "Table Of Contents",
                        Color.maroon,
                        Color.transparent,
                        FontStyle.Helvetica,
                        EncodingType.Winansi,
                        True,
                        18
                    )
                )

                page_width = PdfFileInfo(document_with_blank_page).get_page_width(1)
                toc_title.set_origin(page_width / 3, 700)
                toc_title.pages = [1]
                file_stamp.add_stamp(toc_title)

                # ---- TOC Item 1 ----
                doc1_stamp = Stamp()
                doc1_stamp.bind_logo(
                    FormattedText(
                        "1 - Link to Document 1",
                        Color.black,
                        Color.transparent,
                        FontStyle.Helvetica,
                        EncodingType.Winansi,
                        True,
                        12
                    )
                )
                doc1_stamp.set_origin(150, 650)
                doc1_stamp.pages = [1]
                file_stamp.add_stamp(doc1_stamp)

                # ---- TOC Item 2 ----
                doc2_stamp = Stamp()
                doc2_stamp.bind_logo(
                    FormattedText(
                        "2 - Link to Document 2",
                        Color.black,
                        Color.transparent,
                        FontStyle.Helvetica,
                        EncodingType.Winansi,
                        True,
                        12
                    )
                )
                doc2_stamp.set_origin(150, 620)
                doc2_stamp.pages = [1]
                file_stamp.add_stamp(doc2_stamp)

                # Save stamped document
                file_stamp.save(document_with_toc_heading)
                file_stamp.close()
                document_with_toc_heading.seek(0)

                # ---- Create local links for TOC ----
                content_editor = PdfContentEditor()
                content_editor.bind_pdf(document_with_toc_heading)

                # Link to first document (starts on page 2)
                content_editor.create_local_link(
                    Rectangle(150, 650, 100, 20),
                    2,
                    1,
                    Color.transparent
                )

                # Link to second document
                first_doc_pages = PdfFileInfo(input_file1).number_of_pages
                content_editor.create_local_link(
                    Rectangle(150, 620, 100, 20),
                    first_doc_pages + 2,  # TOC page + first document pages
                    1,
                    Color.transparent
                )

                # Save final PDF
                content_editor.save(output_file)
```

## Concatenate PDF files in folder

[PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class in Aspose.Pdf.Facades namespace offers you the capability to concatenate the PDF file. You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following Python code snippet to achieve this functionality from Aspose.PDF:

```python

import os
from aspose.pdf.facades import PdfFileEditor

def concatenate_pdf_files_in_folder():
    # The path to the documents directory
    data_dir = get_data_dir_aspose_pdf_facades_concatenate()

    # Retrieve all PDF files in the directory
    file_entries = [
        os.path.join(data_dir, file_name)
        for file_name in os.listdir(data_dir)
        if file_name.lower().endswith(".pdf")
    ]

    # Create PdfFileEditor object
    pdf_editor = PdfFileEditor()

    # Concatenate all PDF files into a single output file
    pdf_editor.concatenate(
        file_entries,
        data_dir + "ConcatenatePdfFilesInFolder_out.pdf"
    )
```
