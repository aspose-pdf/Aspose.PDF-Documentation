---
title: Add Signature in PDF File
type: docs
weight: 10
url: /java/add-signature-in-pdf/
description: Learn how to add a digital signature to a PDF document using Aspose.PDF in Java for secure signing and document verification.
lastmod: "2021-06-05"
draft: false
---

## Add Digital Signature in a PDF File (facades)

[PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class allows you to add signature in a PDF file. You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class using input and output PDF files. You also need to create a Rectangle object at which you want to add the signature and in order to set appearance you can specify an image using setSignatureAppearance property of the [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) object.

Aspose.Pdf.Facades also provides different kinds of signatures like PKCS#1, PKCS#7, and PKCS#7Detached. In order to create a signature of a specific type, you need to create an object of the particular class like PKCS1 , PKCS7 or PKCS7Detached using the certificate file and the password.

Once the object of a particular signature type is created, you can use the sign method of the [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class to sign the PDF and pass the particular signature object to this class. You can also specify other attributes for this method. Finally, you need to save the signed PDF using save method of the [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class. The following code snippet shows you how to add signature in a PDF file.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Create a rectangle for signature location
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Create any of the three signature types
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect,
                signature);
        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

The following code example shows us the ability to sign a document with two signatures. In our example, we put the first signature on the first page, and the second on the second page. You can specify the pages that you need.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Sign with 1st signature

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Create a rectangle for 1st signature location
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // Sign with 2nd signature

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Create a rectangle for 2nd signature location
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true,
                rect2, signature2);

        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

For a document with forms or acroforms that needs to be signed, see the following example.
You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class using input and output PDF files. Use bindPdf for binding. Create a signature with the ability to add the required properties. In our example they are 'Reason' and 'CustomAppearance'.

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // Create any of the three signature types
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Sign as Author");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

If our document has two fields, the algorithm for signing it is similar to the first example.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // Create any of the three signature types
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("Sign as Author"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Create any of the three signature types
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("Sign as Reviwer"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```
