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

## Set Privileges on an Existing PDF File

This code snippet demonstrates how to apply access restrictions to a PDF document using Aspose.PDF for Python. By configuring a DocumentPrivilege object to forbid all actions except screen reading, and then encrypting the file with both a user password and an owner password, the document is secured against unauthorized modifications or printing.

This approach is beneficial when distributing sensitive content that should only be viewed using assistive technologies (such as screen readers), while preventing actions like editing, copying, or printing. The use of AES 128-bit encryption (AE_SX128) provides a strong level of security.

With minimal code, developers can enforce strict access control on PDF files, supporting privacy, compliance, and content protection requirements in professional workflows. For more advanced control, Aspose.PDF also supports granular permissions and stronger encryption algorithms.

To set privileges on a PDF file, create an object of the [DocumentPrivilege](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/documentprivilege/)class and specify the rights you want to apply to the document. Once the privileges have been defined, pass this object as an argument to the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object's [encrypt](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method. The following code snippet shows you how to set the privileges of a PDF file.

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

You can use the [encrypt](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method of the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object to encrypt a PDF file. You can pass the user password, owner password, and permissions to the [encrypt](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method. In addition to that, you can pass any value of the [crypto_algorithm](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) enum. This enum provides different combinations of encryption algorithms and key sizes. You can pass the value of your choice. Finally, save the encrypted PDF file using [save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method of the [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.

>Please specify different user and owner passwords while encrypting the PDF file.

- The **user password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **owner password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

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

This code snippet demonstrates how to decrypt a password-protected PDF document using Aspose.PDF for Python. By opening the PDF with the correct password and calling the [decrypt()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method, all encryption and permission restrictions are removed. The resulting unprotected document is then saved to a new file.

This functionality is useful in scenarios where secured documents need to be processed, edited, or redistributed without encryption. It also allows developers to automate PDF security management within larger workflows.

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

This example demonstrates how to change the passwords of a secured PDF document using Aspose.PDF for Python. By opening the PDF with the current owner password and calling the [change_passwords(](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) method, you can update both the user password and the owner password.

This operation is especially useful when rotating credentials for secure documents or updating password policies. Once saved, the output PDF will be protected with the new credentials, while all original content and permissions are preserved.

Aspose.PDF provides a reliable and efficient way to manage PDF security, making it easy to modify encryption settings programmatically as part of your document management or automation processes.

The following code snippet shows you how to change the password of a PDF file.

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

Sometimes there is a requirement to determine the correct password from an array of passwords and open the document with the correct password. The following code snippet demonstrates the steps to iterate through the array of passwords and try opening the document with the correct password.

This code snippet demonstrates how to check if a PDF is password protected and attempt to unlock it using a list of possible passwords with Aspose.PDF for Python.

The process includes:

1. Using PdfFileInfo to detect whether the PDF is encrypted.

1. Iterating through a list of password candidates and trying to open the document with each.

1. If a password is correct, the document is opened successfully, and the number of pages is printed.

1. If the password is incorrect, an error is caught and a message is displayed.

This approach is useful when dealing with documents whose passwords are known only approximately or when automating workflows that involve validating and processing secured PDFs.

Aspose.PDF for Python via .NET provides robust tools for programmatically inspecting, unlocking, and handling password-protected documents, enabling streamlined and secure PDF processing in enterprise applications.

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

