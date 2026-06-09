---
title: Signature Integrity Checks
type: docs
weight: 70
url: /java/signature-integrity-checks/
description: Learn how to validate signature coverage and integrity in Java with the PdfFileSignature facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validate PDF signature coverage and integrity in Java
Abstract: Learn how to inspect signature integrity with Aspose.PDF for Java. The current Java example set uses `verifySignature` to validate the selected signature and `coversWholeDocument` to determine whether the signature protects the entire PDF.
---
## Check signature integrity

This article maps to the same verification workflow exposed by `PdfFileSignatureExamples.java`.

### Steps

1. Bind the signed PDF with `PdfFileSignature`.
2. Select a signature name from the document.
3. Call `verifySignature` to validate the signature contents.
4. Call `coversWholeDocument` to confirm document-wide coverage.
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
