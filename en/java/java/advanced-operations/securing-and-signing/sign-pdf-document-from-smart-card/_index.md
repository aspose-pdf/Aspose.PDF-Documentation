---
title: Sign PDF Documents from a Smart Card in Java
linktitle: PDF Signing with Smart Card
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Review the current Java example coverage for certificate-based PDF signing in Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certificate-based PDF signing coverage in the current Java example set
Abstract: This page describes the current scope of signing examples available in the Java documentation source tree. The repository includes certificate-based PDF signing examples with PFX or PKCS7 credentials, but it does not currently include a dedicated smart-card certificate-store example for Java.
---
The current Java repository does not include a dedicated source-backed smart-card signing example under `facades/pdffilesignature`, but the following workflow shows the typical API pattern for signing a PDF with a certificate selected from a local certificate store.

## Sign a PDF document from a smart card

1. Open the source PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Create a [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Retrieve the local certificate and create the required [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Configure the visual signature appearance and the target [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Apply the signature to the PDF document through [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Save the updated PDF document.
1. Bind the loaded document to the [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) facade with `bindPdf(...)`.
1. Retrieve the local certificate that represents the smart-card credential by calling `getLocalCertificate()`.
1. Check whether a certificate was found. If not, save the unchanged output file and stop the workflow.
1. Create an [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) from the selected certificate.
1. Set the visual signature appearance image with `setSignatureAppearance(...)`.
1. Call `sign(...)` with the target page, reason, contact, location, visibility flag, signature [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), and external signature object.
1. Save the signed PDF to the output path.

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
