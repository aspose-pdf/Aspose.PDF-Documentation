---
title: Signature Management
type: docs
weight: 80
url: /java/signature-management/
description: Learn how to remove an existing PDF signature in Java with the PdfFileSignature facade.
lastmod: "2026-06-03"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove PDF signatures in Java
Abstract: Learn how to remove a signature from a signed PDF with Aspose.PDF for Java. The current Java example set covers removing an existing signature by name and saving the updated document. It does not include a separate sample for cleaning up the associated signature field.
---
## Remove a signature

Use this workflow when an existing digital signature should be removed from the document.

### Steps

1. Create a `PdfFileSignature` instance and bind the signed PDF.
2. Read the signature collection and select a signature name.
3. Call `removeSignature` with that name.
4. Save the updated file and close the facade object.

### Java example

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

The current Java sample set does not include a separate method for removing the associated signature field after deleting the signature.
