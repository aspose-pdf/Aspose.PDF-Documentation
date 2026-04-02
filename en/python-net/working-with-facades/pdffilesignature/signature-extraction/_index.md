---
title: Signature Extraction
type: docs
weight: 50
url: /python-net/signature-extraction/
description: Learn how to extract a signature image and signing certificate from a signed PDF using PdfFileSignature in Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extract Signature Image and Certificate from PDF in Python
Abstract: This article explains how to extract signature-related data from signed PDF documents with Aspose.PDF for Python via .NET. It shows how to read the first available signature, export its image, and save the associated certificate stream to an output file.
---

Aspose.PDF for Python via .NET provides the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade for inspecting and extracting data from signed PDF documents. After a PDF has been signed, you can use it to export signature resources such as the visual signature image and the certificate associated with the signature.

This example demonstrates two common extraction tasks:

1. Extract the visual image associated with a signature.
1. Extract the signing certificate from a signed PDF.

## Extract a signature image

Use this method when the PDF contains a visible signature and you want to export its image data. The example opens the signed document, gets the first available signature name, extracts the image stream, and writes it to a file.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Extract a signature certificate

Use `extract_certificate()` when you need the certificate data attached to a signature. This is useful for inspection, validation workflows, or storing the signer certificate separately from the PDF document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

