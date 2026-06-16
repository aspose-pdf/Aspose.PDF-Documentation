---
title: Sign PDF Documents
linktitle: Sign PDF Documents
type: docs
weight: 10
url: /java/pdf-signing/
description: Learn how to sign PDF documents in Java with the PdfFileSignature facade.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Sign PDF documents with digital signatures in Java
Abstract: Learn how to sign PDF documents with Aspose.PDF for Java. The Java example set covers signing with a configured certificate path and password, and signing with an explicit PKCS7 signature object that includes signature metadata such as reason, contact info, location, and authority.
---
## Sign PDF documents

Use `PdfFileSignature` when you need to apply a visible digital signature to a PDF.

### Steps

1. Create a `PdfFileSignature` instance and bind the source PDF.
2. Load the certificate either through `setCertificate` or by creating a `PKCS7` object.
3. Call `sign` with the target page, visibility settings, signature rectangle, and signature data.
4. Save the signed PDF and close the facade object.

### Java examples

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
