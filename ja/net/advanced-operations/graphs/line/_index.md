---
title: PDFファイルにラインオブジェクトを追加
linktitle: ラインを追加
type: docs
weight: 40
url: /ja/net/add-line/
description: この記事では、Aspose.PDF for .NETを使用してPDFにラインオブジェクトを作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルにラインオブジェクトを追加",
    "alternativeHeadline": "PDFファイルにラインオブジェクトを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf内のライン",
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
    "url": "/net/add-line/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-line/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFにラインオブジェクトを作成する方法について説明します。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## 線オブジェクトの追加

Aspose.PDF for .NETは、PDFドキュメントにグラフオブジェクト（例えばグラフ、線、四角形など）を追加する機能をサポートしています。また、[線](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/line)オブジェクトを追加する際に、ダッシュパターン、色、その他のフォーマットを指定することもできます。

以下の手順に従ってください：

1. 新しいPDF[ドキュメント](https://reference.aspose.com/pdf/net/aspose.pdf/document)を作成する

1. PDFファイルのページコレクションに[ページ](https://reference.aspose.com/pdf/net/aspose.pdf/page)を追加する

1. [グラフ](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)インスタンスを作成する。

1. ページインスタンスのパラグラフコレクションにグラフオブジェクトを追加する。

1. [四角形](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)インスタンスを作成する。

1. 線の幅を設定する。
1. PDFファイルを保存してください。

次のコードスニペットは、色で塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

```csharp
        public static void AddLineObjectToPDF()
        {
            // Documentインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();

            // Graphインスタンスを作成
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // ページインスタンスの段落コレクションにグラフオブジェクトを追加
            page.Paragraphs.Add(graph);

            // Rectangleインスタンスを作成
            var line = new Line(new float[] { 100, 100, 200, 100 });

            // Graphオブジェクトに塗りつぶし色を指定
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            line.GraphInfo.DashPhase = 1;

            // グラフオブジェクトの形状コレクションにRectangleオブジェクトを追加
            graph.Shapes.Add(line);

            // PDFファイルを保存
            document.Save(_dataDir + "AddLineObject_out.pdf");
        }
```
![Add Line](add_line.png)

## PDFドキュメントに点線を追加する方法

```csharp
        public static void DashLengthInBlackAndDashLengthInWhite()
        {
            // Documentインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();

            // 一定の寸法でDrawingオブジェクトを作成
            var canvas = new Aspose.Pdf.Drawing.Graph(100, 400);
            // ページインスタンスの段落コレクションにdrawingオブジェクトを追加
            page.Paragraphs.Add(canvas);

            // Lineオブジェクトを作成
            var line = new Line(new float[] { 100, 100, 200, 100 });
            // Lineオブジェクトの色を設定
            line.GraphInfo.Color = Color.Red;
            // lineオブジェクトのダッシュ配列を指定
            line.GraphInfo.DashArray = new int[] { 0, 1, 0 };
            // Lineインスタンスのダッシュフェーズを設定
            line.GraphInfo.DashPhase = 1;
            // drawingオブジェクトの形状コレクションに線を追加
            canvas.Shapes.Add(line);
            // PDFファイルを保存
            document.Save(_dataDir + "DashLengthInBlackAndDashLengthInWhite_out.pdf");
        }
```
結果を確認しましょう：

![破線](dash_line.png)

## ページを横切る線を描く

また、左下から右上、左上から右下へと交差する線を描くために線オブジェクトを使用することもできます。

以下のコードスニペットを見て、この要件を達成する方法を確認してください。

```csharp
   public static void ExampleLineAcrossPage()
        {

            // ドキュメントインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();
            // ページのすべての側面に対してマージンを0に設定

            page.PageInfo.Margin.Left = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;

            // ページの寸法と同じ幅と高さでグラフオブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(
                (float)page.PageInfo.Width,
                (float)page.PageInfo.Height);

            // ページの左下から右上への最初の線オブジェクトを作成
            var line = new Line(
                    new float[]{
                        (float)page.Rect.LLX, 0,
                        (float)page.PageInfo.Width,
                        (float)page.Rect.URY });

            // 線をグラフオブジェクトの形状コレクションに追加
            graph.Shapes.Add(line);
            // ページの左上から右下への線を描く
            var line2 = new Line(
                new float[]{ 0,
                    (float) page.Rect.URY,
                    (float) page.PageInfo.Width,
                    (float) page.Rect.LLX });

            // 線をグラフオブジェクトの形状コレクションに追加
            graph.Shapes.Add(line2);

            // グラフオブジェクトをページの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "ExampleLineAcrossPage_out.pdf");
        }
```
![線を描く](draw_line.png)

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
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


