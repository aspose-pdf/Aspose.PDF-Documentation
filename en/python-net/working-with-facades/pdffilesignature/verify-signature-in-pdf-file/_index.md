---
title: Verify Signature in PDF File
type: docs
weight: 30
url: /python-net/verify-signature-in-pdf/
description: This section explains how to verify signature in PDF File using PdfFileSignature class.
lastmod: "2026-01-05"
---

## Verifying that a PDF is Signed with a Given Signature

The following code snippet shows you how to verify whether PDF is signed using a given signature.

```python

from aspose.pdf.facades import PdfFileSignature

def is_pdf_signed():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Check if the document contains any signatures
    if pdf_signature.contains_signature():
        print("Document Signed")
```

### Verifying that a PDF is Signed

To determine if a file is signed, without providing the signature name, use the following code.

```python

from aspose.pdf.facades import PdfFileSignature

def is_pdf_signed_with_given_signature():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Verify specific signature field
    if pdf_signature.verify_signature("Signature1"):
        print("PDF Signed")
```

## Verify whether the Signature is Valid

[verify_signed](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/#methods) method of [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature) class allows you to validate a particular signature. This method requires signature name as input and returns true if the signature is valid. The following code snippet shows you how to validate a signature.

```python

from aspose.pdf.facades import PdfFileSignature

def is_pdf_signature_valid():
    data_dir = RunExamples.get_data_dir_aspose_pdf_security_signatures()

    input_pdf = data_dir + "signed_rsa.pdf"

    pdf_signature = PdfFileSignature()

    # Bind PDF document
    pdf_signature.bind_pdf(input_pdf)

    # Verify the specified signature
    if pdf_signature.verify_signature("Signature1"):
        print("Signature Verified")
```