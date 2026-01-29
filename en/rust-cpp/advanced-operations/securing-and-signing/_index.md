---
title: Securing and signing PDF in Rust
linktitle: Securing and signing PDF
type: docs
weight: 50
url: /rust-cpp/securing-and-signing/
description: This section describes the features of using a signature and securing your PDF document using Rust
lastmod: "2026-01-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

This section provides a comprehensive guide to working with secured PDF documents using Aspose.PDF for Rust via C++. It explains how to protect PDF files with passwords, manage access permissions, and safely open or unlock encrypted documents in Rust.

The article walks through common security-related PDF tasks, including encrypting PDFs with modern cryptographic algorithms, decrypting password-protected files, and controlling user access through permission flags. You will also learn how to inspect existing permission settings and open secured documents using the owner's credentials for further processing.

You will learn how to create PDF documents, apply modern cryptographic protection using AES-based encryption, and control user capabilities such as printing, editing content, and filling forms. The article also demonstrates how to open password-protected PDFs using owner credentials and decrypt them to produce unrestricted documents suitable for further processing.

- [Encrypt and PDF File](/pdf/rust-cpp/encrypt-pdf/)
- [Decrypt PDF File](/pdf/rust-cpp/decrypt-pdf/)
- [Get Permissions](/pdf/rust-cpp/get-permissions/)
- [Set permissions](/pdf/rust-cpp/set_permissions/)
- [Open a password-protected PDF](/pdf/rust-cpp/open-password-protected-pdf/)

To work through the Set Permissions and Get Permissions, please refer to the PDF Permissions Reference table.  Which lists the available permission flags that can be applied to a PDF document to control how end users interact with it.

## PDF Permissions Reference

| **Permission** | **Description** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | Allow printing |
| Permissions::MODIFY_CONTENT | Allow modifying content (except forms/annotations) |
| Permissions::EXTRACT_CONTENT | Allow copying/extracting text and graphics |
| Permissions::MODIFY_TEXT_ANNOTATIONS | Allow adding/modifying text annotations |
| Permissions::FILL_FORM | Allow filling interactive forms |
| Permissions::EXTRACT_CONTENT_WITH_DISABILITIES | Allow content extraction for accessibility |
| Permissions::ASSEMBLE_DOCUMENT | Allow inserting/rotating/deleting pages or changing structure |
| Permissions::PRINTING_QUALITY | Allow high-quality / faithful printing |
