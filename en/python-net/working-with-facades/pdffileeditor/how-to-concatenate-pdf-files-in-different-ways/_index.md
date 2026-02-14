---
title: Merge PDF files using Python
linktitle: How to merge PDF
type: docs
weight: 75
url: /python-net/how-to-concatenate-pdf-files-in-different-ways/
description: This article explains possible ways to concatenate any number of existing PDF files into a Single PDF file.
lastmod: "2026-01-05"
---

This article describes that how you can [Concatenate](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/#methods) multiple PDF Documents into a Single PDF Document with the help of [Aspose.PDF for Python via .NET](/pdf/python-net/).

It shows multiple ways to concatenate (merge) PDF files into a single PDF using Python with Aspose.PDF. The examples cover:

1. Concatenating two PDFs by file paths.
1. Concatenating two PDFs by using streams.
1. Concatenating more than two PDFs using an array of streams.

## How to Concatenate PDF Files in Different Ways

### Concatenate Two PDF Files (File Paths)

Our library demonstrates how to merge two PDF documents into a single PDF by providing their file paths. The pages from the first document are added first, followed by the pages from the second document.

```python

import aspose.pdf.facades as apf

def concatenate_two_files(input1: str, input2: str, output: str):
    pdf_editor = apf.PdfFileEditor()
    pdf_editor.concatenate(input1, input2, output)

# Example usage
concatenate_two_files(
    "FirstDocument.pdf",
    "SecondDocument.pdf",
    "ConcatenatedOutput.pdf"
)
```

### Concatenate Two PDF Files (Using Streams)

This example shows how to concatenate two PDF files using file streams. It is useful when working with in-memory files, file uploads, or when avoiding direct file path access.

```python

import aspose.pdf.facades as apf

def concatenate_streams(file1: str, file2: str, output: str):
    pdf_editor = apf.PdfFileEditor()

    with open(file1, "rb") as pdf1, \
         open(file2, "rb") as pdf2, \
         open(output, "wb") as out_stream:

        pdf_editor.concatenate(pdf1, pdf2, out_stream)

# Example usage
concatenate_streams(
    "FirstDocument.pdf",
    "SecondDocument.pdf",
    "ConcatenatedOutput_byStreams.pdf"
)
```

### Concatenate Multiple PDFs (Array of Streams)

Next code snippet illustrates how to merge multiple PDF documents into one output file using a list of input streams. It is ideal for dynamically combining an unknown number of PDF files at runtime.

```python

import aspose.pdf.facades as apf

def concatenate_multiple_streams(inputs: list[str], output: str):
    pdf_editor = apf.PdfFileEditor()

    # Open all input streams
    input_streams = [open(f, "rb") for f in inputs]

    try:
        with open(output, "wb") as out_stream:
            pdf_editor.concatenate(input_streams, out_stream)
    finally:
        # Always close streams
        for st in input_streams:
            st.close()

# Example usage
concatenate_multiple_streams(
    ["file1.pdf", "file2.pdf", "file3.pdf"],
    "Concatenated_Multiple.pdf"
)
```