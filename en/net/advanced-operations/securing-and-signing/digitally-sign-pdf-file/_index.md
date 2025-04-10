---
title: Add digital signature or digitally sign PDF in C#
linktitle: Digitally sign PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /net/digitally-sign-pdf-file/
description: Digitally sign PDF documents using C# or VB.NET. Verify, or validate the digitally sign PDFs using C# or VB.NET.
lastmod: "2025-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add digital signature or digitally sign PDF in C#",
    "alternativeHeadline": "Working with digitally sign PDF",
    "abstract": "Aspose.PDF for .NET introduces powerful capabilities for digitally signing PDF documents using C# or VB.NET, enhancing document integrity and security. Users can implement various signature types, including non-detached and detached signatures with support for PKCS7 and ECDSA, allowing for customizable signing processes tailored to specific cryptographic standards. This feature not only verifies the authenticity of the documents but also enables timestamping and certification, ensuring trusted document handling",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "digital signature, digitally sign PDF, C#, PDF signing, PKCS12 certificate, verify PDF signature, ECDSA signing, timestamp server, custom hash signing, Aspose.PDF for .NET",
    "wordcount": "2020",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2025-02-07",
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


To create a digital signature based on PKCS12 certificates (file extensions .p12, pfx), you should create an instance of the `PdfFileSignature` class, passing the document object to it.
Next, you should specify the desired digital signature method by creating an object of one of the classes:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_You can set the digest algorithm only for `PKCS7Detached`. For `PKCS1` and `PKCS7`, the digest algorithm is always set to SHA-1._

Next, you need to use the received signature algorithm object in the `PdfFileSignature.Sign()` method.
The digital signature will be set for the document after it is saved.

## Sign PDF with digital signatures

The example below creates a PKCS7 non-detached signature with the SHA-1 digest algorithm.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345");
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

The example below creates a detached signature in PKCS7Detached format with the SHA-256 digest algorithm. The key algorithm depends on the certificate key. DSA, RSA, ECDSA are supported.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object using the opened document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password, Aspose.Pdf.DigestHashAlgorithm.Sha256);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

You can verify signatures by using PdfFileSignature.VerifySignature() method.
Previously, the `GetSignNames()` method was used to get signature names. Starting with version 25.02, the `GetSignatureNames()` method should be used, which returns a list of `SignatureName`.
The `SignatureName` prevents collisions when verifying signatures with the same names.
Methods that accept the `SignatureName` type instead of a string signature name should also be used.

_Notes, the __PdfFileSignature.VerifySigned()__ method is deprecated._

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {         
            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

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

## Verify digital signatures with a certificate check

When verifying a digital signature, you can check the signing certificate for revocation.

Unfortunately, Aspose.PDF cannot verify the authenticity of the root or intermediate certificates in the certificate chain.  
Therefore, only the revocation status of the signing certificate is checked using CRL and OCSP.

To configure certificate validation, you can use the `ValidationOptions` parameter.

The `ValidationMode` option offers three validation modes:

- **None** – the certificate is not checked.
- **Strict** – certificate revocation affects the result of the `Verify` method.
- **OnlyCheck** – allows checking the certificate without affecting the signature verification result.

The `ValidationMethod` specifies the method used to check the certificate:

- **Auto** – automatic method selection. OCSP is preferred. The revocation status is determined by the method that successfully performs the check.
- **Ocsp** – revocation is checked using OCSP.
- **Crl** – revocation is checked using CRL.
- **All** – both methods are used to check the certificate. For the validation to pass, both methods must confirm that the certificate is not revoked.

The `CheckCertificateChain` option enables checking for the presence of a certificate chain in the signature.  
If the certificate chain is not found, the certificate verification result will be `Undefined`.

The result of the verification can be obtained through an output parameter of type `ValidationResult`.  
The possible statuses are: `Valid`, `Invalid`, and `Undefined`.  
`Undefined` typically means that the certificate could not be validated or the certificate chain is missing.

Setting both `CheckCertificateChain` and `ValidationMode = ValidationMode.Strict` corresponds to Adobe Acrobat’s behavior.  
If Adobe Acrobat cannot find the certificate chain, it does not check the revocation status, and the signature is considered invalid.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifySignatureWithCertificateCheck(string filePath)
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(filePath))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Find all signatures
            foreach (var signName in pdfSign.GetSignatureNames())
            {
                // Create a certificate validation option
                var options = new Aspose.Pdf.Security.ValidationOptions();
                options.ValidationMode = ValidationMode.Strict;
                options.ValidationMethod = ValidationMethod.Auto;
                options.CheckCertificateChain = true;
                options.RequestTimeout = 20000;

                Aspose.Pdf.Security.ValidationResult validationResult;
                // Verify a digital signature
                bool verified = pdfSign.VerifySignature(signName, options, out validationResult);
                Console.WriteLine("Certificate validation resul: " + validationResult.Status);
                Console.WriteLine("Is verified: " + verified);
            } 
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifySignatureWithCertificateCheck(string filePath)
{
    // Open PDF document
    using var document = new Aspose.Pdf.Document(filePath));
    
    // Create an instance of PdfFileSignature for working with signatures in the document
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document));
    
    // Find all signatures
    foreach (var signName in pdfSign.GetSignatureNames())
    {
        // Create a certificate validation option
        var options = new Aspose.Pdf.Security.ValidationOptions();
        options.ValidationMode = ValidationMode.Strict;
        options.ValidationMethod = ValidationMethod.Auto;
        options.CheckCertificateChain = true;
        options.RequestTimeout = 20000;

        Aspose.Pdf.Security.ValidationResult validationResult;
        // Verify a digital signature
        bool verified = pdfSign.VerifySignature(signName, options, out validationResult);
        Console.WriteLine($"Certificate validation resul: {validationResult.Status}");
        Console.WriteLine($"Is verified: {verified}" );
    }             
}
```
{{< /tab >}}
{{< /tabs >}}

## Add timestamp to digital signature

### How to digitally sign a PDF with timestamp

Aspose.PDF for .NET supports to digitally sign the PDF with a timestamp server or Web service.

In order to accomplish this requirement, the [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) class has been added to the Aspose.PDF namespace. Please take a look at the following code snippet which obtains timestamp and adds it to PDF document:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithTimeStampServer(string pfxFilePath, string password)
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);
            // Create TimestampSettings settings
            var timestampSettings = new Aspose.Pdf.TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password can be omitted
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Create any of the three signature types
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // Save PDF document
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
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create a delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving a response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
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

- A `PdfFileSignature` object is created and bound to the input PDF.
- A `PKCS7` object is initialized using the PFX certificate and its password. The 'CustomSignHash' method is assigned as the custom hash signing function.
- The `Sign` method is called, specifying the page number (1 in this case), signature details (reason, cont, loc), and the position (a rectangle with coordinates (0, 0, 500, 500)) for the signature.
- The signed PDF is then saved to the specified output path.

3. Custom Hash Signing:

- The `CustomSignHash` method accepts a byte array signableHash (the hash to be signed).
- It loads the same PFX certificate and retrieves its private key.
- The private key is used to sign the hash using the `RSACryptoServiceProvider` and the SHA-1 algorithm.
- The signed data (byte array) is returned to be applied to the PDF signature.

The digest algorithm can be specified in the PKCS7Detached constructor. A third-party service can be called in the CustomSignHash delegate. The signature algorithm used in CustomSignHash must match the key algorithm in the certificate passed to PKCS7/PKCS7Detached.

The example below creates a non-detached signature with the RSA algorithm and the SHA-1 digest algorithm.
If you use PKCS7Detached instead of PKCS7, you can use ECDCA and set the desired digest algorithm.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
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
}
```

To create a signature, a preliminary estimate of the length of the future digital signature is required.
If you use SignHash to create a digital signature, you may find that the delegate is called twice during the document saving process.
If for some reason you cannot afford two calls, for example, if a PIN code request occurs during the call, you can use the `AvoidEstimatingSignatureLength` option for the PKCS1, PKCS7, PKCS7Detached, and ExternalSignature classes.
Setting this option avoids the signature length estimation step by setting a fixed value as the expected length - `DefaultSignatureLength`. The default value for the DefaultSignatureLength property is 3000 bytes.
The AvoidEstimatingSignatureLength option only works if the SignHash delegate is set in the CustomSignHash property.
If the resulting signature length exceeds the expected length specified by the DefaultSignatureLength property, you will receive a `SignatureLengthMismatchException` indicating the actual length.
You can adjust the value of the DefaultSignatureLength parameter at your discretion.


```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Set an option to avoiding twice SignHash calling.
        pkcs7.AvoidEstimatingSignatureLength = true;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
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
You can specify the digest algorithm in the `PKCS7Detached` constructor.

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
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifyEcda()
{
   // The path to the documents directory
   var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

   // Open PDF document
   using (var document = new Aspose.Pdf.Document(dataDir + "signed_ecdsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Check if the document contains any digital signatures
            if (!signature.ContainsSignature())
            {
                throw new Exception("Not contains signature");
            }

            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

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

private static void SignEcdsa(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures(); 

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create an instance of PdfFileSignature to sign the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create a PKCS7Detached object using the provided certificate and password
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, "12345", Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Sign the first page of the document, setting the signature's appearance at the specified location
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);

            // Save PDF document
            signature.Save(dataDir + "SignEcdsa_out.pdf");
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
