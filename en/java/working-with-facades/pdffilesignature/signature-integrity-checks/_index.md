---
title: Signature Integrity Checks
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: Learn how the current Java signature verification example checks signature validity and whole-document coverage.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Check PDF signature integrity in Java with PdfFileSignature
Abstract: This article maps signature-integrity checks to the `verifyPdfSignature` example in `PdfFileSignatureExamples`. The current Java source verifies the selected signature and checks whether it covers the whole document, which is the available integrity-related coverage in this section.
---
There is no separate Java method dedicated only to integrity checks in the current `PdfFileSignatureExamples` class.

For the actual source-backed workflow, see `verifyPdfSignature`, which demonstrates:

- validating the selected signature with `verifySignature(...)`
- checking full-document coverage with `coversWholeDocument(...)`
