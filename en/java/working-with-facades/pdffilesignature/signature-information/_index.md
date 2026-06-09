---
title: Signature Information
type: docs
weight: 60
url: /java/signature-information/
description: Learn how to read signature names and signer details from signed PDFs in Java with PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read signature details from PDF documents in Java
Abstract: Learn how to inspect signature metadata with Aspose.PDF for Java. The Java example reads the first available signature name and then retrieves the signer, date, reason, and location from the signed PDF.
---
## Get signature information

Use this workflow when you need to inspect who signed a PDF and what signature metadata was stored.

### Steps

1. Create a `PdfFileSignature` instance and bind the signed PDF.
2. Read the signature collection and select a signature name.
3. Call the signature-information accessors for signer name, date, reason, and location.
4. Close the facade object when finished.

### Java example

```java
public static void getSignatureInformation(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature Names: " + pdfSignature.getSignNames());
        System.out.println("Signer: " + pdfSignature.getSignerName(signatureName));
        System.out.println("Date: " + pdfSignature.getDateTime(signatureName));
        System.out.println("Reason: " + pdfSignature.getReason(signatureName));
        System.out.println("Location: " + pdfSignature.getLocation(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
