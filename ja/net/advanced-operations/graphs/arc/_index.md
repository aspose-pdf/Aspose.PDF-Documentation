---
title: PDFファイルにアークオブジェクトを追加
linktitle: アークの追加
type: docs
weight: 10
url: ja/net/add-arc/
description: この記事では、Aspose.PDF for .NETを使用してPDFにアークオブジェクトを作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルにアークオブジェクトを追加",
    "alternativeHeadline": "PDFファイルでアークを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf内のアーク",
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
    "url": "/net/add-arc/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-arc/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFにアークオブジェクトを作成する方法について説明します。"
}
</script>

以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## アークオブジェクトを追加する

Aspose.PDF for .NET は、PDFドキュメントにグラフオブジェクト（例えばグラフ、ライン、長方形など）を追加する機能をサポートしています。また、アークオブジェクトを特定の色で塗りつぶす機能も提供しています。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) インスタンスを作成する

1. 特定の寸法で [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing) を作成する

1. Drawing objectの [Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border) を設定する

1. [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) オブジェクトをページのパラグラフコレクションに追加する

1. PDFファイルを保存する

以下のコードスニペットは [Arc](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/arc) オブジェクトを追加する方法を示しています。

```csharp
 public static void Arc()
        {
            // Document インスタンスを作成
            var document = new Document();

            // ページをPDFファイルのページコレクションに追加
            var page = document.Pages.Add();

            // 特定の寸法で Drawing オブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Drawing オブジェクトの境界を設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc1 = new Arc(100, 100, 95, 0, 90);
            arc1.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(arc1);

            var arc2 = new Arc(100, 100, 90, 70, 180);
            arc2.GraphInfo.Color = Color.DarkBlue;
            graph.Shapes.Add(arc2);

            var arc3 = new Arc(100, 100, 85, 120, 210);
            arc3.GraphInfo.Color = Color.Red;
            graph.Shapes.Add(arc3);

            // Graph オブジェクトをページのパラグラフコレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingArc_out.pdf");

        }
```
## 塗りつぶされたアークオブジェクトの作成

次の例は、色と特定の寸法で塗りつぶされたアークオブジェクトを追加する方法を示しています。

```csharp
        public static void ArcFilled()
        {
            // ドキュメントインスタンスを作成する
            var document = new Document();

            // PDFファイルのページコレクションにページを追加する
            var page = document.Pages.Add();

            // 特定の寸法で描画オブジェクトを作成する
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // 描画オブジェクトにボーダーを設定する
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var arc = new Arc(100, 100, 95, 0, 90);
            arc.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(arc);

            var line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
            line.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(line);

            // グラフオブジェクトをページの段落コレクションに追加する
            page.Paragraphs.Add(graph);

            // PDFファイルを保存する
            document.Save(_dataDir + "ExampleFilledArc_out.pdf");

        }
```
# 塗りつぶされたアークの追加結果を見てみましょう：

![Filled Arc](filled_arc.png)

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
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "販売",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "販売",
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

