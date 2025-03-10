---
title: 注釈の追加、削除、取得
linktitle: 注釈の追加、削除、取得
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/add-delete-and-get-annotation/
description: Aspose.PDF for .NETを使用すると、PDFファイルから注釈を追加、削除、取得できます。タスクを解決するために、すべての注釈リストを確認してください。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add, Delete and Get Annotation",
    "alternativeHeadline": "Manage PDF Annotations with Aspose.PDF for .NET",
    "abstract": "Aspose.PDF for .NETの新しい注釈の追加、削除、取得機能を使用して、PDF操作能力を強化します。この強力な機能により、ユーザーはPDFファイル内の注釈をシームレスに管理でき、編集が簡素化され、コンテンツのインタラクションが向上します。特定の文書ニーズに応じてさまざまな種類の注釈を操作する方法を発見してください。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "add annotation, delete annotation, get annotation, Aspose.PDF for .NET, PDF document generation, PDF annotations, multimedia annotation, PDF text annotation, highlights annotation, PDF manipulation library",
    "wordcount": "174",
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
    "url": "/net/add-delete-and-get-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-delete-and-get-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NETを使用すると、PDFファイルから注釈を追加、削除、取得できます。タスクを解決するために、すべての注釈リストを確認してください。"
}
</script>

**PDFドキュメントにおける注釈とは何ですか？**

これは、テキストの内容を拡張したり、他のユーザーへの編集やコメントを行ったりするためにファイルに追加する追加オブジェクトです。また、文書内のテキストをより読みやすくしたり、ハイライトしたり、下線を引いたり、まったく新しいテキストを追加したりすることも可能です。

私たちは、Aspose.PDF for .NETライブラリで利用可能なさまざまな種類の注釈をグループにまとめました：

- [PDFテキスト注釈](/pdf/net/text-annotation/)
- [PDFハイライト注釈](/pdf/net/highlights-annotation/)
- [PDF図形注釈](/pdf/net/figures-annotation/)
- [マルチメディア注釈](/pdf/net/multimedia-annotation/)
- [PDFスティッキー注釈](/pdf/net/sticky-annotations/)
- [リンク注釈](/pdf/net/link-annotations/)
- [追加の注釈](/pdf/net/extra-annotations/)

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