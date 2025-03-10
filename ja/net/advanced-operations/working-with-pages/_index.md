---
title: C#でのPDFページの操作
linktitle: ページの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/working-with-pages/
description: このセクションでは、ページの追加、ヘッダーとフッターの追加、透かしの追加方法について説明します。Aspose.PDF for .NETがこのトピックのすべての詳細を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF Pages in C#",
    "alternativeHeadline": "Enhance PDF Management with C# Page Features",
    "abstract": "ページの追加、移動、削除を正確に行うためのAspose.PDF for .NETの高度な機能を発見してください。この機能により、ユーザーはヘッダー、フッター、透かし、カスタムページサイズを直感的なC#コードを通じてPDF文書に組み込むことができます。シームレスなPDF操作とカスタマイズ機能で文書ワークフローを最適化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "450",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2024-11-26",
    "description": "このセクションでは、ページの追加、ヘッダーとフッターの追加、透かしの追加方法について説明します。Aspose.PDF for .NETがこのトピックのすべての詳細を説明します。"
}
</script>

**Aspose.PDF for .NET** は、PDF文書の任意の位置にページを挿入したり、PDFファイルの末尾にページを追加したりできます。このセクションでは、Acrobat Readerを使用せずにPDFにページを追加する方法を示します。
PDFファイルのヘッダーとフッターにテキストや画像を追加し、AsposeのC#ライブラリを使用して文書内で異なるヘッダーを選択できます。
また、C#を使用してプログラム的にPDF文書のページをトリミングすることも試みてください。

このセクションでは、Artifactクラスを使用してPDFファイルに透かしを追加する方法を学びます。このタスクのプログラミングサンプルを確認します。
PageNumberStampクラスを使用してページ番号を追加します。文書にスタンプを追加するには、ImageStampおよびTextStampクラスを使用します。**Aspose.PDF for .NET**を使用してPDFファイルに背景画像を作成するための透かしを追加します。

以下のことができます：

- [ページを追加](/pdf/ja/net/add-pages/) - 希望の位置にページを追加したり、PDFファイルの末尾に追加したり、文書からページを削除します。
- [ページを移動](/pdf/ja/net/move-pages/) - 1つの文書から別の文書にページを移動します。
- [ページを削除](/pdf/ja/net/delete-pages/) - PageCollectionコレクションを使用してPDFファイルからページを削除します。
- [ページサイズを変更](/pdf/ja/net/change-page-size/) - Aspose.PDFライブラリを使用してコードスニペットでPDFページサイズを変更できます。
- [ページを回転](/pdf/ja/net/rotate-pages/) - 既存のPDFファイル内のページの向きを変更できます。
- [ページを分割](/pdf/ja/net/split-document/) - PDFファイルを1つまたは複数のPDFに分割できます。
- [ヘッダーおよび/またはフッターを追加](/pdf/ja/net/add-headers-and-footers-of-pdf-file/) - PDFファイルのヘッダーとフッターにテキストや画像を追加します。
- [ページをトリミング](/pdf/ja/net/crop-pages/) - 異なるページプロパティを使用してプログラム的にPDF文書のページをトリミングできます。
- [透かしを追加](/pdf/ja/net/add-watermarks/) - Artifactクラスを使用してPDFファイルに透かしを追加します。
- [PDFファイルにページ番号を追加](/pdf/ja/net/add-page-number/) - PageNumberStampクラスを使用してPDFファイルにページ番号を追加します。
- [背景を追加](/pdf/ja/net/add-backgrounds/) - 背景画像を使用して透かしを追加できます。
- [スタンピング](/pdf/ja/net/stamping/) - ImageStampクラスを使用してPDFファイルに画像スタンプを追加し、TextStampクラスを使用してテキストを追加できます。

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