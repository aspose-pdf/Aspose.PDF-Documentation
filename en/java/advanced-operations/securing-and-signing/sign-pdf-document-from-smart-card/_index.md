---
title: Sign PDF Documents from a Smart Card in Java
linktitle: PDF Signing with Smart Card
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Review the current Java example coverage for certificate-based PDF signing in Aspose.PDF.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certificate-based PDF signing coverage in the current Java example set
Abstract: This page describes the current scope of signing examples available in the Java documentation source tree. The repository includes certificate-based PDF signing examples with PFX or PKCS7 credentials, but it does not currently include a dedicated smart-card certificate-store example for Java.
---
The current Java repository does not include a dedicated source-backed smart-card signing example under `facades/pdffilesignature`, but the following workflow shows the typical API pattern for signing a PDF with a certificate selected from a local certificate store.

## Sign a PDF document from a smart card

1. Open the input PDF with `Document` and create a `PdfFileSignature` facade for signing.
2. Bind the loaded document to the signature facade with `bindPdf(...)`.
3. Retrieve the local certificate that represents the smart-card credential by calling `getLocalCertificate()`.
4. Check whether a certificate was found. If not, save the unchanged output file and stop the workflow.
5. Create an `ExternalSignature` from the selected certificate.
6. Set the visual signature appearance image with `setSignatureAppearance(...)`.
7. Call `sign(...)` with the target page, reason, contact, location, visibility flag, signature rectangle, and external signature object.
8. Save the signed PDF to the output path.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
