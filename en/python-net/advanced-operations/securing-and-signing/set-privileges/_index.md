---
title: Set Privileges, Encrypt and Decrypt PDF
linktitle: Encrypt and Decrypt PDF File
type: docs
weight: 70
url: /python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Encrypt PDF File with Python using Different Encryption Types and Algorithms. Also, decrypt PDF Files using Owner Password.
lastmod: "2025-06-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Encrypt or Decrypt PDF File with Python
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

## Set Privileges on an Existing PDF File

You can restrict or allow specific operations (e.g., printing, copying, form filling) by assigning user and owner passwords along with access privileges.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate Document Privileges object
        # Apply restrictions on all privileges
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        # Only allow screen reading
        document_privilege.allow_screen_readers = True
        # Encrypt the file with User and Owner password
        # Need to set the password, so that once the user views the file with user password
        # Only screen reading option is enabled
        document.encrypt("user", "owner", document_privilege, ap.CryptoAlgorithm.AE_SX128, False)
        # Save PDF document
        document.save(path_outfile)
```

## Encrypt PDF File using Different Encryption Types and Algorithms

Encrypting a PDF ensures only users with valid credentials can open or modify the file.

>Key Terms:

- User Password. Required to open the document.

- Owner Password. Required to change permissions or remove encryption.

- KeySize. Use AE_SX128 for maximum security in modern workflows.

The following code snippet shows you how to encrypt PDF files.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Encrypt PDF
        document.encrypt("user", "owner", ap.Permissions.EXTRACT_CONTENT, ap.CryptoAlgorithm.AE_SX128)
        # Save PDF document
        document.save(path_outfile)
```

## Decrypt PDF File using Owner Password

To remove password protection and restore full access:

1. Loads the encrypted PDF using the correct password ('password' is the user or owner password).
1. Removes all password protection and encryption settings from the document.
1. Saves the now unprotected PDF to the specified output file.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "password") as document:
        # Decrypt PDF
        document.decrypt()
        # Save PDF document
        document.save(path_outfile)
```

## Change Password of a PDF File

To update the security credentials (user and owner passwords) of a PDF document while preserving its content and structure.

1. Opens the PDF using the existing owner password ('owner'), which gives full access including permission to change security settings.
1. Replaces the old passwords with a new user password ('newuser') and a new owner password ('newowner').
1. Saves the PDF with the updated password settings.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document with password
    with ap.Document(path_infile, "owner") as document:
        # Change password
        document.change_passwords("owner", "newuser", "newowner")
        # Save PDF document
        document.save(path_outfile)
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

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    with ap.facades.PdfFileInfo() as pdf_file_info:
        # Bind PDF document
        pdf_file_info.bind_pdf(path_infile)
        # Determine if the source PDF is encrypted
        print("File is password protected " + str(pdf_file_info.is_encrypted))

        passwords = ["test", "test1", "test2", "test3", "sample"]

        for password_index in range(len(passwords)):
            try:
                with ap.Document(path_infile, passwords[password_index]) as document:
                    if len(document.pages) > 0:
                        print("Number of Pages in document are = " + str(len(document.pages)))
                    password_index = password_index + 1
            except Exception as e:
                print("Password = " + passwords[password_index] + " is not correct")
                password_index = password_index + 1
```

