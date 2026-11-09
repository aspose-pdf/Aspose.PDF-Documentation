---
title: Manage PDF passwords and permissions in C++
linktitle: PdfFileSecurity Class
type: docs
weight: 125
url: /cpp/pdffilesecurity-class/
description: Encrypt and decrypt PDF files, change passwords, and apply document privileges with direct or Try methods using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configure PDF Encryption and Permissions in C++
Abstract: Use PdfFileSecurity to encrypt, decrypt, and update passwords and document privileges. The examples include explicit encryption settings and Try methods that check success before saving.
---

Use [PdfFileSecurity](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffilesecurity/) to encrypt and decrypt PDF files, change passwords, and apply document privileges with direct or Try methods.

The passwords in these examples are fixture values. Substitute the passwords for your own input and output documents. Permission examples configure DocumentPrivilege; Try methods save only when the operation succeeds.

Choose a topic below for task-specific instructions and C++ examples.

## Topics

- [Change Password of PDF File](/pdf/cpp/change-password/) - Change both passwords using the existing owner password and reset privileges to printing only with x128 key size. Change the user and owner passwords using the existing owner password. Check TryChangePassword and save only when it returns true; otherwise print a diagnostic.
- [Decrypt PDF File](/pdf/cpp/decrypt-pdf-file/) - Decrypt the PDF using the owner password and save the result. Check TryDecryptFile and save only when it returns true; otherwise print a diagnostic.
- [Encrypt PDF File](/pdf/cpp/encrypt-pdf-file/) - Encrypt with AES, x256 key size, and printing allowed. Encrypt with x128 key size while disabling printing and copying from an initially AllowAll privilege set. Encrypt with sample user and owner passwords, x128 key size, and printing allowed.
- [Set Privileges on an Existing PDF File](/pdf/cpp/set-privileges/) - Set printing allowed and copying disabled using the supplied sample passwords. Set a printing-only privilege set using the overload without password arguments. Check TrySetPrivilege and save only when it returns true; otherwise print a diagnostic.
