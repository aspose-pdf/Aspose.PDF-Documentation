---
title: アノテーションを使用する
linktitle: PDFのアノテーション
type: docs
weight: 100
url: ja/net/annotations/
description: このセクションでは、Aspose.PDF ライブラリを使用して PDF ファイルにすべての種類のアノテーションを使用する方法を示します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /net/working-with-annotations/
    - /net/annotation/
    - /net/working-with-annotations-facades/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF アノテーション",
    "alternativeHeadline": "PDFでのアノテーションの使用",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf ドキュメント生成",
    "keywords": "pdf, c#, アノテーション",
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
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、Aspose.PDF ライブラリを使用して PDF ファイルにすべての種類のアノテーションを使用する方法を示します。"
}
</script>
PDFページの中身を編集することは難しいですが、PDF仕様ではページ内容を変更せずにPDFページに追加できるオブジェクトの完全なセットを定義しています。

これらのオブジェクトは注釈と呼ばれ、ページ内容のマークアップからフォームなどのインタラクティブ機能の実装まで、さまざまな目的があります。

PDFビューアは通常、テキストのハイライト、ノート、ライン、形状など、さまざまな注釈タイプの作成と編集を許可します。作成できる注釈タイプに関わらず、PDF仕様に準拠しているPDFビューアは、すべての注釈タイプのレンダリングもサポートする必要があります。

注釈はPDFファイルの重要な部分です。Aspose.PDF for .NETを使用すると、新しい注釈を追加、既存の注釈を編集、注釈を削除するなどができます。このセクションでは以下のトピックをカバーしています：

以下のことができます：

- [注釈の概要](/pdf/net/overview-of-annotations/) - PDF仕様によって定義された注釈の種類とAspose.PDFがサポートする内容を学びます。
- [注釈の追加、削除、取得](/pdf/net/add-delete-and-get-annotation/) - このセクションでは、許可されたすべてのタイプの注釈を扱う方法について説明します。
- [アノテーションの追加、削除、取得](/pdf/net/add-delete-and-get-annotation/) - このセクションでは、許可されているすべてのタイプのアノテーションの操作方法について説明します。
- [XFDF形式でアノテーションをインポートおよびエクスポートする](/pdf/net/import-export-xfdf/) - Aspose.PDFライブラリは、アノテーションデータをXFDFファイルにインポートおよびエクスポートするための方法を提供します。

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


