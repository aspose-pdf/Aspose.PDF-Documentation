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
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Instantiate PdfFileSignature object
    with ap.facades.PdfFileSignature(document) as signature:
        # Create PKCS#7 object for sign
        pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
        # Sign PDF file
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        #  Save PDF document
        signature.save(path_outfile)
```

A **PKCS#7 detached signature** adds a digital signature to a document without embedding the content into the signature block.

Use these examples when you need to apply certificate-based signatures to PDF files, verify signature validity, or add trusted timestamps to signed documents.

The next example signs a PDF document using a PKCS#7 detached digital signature, applying the signature to the first page in a specified rectangular area.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Instantiate PdfFileSignature object using the opened document
    with ap.facades.PdfFileSignature(document) as signature:
        # Create PKCS#7 detached object for sign
        pkcs = ap.forms.PKCS7Detached(
            path_pfxfile, password, ap.DigestHashAlgorithm.SHA256
        )
        # Sign PDF file
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        #  Save PDF document
        signature.save(path_outfile)
```

This Python code snippet verifies a digital signature in a PDF file using 'file_sign.verify_signature()' method.

1. Creates an instance of PdfFileSignature that allows you to interact with signatures in PDF.
1. Get a list of signature names `get_signature_names(True)`.
1. Checks the first signature in the list `verify_signature` for compliance with the specified certificate.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile

# Create an instance of PdfFileSignature for working with signatures in the document
with ap.facades.PdfFileSignature(path_infile) as file_sign:
    # Get a list of signatures
    signature_names = file_sign.get_signature_names(True)
    # Verify the signature with the given name.
    return file_sign.verify_signature(signature_names[0], certificate)
```

## Add timestamp to digital signature

### How to digitally sign a PDF with timestamp

Aspose.PDF for Python supports to digitally sign the PDF with a timestamp server or Web service.

In order to accomplish this requirement, the [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) class has been added to the Aspose.PDF namespace. Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(document) as signature:
        pkcs = ap.forms.PKCS7(path_pfxfile, password)
        # Create TimestampSettings settings
        timestamp_settings = ap.TimestampSettings(
            "https://freetsa.org/tsr", "", ap.DigestHashAlgorithm.SHA256
        )  # User/Password can be omitted
        pkcs.timestamp_settings = timestamp_settings
        rect = drawing.Rectangle(
            100, 100, 200, 100
        )  # Creating a rectangle for the signature
        # Create any of the three signature types
        signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
        # Save PDF document
        signature.save(path_outfile)
```

## Signing PDF documents using ECDSA

Signing PDF documents using ECDSA (Elliptic Curve Digital Signature Algorithm) involves utilizing elliptic curve cryptography to generate digital signatures.

The code snippet above illustrates how to apply a PKCS#7 detached digital signature to a PDF document using Aspose.PDF for Python. By loading the document, configuring the signature appearance and security settings, and saving the result, this example demonstrates a complete, reliable workflow for digitally signing PDF files.

This method ensures the document’s authenticity and integrity by embedding a secure, verifiable signature on the first page. The use of SHA-256 as the digest algorithm meets modern cryptographic standards, while the ability to control signature placement offers flexibility for visible approval marks.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Create an instance of PdfFileSignature to sign the document
    with ap.facades.PdfFileSignature(document) as signature:
        # Create a PKCS7Detached object using the provided certificate and password
        pkcs = ap.forms.PKCS7Detached(
            path_pfxfile, password, ap.DigestHashAlgorithm.SHA256
        )

        # Sign the first page of the document, setting the signature's appearance at the specified location
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

        # Save PDF document
        signature.save(path_outfile)
```

## Related Security Topics

- [Secure and sign PDF files in Python](/pdf/python-net/securing-and-signing/)
- [Extract image and signature information in Python](/pdf/python-net/extract-image-and-signature-information/)
- [Sign PDF documents from a smart card in Python](/pdf/python-net/sign-pdf-document-from-smart-card/)
- [Encrypt and decrypt PDF files in Python](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)