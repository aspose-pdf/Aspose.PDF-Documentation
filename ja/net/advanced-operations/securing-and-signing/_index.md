---
title: C#でのPDFのセキュリティと署名
linktitle: PDFのセキュリティと署名
type: docs
weight: 210
url: /ja/net/securing-and-signing/
description: このセクションでは、C#を使用して署名を行い、PDFドキュメントを保護する機能について説明します。
lastmod: "2024-11-23"
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
    "abstract": "C#を使用してPDFドキュメントを保護し、デジタル署名する高度な機能を発見してください。この機能により、ユーザーはさまざまなアルゴリズムとダイジェストオプションを使用して堅牢なデジタル署名を適用でき、ドキュメントの整合性と真正性を確保します。Aspose.PDFの包括的な署名機能を使用して、.NETアプリケーションへのシームレスな統合を実現し、PDFのセキュリティを強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Securing PDF, signing PDF, digital signature, electronic signature, PKCS1, PKCS7, digest algorithms, Aspose.PDF, C# PDF manipulation, timestamp signature",
    "wordcount": "105",
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
    "dateModified": "2025-04-09",
    "description": "このセクションでは、C#を使用して署名を行い、PDFドキュメントを保護する機能について説明します。"
}
</script>

このセクションでは、C#を使用してPDFドキュメントに安全にデジタル署名する方法について説明します。電子署名とデジタル署名という用語は互換的に使用されますが、基本的には異なります。一般的に、デジタル署名は[認証機関](https://en.wikipedia.org/wiki/Certificate_authority)によって承認された印章を伴い、署名されたドキュメントを改ざんから保護するために使用されます。一方、電子署名は、ドキュメントに署名する意図を示すために使用されることが多いです。

Aspose.PDFはデジタル署名をサポートしています：
- RSA署名アルゴリズムとSHA-1ダイジェストを使用したPKCS1。
- RSA署名アルゴリズムとSHA-1ダイジェストを使用したPKCS7。
- DSA、RSA、ECDSA署名アルゴリズムを使用したPKCS7デタッチド。サポートされるダイジェストアルゴリズムは署名アルゴリズムによって異なります。
- タイムスタンプ署名。

PKCS7デタッチド用のダイジェストアルゴリズム：
- DSA - SHA-1。
- RSA - SHA-1、SHA-256、SHA-384、SHA-512。
- ECDSA - SHA-256、SHA-384、SHA-512、SHA3-256、SHA3-384、SHA3-512。

SHA-1ダイジェストアルゴリズムを使用したデジタル署名は、その安全性の低さから避けることをお勧めします。

- [PDFファイルにデジタル署名する](/pdf/ja/net/digitally-sign-pdf-file/)
- [権限を設定し、PDFファイルを暗号化および復号化する](/pdf/ja/net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [画像と署名情報を抽出する](/pdf/ja/net/extract-image-and-signature-information/)
- [スマートカードからPDFドキュメントに署名する](/pdf/ja/net/sign-pdf-document-from-smart-card/)
- [カスタムセキュリティハンドラー](/pdf/ja/net/custom-security-handler/)

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