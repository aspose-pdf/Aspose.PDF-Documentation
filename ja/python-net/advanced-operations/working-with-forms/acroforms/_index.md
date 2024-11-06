---
title: Pythonを使用したAcroFormsの操作
linktitle: AcroForms
type: docs
weight: 10
url: ja/python-net/acroforms/
description: Aspose.PDF for Pythonを使用すると、最初からフォームを作成したり、PDFドキュメントのフォームフィールドに入力したり、フォームからデータを抽出したりすることができます。
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Pythonを使用したAcroFormsの操作",
    "alternativeHeadline": "PDFでのAcroFormsの操作オプション",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, acroforms in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/acroforms/"
    },
    "dateModified": "2023-02-04",
    "description": "Aspose.PDF for Pythonを使用すると、最初からフォームを作成したり、PDFドキュメントのフォームフィールドに入力したり、フォームからデータを抽出したりすることができます。"
}
</script>


## AcroFormsの基本

**AcroForms** - AdobeによるユニークなPDFフォーム技術。AcroFormsはページ指向のフォームです。1998年に初めて登場しました。データフォーマットまたはFDFおよびXMLフォームデータフォーマットまたはxFDFの形式で入力を受け付けます。サードパーティプロバイダーがAcroFormsをサポートしています。AdobeがAcroFormsを導入した際、彼らはそれを「Adobe Acrobat Pro/Standardの著者によるPDFフォームであり、静的または動的なXFAフォームの特別なタイプではない」と呼びました。AcroFormsはポータブルで、すべてのプラットフォームで動作します。

AcroFormsを使用してPDFフォームドキュメントに追加のページを追加することができます。テンプレートの概念により、複数のデータベースレコードでフォームを埋めることをサポートするためにAcroFormsを使用できます。

PDF 1.7は、データとPDFフォームを統合するための2つの異なる方法をサポートしています。

*AcroForms（アクロバットフォームとしても知られています）*、PDF 1.2形式仕様で導入され、含まれています。

Javaライブラリの機能についての詳細な学習のために、以下の記事を参照してください：

- [Create AcroForm](/pdf/python-net/create-form) - Pythonでゼロからフォームを作成します。
- [AcroForm を記入する](/pdf/python-net/fill-form) - PDFドキュメントのフォームフィールドに記入します。
- [AcroForm を抽出する](/pdf/python-net/extract-form) - PDFドキュメントのすべてまたは個別のフィールドから値を取得します。

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF 操作ライブラリ for Python",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>