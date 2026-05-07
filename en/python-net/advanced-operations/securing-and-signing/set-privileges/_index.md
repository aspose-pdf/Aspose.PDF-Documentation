---
title: Encrypt and Decrypt PDF Files in Python
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 70
url: /python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Learn how to set PDF privileges, encrypt files, decrypt protected PDFs, and change passwords in Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Set PDF permissions and manage encryption in Python
Abstract: This documentation page explains how to set document privileges, apply encryption, and decrypt PDF files using Aspose.PDF for Python. It guides developers through configuring user and owner passwords, defining access restrictions (such as printing, copying, or editing). Code examples illustrate how to protect sensitive content and manage PDF security effectively within Python applications, ensuring controlled access and data confidentiality.     
---

Managing document security is essential when working with sensitive or business-critical content. Aspose.PDF for Python via .NET provides a robust API for programmatically applying encryption, controlling access through permissions, and decrypting protected PDF files.

This article walks Python developers through practical examples for setting privileges, applying and removing encryption, changing passwords, and detecting protection states — all within a PDF workflow.

Aspose.PDF for Python via .NET gives developers full control over PDF security:

**Set Privileges** - Fine-grained access control using permissions.
**Encrypt File** - Apply AES or RC4 encryption with custom passwords.
**Decrypt File** - Remove security using the owner password.
**Change Passwords** - Rotate or update credentials without altering content.
**Inspect Security** - Detect encryption status or required password types.

Use this page when you need to protect PDF documents with passwords, restrict printing or copying, rotate credentials, or inspect whether a document is encrypted.

## Set Privileges on an Existing PDF File

You can restrict or allow specific operations (e.g., printing, copying, form filling) by assigning user and owner passwords along with access privileges.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## Encrypt PDF File using Different Encryption Types and Algorithms

Encrypting a PDF ensures only users with valid credentials can open or modify the file.

>Key Terms:

- User Password. Required to open the document.

- Owner Password. Required to change permissions or remove encryption.

- KeySize. Use AE_SX128 for maximum security in modern workflows.

The following code snippet shows you how to encrypt PDF files.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## Decrypt PDF File using Owner Password

To remove password protection and restore full access:

1. Loads the encrypted PDF using the correct password ('password' is the user or owner password).
1. Removes all password protection and encryption settings from the document.
1. Saves the now unprotected PDF to the specified output file.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## Encrypt and Decrypt a PDF with Public Key Certificates

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## Change Password of a PDF File

To update the security credentials (user and owner passwords) of a PDF document while preserving its content and structure.

1. Opens the PDF using the existing owner password ('owner'), which gives full access including permission to change security settings.
1. Replaces the old passwords with a new user password ('newuser') and a new owner password ('newowner').
1. Saves the PDF with the updated password settings.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## How to - determine if the source PDF is password protected

### Determine correct password from Array

In some scenarios, you may need to identify the correct password from a list of potential candidates in order to access a secured PDF. The code snippet below demonstrates how to check whether a PDF file is password protected and then attempt to unlock it by iterating through a predefined list of passwords using Aspose.PDF for Python via .NET.

The process includes:

1. Using PdfFileInfo to detect whether the PDF is encrypted.
1. Tries to open the PDF with each password using ap.Document().
1. If successful, it prints the number of pages.
1. If not, it catches the exception and reports the failed password.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## Related Security Topics

- [Secure and sign PDF files in Python](/pdf/python-net/securing-and-signing/)
- [Digitally sign PDF files in Python](/pdf/python-net/digitally-sign-pdf-file/)
- [Extract signature information from PDF in Python](/pdf/python-net/extract-image-and-signature-information/)
- [Sign PDF documents from a smart card in Python](/pdf/python-net/sign-pdf-document-from-smart-card/)

