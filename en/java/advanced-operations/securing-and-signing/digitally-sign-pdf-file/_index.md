---
title: Add digital signature or digitally sign PDF in Java
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Learn how to digitally sign and certify PDF documents in Java using Aspose.PDF.
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Digitally sign PDF files with Java
Abstract: This guide explains how to digitally sign PDF documents using Aspose.PDF for Java. It covers signing with a certificate object, signing with basic certificate parameters, and certifying a document with a DocMDP signature to control allowed post-signing changes.
---
Aspose.PDF for Java supports multiple signing flows through `PdfFileSignature`.

## Sign a PDF with a certificate object

1. Create the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Create the [PKCS7](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pkcs7/) signature object and configure the signing options.
1. Apply the signature to the PDF document through [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/).
1. Save the updated PDF document.

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
```

This approach builds a `PKCS7` signature object first and then applies it to page 1.

## Sign a PDF with basic certificate parameters

1. Create the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Configure the certificate parameters required by the signing example.
1. Apply the signature to the PDF document through [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/).
1. Save the updated PDF document.

```java
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

## Certify a PDF with DocMDP

Use a document modification detection and prevention signature when you need certification-level restrictions:

1. Create the [PdfFileSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf.facades/pdffilesignature/) facade and bind the source PDF document.
1. Create the [DocMDPSignature](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docmdpsignature/) object and configure the [DocMDPAccessPermissions](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/docmdpaccesspermissions/) signing options.
1. Apply the certification signature and save the updated PDF document.

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com",
                "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
