---
title: PDFにおけるナビゲーションとインタラクション
linktitle: ナビゲーションとインタラクション
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /ja/net/navigation-and-interaction/
description: このセクションでは、リンク、アクション、およびブックマークに関する機能について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Links in PDF programmatically",
    "alternativeHeadline": "Programmatically Add Links to PDF Files in C#",
    "abstract": "C#を使用してPDF文書内のリンクをプログラムで管理する新しい機能を発見してください。この機能により、内部ページリンクや外部ウェブサイトのハイパーリンクを簡単に追加でき、PDF内のナビゲーションとインタラクティビティが向上します。PDF管理プロセスを効率化したい開発者に最適です！",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Working with Links, PDF programmatically, internal page link, external website hyperlink, C# language, PDF document generation, create links in PDF, extract links from PDF, update link destinations, Aspose.PDF for .NET",
    "wordcount": "118",
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
    "url": "/net/navigation-and-interaction/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/navigation-and-interaction/"
    },
    "dateModified": "2024-11-25",
    "description": "このセクションでは、リンク、アクション、およびブックマークに関する機能について説明します。"
}
</script>

- [リンク](/pdf/net/links/) - C#を使用してリンクを簡単に作成、更新、抽出できます。
- [アクション](/pdf/net/actions/) - PDFファイルにハイパーリンクを追加および取得、作成することが可能です。また、この記事では、PDFファイルからドキュメントオープンアクションを削除する方法や、ドキュメントを表示する際にPDFページを指定する方法について学びます。
- [ブックマーク](/pdf/net/bookmarks/) - 大規模な出版物には通常、ブックマークのフレームワークが含まれており、ブックマークペインで簡単に表示および選択できます。これにより、ブックマークをクリックしてそれが表すページや章にジャンプできます。ブックマークペインはコンテンツ認識要素であり、開いているPDF文書にブックマーク構造が含まれている場合にのみサイドバーに表示されます。

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