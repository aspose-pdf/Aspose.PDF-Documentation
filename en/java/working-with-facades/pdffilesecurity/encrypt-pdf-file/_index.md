---
title: Encrypt PDF File
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: Learn how to encrypt a PDF in Java with PdfFileSecurity using passwords, permissions, and algorithm settings.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Encrypt PDFs in Java with passwords and permission controls
Abstract: This article explains how to use the encryption examples from `PdfFileSecurityExamples` in Aspose.PDF for Java. The current Java source includes encrypting a PDF with user and owner passwords, encrypting while adjusting permission flags, and encrypting with a specific key size and AES algorithm.
---
The current Java source provides three encryption examples:

- `encryptPdfWithUserOwnerPassword`, which starts from `DocumentPrivilege.getForbidAll()`, re-enables printing, and encrypts the PDF with user and owner passwords
- `encryptPdfWithPermissions`, which starts from `DocumentPrivilege.getAllowAll()`, disables printing and copying, and saves the encrypted result
- `encryptPdfWithEncryptionAlgorithm`, which uses `KeySize.x256` together with `Algorithm.AES`

These examples demonstrate how to bind the input PDF, configure the `DocumentPrivilege` object, call the appropriate `encryptFile(...)` overload, and save the secured output.
