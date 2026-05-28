---
title: Signature Extraction
linktitle: Signature Extraction
type: docs
weight: 50
url: /java/signature-extraction/
description: Learn how to extract a signing certificate from a PDF signature in Java with PdfFileSignature.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract PDF signature certificates in Java
Abstract: This article explains how to use the `extractSignatureCertificate` example from `PdfFileSignatureExamples` in Aspose.PDF for Java. The current Java source reads the first available signature, opens the certificate stream with `extractCertificate(...)`, and writes that stream to an output certificate file.
---
The current Java example for this article is `extractSignatureCertificate`.

It demonstrates how to:

- access the first available signature name
- open the embedded certificate stream with `extractCertificate(...)`
- copy the certificate data to an output file

The current Java source does not include a signature-image extraction example.
