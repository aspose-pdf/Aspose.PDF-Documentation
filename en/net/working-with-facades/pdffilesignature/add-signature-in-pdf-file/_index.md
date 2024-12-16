---
title: Add Signature in PDF File
type: docs
weight: 10
url: /net/add-signature-in-pdf/
description: This section explains how to add signature to PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "Enhance your PDF documents with the new ability to add digital signatures using the PdfFileSignature class. This feature allows users to apply various signature types, including PKCS#1, PKCS#7, and PKCS#7Detached, while customizing the signature appearance with images and specific attributes. Streamline your document verification process by incorporating multiple signatures on different pages with ease",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

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
