---
title: Extract Image and Signature Information
linktitle: Extract Image and Signature Information
type: docs
weight: 30
url: /java/extract-image-and-signature-information/
description: You may extract images from the signature field and extract signature information using the SignatureField class with Java.
lastmod: "2021-04-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extracting Image from Signature Field

Aspose.PDF for .NET supports the feature to digitally sign the PDF files using the [SignatureField](https://apireference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) class and while signing the document, you can also set an image for SignatureAppearance. Now, this API also provides the capability to extract signature information as well as the image associated with the signature field.

In order to extract signature information, we have introduced the [ExtractImage](https://apireference.aspose.com/pdf/java/com.aspose.pdf/SignatureField#extractImage--) method to the [SignatureField](https://apireference.aspose.com/pdf/java/com.aspose.pdf/SignatureField) class. Please take a look at the following code snippet which demonstrates the steps to extract an image from the SignatureField object:

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

Aspose.PDF for Java supports the feature to digitally sign the PDF files using the [SignatureField](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) class. Currently, we can also determine the validity of the certificate but we cannot extract the whole certificate. The information which can be extracted is a public key, thumbprint, issuer, etc.

To extract signature information, we have introduced the [ExtractCertificate](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) method to the [SignatureField](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) class. Please take a look at the following code snippet which demonstrates the steps to extract the certificate from SignatureField object:

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
