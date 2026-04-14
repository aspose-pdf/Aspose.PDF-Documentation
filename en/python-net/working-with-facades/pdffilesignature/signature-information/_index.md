---
title: Signature Information
type: docs
weight: 60
url: /python-net/signature-information/
description: Learn how to read signature names, signer details, timestamps, and signature metadata from signed PDF files using PdfFileSignature in Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Read Signature Details from PDF Documents in Python
Abstract: This article explains how to inspect signature metadata in signed PDF documents with Aspose.PDF for Python via .NET. It shows how to list signature names, read signer details, get the signing date and time, and extract the signature reason and location.
---

Aspose.PDF for Python via .NET provides the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade for inspecting digital signatures in PDF documents. After a document has been signed, you can use it to read the signature names and retrieve metadata such as the signer name, contact information, signing time, reason, and location.

This example demonstrates four common signature information tasks:

1. List all signature names in a signed PDF.
1. Read signer details for a selected signature.
1. Get the signing date and time.
1. Read the signature reason and location.

## Get signature names

Use this method when a PDF may contain one or more signatures and you want to inspect which signature entries are available. The example opens the document and prints the list returned by `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Get signer details

Once you know the signature name, you can retrieve signer-specific metadata. This example reads the signer name and contact information for the first available signature in the document.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Get signature date and time

Use `get_date_time()` to determine when a specific signature was applied. This is useful for auditing and for displaying signature history in document workflows.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Get signature reason and location

Digital signatures can also store descriptive metadata such as the signing reason and location. This example retrieves both values for the selected signature and prints them together.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```

