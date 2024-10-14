---
title: PDFページサイズをC#で変更する
linktitle: PDFページサイズの変更
type: docs
weight: 40
url: /net/change-page-size/
description: Aspose.PDF for .NETライブラリを使用してPDFドキュメントのページサイズを変更します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFページサイズをC#で変更する",
    "alternativeHeadline": ".NETでPDFページをリサイズ",
    "author": {
        "@type": "Person",
        "name": "アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdfサイズ変更, pdfリサイズ",
    "wordcount": "302",
    "proficiencyLevel": "初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDFドキュメントチーム",
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/change-page-size/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-page-size/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NETライブラリを使用してPDFドキュメントのページサイズを変更します。"
}
</script>
## PDFページサイズの変更

Aspose.PDF for .NETを使用すると、.NETアプリケーションでPDFページサイズを簡単なコードで変更できます。このトピックでは、既存のPDFファイルのページ寸法（サイズ）を更新/変更する方法について説明します。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも機能します。

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) クラスには、SetPageSize(...) メソッドが含まれており、ページサイズを設定できます。以下のコードスニペットは、数ステップでページ寸法を更新します：

1. ソースPDFファイルを読み込む。
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) オブジェクトにページを取得する。
1. 特定のページを取得する。
1. SetPageSize(..) メソッドを呼び出してその寸法を更新する。
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) クラスの Save(..) メソッドを呼び出して、ページ寸法が更新されたPDFファイルを生成する。

{{% alert color="primary" %}}

高さと幅のプロパティは基本単位としてポイントを使用することに注意してください。ここで、1インチ = 72ポイント、1 cm = 1/2.54インチ = 0.3937インチ = 28.3ポイントです。
高さと幅のプロパティは基本単位としてポイントを使用します。1インチ = 72ポイント、1cm = 1/2.54インチ = 0.3937インチ = 28.3ポイントです。

{{% /alert %}}

以下のコードスニペットは、PDFページの寸法をA4サイズに変更する方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-UpdateDimensions-UpdateDimensions.cs" >}}

## PDFページサイズの取得

既存のPDFファイルのPDFページサイズを読み取ることができます。次のコードサンプルは、C#を使用してPDFページの寸法を読み取る方法を示しています。

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetDimensions-GetDimensions.cs" >}}

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


