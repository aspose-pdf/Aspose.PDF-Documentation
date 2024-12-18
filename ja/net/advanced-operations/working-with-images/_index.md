---
title: PDFでの画像操作についてのC#使用方法
linktitle: 画像操作
type: docs
weight: 40
url: /ja/net/working-with-images/
description: このセクションでは、C# ライブラリを使用して PDF ファイルで画像を操作する機能について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/manipulate-images/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFでの画像操作についてのC#使用方法",
    "alternativeHeadline": "PDFでの画像操作方法.NETを使って",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdf内の画像",
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
    "url": "/net/working-with-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-images/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、C# ライブラリを使用して PDF ファイルで画像を操作する機能について説明します。"
}
</script>
PDF形式の画像は非常に複雑なトピックです。PDFドキュメントの作業に直面したユーザーを待っている画像のさまざまな操作があります。私たちは、画像をファイルに追加または削除することしかできないと思っていますが、Aspose.PDFライブラリを使用すると、画像サイズの設定、画像の置換、画像の抽出、検索、PDFドキュメントからの画像の取得なども可能です。

**PDFに画像を追加する方法は？** Aspose.PDFを使用したPDFの画像に関する最も人気のある質問に答えます。

**Aspose.PDF for .NET** はデジタルドキュメントを扱うための賢く効率的なツールで、任意のグラフィックオブジェクトを既存のPDFにすばやくインポートして配置できます。
C#ライブラリを使用することも、レポートにチャートを挿入したり、プロジェクトにフロアプランのオーバーレイを追加したり、履歴書に写真を含めたりする場合に役立ちます。PDFドキュメントで画像を挿入および編集する高度な方法を探している場合は、次の記事を学ぶことを強くお勧めします。

以下の操作が可能です：
以下の操作が可能です：

- [既存のPDFファイルに画像を追加する](/pdf/ja/net/add-image-to-existing-pdf-file/) - PDFドキュメントに単一の画像とその参照を追加し、その後品質を管理します。
- [PDFファイルから画像を削除する](/pdf/ja/net/delete-images-from-pdf-file/) - PDFファイルから画像を削除するためのコードスニペットを確認します。
- [PDFファイルから画像を抽出する](/pdf/ja/net/extract-images-from-pdf-file/) - Imagesコレクションを使用してPDFファイルから画像を抽出します。
- [埋め込まれた画像の解像度と寸法を取得する](/pdf/ja/net/get-resolution-and-dimensions-of-embedded-images/) - Aspose.PDF名前空間内のオペレータークラスを使用して、解像度と寸法情報を取得する機能を提供します。
- [画像配置の操作](/pdf/ja/net/working-with-image-placement/) - PDFドキュメントで画像の解像度と位置を取得することが可能です。
- [PDFドキュメントから画像を検索して取得する](/pdf/ja/net/search-and-get-images-from-pdf-document/) - 個々のページから画像を取得し、C#を使用して全ページの画像の中から検索することができます。
- [PDFドキュメントから画像を検索して取得する](/pdf/ja/net/search-and-get-images-from-pdf-document/) - 個々のページから画像を取得し、すべてのページの画像を検索することができます。
- [既存のPDFファイル内の画像を置換する](/pdf/ja/net/replace-image-in-existing-pdf-file/) - このコードスニペットを確認してください。PDFファイル内の画像を置換する方法を示しています。
- [画像サイズの設定](/pdf/ja/net/set-image-size/) - C# ライブラリを使用して画像のサイズを設定できます。
- [デフォルトフォント名の設定](/pdf/ja/net/set-default-font-name/) - 変換プロセスのデフォルトフォント名を設定します。
- [PDFドキュメントからサムネイル画像を生成する](/pdf/ja/net/generate-thumbnail-images-from-pdf-documents/) - 次の記事では、最初にAcrobat SDKを使用し、次にAspose.PDFを使用してPDFドキュメントからサムネイル画像を生成する方法を示しています。
- DICOM画像のサポート - Aspose.PDF for .NETは、特別な医療用グラフィック標準の画像をサポートしています。
- DICOM画像のサポート - Aspose.PDF for .NETは、特別な医療用グラフィック標準の画像をサポートしています。

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


