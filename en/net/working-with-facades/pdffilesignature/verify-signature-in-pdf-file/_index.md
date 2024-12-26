---
title: Verify Signature in PDF File
type: docs
weight: 30
url: /net/verify-signature-in-pdf/
description: This section explains how to verify signature in PDF File using PdfFileSignature class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Verify Signature in PDF File",
    "alternativeHeadline": "Verify Signatures in PDF Files Efficiently",
    "abstract": "The feature allows users to efficiently verify signatures within PDF files using the PdfFileSignature class. With methods to check both the existence of a signature and its validity, this functionality simplifies the process of ensuring document authenticity and integrity. Optimize document management by seamlessly confirming the security of your PDFs",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/verify-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/verify-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Verify Whether the PDF File is Signed Using a Signature

To verify whether a PDF file is signed using a [particular signature](/pdf/net/working-with-signature-in-a-pdf-file/), use the VerifySigned method of the [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class. This method requires the signature name and returns true if the PDF is signed using that signature name. It is also possible to verify that a [PDF is signed](/pdf/net/working-with-signature-in-a-pdf-file/), without verifying which signature it is signed with.

### Verifying that a PDF is Signed with a Given Signature

The following code snippet shows you how to verify whether PDF is signed using a given signature.

```csharp
// For complete examples and data files, check for https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void IsPdfSigned()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {      
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.ContainsSignature())
        {
            Console.WriteLine("Document Signed");
        }

        pdFileSignature.Close();
    }
}
```

### Verifying that a PDF is Signed

To determine if a file is singed, without providing the signature name, use the following code.

```csharp
// For complete examples and data files, check for https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void IsPdfSignedWithGivenSignature()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("PDF Signed");
        }
    }
}
```

## Verify whether the Signature is Valid

[VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) method of [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) class allows you to validate a particular signature. This method requires signature name as input and returns true if the signature is valid. The following code snippet shows you how to validate a signature.

```csharp
// For complete examples and data files, check for https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void IsPdfSignatureValid()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        pdFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        if (pdFileSignature.VerifySignature("Signature1"))
        {
            Console.WriteLine("Signature Verified");
        }
    }
}
```