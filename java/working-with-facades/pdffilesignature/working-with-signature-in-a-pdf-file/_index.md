---
title: Working with Signature in PDF File
type: docs
weight: 40
url: /java/working-with-signature-in-a-pdf-file/
description: This section explains how to work with Signature in a PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---

## How to Extract Signature Information

Aspose.PDF for Java supports the feature to digitally sign PDF files using the PdfFileSignature class. Currently, it is also possible to determine the validity of a certificate but we cannot extract the whole certificate. The information that can be extracted is the public key, thumbprint, and issuer, etc.

To extract signature information, we have introduced the extractCertificate(..) method to the PdfFileSignature class. Please take a look at the following code snippet which demonstrates the steps to extract certificate from the PdfFileSignature object:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```

## Extracting Image from Signature Field (PdfFileSignature)

Aspose.PDF for Java supports the feature to digitally sign the PDF files using the PdfFileSignature class and while signing the document, you can also set an image for SignatureAppearance. Now this API also provides the capability to extract signature information as well as the image associated with the signature field.

In order to extract signature information, we have introduced the [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) method to the PdfFileSignature class. Please take a look at the following code snippet which demonstrates the steps to extract image from the PdfFileSignature object:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```

## Suppress Location and Reason

Aspose.PDF functionality allows flexible configuration for digital sign instance. [PdfFileSignature ](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) class provides ability sign PDF file. Sign method implementation allows to sign the PDF and pass the particular signature object to this class. Sign method contains set of attributes for the customization of output digital sing. In case if you need to suppress some text attributes from result sing you can leave them empty. The following code snippet demonstrate how to suppress Location and Reason two rows from signature block:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Create a rectangle for signature location
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Set signature appearance
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Create any of the three signature types
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

## Customization Features for Digital Sign

Aspose.PDF for Java allows customization features for a digital sign. The Sign method of class SignatureCustomAppearance implements with 6 overloads for your comfortable usage. For example, you can configure result sign only by SignatureCustomAppearance class instance and its properties values. The following code snippet demonstrates how to hide "Digitally signed by" caption from output digital sign of your PDF. 

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Create a rectangle for signature location
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("SIGNED BY:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // Save output PDF file
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

## Change Language In Digital Sign Text

Using Aspose.PDF for Java API, you can sign a PDF file using any of the following three types of signatures:

- PKCS#1
- PKCS#7
- PKCS#7

Each of provided signatures contains a set of configuration properties implemented for your convenience(localization, date time format, font family etc). Class SignatureCustomAppearance provides corresponding functionality. The following code snippet demonstrates how to change language in digital sign text:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // create a rectangle for signature location
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // create any of the three signature types
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // sign the PDF file
        pdfSign.sign(1, true, rect, pkcs);
        // save output PDF file
        pdfSign.save(outFile);
    }
```
