---
title: Signature Verification
linktitle: Signature Verification
type: docs
weight: 90
url: /java/signature-verification/
description: Learn how to verify PDF signatures in Java with the PdfFileSignature facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verify PDF signatures in Java
Abstract: Learn how to verify a PDF signature with Aspose.PDF for Java. The Java example selects the first available signature, validates the signature, and checks whether it covers the whole document.
---
## Verify PDF signature

Use this workflow when you need a quick validation pass over an existing signed PDF.

### Steps

1. Create a `PdfFileSignature` instance and bind the signed PDF.
2. Select the signature name you want to inspect.
3. Call `verifySignature` to validate the signature.
4. Call `coversWholeDocument` to check coverage.
5. Close the facade object.

### Java example

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
