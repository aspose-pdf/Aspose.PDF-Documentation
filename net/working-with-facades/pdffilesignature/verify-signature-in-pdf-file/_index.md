---
title: Verify Signature in PDF File
type: docs
weight: 30
url: /net/verify-signature-in-pdf/
description: This section explains how to verify signature in PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---

## Verify Whether the PDF File is Signed Using a Signature

To verify whether a PDF file is signed using a [particular signature](/pdf/net/working-with-signature-in-a-pdf-file/), use the VerifySigned method of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class. This method requires the signature name and returns true if the PDF is signed using that signature name. It is also possible to verify that a [PDF is signed](/pdf/net/working-with-signature-in-a-pdf-file/), without verifying which signature it is signed with.

### Verifying that a PDF is Signed with a Given Signature

The following code snippet shows you how to verify whether PDF is signed using a given signature.

```csharp
public static void IsPdfSigned()
{
    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
    if (pdfSign.ContainsSignature())
    {
        Console.WriteLine("Document Signed");
    }
    pdfSign.Close();
}
```

### Verifying that a PDF is Signed

To determine if a file is singed, without providing the signature name, use the following code.

```csharp
public static void IsPdfSignedWithGivenSignature()
{
    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
    if (pdfSign.VerifySigned("Signature1"))
    {
        Console.WriteLine("PDF Signed");
    }
}
```

## Verify whether the Signature is Valid

[VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) method of [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class allows you to validate a particular signature. This method requires signature name as input and returns true if the signature is valid. The following code snippet shows you how to validate a signature.

```csharp
public static void IsPdfSignatureValid()
{
    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
    if (pdfSign.VerifySignature("Signature1"))
    {
        Console.WriteLine("Signature Verified");
    }
}
```