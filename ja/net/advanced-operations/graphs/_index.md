---
title: PDFファイルでのグラフの扱い方
linktitle: グラフの操作
type: docs
weight: 70
url: /ja/net/graphs/
description: この記事では、グラフとは何か、塗りつぶされた長方形オブジェクトの作成方法、およびその他の機能について説明しています。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルでのグラフの扱い方",
    "alternativeHeadline": "PDFでグラフを作成する方法",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, PDF内のグラフ",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
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
                "contactType": "セールス",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "セールス",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "セールス",
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
    "dateModified": "2022-02-04",
    "description": "この記事では、グラフとは何か、塗りつぶされた長方形オブジェクトの作成方法、およびその他の機能について説明しています。"
}
</script>

## グラフとは何か

PDFドキュメントにグラフを追加することは、Adobe Acrobat Writerや他のPDF処理アプリケーションを使用している開発者にとって非常に一般的なタスクです。PDFアプリケーションで使用できる多くの種類のグラフがあります。
[Aspose.PDF for .NET](/pdf/ja/net/) はPDFドキュメントにグラフを追加することもサポートしています。この目的のために、Graphクラスが提供されています。Graphは段落レベルの要素であり、PageインスタンスのParagraphsコレクションに追加することができます。Graphインスタンスには、形状のコレクションが含まれています。

以下のタイプの形状は、[Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)クラスによってサポートされています：

- [Arc](/pdf/ja/net/add-arc/) - 隣接する頂点の順序付きペアとしても呼ばれることがありますが、指向性のある線とも呼ばれることがあります。
- [Circle](/pdf/ja/net/add-circle/) - セクターに分割された円を使用してデータを表示します。データが1つの全体または1つのグループの部分をどのように表しているかを示すために、円グラフ（パイチャートとも呼ばれる）を使用します。
- [Curve](/pdf/ja/net/add-curve/) - プロジェクティブラインの連合で、各ラインは通常の二重点で他の3つのラインと会います。
- [Curve](/pdf/ja/net/add-curve/) - 投影線の接続された連合であり、各線は通常の二重点で他の三つと接触します。
- [Line](/pdf/ja/net/add-line) - 折れ線グラフは連続データを表示するのに使用され、時間をかけてトレンドが表示される場合、将来のイベントを予測するのに役立ちます。
- [Rectangle](/pdf/ja/net/add-rectangle/) - グラフで見られる多くの基本的な形状の一つであり、問題を解決するのに非常に役立ちます。
- [Ellipse](/pdf/ja/net/add-ellipse/) - 平面上の点の集合で、楕円形の曲線を作成します。

上記の詳細は以下の図にも示されています：

![Figures in Graphs](graphs.png)

