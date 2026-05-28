---
title: Sign PDF Documents
type: docs
weight: 10
url: /java/pdf-signing/
description: Learn how to sign PDF documents in Java with PdfFileSignature using certificate parameters or a PKCS7 signature object.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sign PDF documents in Java with PdfFileSignature
Abstract: This article explains how to use the signing examples from `PdfFileSignatureExamples` in Aspose.PDF for Java. The current Java source includes signing a PDF with certificate parameters set directly on `PdfFileSignature` and signing with a prepared PKCS7 signature object.
---
The current Java source provides two signing examples:

- `signPdfWithBasicParameters`, which sets the certificate file and password with `setCertificate(...)` and then calls `sign(...)` with reason, contact, location, visibility, and rectangle parameters
- `signPdfWithCertificateObject`, which creates a PKCS7 signature object, sets reason, contact, location, and authority metadata on it, and then passes that object into `sign(...)`

Both examples apply a visible signature on page 1 and save the signed output PDF.
