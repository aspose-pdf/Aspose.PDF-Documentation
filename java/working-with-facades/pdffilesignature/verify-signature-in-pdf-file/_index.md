---
title: Verify Signature in PDF File
type: docs
weight: 30
url: /java/verify-signature-in-pdf/
description: This section explains how to work with Signature in a PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---

## Verify Whether the PDF File is Signed Using a Signature

To verify whether a PDF file is signed using VerifySigned method of the [PdfFileSignature](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class. This method requires the signature name and returns true if the PDF is signed using that signature name. It is also possible to verify that a [PDF is signed](/pdf/java/working-with-signature-in-a-pdf-file/), without verifying which signature it is signed with.

### Verifying that a PDF is Signed with a Given Signature

The following code snippet shows you how to verify whether PDF is signed using a given signature.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Document Signed");

        pdfSign.close();
    }
```

### Verifying that a PDF is Signed

To determine if a file is singed, without providing the signature name, use the following code.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Signed");
        }
    }
```

## Verify whether the Signature is Valid

[VerifySignature](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) method of [PdfFileSignature](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class allows you to validate a particular signature. This method requires signature name as input and returns true if the signature is valid. The following code snippet shows you how to validate a signature.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Signature Verified");
        }
    }
```