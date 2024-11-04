---
title: PDF内のテキストをC#を使用して操作する
linktitle: テキスト操作
type: docs
weight: 30
url: /net/working-with-text/
description: このセクションでは、テキスト処理のさまざまな技術について説明します。Aspose.PDFとC#を使用してテキストを追加、置換、回転、検索する方法を学びます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF内のテキストをC#を使用して操作する",
    "alternativeHeadline": "PDFファイルでテキストを追加、回転、検索、削除する",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, テキストを追加, テキストを検索, テキストを削除, PDF内のテキストを操作",
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
    "url": "/net/working-with-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-text/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、テキスト処理のさまざまな技術について説明します。Aspose.PDFとC#を使用してテキストを追加、置換、回転、検索する方法を学びます。"
}
</script>
私たちは時々PDFファイルにテキストを追加する必要があります。たとえば、メインテキストの下に翻訳を追加したい場合、画像の隣にキャプションを配置したい場合、または単に申請書に記入したい場合などです。すべてのテキスト要素を自分の望むスタイルでフォーマットできると便利です。PDFファイルで最も人気のあるテキスト操作には、PDFにテキストを追加する、PDFファイル内のテキストをフォーマットする、ドキュメント内のテキストを置換および回転するなどがあります。**Aspose.PDF for .NET**は、PDFコンテンツとの対話に必要なすべてを備えた最適なソリューションです。

以下の操作が可能です：

- [PDFファイルにテキストを追加する](/pdf/net/add-text-to-pdf-file/) - PDFにテキストを追加し、ストリームとファイルからフォントを使用し、HTML文字列を追加し、ハイパーリンクなどを追加します。
- [PDFツールチップ](/pdf/net/pdf-tooltip/) - C#を使用して透明なボタンを追加することにより、検索されたテキストにツールチップを追加できます。
- [PDF内のテキストフォーマット](/pdf/net/text-formatting-inside-pdf/) - ドキュメントに追加できる多くの機能があります。
- [PDF内のテキストフォーマット](/pdf/net/text-formatting-inside-pdf/) - テキストのフォーマット時に文書に追加できる多くの機能。
- [PDF内のテキストを置換する](/pdf/net/replace-text-in-pdf/) - PDFドキュメントの全ページのテキストを置換するには、最初にTextFragmentAbsorberを使用する必要があります。
- [PDF内のテキストを回転する](/pdf/net/rotate-text-inside-pdf/) - TextFragmentクラスの回転プロパティを使用してPDF内のテキストを回転します。
- [PDFドキュメントのページからテキストを検索して取得する](/pdf/net/search-and-get-text-from-pdf/) - ページからテキストを検索して取得するためにTextFragmentAbsorberクラスを使用できます。
- [改行を特定する](/pdf/net/determine-line-break/) - このトピックでは、複数行のテキストフラグメントの改行を追跡する方法について説明します。

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

