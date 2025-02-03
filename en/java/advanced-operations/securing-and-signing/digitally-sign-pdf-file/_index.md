---
title: How to digitally sign PDF
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /java/digitally-sign-pdf-file/
description: Learn how to digitally sign a PDF file to ensure its authenticity and integrity using Aspose.PDF for Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add digital signatures to PDF documents using the Aspose.PDF library for Java
Abstract: The article provides an overview of how to add digital signatures to PDF documents using the Aspose.PDF library for Java. It highlights the significance of certifying a document to maintain its integrity and outlines recent changes to the public API, including the introduction of the `isCertified(…)` method in the `PdfFileSignature` class. The article includes practical examples of signing a PDF with a digital signature using the `PKCS7` protocol and demonstrates how to add a timestamp to a digital signature by incorporating the `TimestampSettings` class. Code snippets illustrate the process of digitally signing a PDF document and adding a timestamp using a timestamp server, ensuring that the document's authenticity and integrity can be trusted.
SoftwareApplication: java
---

When signing a PDF document using a signature, you basically confirm that its contents should remain “as is”. Consequently, any changes made afterwards invalidate the signature and thus, you know if the document has been altered. Certifying a document first, allows you to specify the changes that a user can make to the document without invalidating the certification.

In other words, the document would still be considered to retain its integrity and the recipient could still trust the document. For further details, please visit Certifying and signing a PDF.

To accomplish the above stated requirement, the following public API changes have been made.

isCertified(…) method is added to PdfFileSignature class.

## Sign PDF with digital signatures

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // Use PKCS7/PKCS7Detached
                                                                                              // objects
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // Save output PDF file
        signature.save(outFile);
    }
```

## Add timestamp to digital signature

Aspose.PDF for Java supports to digitally sign the PDF with a timestamp server or Web service.

In order to accomplish this requirement, the [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) class has been added to the Aspose.PDF namespace. Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // User/Password can
                                                                                                    // be omitted
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // Create any of the three signature types
        signature.sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
        // Save output PDF file
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```
