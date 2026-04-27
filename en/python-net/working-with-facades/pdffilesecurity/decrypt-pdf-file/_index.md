---
title: Decrypt PDF File
type: docs
weight: 20
url: /python-net/decrypt-pdf-file/
description: This guide explains how to remove restrictions such as printing, copying, and editing to gain full access to your PDF document.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Remove Password Protection from a PDF
Abstract: This article demonstrates how to decrypt a PDF file using an owner password. It covers the process of removing security restrictions that limit actions like printing, editing, or copying content. By applying the correct owner password, users can unlock the document and regain full control over its functionality.
---

## Decrypt PDF with Owner Password

Decrypt a password-protected PDF document using the owner password with Aspose.PDF for Python via .NET. This operation removes encryption and allows unrestricted access to the document.

1. Create a 'PdfFileSecurity' object.
1. Load the encrypted PDF using the 'bind_pdf()' method.
1. Decrypt the Document.
1. Save the decrypted PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## Try Decrypt PDF Without Exception

PDF documents are often protected with passwords to restrict access and usage. To fully access or modify such documents, you may need to remove encryption. Decrypt a secured PDF document using the owner password to remove encryption and access restrictions with Aspose.PDF for Python via .NET.

1. Create a 'PdfFileSecurity' object.
1. Bind the input PDF.
1. Decrypt the PDF.
1. Save the Output PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
