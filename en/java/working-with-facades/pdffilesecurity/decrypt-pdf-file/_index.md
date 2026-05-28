---
title: Decrypt PDF File
linktitle: Decrypt PDF File
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: Learn how to decrypt a PDF in Java with PdfFileSecurity using the owner password.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Decrypt PDFs in Java with PdfFileSecurity
Abstract: This article explains how to use the decryption examples from `PdfFileSecurityExamples` in Aspose.PDF for Java. The current Java source includes a direct decryption workflow with `decryptFile(...)` and a boolean-returning workflow with `tryDecryptFile(...)` for cases where you want to avoid exception-style failure handling.
---
The current Java source provides two decryption examples:

- `decryptPdfWithOwnerPassword`, which binds the secured PDF, calls `decryptFile("owner_password")`, and saves the unlocked output
- `tryDecryptPdfWithoutException`, which calls `tryDecryptFile("owner_password")` and only saves the file if the operation succeeds

These examples show both the direct owner-password decryption flow and the try-style pattern for handling decryption failures without throwing a custom exception in your own code.
