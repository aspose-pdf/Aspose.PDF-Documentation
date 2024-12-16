---
title: PDFファイルに円オブジェクトを追加
linktitle: 円を追加
type: docs
weight: 20
url: /ja/net/add-circle/
description: この記事では、Aspose.PDF for .NETを使用してPDFに円オブジェクトを作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルに円オブジェクトを追加",
    "alternativeHeadline": "PDFファイルで円オブジェクトを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdf内の円",
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
    "url": "/net/add-circle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-circle/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFに円オブジェクトを作成する方法について説明します。"
}
</script>

以下のコードスニペットは[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリともに動作します。

## 円オブジェクトの追加

棒グラフと同様に、円グラフも複数の別々のカテゴリのデータを表示するために使用できます。しかし、棒グラフと異なり、円グラフは全体を構成するすべてのカテゴリのデータがある場合にのみ使用できます。それでは、Aspose.PDF for .NETで[Circle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/circle)オブジェクトを追加する方法を見ていきましょう。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)インスタンスを作成する

1. 特定の寸法で[Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing)を作成する

1. Drawingオブジェクトに[Border](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph/properties/border)を設定する

1. [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)オブジェクトをページの段落コレクションに追加する

1. PDFファイルを保存する

```csharp
        public static void Circle()
        {
            // Documentインスタンスを作成
            var document = new Document();

            // ページをPDFファイルのページコレクションに追加
            var page = document.Pages.Add();

            // 特定の寸法でDrawingオブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);
            // Drawingオブジェクトに境界を設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);

            circle.GraphInfo.Color = Color.GreenYellow;
            graph.Shapes.Add(circle);

            // Graphオブジェクトをページの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingCircle1_out.pdf");
        }
```
私たちが描いた円はこのように見えます：

![Drawing Circle](drawing_circle.png)

## 塗りつぶされた円オブジェクトの作成

この例では、色で塗りつぶされた円オブジェクトを追加する方法を示します。

```csharp
        public static void CircleFilled()
        {
            // Documentインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();

            // 特定の寸法でDrawingオブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 200);

            // Drawingオブジェクトの境界を設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var circle = new Circle(100, 100, 40);
            circle.GraphInfo.Color = Color.GreenYellow;
            circle.GraphInfo.FillColor = Color.Green;
            circle.Text = new TextFragment("Circle");

            graph.Shapes.Add(circle);

            // Graphオブジェクトをページの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingCircle2_out.pdf");
        }
```

塗りつぶし円を追加した結果を見てみましょう:

![Filled Circle](filled_circle.png)

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
    "applicationCategory": "PDF操作ライブラリ for .NET",
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
```

