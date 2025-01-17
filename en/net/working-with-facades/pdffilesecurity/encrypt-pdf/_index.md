---
title: Encrypt PDF File
type: docs
weight: 10
url: /net/encrypt-pdf-file/
description: This topic explains how to Encrypt PDF File using PdfFileSecurity Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "Discover how to enhance the security of your sensitive documents with the new PDF encryption feature using the PdfFileSecurity Class. This functionality allows you to password-protect your PDF files, ensuring that only authorized users can access them. Explore various encryption types and algorithms, including AES with a key length of up to 256 bits, for robust protection during file sharing and archiving",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Encrypting a PDF document protects its content from unauthorized access from outside, especially during file sharing or archiving.

Confidential PDF documents can be encrypted and password protected. Only user who know the password will be able to decrypt, open and view these documents.

Let's take a look at how PDF encryption works with Aspose.PDF library.

## Encrypt PDF File using Different Encryption Types and Algorithms

In order to encrypt a PDF file, you need to create [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) object and then call the [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You can pass user password, owner password and privileges to [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) method. You also need to pass KeySize and Algorithm values to this method. 

Review a possible list of such [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm): 

|**Member name**|**Value**|**Description**|
| :- | :- | :- |
|RC4x40|0|RC4 with key length 40.|
|RC4x128|1|RC4 with key length 128.|
|AESx128|2|AES with key length 128.|
|AESx256|3|AES with key length 256.|

The following code snippet shows you how to encrypt PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```

