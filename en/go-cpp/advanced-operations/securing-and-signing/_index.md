---
title: Securing and signing PDF in Go
linktitle: Securing and signing PDF
type: docs
weight: 50
url: /go-cpp/securing-and-signing/
description: This section describes the features of using a signature and securing your PDF document using Go
lastmod: "2026-01-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

This section provides a comprehensive guide to working with secured PDF documents using Aspose.PDF for Go via C++. It explains how to protect PDF files with passwords, manage access permissions, and safely open or unlock encrypted documents in Go applications.

The article walks through common security-related PDF tasks, including encrypting PDFs with modern cryptographic algorithms, decrypting password-protected files, and controlling user access through permission flags. You will also learn how to inspect existing permission settings and open secured documents using the owner's credentials for further processing.

## PDF Permissions Reference

| **Permission** | **Description** |
| :- | :- |
| PrintDocument | Allow printing |
| ModifyContent | Allow modifying content (except forms/annotations) |
| ExtractContent | Allow copying/extracting text and graphics |
| ModifyTextAnnotations | Allow adding/modifying text annotations |
| FillForm | Allow filling interactive forms |
| ExtractContentWithDisabilities | Allow content extraction for accessibility |
| AssembleDocument | Allow inserting/rotating/deleting pages or changing structure |
| PrintingQuality | Allow high-quality / faithful printing |

You will learn how to create PDF documents, apply modern cryptographic protection using AES-based encryption, and control user capabilities such as printing, editing content, and filling forms. The article also demonstrates how to open password-protected PDFs using owner credentials and decrypt them to produce unrestricted documents suitable for further processing.

- [Encrypt and PDF File](/pdf/go-cpp/encrypt-pdf/)
- [Decrypt PDF File](/pdf/go-cpp/decrypt-pdf/)
- [Get Permissions](/pdf/get-permissions/)
- [Set permissions](/pdf/go-cpp/set_permissions/)
- [Open a password-protected PDF](/pdf/go-cpp/open-password-protected-pdf/)

