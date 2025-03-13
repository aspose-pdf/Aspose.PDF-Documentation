---
title: PDFファイルでのグラフの操作
linktitle: グラフの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/working-with-graphs/
description: この記事では、グラフとは何か、塗りつぶされた長方形オブジェクトの作成方法、およびその他の機能について説明します
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Graphs in PDF file",
    "alternativeHeadline": "Create and Manipulate Graphs in PDF Files",
    "abstract": "Aspose.PDF for .NETを使用してPDF文書内でグラフを生成および操作するための強力な新機能を発見してください。この機能により、開発者はアーク、円、線、長方形など、さまざまなグラフ形状を作成でき、アプリケーション内のデータの視覚的プレゼンテーションを向上させます。PDF生成プロセスを最適化し、動的なデータビジュアライゼーションを簡単に提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Graph, PDF documents, Aspose.PDF for .NET, Graph class, Shapes, Arc, Circle, Line graph, Rectangle, PDF manipulation",
    "wordcount": "329",
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
    "url": "/net/graphs/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/graphs/"
    },
    "dateModified": "2024-11-25",
    "description": "この記事では、グラフとは何か、塗りつぶされた長方形オブジェクトの作成方法、およびその他の機能について説明します"
}
</script>

## グラフとは

PDF文書にグラフを追加することは、Adobe Acrobat Writerやその他のPDF処理アプリケーションを使用する開発者にとって非常に一般的な作業です。PDFアプリケーションで使用できるグラフの種類は多数あります。
[Aspose.PDF for .NET](/pdf/net/)もPDF文書にグラフを追加することをサポートしています。この目的のために、Graphクラスが提供されています。Graphは段落レベルの要素であり、PageインスタンスのParagraphsコレクションに追加できます。GraphインスタンスにはShapesのコレクションが含まれています。

[Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)クラスでサポートされている形状の種類は次のとおりです：

- [アーク](/pdf/ja/net/add-arc/) - 時にはフラグとも呼ばれ、隣接する頂点の順序対ですが、時には有向線とも呼ばれます。
- [円](/pdf/ja/net/add-circle/) - データをセクターに分割された円を使用して表示します。データが全体またはグループの一部を表す方法を示すために円グラフ（パイチャートとも呼ばれます）を使用します。
- [曲線](/pdf/ja/net/add-curve/) - 各線が他の三つの線と通常の二重点で交わる投影線の接続された集合です。
- [線](/pdf/ja/net/add-line) - 線グラフは連続データを表示するために使用され、時間の経過に伴うトレンドを示すときに将来のイベントを予測するのに役立ちます。
- [長方形](/pdf/ja/net/add-rectangle/) - グラフで見る多くの基本的な形状の一つであり、問題を解決するのに非常に役立ちます。
- [楕円](/pdf/ja/net/add-ellipse/) - 平面上の点の集合で、楕円形の曲線を作成します。

形状タイプに対してサポートされている操作は次のとおりです：
- [境界をチェック](/pdf/net/aspose-pdf-drawing-graph-shapes-bounds-check/) - Shapesコレクション内の形状の境界をチェックします。

上記の詳細は以下の図にも示されています：

![グラフの図](graphs.png)


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