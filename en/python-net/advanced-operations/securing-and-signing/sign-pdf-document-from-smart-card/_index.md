---
title: Sign PDF Documents from a Smart Card in Python
linktitle: PDF Signing with Smart Card
type: docs
weight: 30
url: /python-net/sign-pdf-document-from-smart-card/
description: Learn how to sign PDF documents with smart cards and external certificates in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Sign PDF documents from a Smart Card with Python
Abstract: This guide explains how to digitally sign PDF documents using a smart card with Aspose.PDF for Python via .NET. It demonstrates how to access certificates stored on hardware devices (such as USB tokens or smart cards) through the Windows Certificate Store and apply them for signing PDF files. The documentation includes code examples that show how to locate the appropriate certificate, configure signature properties, and embed the digital signature into the PDF. This enables secure, hardware-backed signing in compliance with digital signature standards, suitable for high-trust enterprise and legal workflows.  
---

Aspose.PDF provides robust capabilities for integrating visual and cryptographic signature components, ensuring both authenticity and professional presentation in digitally signed PDF documents.

Use this workflow when your signing process depends on certificates stored in hardware-backed devices such as smart cards, USB tokens, or managed certificate stores.

## Sign With Smart Card Using Signature Field

This example demonstrates how to digitally sign a PDF document using an external certificate with Aspose.PDF for Python and apply a custom signature appearance image:

1. Opening the PDF document.
1. Creating a PdfFileSignature object and binding it to the document.
1. Retrieving a local digital certificate using a custom method `get_local_certificate()`.
1. Setting up an ExternalSignature based on the selected certificate.
1. Applying a custom signature appearance image (e.g., a company logo or handwritten signature).
1. Digitally signing the first page of the document with specified metadata (reason, contact, location).
1. Saving the signed document to a new output file.

This method is ideal for cases where signatures must be applied programmatically using external certificates—such as hardware tokens, certificate stores, or trusted providers—and presented with a personalized visual layout.

Following are the code snippets to sign a PDF document from a smart card:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## Verify Digital Signatures

This code snippet demonstrates how to verify digital signatures in a PDF document using Aspose.PDF for Python:

1. Opening the PDF file.
1. Creating a 'PdfFileSignature object' and binding it to the document.
1. Retrieving the list of all signature field names using 'get_signature_names()'.
1. Iterating through each signature and verifying its validity with 'verify_signature()'.
1. Raising an exception if any signature fails verification.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Sign with External Certificate

This code snippet demonstrates how to add and sign a digital signature field in a PDF document using Aspose.PDF for Python with an external certificate:

1. Opening the PDF file as a binary stream.
1. Creating a SignatureField and placing it on the first page of the document at a specified position.
1. Retrieving a local digital certificate using a custom method `get_local_certificate()`.
1. Setting up an ExternalSignature with metadata such as authority, reason, and contact information.
1. Assigning a unique field name to the signature field (partial_name = "sig1").
1. Adding the signature field to the form fields of the PDF.
1. Signing the field with the external certificate.
1. Saving the signed document to an output file.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## Related Security Topics

- [Secure and sign PDF files in Python](/pdf/python-net/securing-and-signing/)
- [Digitally sign PDF files in Python](/pdf/python-net/digitally-sign-pdf-file/)
- [Extract signature information from PDF in Python](/pdf/python-net/extract-image-and-signature-information/)
- [Encrypt and decrypt PDF files in Python](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

