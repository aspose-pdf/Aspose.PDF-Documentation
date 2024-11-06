---
title: PDFファイルに長方形オブジェクトを追加
linktitle: 長方形を追加
type: docs
weight: 50
url: ja/net/add-rectangle/
description: この記事では、Aspose.PDF for .NETを使用してPDFにRectangleオブジェクトを作成する方法を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルに長方形オブジェクトを追加",
    "alternativeHeadline": "PDFファイルに長方形オブジェクトを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "pdf, c#, pdf内の長方形",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFにRectangleオブジェクトを作成する方法を説明します。"
}
</script>
次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

## Rectangle オブジェクトの追加

Aspose.PDF for .NETは、PDF文書にグラフィックオブジェクト（例えばグラフ、ライン、レクタングルなど）を追加する機能をサポートしています。[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) オブジェクトを追加する際に、特定の色でレクタングルオブジェクトを塗りつぶす機能、Z-Orderを制御する機能、グラデーションカラーの塗りつぶしを追加する機能なども提供しています。

まず、Rectangleオブジェクトを作成する可能性について見てみましょう。

以下の手順に従ってください：

1. 新しいPDF [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) を作成する

1. PDFファイルのページコレクションに [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) を追加する

1. ページインスタンスのパラグラフコレクションに [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) を追加する

1. [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph) インスタンスを作成する

1.
1. Rectangle インスタンスを作成する

1. [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle) オブジェクトを Graph オブジェクトの shapes コレクションに追加する

1. Graph オブジェクトをページインスタンスの paragraphs コレクションに追加する

1. [Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment) をページインスタンスの paragraphs コレクションに追加する

1. PDFファイルを保存する

```csharp
 private static void AddRectangle(Page page, float x, float y, float width, float height, Color color, int zindex)
        {
            // Rectangle オブジェクトの指定された寸法と同じ寸法の graph オブジェクトを作成する
            Aspose.Pdf.Drawing.Graph graph = new Aspose.Pdf.Drawing.Graph(width, height)
            {
                // graph インスタンスの位置を変更できるか
                IsChangePosition = false,
                // Graph インスタンスの Left 座標位置を設定
                Left = x,
                // Graph オブジェクトの Top 座標位置を設定
                Top = y
            };
            // "graph" 内に rectangle を追加する
            Rectangle rect = new Rectangle(0, 0, width, height);
            // rectangle の塗りつぶし色を設定
            rect.GraphInfo.FillColor = color;
            // graph オブジェクトの色
            rect.GraphInfo.Color = color;
            // rectangle を graph インスタンスの shapes コレクションに追加する
            graph.Shapes.Add(rect);
            // rectangle オブジェクトの Z-Index を設定する
            graph.ZIndex = zindex;
            // graph をページオブジェクトの paragraphs コレクションに追加する
            page.Paragraphs.Add(graph);
        }
```
![Create Rectangle](create_rectangle.png)

## 塗りつぶされた長方形オブジェクトの作成

Aspose.PDF for .NETは、特定の色で長方形オブジェクトを塗りつぶす機能も提供しています。

以下のコードスニペットは、色で塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

```csharp
    {
        private const string _dataDir = "C:\\Samples\\";
        public static void RectangleFilled()
        {
            // Document インスタンスを作成
            var doc = new Document();

            // ページをPDFファイルのページコレクションに追加
            var page = doc.Pages.Add();
            // Graph インスタンスを作成
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

            // Graphオブジェクトをページインスタンスの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // Rectangle インスタンスを作成
            var rect = new Rectangle(100, 100, 200, 120);

            // Graphオブジェクトの塗りつぶし色を指定
            rect.GraphInfo.FillColor = Color.Red;

            // RectangleオブジェクトをGraphオブジェクトの形状コレクションに追加
            graph.Shapes.Add(rect);

            // PDFファイルを保存
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
固体色で塗りつぶされた長方形の結果を見てください：

![Filled Rectangle](fill_rectangle.png)

## グラデーション塗りつぶしを追加する

Aspose.PDF for .NETは、PDFドキュメントにグラフオブジェクトを追加する機能をサポートしており、グラフオブジェクトをグラデーションカラーで塗りつぶすことが必要な場合があります。グラフオブジェクトをグラデーションカラーで塗りつぶすには、gradientAxialShadingオブジェクトを使用してsetPatterColorSpaceを設定する必要があります。

次のコードスニペットは、グラデーションカラーで塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

```csharp
 public static void CreateFilledRectangletGradientFill()
        {
            // Create Document instance
            var doc = new Document();

            // Add page to pages collection of PDF file
            var page = doc.Pages.Add();
            // Create Graph instance
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // Add graph object to paragraphs collection of page instance
            page.Paragraphs.Add(graph);
            // Create Rectangle instance
            var rect = new Rectangle(0, 0, 300, 300);
            // Specify fill color for Graph object
            var gradientColor = new Color();
            var gradientSettings = new GradientAxialShading(Color.Red, Color.Blue)
            {
                Start = new Point(0, 0),
                End = new Point(350, 350)
            };
            gradientColor.PatternColorSpace = gradientSettings;
            rect.GraphInfo.FillColor = gradientColor;

            // Add rectangle object to shapes collection of Graph object
            graph.Shapes.Add(rect);

            // Save PDF file
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![グラデーションの長方形](gradient.png)

## アルファカラーチャネル付きの長方形を作成

Aspose.PDF for .NETは、特定の色で長方形オブジェクトを塗りつぶすことをサポートしています。長方形オブジェクトはアルファカラーチャネルも持つことができ、透明な外観を与えることができます。次のコードスニペットは、アルファカラーチャネルを持つ[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

画像のピクセルは、色の値とともに不透明度に関する情報を保存することができます。これにより、透明または半透明のエリアを持つ画像を作成することができます。

色を透明にする代わりに、各ピクセルはどれだけ不透明であるかの情報を保存します。この不透明度データはアルファチャネルと呼ばれ、通常はピクセルの色チャネルの後に格納されます。

```csharp
     public static void RectangleFilled_AlphaChannel()
        {
            // Documentインスタンスを作成
            var doc = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = doc.Pages.Add();
            // Graphインスタンスを作成
            var graph = new Aspose.Pdf.Drawing.Graph(100, 400);
            // ページインスタンスの段落コレクションにグラフオブジェクトを追加
            page.Paragraphs.Add(graph);
            // Rectangleインスタンスを作成
            var rect = new Rectangle(100, 100, 200, 120);
            // Graphオブジェクトの塗りつぶし色を指定
            rect.GraphInfo.FillColor = Color.FromArgb(128, 244, 180, 0);

            // Graphオブジェクトの形状コレクションに長方形オブジェクトを追加
            graph.Shapes.Add(rect);

            // 2つ目の長方形オブジェクトを作成
            var rect1 = new Rectangle(200, 150, 200, 100);
            rect1.GraphInfo.FillColor = Color.FromArgb(160, 120, 0, 120);
            graph.Shapes.Add(rect1);

            // ページオブジェクトの段落コレクションにグラフインスタンスを追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            doc.Save(_dataDir + "CreateFilledRectangle_out.pdf");
        }
```
![Rectangle Alpha Channel Color](rectangle_color.png)

## 四角形のZオーダーを制御する

Aspose.PDF for .NETは、PDFドキュメントにグラフオブジェクト（例えばグラフ、ライン、四角形など）を追加する機能をサポートしています。PDFファイル内に同じオブジェクトの複数のインスタンスを追加する場合、Zオーダーを指定することによって、それらのレンダリングを制御できます。Zオーダーは、オブジェクトを互いに重ねてレンダリングする必要がある場合にも使用されます。

以下のコードスニペットは、[四角形](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを互いに重ねてレンダリングする手順を示しています。

```csharp
 public static void AddRectangleZOrder()
        {
            // Documentクラスオブジェクトをインスタンス化
            Document doc1 = new Document();
            /// PDFファイルのページコレクションにページを追加
            Page page1 = doc1.Pages.Add();
            // PDFページのサイズを設定
            page1.SetPageSize(375, 300);
            // ページオブジェクトの左マージンを0に設定
            page1.PageInfo.Margin.Left = 0;
            // ページオブジェクトの上マージンを0に設定
            page1.PageInfo.Margin.Top = 0;
            // 赤色、Zオーダー0、特定の寸法で新しい四角形を作成
            AddRectangle(page1, 50, 40, 60, 40, Color.Red, 2);
            // 青色、Zオーダー0、特定の寸法で新しい四角形を作成
            AddRectangle(page1, 20, 20, 30, 30, Color.Blue, 1);
            // 緑色、Zオーダー0、特定の寸法で新しい四角形を作成
            AddRectangle(page1, 40, 40, 60, 30, Color.Green, 0);
            // 結果のPDFファイルを保存
            doc1.Save(_dataDir + "ControlRectangleZOrder_out.pdf");
        }
```
![Z オーダーの制御](control.png)

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

