---
title: Protect PDF Files in Python
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 70
url: /python-net/protect-pdf-file/
description: Learn how to encrypt files, decrypt protected PDFs, and change passwords in Python.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set PDF permissions and manage encryption in Python
Abstract: This page explains how to set document privileges, apply encryption, decrypt PDF files, and change passwords using Aspose.PDF for Python via .NET. It covers configuring user and owner passwords, defining access restrictions (such as printing, copying, and editing), and managing PDF security in Python applications.
---

## Encrypt PDF with password and permissions

Use Aspose.PDF for Python via .NET to secure a PDF document with password-based encryption and restricted permissions.

1. Load the PDF document.
1. Create a `DocumentPrivilege` permissions object.
1. Enable the required permissions.
1. Set user and owner passwords.
1. Choose the encryption algorithm.
1. Apply encryption to the document.
1. Save the encrypted PDF.

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## Encrypt PDF with full permissions

Encrypt a PDF document while allowing full access permissions using Aspose.PDF for Python via .NET. This example uses RC4 128-bit encryption for compatibility with older PDF viewers.

1. Load the PDF document.
1. Define user and owner passwords.
1. Set full access permissions.
1. Choose the encryption algorithm.
1. Call `encrypt()` with passwords, permissions, and algorithm.
1. Save the encrypted PDF.

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## Decrypt PDF File using Owner Password

To remove password protection and restore full access:

1. Load the encrypted PDF using the correct password (user or owner).
1. Remove all password protection and encryption settings from the document.
1. Save the now unprotected PDF to the specified output file.

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## Change Password of a PDF File

Update the security credentials (user and owner passwords) of a PDF document while preserving its content and structure.

1. Open the PDF using the existing owner password, which provides full access to security settings.
1. Replace the old passwords with a new user password and a new owner password.
1. Save the PDF with the updated password settings.

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Determine correct password from Array

In some scenarios, you may need to identify the correct password from a list of possible candidates to access a secured PDF. The snippet below checks whether a PDF file is encrypted and then attempts to open it by iterating through a predefined list of passwords.

The process includes:

1. Use `PdfFileInfo` to detect whether the PDF is encrypted.
1. Open the PDF with each password using `ap.Document()`.
1. If successful, it prints the number of pages.
1. If not, it catches the exception and reports the failed password.

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
