---
title: PDFファイルにカーブオブジェクトを追加
linktitle: カーブを追加
type: docs
weight: 30
url: /net/add-curve/
description: この記事では、Aspose.PDF for .NETを使用してPDFにカーブオブジェクトを作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルにカーブオブジェクトを追加",
    "alternativeHeadline": "PDFファイルにカーブオブジェクトを作成する方法",
    "author": {
        "@type": "Person",
        "name":"アナスタシア・ホルブ",
        "givenName": "アナスタシア",
        "familyName": "ホルブ",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, .net, pdf内のカーブ",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF ドキュメントチーム",
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
    "url": "/net/add-curve/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-curve/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFにカーブオブジェクトを作成する方法について説明します。"
}
</script>
次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも機能します。

## Curve オブジェクトの追加

グラフ [Curve](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/curve) は、各線が通常の二重点で他の3つの線と接続される射影線の連合です。

Aspose.PDF for .NETは、グラフでベジェ曲線の使用方法を示しています。
ベジェ曲線は、滑らかな曲線をモデル化するためにコンピュータグラフィックスで広く使用されています。曲線は、その制御点の凸包に完全に含まれ、点はグラフィカルに表示され、曲線を直感的に操作するために使用されることができます。
全体の曲線は、与えられた四つの点（それらの凸包）の角がある四角形に含まれています。

この記事では、PDFドキュメントで作成できる単純なグラフカーブと塗りつぶされたカーブについて調査します。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) インスタンスを作成する

1.
1. [Drawing](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) オブジェクトに枠線を設定する

1. [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) オブジェクトをページのパラグラフコレクションに追加する

1. PDFファイルを保存する

```csharp
 public static void ExampleCurve()
        {
            // Documentインスタンスを作成する
            var document = new Document();

            // ページをPDFファイルのページコレクションに追加する
            var page = document.Pages.Add();

            // 特定の寸法でDrawingオブジェクトを作成する
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Drawingオブジェクトに枠線を設定する
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // Graphオブジェクトをページのパラグラフコレクションに追加する
            page.Paragraphs.Add(graph);

            // PDFファイルを保存する
            document.Save(_dataDir + "DrawingCurve1_out.pdf");
        }
```
以下の画像は、私たちのコードスニペットを実行した結果を示しています。

![Drawing Curve](drawing_curve.png)

## 塗りつぶされたカーブオブジェクトの作成

この例は、色で塗りつぶされたカーブオブジェクトを追加する方法を示しています。

```csharp
      public static void CurveFilled()
        {
            // ドキュメントインスタンスを作成
            var document = new Document();

            // ページをPDFファイルのページコレクションに追加
            var page = document.Pages.Add();

            // 特定の寸法で描画オブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // 描画オブジェクトに境界を設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120 });
            curve1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(curve1);

            // グラフオブジェクトをページの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingCurve2_out.pdf");
        }
```
充填されたカーブを追加した結果を見てください：

![充填カーブ](filled_curve.png)

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
                "contactType": "販売",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "総合評価",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

