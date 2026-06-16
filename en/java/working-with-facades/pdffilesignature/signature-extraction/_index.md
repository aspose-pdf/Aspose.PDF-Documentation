---
title: Signature Extraction
linktitle: Signature Extraction
type: docs
weight: 50
url: /java/signature-extraction/
description: Learn how to extract the signing certificate from a signed PDF in Java with PdfFileSignature.
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract a signature certificate from PDF in Java
Abstract: Learn how to extract the certificate associated with a PDF signature using Aspose.PDF for Java. The current Java example set includes certificate extraction to an output stream, but it does not include a separate signature-image extraction sample.
---
## Extract signature certificate

Use this workflow when you need to save the certificate associated with an existing signature.

### Steps

1. Create a `PdfFileSignature` instance and bind the signed PDF.
2. Select the signature name to inspect.
3. Call `extractCertificate` to open the certificate stream.
4. Copy the certificate bytes to an output file.
5. Close the stream resources and the facade object.

### Java example

```java
public static void extractSignatureCertificate(Path inputFile, Path outputFile) throws Exception {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        try (InputStream inputStream = pdfSignature.extractCertificate(signatureName);
             OutputStream outputStream = Files.newOutputStream(outputFile)) {
            inputStream.transferTo(outputStream);
        }
    } finally {
        pdfSignature.close();
    }
}
```

The current `PdfFileSignatureExamples.java` class does not include a dedicated Java sample for extracting a rendered signature image.
