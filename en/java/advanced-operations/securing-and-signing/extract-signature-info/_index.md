---
title: Extract Signature Information from PDF in Java
linktitle: Extract details from Signature
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Learn how to extract certificate and digital signature details from PDF files in Java.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract signature details and certificate data from signed PDFs in Java
Abstract: This article explains how to inspect digital signatures in PDF documents using Aspose.PDF for Java. Learn how to read signer details, verify a signature, check whether a signature covers the whole document, extract the embedded signing certificate, and remove an existing signature.
---
Use `PdfFileSignature` to inspect and manage signatures that already exist in a PDF document.

## Read signature information

1. Create the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Access the document signature name and configure the signature-inspection flow required by the example.
1. Read and verify the signature information from the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade.
1. Read the returned values or continue with your next processing step.

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

## Verify a signature

1. Create the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Access the document signature name and configure the verification flow required by the example.
1. Read and verify the signature information from the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade.

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: "
                + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: "
                + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```

## Extract the signing certificate

1. Create the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Access the document signature name required for certificate extraction.
1. Write the extracted output or inspect the returned values from the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade.

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
