---
title: Add Signature in PDF File
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: This section explains how to add signature to PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---

## Add Digital Signature in a PDF File

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class allows you to add signature in a PDF file. You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class using input and output PDF files. You also need to create a [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) object at which you want to add the signature and in order to set appearance you can specify an image using [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) property of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) object. Aspose.Pdf.Facades also provides different kinds of signatures like PKCS#1, PKCS#7, and PKCS#7Detached. In order to create a signature of a specific type, you need to create an object of the particular class like **PKCS1** , **PKCS7** or **PKCS7Detached** using the certificate file and the password.

Once the object of a particular signature type is created, you can use the [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) method of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class to sign the PDF and pass the particular signature object to this class. You can also specify other attributes for this method. Finally, you need to save the signed PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) method of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class. The following code snippet shows you how to add signature in a PDF file.

```csharp
public static void AddPdfFileSignature()
{
    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.BindPdf(dataDir + "sample01.pdf");

    // Create a rectangle for signature location
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
    // Set signature appearance
    pdfSign.SignatureAppearance = dataDir + "aspose-logo.png";

    // Create any of the three signature types
    PKCS1 signature = new PKCS1(dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

    pdfSign.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
    // Save output PDF file
    pdfSign.Save(dataDir + "DigitallySign.pdf");
}
```

The following code example shows us the ability to sign a document with two signatures. In our example, we put the first signature on the first page, and the second on the second page. You can specify the pages that you need.

```csharp
public static void AddTwoSignature()
{
    PdfFileSignature pdfSign = new PdfFileSignature();

    // Sign with 1st signature
    pdfSign.BindPdf(dataDir + "sample01.pdf");

    // Create a rectangle for 1st signature location
    System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

    // Create 1st signature object
    PKCS1 signature1 = new PKCS1(dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

    pdfSign.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
    pdfSign.Save(dataDir + "DigitallySign.pdf");

    // Sign with 2nd signature
    pdfSign.BindPdf(dataDir + "DigitallySign.pdf");

    // Create a rectangle for 2nd signature location
    System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

    // Create 2nd signature object
    PKCS1 signature2 = new PKCS1(dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

    pdfSign.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

    // Save output PDF file
    pdfSign.Save(dataDir + "DigitallySign.pdf");
}
```

For a document with forms or acroforms that needs to be signed, see the following example.
You need to create an object of [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class using input and output PDF files. Use [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) for binding. Create a signature with the ability to add the required properties. In our example they are 'Reason' and 'CustomAppearance'.

```csharp
public static void AddPdfFileSignatureField()
{
    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.BindPdf(dataDir + "sample02.pdf");

    // Create any of the three signature types
    PKCS1 signature = new PKCS1(dataDir + "test02.pfx", "Aspose2021")
    {
        Reason = "Sign as Author",
        CustomAppearance = new SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Calibri"
        }
    }; // PKCS#1
    pdfSign.Sign("Signature1", signature);
    // Save output PDF file
    pdfSign.Save(dataDir + "DigitallySign.pdf");
}
```

If our document has two fields, the algorithm for signing it is similar to the first example.

```csharp
public static void AddPdfFileSignatureField2()
{
    PdfFileSignature pdfSign = new PdfFileSignature();
    pdfSign.BindPdf(dataDir + "sample03.pdf");

    // Create any of the three signature types
    PKCS1 signature1 = new PKCS1(dataDir + "test01.pfx", "Aspose2021")
    {
        Reason = "Sign as Author",
        CustomAppearance = new SignatureCustomAppearance
        {
            FontSize = 6
        }
    }; // PKCS#1
    pdfSign.Sign("Signature1", signature1);
    // Save output PDF file
    pdfSign.Save(dataDir + "DigitallySign.pdf");

    pdfSign.BindPdf(dataDir + "DigitallySign.pdf");

    // Create any of the three signature types
    PKCS1 signature2 = new PKCS1(dataDir + "test02.pfx", "Aspose2021")
    {
        Reason = "Sign as Reviwer",
        CustomAppearance = new SignatureCustomAppearance
        {
            FontSize = 6
        }
    }; // PKCS#1
    pdfSign.Sign("Signature2", signature2);
    // Save output PDF file
    pdfSign.Save(dataDir + "DigitallySign.pdf");
}
```
