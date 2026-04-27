---
title: Signature Integrity Checks
type: docs
weight: 70
url: /python-net/signature-integrity-checks/
description: Learn how to check whether a PDF signature covers the whole document and validate signed document integrity using PdfFileSignature in Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Validate PDF Signature Coverage and Integrity in Python
Abstract: This article explains how to inspect digital signature integrity in signed PDF documents with Aspose.PDF for Python via .NET. It shows how to verify whether a signature covers the whole document and how to validate the integrity of the signed content.
---

Aspose.PDF for Python via .NET provides the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade for validating signed PDF documents. After a file has been signed, you can use it to check whether the signature applies to the complete document and whether the signed content is still valid.

This example demonstrates two common integrity checks:

1. Check whether a signature covers the whole document.
1. Validate the integrity of the signed PDF content.

## Check whether a signature covers the whole document

Use `covers_whole_document()` when you need to confirm that the signature applies to the complete PDF and not only to part of its content. The example reads the first available signature name and checks its coverage.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## Validate document integrity

Use `verify_signed()` to confirm that the signed document content has not been altered after the signature was applied. This method helps verify whether the document remains valid for the selected signature.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

