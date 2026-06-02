---
title: Extract Signature Information from PDF in Java
linktitle: Extract details from Signature
type: docs
weight: 20
url: /java/extract-image-and-signature-information/
description: Learn how to extract certificate and digital signature details from PDF files in Java.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract signature details and certificate data from signed PDFs in Java
Abstract: This article explains how to inspect digital signatures in PDF documents using Aspose.PDF for Java. Learn how to read signer details, verify a signature, check whether a signature covers the whole document, extract the embedded signing certificate, and remove an existing signature.
---
Use `PdfFileSignature` to inspect and manage signatures that already exist in a PDF document.

## Read signature information

1. Open the PDF document used in this example.
2. Use the Aspose.PDF API calls shown here to read signature information.
3. Read the returned values or continue with your next processing step.

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

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to verify a signature.
3. Save the document or inspect the result, depending on the scenario.

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

1. Open the source PDF document used in this example.
2. Run the Aspose.PDF operations required to extract the signing certificate.
3. Write the extracted output or inspect the returned values.

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

The same example class also includes `removeSignature`, which deletes the first signature and saves the updated PDF.
