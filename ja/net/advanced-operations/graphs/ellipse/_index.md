---
title: PDFファイルに楕円オブジェクトを追加
linktitle: 楕円を追加
type: docs
weight: 60
url: ja/net/add-ellipse/
description: この記事では、Aspose.PDF for .NETを使用してPDFに楕円オブジェクトを作成する方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDFファイルに楕円オブジェクトを追加",
    "alternativeHeadline": "PDFファイルに楕円オブジェクトを作成する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "pdf, c#, pdf内の楕円",
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
    "url": "/net/add-ellipse/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-ellipse/"
    },
    "dateModified": "2022-02-04",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFに楕円オブジェクトを作成する方法について説明します。"
}
</script>
以下のコードスニペットも [Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリで動作します。

## 楕円オブジェクトを追加

Aspose.PDF for .NET はPDFドキュメントに [楕円](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse) オブジェクトを追加することをサポートしています。また、楕円オブジェクトを特定の色で塗りつぶす機能も提供しています。

```csharp
 public static void Ellipse()
        {
            // Documentインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();

            // 特定の寸法でDrawingオブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Drawingオブジェクトに境界線を設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(150, 100, 120, 60);
            ellipse1.GraphInfo.Color = Color.GreenYellow;
            ellipse1.Text = new TextFragment("Ellipse");
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(50, 50, 18, 300);
            ellipse2.GraphInfo.Color = Color.DarkRed;

            graph.Shapes.Add(ellipse2);

            // Graphオブジェクトをページの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingEllipse_out.pdf");

        }
```
![Add Ellipse](ellipse.png)

## 塗りつぶした楕円オブジェクトの作成

次のコードスニペットは、色で塗りつぶされた[Ellipse](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/ellipse)オブジェクトを追加する方法を示しています。

```csharp
     public static void EllipseFilled()
        {
            // Documentインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();

            // 特定の寸法でDrawingオブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

            // Drawingオブジェクトに境界を設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            graph.Shapes.Add(ellipse1);

            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            graph.Shapes.Add(ellipse2);

            // Graphオブジェクトをページの段落コレクションに追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingEllipse_out.pdf");
        }
```
![Filled Ellipse](fill_ellipse.png)

## 楕円内にテキストを追加

Aspose.PDF for .NETは、グラフオブジェクト内にテキストを追加するサポートを提供します。グラフオブジェクトのTextプロパティは、グラフオブジェクトのテキストを設定するオプションを提供します。次のコードスニペットは、Rectangleオブジェクト内にテキストを追加する方法を示しています。

```csharp
        public static void EllipseWithText()
        {
            // ドキュメントインスタンスを作成
            var document = new Document();

            // PDFファイルのページコレクションにページを追加
            var page = document.Pages.Add();

            // 特定の寸法で描画オブジェクトを作成
            var graph = new Aspose.Pdf.Drawing.Graph(400, 400);
            // 描画オブジェクトのボーダーを設定
            var borderInfo = new BorderInfo(BorderSide.All, Color.Green);
            graph.Border = borderInfo;

            var textFragment = new TextFragment("Ellipse");
            textFragment.TextState.Font = FontRepository.FindFont("Helvetica");
            textFragment.TextState.FontSize = 24;

            var ellipse1 = new Ellipse(100, 100, 120, 180);
            ellipse1.GraphInfo.FillColor = Color.GreenYellow;
            ellipse1.Text = textFragment;
            graph.Shapes.Add(ellipse1);


            var ellipse2 = new Ellipse(200, 150, 180, 120);
            ellipse2.GraphInfo.FillColor = Color.DarkRed;
            ellipse2.Text = textFragment;
            graph.Shapes.Add(ellipse2);

            // ページの段落コレクションにグラフオブジェクトを追加
            page.Paragraphs.Add(graph);

            // PDFファイルを保存
            document.Save(_dataDir + "DrawingEllipseText_out.pdf");

        }
 ```
![Text inside Ellipse](text_ellipse.png)

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
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>

