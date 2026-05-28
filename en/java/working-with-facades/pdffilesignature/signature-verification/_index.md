---
title: Signature Verification
type: docs
weight: 90
url: /java/signature-verification/
description: Learn how to verify a PDF digital signature in Java with PdfFileSignature.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verify PDF signatures in Java with PdfFileSignature
Abstract: This article explains how to use the `verifyPdfSignature` example from `PdfFileSignatureExamples` in Aspose.PDF for Java. The current Java source retrieves the first available signature, verifies it with `verifySignature(...)`, and also reports whether that signature covers the whole document.
---
The current Java example for this article is `verifyPdfSignature`.

It demonstrates how to call:

- `verifySignature(...)` to validate the selected signature
- `coversWholeDocument(...)` to check whether the signature applies to the full PDF
