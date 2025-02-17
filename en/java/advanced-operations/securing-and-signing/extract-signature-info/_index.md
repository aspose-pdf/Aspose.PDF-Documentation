---
title: Extract Image and Signature Information
linktitle: Extract Image and Signature Information
type: docs
weight: 30
url: /java/extract-image-and-signature-information/
description: You may extract images from the signature field and extract signature information using the SignatureField class with Java.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extract various data from Signature using Aspose.PDF for Java
Abstract: The article discusses the enhanced functionality of the Aspose.PDF for Java API, focusing on the extraction of images and signature information from digital signature fields in PDF documents. The API now includes the `extractImage()` method in the `SignatureField` class, allowing users to retrieve images associated with signature fields. A code snippet demonstrates how to extract images and save them as JPEG files using this method. Additionally, the article covers the replacement of signature images, guiding users on how to identify and manipulate signature fields to overlay new images. Furthermore, the article explains the process of extracting signature information using the `extractCertificate()` method, which retrieves details like the public key, thumbprint, and issuer from the signature field. Another code snippet illustrates how to extract the certificate from a PDF and save it as a `.cer` file. These capabilities enhance the manipulation of digital signatures in PDFs, providing developers with tools to manage signature appearance and extract relevant data programmatically.
SoftwareApplication: java
---

## Extracting Image from Signature Field

Aspose.PDF for Java supports the feature to digitally sign the PDF files using the [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) class and while signing the document, you can also set an image for SignatureAppearance. Now, this API also provides the capability to extract signature information as well as the image associated with the signature field.

In order to extract signature information, we have introduced the [ExtractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) method to the [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) class. Please take a look at the following code snippet which demonstrates the steps to extract an image from the SignatureField object:

```java
public class ExampleExtractImageAndSignature {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void ExtractingImageFromSignatureField() {
        Document pdfDocument = new Document(_dataDir + "ExtractingImage.pdf");

        int i = 0;
        try {
            for (WidgetAnnotation field : pdfDocument.getForm()) {
                SignatureField sf = (SignatureField) field;
                if (sf != null) {
                    FileOutputStream output = new FileOutputStream(_dataDir + "im" + i + ".jpeg");
                    InputStream tempStream = sf.extractImage();
                    byte[] b = new byte[tempStream.available()];
                    tempStream.read(b);
                    output.write(b);
                    output.close();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (pdfDocument != null)
                pdfDocument.dispose();
        }

    }
```

### Replace signature Image

Sometimes you may have a requirement to only replace the image of an already present signature field inside PDF file. In order to accomplish this requirement, first, we need to search form fields inside the PDF file, identify Signature fields, get the dimensions (Rectangular dimensions) of the signature field and then stamp an image over the same dimensions.

## Extract Signature Information

Aspose.PDF for Java supports the feature to digitally sign the PDF files using the [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) class. Currently, we can also determine the validity of the certificate but we cannot extract the whole certificate. The information which can be extracted is a public key, thumbprint, issuer, etc.

To extract signature information, we have introduced the [ExtractCertificate](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractCertificate--) method to the [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) class. Please take a look at the following code snippet which demonstrates the steps to extract the certificate from SignatureField object:

```java
    public static void ExtractSignatureInformation() throws IOException {
        String input = _dataDir + "ExtractSignatureInfo.pdf";
        Document pdfDocument = new Document(input);

        for (WidgetAnnotation field : pdfDocument.getForm()) {
            SignatureField sf = (SignatureField) field;
            if (sf != null) {
                InputStream cerStream = sf.extractCertificate();
                if (cerStream != null) {

                    byte[] buffer = new byte[cerStream.available()];
                    cerStream.read(buffer);

                    File targetFile = new File(_dataDir+"targetFile.cer");
                    OutputStream outStream = new FileOutputStream(targetFile);
                    outStream.write(buffer);
                    outStream.close();
                }
            }
        }
    }
}
```
