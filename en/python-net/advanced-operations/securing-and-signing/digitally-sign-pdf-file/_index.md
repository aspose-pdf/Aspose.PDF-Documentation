---
title: Add digital signature or digitally sign PDF in Python
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /python-net/digitally-sign-pdf-file/
description: Learn how to digitally sign PDF documents, add timestamps, and validate signatures in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Digitally sign PDF files with Python
Abstract: This guide explains how to digitally sign PDF documents using Aspose.PDF for Python via .NET. It details the process of applying standard and advanced digital signatures, utilizing certificates (PFX and PKCS#12), and customizing signature appearance and behavior. The documentation includes code examples that demonstrate how to sign existing PDFs, add timestamps, and verify signature validity. This enables developers to ensure document authenticity, integrity, and compliance with digital signature standards in their Python Applications.   
---

## Sign PDF with digital signatures

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

A **PKCS#7 detached signature** adds a digital signature to a document without embedding the content into the signature block.

Use these examples when you need to apply certificate-based signatures to PDF files, verify signature validity, or add trusted timestamps to signed documents.

The next example signs a PDF document using a PKCS#7 detached digital signature, applying the signature to the first page in a specified rectangular area.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Verify all digital signatures in a PDF document**

1. Creates an instance of PdfFileSignature that allows you to interact with signatures in PDF.
1. Get a list of signature names `get_signature_names(True)`.
1. Checks the first signature in the list `verify_signature` for compliance with the specified certificate.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**Verify a signature with a public key certificate file**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**Verify a signature with the certificate extracted from the file**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**Verify signatures with certificate-chain validation enabled**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## Add timestamp to digital signature

### How to digitally sign a PDF with timestamp

Aspose.PDF for Python supports to digitally sign the PDF with a timestamp server or Web service.

In order to accomplish this requirement, the [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) class has been added to the Aspose.PDF namespace. Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## Signing PDF documents using ECDSA

Signing PDF documents using ECDSA (Elliptic Curve Digital Signature Algorithm) involves utilizing elliptic curve cryptography to generate digital signatures.

The code snippet above illustrates how to apply a PKCS#7 detached digital signature to a PDF document using Aspose.PDF for Python. By loading the document, configuring the signature appearance and security settings, and saving the result, this example demonstrates a complete, reliable workflow for digitally signing PDF files.

This method ensures the document’s authenticity and integrity by embedding a secure, verifiable signature on the first page. The use of SHA-256 as the digest algorithm meets modern cryptographic standards, while the ability to control signature placement offers flexibility for visible approval marks.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Verify ECDSA signatures in a PDF document**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Related Security Topics

- [Secure and sign PDF files in Python](/pdf/python-net/securing-and-signing/)
- [Extract image and signature information in Python](/pdf/python-net/extract-image-and-signature-information/)
- [Sign PDF documents from a smart card in Python](/pdf/python-net/sign-pdf-document-from-smart-card/)
- [Encrypt and decrypt PDF files in Python](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)