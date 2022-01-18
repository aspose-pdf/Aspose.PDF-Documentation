---
title: Working with Signature in PDF File
type: docs
weight: 40
url: /net/working-with-signature-in-a-pdf-file/
description: This section explains how to to extract signature information, extract image from signature, change language, and etc using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---

## How to Extract Signature Information

Aspose.PDF for .NET supports the feature to digitally sign PDF files using the PdfFileSignature class. Currently, it is also possible to determine the validity of a certificate but we cannot extract the whole certificate. The information that can be extracted is the public key, thumbprint, and issuer, etc.

To extract signature information, we have introduced the ExtractCertificate(..) method to the PdfFileSignature class. Please take a look at the following code snippet which demonstrates the steps to extract certificate from the PdfFileSignature object:

```csharp
public static void ExtractSignatureInfo()
        {
            string input = _dataDir + "DigitallySign.pdf";
            string certificateFileName = "extracted_cert.pfx";
            using (PdfFileSignature pdfFileSignature = new PdfFileSignature())
            {
                pdfFileSignature.BindPdf(input);
                var sigNames = pdfFileSignature.GetSignNames();
                if (sigNames.Count > 0)
                {
                    string sigName = sigNames[0];
                    if (!string.IsNullOrEmpty(sigName))
                    {
                        Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
                        if (cerStream != null)
                        {
                            using (cerStream)
                            {
                                using (FileStream fs = new FileStream(_dataDir + certificateFileName, FileMode.CreateNew))
                                {
                                    cerStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Extracting Image from Signature Field (PdfFileSignature)

Aspose.PDF for .NET supports the feature to digitally sign the PDF files using the PdfFileSignature class and while signing the document, you can also set an image for SignatureAppearance. Now this API also provides the capability to extract signature information as well as the image associated with the signature field.

In order to extract signature information, we have introduced the ExtractImage(..) method to the PdfFileSignature class. Please take a look at the following code snippet which demonstrates the steps to extract image from the PdfFileSignature object:

```csharp
public static void ExtractSignatureImage()
        {
            using (PdfFileSignature signature = new PdfFileSignature())
            {
                signature.BindPdf(_dataDir + "DigitallySign.pdf");

                if (signature.ContainsSignature())
                {
                    foreach (string sigName in signature.GetSignNames())
                    {
                        string outFile = _dataDir + "ExtractImages_out.jpg";
                        using (Stream imageStream = signature.ExtractImage(sigName))
                        {
                            if (imageStream != null)
                            {
                                imageStream.Position = 0;
                                using (FileStream fs = new FileStream(outFile, FileMode.OpenOrCreate))
                                {
                                    imageStream.CopyTo(fs);
                                }
                            }
                        }
                    }
                }
            }
        }
```

## Suppress Location and Reason

Aspose.PDF functionality allows flexible configuration for digital sign instance. [PdfFileSignature](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)class provides ability sign PDF file. Sign method implementation allows to sign the PDF and pass the particular signature object to this class. Sign method contains set of attributes for the customization of output digital sing. In case if you need to suppress some text attributes from result sing you can leave them empty. The following code snippet demonstrate how to suppress Location and Reason two rows from signature block:

```csharp
public static void SupressLocationReason()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
            // Set signature appearance
            pdfSign.SignatureAppearance = _dataDir + "aspose-logo.png";

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            pdfSign.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Customization Features for Digital Sign

Aspose.PDF for .NET allows customization features for a digital sign. The Sign method of class [SignatureCustomAppearance](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance)implements with 6 overloads for your comfortable usage. For example, you can configure result sign only by SignatureCustomAppearance class instance and its properties values. The following code snippet demonstrates how to hide "Digitally signed by" caption from output digital sign of your PDF. 

```csharp
  public static void CustomizationFeaturesForDigitalSign()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "sample01.pdf");

            // Create a rectangle for signature location
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

            // Create any of the three signature types
            PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

            SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Times New Roman",
                DigitalSignedLabel = "Signed by:"
            };
            signature.CustomAppearance = signatureCustomAppearance;

            pdfSign.Sign(1, true, rect, signature);
            // Save output PDF file
            pdfSign.Save(_dataDir + "DigitallySign.pdf");
        }
```

## Change Language In Digital Sign Text

Using Aspose.PDF for .NET API, you can sign a PDF file using any of the following three types of signatures:

- PKCS#1
- PKCS#7
- PKCS#7

Each of provided signatures contains a set of configuration properties implemented for your convenience(localization, date time format, font family etc). Class [SignatureCustomAppearance](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) provides corresponding functionality. The following code snippet demonstrates how to change language in digital sign text:

```csharp
     public static void ChangeLanguageInDigitalSignText()
        {
            string inFile = _dataDir + "sample01.pdf";
            string outFile = _dataDir + "DigitallySign.pdf";

            using (Aspose.Pdf.Facades.PdfFileSignature pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
            {
                pdfSign.BindPdf(inFile);
                //create a rectangle for signature location
                System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

                //create any of the three signature types
                PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021")
                {
                    Reason = "Pruebas Firma",
                    ContactInfo = "Contacto Pruebas",
                    Location = "Población (Provincia)",
                    Date = DateTime.Now
                };
                SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance
                {
                    DateSignedAtLabel = "Fecha",
                    DigitalSignedLabel = "Digitalmente firmado por",
                    ReasonLabel = "Razón",
                    LocationLabel = "Localización",
                    FontFamilyName = "Arial",
                    FontSize = 10d,
                    Culture = System.Globalization.CultureInfo.InvariantCulture,
                    DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
                };
                pkcs.CustomAppearance = signatureCustomAppearance;
                // sign the PDF file
                pdfSign.Sign(1, true, rect, pkcs);
                //save output PDF file
                pdfSign.Save(outFile);
            }
        }
```
