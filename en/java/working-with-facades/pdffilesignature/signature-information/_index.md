---
title: Signature Information
type: docs
weight: 60
url: /java/signature-information/
description: Learn how to inspect signer, date, reason, and location information in Java with PdfFileSignature.
lastmod: "2026-05-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF signature details in Java with PdfFileSignature
Abstract: This article explains how to use the `getSignatureInformation` example from `PdfFileSignatureExamples` in Aspose.PDF for Java. The current Java source reads the first available signature name, prints the available signature list, and retrieves signer, date, reason, and location values from the signed document.
---
The current Java example for this article is `getSignatureInformation`.

It demonstrates how to:

- access the first signature through `getSignatureNames()`
- print the signature list with `getSignNames()`
- read signer information with `getSignerName(...)`
- inspect date, reason, and location metadata for the signature
