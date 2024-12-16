---
title: PDFでのテーブル操作についてのC#使用法
linktitle: テーブルの操作
type: docs
weight: 50
url: /ja/net/working-with-tables/
description: このセクションでは、テーブルの追加と抽出、C#ライブラリを使用したテーブルの操作と統合方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFでのテーブル操作についてのC#使用法",
    "alternativeHeadline": "PDFでのテーブルの操作方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdf内のテーブル",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
    "url": "/net/working-with-tables/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-tables/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、テーブルの追加と抽出、C#ライブラリを使用したテーブルの操作と統合方法について説明します。"
}
</script>
PDF フォームには多くの場合、テーブルが含まれています。さまざまな形式のフォームでテーブルを見つけることができます。

**Aspose.PDF for .NET** は、PDF ファイルで高度にテーブルを扱うことができます。この完璧なツールは、実際のデータのテーブルを抽出することで PDF の単純さを克服するのに役立ちます。.NET ライブラリリソースを使用すると、既存の PDF ドキュメントにテーブルを簡単に作成または追加したり、テーブルを抽出したり、データソースとテーブルを統合したり、既存の PDF からテーブルを削除したりすることができます。

以下の操作が可能です：

- [既存の PDF ドキュメントにテーブルを作成または追加する](/pdf/ja/net/add-table-in-existing-pdf-document/) - 列または行の結合、境界線、余白、パディングを考慮して PDF ファイルにテーブルを作成します。
- [既存の PDF ドキュメントからテーブルを抽出する](/pdf/ja/net/extract-table-from-existing-pdf-document/) - PDF ファイルからテーブルを抽出するか、テーブルの境界線を画像として抽出します。
- [データソースとテーブルを統合する](/pdf/ja/net/integrate-table/) - データベースとテーブルを統合する、Entity Framework ソースを使用して .NET ライブラリとテーブルを統合します。
- [既存の PDF でテーブルを操作する](/pdf/ja/net/manipulate-tables-in-existing-pdf/) - TableAbsorber を使用して PDF のテーブルを操作します。
- [既存のPDF内の表を操作する](/pdf/ja/net/manipulate-tables-in-existing-pdf/) - TableAbsorberを使用してPDF内の表を操作します。
- [既存のPDFから表を削除する](/pdf/ja/net/remove-tables-from-existing-pdf/) - PDFドキュメントから表または複数の表を削除します。

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

