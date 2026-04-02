---
title: Signature Verification
type: docs
weight: 90
url: /python-net/signature-verification/
description: Learn how to verify digital signatures and check whether a PDF contains signatures using PdfFileSignature in Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Verify PDF Signatures in Python
Abstract: This article explains how to verify digital signatures in PDF documents with Aspose.PDF for Python via .NET. It shows how to validate an existing signature and how to check whether a PDF contains any signatures.
---

Aspose.PDF for Python via .NET provides the [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) facade for validating signed PDF documents. After a PDF has been signed, you can use it to confirm that a signature is valid and to detect whether the document contains any signature entries.

This example demonstrates two common verification tasks:

1. Verify that an existing PDF signature is valid.
1. Check whether a PDF contains any signatures.

## Verify a PDF signature

Use `verify_signature()` when you need to validate a specific signature in the document. The example resolves the first available signature name and verifies whether that signature is valid.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Check whether a PDF contains signatures

Use `contains_signature()` when you only need to know whether the PDF includes any signatures at all. This is useful as a quick check before running more detailed verification or extraction logic.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path

def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
