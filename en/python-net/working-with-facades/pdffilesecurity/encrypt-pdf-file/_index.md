---
title: Encrypt PDF File
type: docs
weight: 30
url: /python-net/encrypt-pdf-file/
description: Encrypt a PDF document and configure permissions to control what users can do with the file.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Encrypt PDF and Control User Actions
Abstract: Learn how to encrypt a PDF while defining specific user permissions using Aspose.PDF for Python via .NET. This guide shows how to allow or restrict actions such as printing and copying while keeping the document secure.    
---

## Encrypt PDF with User and Owner Password

Securing PDF documents is essential when sharing sensitive or restricted content. Encryption allows you to protect a document with passwords and define what actions users are allowed to perform. This code snippet shows how to apply user and owner passwords along with access permissions to secure a PDF file.

1. Create a PdfFileSecurity object.
1. Bind the input PDF.
1. Define Document Privileges.
1. Encrypt the PDF.
1. Save the Encrypted PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Encrypt PDF with Permissions

Next code snippet explain how to allow selected actions like printing and copying while restricting others.

1. Initialize the [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) class.
1. Bind the Input PDF.
1. Configure Document Privileges.
1. Call the 'encrypt_file()' method.
1. Save the Encrypted PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Encrypt PDF with Encryption Algorithm

PDF encryption not only protects documents with passwords but also allows you to choose the encryption algorithm and strength. Selecting the appropriate algorithm ensures stronger security for sensitive documents.

1. Create a PdfFileSecurity Object.
1. Bind the Input PDF.
1. Define Document Privileges.
1. Encrypt the PDF with Algorithm.
1. Save the Encrypted PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
