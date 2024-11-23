---
title: How to add Smart Card signature to PDF
linktitle: PDF Signing with Smart Card
type: docs
weight: 30
url: /net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for .NET allows you to sign PDF documents from a smart card using signature field.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to add Smart Card signature to PDF",
    "alternativeHeadline": "Working with Smart Card signature in PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, smart card signature",
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
    "url": "/net/sign-pdf-document-from-smart-card/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sign-pdf-document-from-smart-card/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET allows you to sign PDF documents from a smart card using signature field."
}
</script>

Aspose.PDF for .NET offers the functionality to add digital signatures from a key store location. You can apply the signature by accepting the certificate provided by the certificate store, smart card or [PIV card](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card) connected to the system at run-time. 

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

Following are the code snippets to sign a PDF document from a smart card:

## Sign With Smart Card Using Signature Field

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

File.Copy(dataDir + "blank.pdf", dataDir + "externalSignature1.pdf", true);
using (FileStream fs = new FileStream(dataDir + "externalSignature1.pdf", FileMode.Open, FileAccess.ReadWrite))
{
    using (Document document = new Document(fs))
    {
        SignatureField field1 = new SignatureField(doc.Pages[1], new Rectangle(100, 400, 10, 10));

        // Sign with certificate selection in the windows certificate store
        System.Security.Cryptography.X509Certificates.X509Store store = new System.Security.Cryptography.X509Certificates.X509Store(System.Security.Cryptography.X509Certificates.StoreLocation.CurrentUser);
        store.Open(System.Security.Cryptography.X509Certificates.OpenFlags.ReadOnly);
        // Manually chose the certificate in the store
        System.Security.Cryptography.X509Certificates.X509Certificate2Collection sel = System.Security.Cryptography.X509Certificates.X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, System.Security.Cryptography.X509Certificates.X509SelectionFlag.SingleSelection);

        ExternalSignature externalSignature = new ExternalSignature(sel[0])
        {
            Authority = "Me",
            Reason = "Reason",
            ContactInfo = "Contact"
        };

        field1.PartialName = "sig1";
        document.Form.Add(field1, 1);
        field1.Sign(externalSignature);
        // Save result file
        document.Save();
    }
}

using (Document document = new Document(dataDir + "externalSignature1.pdf"))
{
    using (PdfFileSignature pdfSign = new PdfFileSignature(document))
    {
        IList<string> sigNames = pdfSign.GetSignNames();
        for (int index = 0; index <= sigNames.Count - 1; index++)
        {
            if (!pdfSign.VerifySigned(sigNames[index]) || !pdfSign.VerifySignature(sigNames[index]))
            {
                throw new ApplicationException("Not verified");
            }
        }
    }
}
```

## Sign With Smart Card Using PDF File Signature

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

using (Document document = new Document(dataDir + "blank.pdf"))
{
    using (Facades.PdfFileSignature pdfSign = new Facades.PdfFileSignature())
    {
        pdfSign.BindPdf(document);

        // Sign with certificate selection in the windows certificate store
        System.Security.Cryptography.X509Certificates.X509Store store = new System.Security.Cryptography.X509Certificates.X509Store(System.Security.Cryptography.X509Certificates.StoreLocation.CurrentUser);
        store.Open(System.Security.Cryptography.X509Certificates.OpenFlags.ReadOnly);
        // Manually chose the certificate in the store
        System.Security.Cryptography.X509Certificates.X509Certificate2Collection sel = System.Security.Cryptography.X509Certificates.X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, System.Security.Cryptography.X509Certificates.X509SelectionFlag.SingleSelection);

        ExternalSignature externalSignature = new ExternalSignature(sel[0]);
        pdfSign.SignatureAppearance = dataDir + "demo.png";
        pdfSign.Sign(1, "Reason", "Contact", "Location", true, new System.Drawing.Rectangle(100, 100, 200, 200), externalSignature);
        // Save result file
        pdfSign.Save(dataDir + "externalSignature2.pdf");
    }
}

using (Document document = new Document(dataDir + "externalSignature1.pdf"))
{
    using (Facades.PdfFileSignature pdfSign = new Facades.PdfFileSignature(document))
    {
        IList<string> sigNames = pdfSign.GetSignNames();
        for (int index = 0; index <= sigNames.Count - 1; index++)
        {
            if (!pdfSign.VerifySigned(sigNames[index]) || !pdfSign.VerifySignature(sigNames[index]))
            {
                throw new ApplicationException("Not verified");
            }
        }
    }
}
```

You can use the ExternalSignature class for an external signing service. ExternalSignature creates PKCS7 and PKCS7 detached signatures.
You can pass the desired hashing algorithm to the ExternalSignature constructor. Note that non-detached signatures can only use SHA1.
It will be chosen automatically if you do not explicitly specify the hashing algorithm. For non-detached signatures, it will be SHA1; for detached, it will be SHA-256 for an RSA key. For an ECDSA key, the hash size depends on the key size.

The ExternalSignature constructor also accepts a key certificate (it can be in Base64 format). You can pass a certificate containing a private key and a certificate containing only a public key. In either case, the signature will be performed externally in the CustomSignHash delegate code, but the external algorithm must create a signature corresponding to the key of the passed certificate. The certificate is needed to correctly generate the signed document. ECDSA signature does not support SHA-1.

```csharp
var inputPdf = "";
var outputPdf = "";

using (var sign = new PdfFileSignature())
{
    sign.BindPdf(inputPdf);

    X509Certificate2 signerCert = GetPublicCertificate();
    
    var signature = new ExternalSignature(signerCert, DigestHashAlgorithm.Sha256);

    SignHash customSignHash = delegate(byte[] signableHash, DigestHashAlgorithm digestHashAlgorithm)
    {
        return CallExternalSignatureService(signableHash, digestHashAlgorithm);
    };
    
    signature.CustomSignHash = customSignHash;
    sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
    // Save result file
    sign.Save(outputPdf);
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
