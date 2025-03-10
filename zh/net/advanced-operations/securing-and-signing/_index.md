---
title: 在 C# 中保护和签署 PDF
linktitle: 在 PDF 中保护和签署
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 210
url: /zh/net/securing-and-signing/
description: 本节描述了使用 C# 对 PDF 文档进行签名和保护的功能
lastmod: "2024-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Securing and signing PDF in C#",
    "alternativeHeadline": "Securely Digitally Sign PDFs with C#",
    "abstract": "发现使用 C# 保护和数字签署 PDF 文档的高级功能。此功能使用户能够应用各种算法和摘要选项的强大数字签名，确保文档的完整性和真实性。通过 Aspose.PDF 的全面签署功能增强您的 PDF 安全性，旨在与 .NET 应用程序无缝集成",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "302",
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
    "dateModified": "2024-02-07",
    "description": "本节描述了使用 C# 对 PDF 文档进行签名和保护的功能"
}
</script>

本节描述了如何使用 C# 安全地数字签署 PDF 文档。电子签名和数字签名这两个术语可以互换使用，但本质上两者是不同的。更一般地说，数字签名附带一个 [认证机构](https://en.wikipedia.org/wiki/Certificate_authority) 批准的印章，用于保护已签署的文档不被篡改。相反，电子签名通常用于表明签署文档的意图。

Aspose.PDF 支持数字签名：
- PKCS1 使用 RSA 签名算法和 SHA-1 摘要。
- PKCS7 使用 RSA 签名算法和 SHA-1 摘要。
- PKCS7 分离使用 DSA、RSA 和 ECDSA 签名算法。支持的摘要算法取决于签名算法。
- 时间戳签名。

PKCS7 分离的摘要算法：
- DSA - SHA-1。
- RSA - SHA-1、SHA-256、SHA-384、SHA-512。
- ECDSA - SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、SHA3-512。

建议避免使用 SHA-1 摘要算法的数字签名，因为其不安全。

- [数字签署 PDF 文件](/pdf/net/digitally-sign-pdf-file/)
- [设置权限，加密和解密 PDF 文件](/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [提取图像和签名信息](/pdf/net/extract-image-and-signature-information/)
- [从智能卡签署 PDF 文档](/pdf/net/sign-pdf-document-from-smart-card/)

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