---
title: Add digital signature or digitally sign PDF in C#
linktitle: Digitally sign PDF
type: docs
weight: 10
url: /net/digitally-sign-pdf-file/
description: Digitally sign PDF documents using C# or VB.NET. Verify, or validate the digitally sign PDFs using C# or VB.NET.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to digitally sign PDF",
    "alternativeHeadline": "Wirking with digitally sign PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, digitally sign pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "Digitally sign PDF documents using C# or VB.NET. Verify, or validate the digitally sign PDFs using C# or VB.NET."
}
</script>

Aspose.PDF for .NET supports the feature to digitally sign the PDF files using the SignatureField class. You can also certify a PDF file with a PKCS12-Certificate. Something similar to [Adding Signatures and Security in Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

When signing a PDF document using a signature, you basically confirm its contents "as is". Consequently, any other changes made afterward invalidate the signature and thus, you would know if the document was altered. Whereas, certifying a document first allows you to specify the changes that a user can make to the document without invalidating the certification.

In other words, the document would still be considered to retain its integrity and the recipient could still trust the document. For further details, please visit Certifying and signing a PDF. In general, certifying a document can be compared to Code-signing a .NET executable.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Aspose.PDF for .NET signing features

We can use follwing classed and method for PDF signing

- Class [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature).
- Enumeration [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions).
- Property [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) in [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class.


To create a digital signature based on PKCS12 certificates (file extensions .p12, pfx), you should create an instance of the PdfFileSignature class, passing the document object to it.
Next, you should specify the desired digital signature method by creating an object of one of the classes:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_You can set the digest algorithm only for PKCS7Detached. For PKCS1 and PKCS7, the digest algorithm is always set to SHA-1._

Next, you need to use the received signature algorithm object in the PdfFileSignature.Sign() method.
The digital signature will be set for the document after it is saved.

## Sign PDF with digital signatures

The example below creates a PKCS7 non-detached signature with the SHA-1 digest algorithm.
```csharp
public static void SignDocument()
{
    string inFile = dataDir + "DigitallySign.pdf";
    string outFile = dataDir + "DigitallySign_out.pdf";
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020");
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save output PDF file
            signature.Save(outFile);
        }
    }
}
```

The example below creates a detached signature in PKCS7 format with the SHA-1 digest algorithm. The key algorithm depends on the certificate key. DSA, RSA, ECDSA are supported.

```csharp
public static void SignDocument()
{
    string inFile = dataDir + "DigitallySign.pdf";
    string outFile = dataDir + "DigitallySign_out.pdf";
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7Detached(@"C:\Keys\test.pfx", "Pa$$w0rd2020", DigestHashAlgorithm.Sha256);
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save output PDF file
            signature.Save(outFile);
        }
    }
}
```

You can verify a signatures by using PdfFileSignature.VerifySignature() method. 

_Notes, the __PdfFileSignature.VerifySigned()__ method is deprecated._

```csharp
public void Verify(string fileName)
{
    // Open the PDF document from the specified file
    using (Document document = new Document(fileName))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {         
            // Get a list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## Add timestamp to digital signature

### How to digitally sign a PDF with timestamp

Aspose.PDF for .NET supports to digitally sign the PDF with a timestamp server or Web service.

In order to accomplish this requirement, the [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) class has been added to the Aspose.PDF namespace. Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(dataDir + "SimpleResume.pdf"))
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
            signature.Save(dataDir + "DigitallySignWithTimeStamp_out.pdf");
        }
    }
}
```

## Sign PDF with X509Certificate2 in base64 format

This code signs the PDF using an external certificate, possibly interacting with a server to retrieve the signed hash and embed the signature into the PDF document.

Steps to sign PDF:

1. Create An instance of PdfFileSignature.
1. Define the Custom Signature Hash.
1. Loading the certificate.
1. Signing the data.
1. Binding and Signing the PDF.
1. Saving the Signed PDF.

```cs
var base64Str = "sign";
using (var pdfSign = new PdfFileSignature())
{
    var sign = new ExternalSignature(base64Str, false);//without Private Key
    sign.ShowProperties = false;
    SignHash customSignHash = delegate (byte[] signableHash)
    {
        //Simulated Server Part (This will probably just be sending data and receiving a response)
        var signerCert = new X509Certificate2(inputP12, "123456", X509KeyStorageFlags.Exportable);//must have Private Key
        var rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    };
    sign.CustomSignHash = customSignHash;
    pdfSign.BindPdf(inputPdf);
    pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
                    new System.Drawing.Rectangle(200, 200, 200, 100),
                    sign);
    pdfSign.Save(outputPdf);
}
```

## Sign a PDF with HASH signing function

Using a custom hash signing function, the signing authority can implement specific cryptographic standards or internal security policies that go beyond standard signing methods, ensuring the document's integrity. 
This approach helps verify that the document has not been altered since the signature was applied and provides a legally binding digital signature with verifiable proof of the signer's identity using the PFX certificate.

This code snippet demonstrates digitally signing a PDF document using a PFX (PKCS#12) certificate with a custom hash signing function in C#.

Let’s take a closer look at the DPF signing process:

1. Define File Paths and Certificate Information:

- inputPdf: The path to the input PDF document that needs to be signed.
- inputP12: The path to the .p12 (PFX) certificate file used for signing.
- inputPfxPassword: The password for the PFX certificate.
- outputPdf: The path where the signed PDF will be saved.

2. Signature Process:

- A 'PdfFileSignature' object is created and bound to the input PDF.
- A 'PKCS7' object is initialized using the PFX certificate and its password. The 'CustomSignHash' method is assigned as the custom hash signing function.
- The Sign method is called, specifying the page number (1 in this case), signature details (reason, cont, loc), and the position (a rectangle with coordinates (0, 0, 500, 500)) for the signature.
- The signed PDF is then saved to the specified output path.

3. Custom Hash Signing:

- The 'CustomSignHash' method accepts a byte array signableHash (the hash to be signed).
- It loads the same PFX certificate and retrieves its private key.
- The private key is used to sign the hash using the 'RSACryptoServiceProvider' and the SHA-1 algorithm.
- The signed data (byte array) is returned to be applied to the PDF signature.

The digest algorithm can be specified in the PKCS7Detached constructor. A third-party service can be called in the CustomSignHash delegate. The signature algorithm used in CustomSignHash must match the key algorithm in the certificate passed to PKCS7/PKCS7Detached.

The example below creates a non-detached signature with the RSA algorithm and the SHA-1 digest algorithm.
If you use PKCS7Detached instead of PKCS7, you can use ECDCA and set the desired digest algorithm.

```csharp
var inputPdf = "111.pdf";
var inputP12 = "111.p12";
var inputPfxPassword = "123456";
var outputPdf = "111_out.pdf";
using (var sign = new PdfFileSignature())
{
    sign.BindPdf(inputPdf);
    var pkcs7 = new PKCS7(inputP12, inputPfxPassword);// You can use PKCS7Detached with digest algorithm argument.
    pkcs7.CustomSignHash = CustomSignHash;
    sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
    sign.Save(outputPdf);
}

// Custom hash signing function to generate a digital signature
private byte[] CustomSignHash(byte[] signableHash, DigestHashAlgorithm digestHashAlgorithm)
{
    var inputP12 = "111.p12";
    var inputPfxPassword = "123456";
    X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
    RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
    var xmlString = signerCert.PrivateKey.ToXmlString(true);
    rsaCSP.FromXmlString(xmlString);
    byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
    return signedData;
}
```

## Signing PDF documents using ECDSA

Signing PDF documents using ECDSA (Elliptic Curve Digital Signature Algorithm) involves utilizing elliptic curve cryptography to generate digital signatures. This offers high security and efficiency, especially for mobile and resource-constrained environments. This approach ensures that your PDF documents are digitally signed with the security advantages of elliptic curve cryptography.

Aspose.PDF supports ECDSA-based digital signature creation and verification.
The following elliptic curves are supported for digital signature creation and verification:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

The default digest algorithm is SHA2 with a length dependent on the ECDSA key size.
You can specify the digest algorithm in the PKCS7Detached constructor.

ECDSA digital signatures with the following digest algorithms can be signed: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.
ECDSA digital signatures with the following digest algorithms can be verified: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

You can check the signature and verification by creating a PFX(output.pfx) certificate in OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Available curve names for signature and verification in Aspose.PDF (the list of curves in OpenSSL can be obtained with the command 'openssl ecparam -list_curves'): prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

To sign a PDF document using ECDSA, the general steps in C# would be:

1. You'll need an ECDSA certificate in PFX or P12 format. These certificates contain both the public and private keys needed for signing.
1. Using an Aspose.PDF library, you bind the document to a signature handler.
1. Use the ECDSA private key to sign the hash of the document content.
1. Place the generated signature inside the PDF file along with metadata such as the reason for signing, location, and contact details.

```csharp
public void Verify(string fileName)
{
    // Open the PDF document from the specified file
    using (Document document = new Document(fileName))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            // Check if the document contains any digital signatures
            if (!signature.ContainsSignature())
            {
                throw new Exception("Not contains signature");
            }

            // Get a list of signature names in the document
            var sigNames = signature.GetSignNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}

public void Sign(string cert, string inputPdfFile, string outFile)
{
    // Open the PDF document from the specified input file
    using (Document document = new Document(inputPdfFile))
    {
        // Create an instance of PdfFileSignature to sign the document
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            // Create a PKCS7Detached object using the provided certificate and password
            PKCS7Detached pkcs = new PKCS7Detached(cert, "12345", DigestHashAlgorithm.Sha256);

            // Sign the first page of the document, setting the signature's appearance at the specified location
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);

            // Save the signed document to the specified output file
            signature.Save(outFile);
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
