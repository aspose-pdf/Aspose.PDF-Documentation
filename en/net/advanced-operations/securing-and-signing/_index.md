---
title: Securing and signing PDF in C#
linktitle: Securing and signing in PDF
type: docs
weight: 210
url: /net/securing-and-signing/
description: This section describes the features of using a signature and securing your PDF document using C#
lastmod: "2024-11-23"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - net/working-with-security-and-signatures/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Securing and signing PDF in C#",
    "alternativeHeadline": "Securely Digitally Sign PDFs with C#",
    "abstract": "Discover the advanced capabilities of securing and digitally signing PDF documents using C#. This feature enables users to apply robust digital signatures with various algorithms and digest options, ensuring document integrity and authenticity. Enhance your PDF security with Aspose.PDF comprehensive signing functionalities tailored for seamless integration in .NET applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "269",
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
    "url": "/net/securing-and-signing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/securing-and-signing/"
    },
    "dateModified": "2024-11-25",
    "description": "This section describes the features of using a signature and securing your PDF document using C#"
}
</script>

This section describes how to securely digitally sign PDF documents using C#. The terms electronic signature and digital signature are used interchangeably, but essentially the two are different. More generally, a digital signature comes with a [certification authority](https://en.wikipedia.org/wiki/Certificate_authority) approved seal and is used to protect the signed document from tampering. Instead, an electronic signature is often used to demonstrate the intention to sign a document.

Aspose.PDF supports digital signatures:
- PKCS1 with RSA signature algorithm and SHA-1 digest.
- PKCS7 with RSA signature algorithm and SHA-1 digest.
- PKCS7 detached with DSA, RSA and ECDSA signature algorithms. The supported digest algorithms depend on the signature algorithm.
- Timestamp signature.

Digest algorithms for PKCS7 detached:
- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

It is recommended to avoid digital signatures with the SHA-1 digest algorithm due to its insecurity.

- [Digitally sign PDF file](/pdf/net/digitally-sign-pdf-file/)
- [Set Privileges, Encrypt and Decrypt PDF File](/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extract Image and Signature Information](/pdf/net/extract-image-and-signature-information/)
- [Sign PDF Document From Smart Card](/pdf/net/sign-pdf-document-from-smart-card/)
- [Custom security handler](/pdf/net/custom-security-handler/)

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
