---
title: PDFの添付ファイルの操作
linktitle: 添付ファイルの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 190
url: /ja/net/attachments/
description: C# PDF APIを使用して、アプリケーション内からPDFファイルの添付ファイルにアクセスし、追加および削除する方法を説明します。C#コードサンプルを含む完全なガイドです。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Attachments in PDF",
    "alternativeHeadline": "Effortlessly Manage PDF Attachments with C#",
    "abstract": "強力なC# PDF APIを使用して、PDFファイル内の添付ファイルを効率的に管理する方法を発見してください。この機能により、開発者はPDFに添付されたさまざまなファイルタイプにアクセスし、追加および削除することができ、アプリケーションへのシームレスな統合のための詳細なC#コードサンプルが含まれています。この包括的なガイドを活用して、PDF操作機能を向上させましょう。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF API, attachments in PDF, add attachments, remove attachments, extract attachments, Aspose.PDF for .NET, manipulate PDF documents, save attachment to file, delete attachment from PDF",
    "wordcount": "181",
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
    "url": "/net/attachments/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attachments/"
    },
    "dateModified": "2024-11-25",
    "description": "C# PDF APIを使用して、アプリケーション内からPDFファイルの添付ファイルにアクセスし、追加および削除する方法を説明します。C#コードサンプルを含む完全なガイドです。"
}
</script>

このセクションでは、Aspose.PDF for .NETを使用してPDFの添付ファイルを操作する方法を説明します。
添付ファイルとは、親文書に添付された追加のファイルであり、pdf、word、画像、またはその他のファイルタイプなど、さまざまなファイルタイプが含まれます。
PDFに添付ファイルを追加する方法、添付ファイルの情報を取得し、ファイルに保存する方法、C#を使用してプログラム的にPDFから添付ファイルを削除する方法を学びます。

- [PDF文書に添付ファイルを追加する](/pdf/net/add-attachment-to-pdf-document/)
- [添付ファイルを抽出して保存する](/pdf/net/extract-and-save-an-attachment/)
- [既存のPDFから添付ファイルを削除する](/pdf/net/removing-attachment-from-an-existing-pdf/)
- [ポートフォリオ](/pdf/net/portfolio/)

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