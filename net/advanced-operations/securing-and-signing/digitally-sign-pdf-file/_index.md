---
title: Digitally sign PDF file 
type: docs
weight: 10
url: /net/digitally-sign-pdf-file/
---

Aspose.PDF for .NET supports the feature to digitally sign the PDF files using the SignatureField class. You can also certify a PDF file with a PKCS12-Certificate. Something similar to [Adding Signatures and Security in Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

When signing a PDF document using a signature, you basically confirm its contents "as is". Consequently, any other changes made afterward invalidate the signature and thus, you would know if the document was altered. Whereas, certifying a document first allows you to specify the changes that a user can make to the document without invalidating the certification.

In other words, the document would still be considered to retain its integrity and the recipient could still trust the document. For further details, please visit Certifying and signing a PDF. In general, certifying a document can be compared to Code-signing a .NET executable.

## Sign 

- [DocMDPSignature](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature) class was added
- **DocMDPAccessPermissions** enumeration was added
- **IsCertified** property is added to **PdfFileSignature** class

## Sign PDF with digital signatures

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // Use PKCS7/PKCS7Detached objects
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save output PDF file
            signature.Save(outFile);
        }
    }
    
}
```
## Add a timestamp to a digital signature

Aspose.PDF for .NET supports to digitally sign the PDF with a timestamp server or Web service.

In order to accomplish this requirement, the TimestampSettings class has been added to the Aspose.PDF namespace. Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:
```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password can be omitted
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Create any of the three signature types
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // Save output PDF file
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
}
```
