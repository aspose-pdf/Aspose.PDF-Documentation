---
title: PDFファイルに矩形オブジェクトを追加
linktitle: 矩形を追加
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ja/net/add-rectangle/
description: この記事では、Aspose.PDF for .NETを使用してPDFに矩形オブジェクトを作成する方法を説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Rectangle Object to PDF file",
    "alternativeHeadline": "Add Rectangle to PDF file",
    "abstract": "Aspose.PDF for .NETの新機能により、ユーザーはPDF文書に矩形オブジェクトをシームレスに追加できます。この機能には、矩形を単色、グラデーション塗り、透明度でカスタマイズするオプションが含まれており、PDFコンテンツの視覚的カスタマイズとレイヤー制御を強化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Add Rectangle, PDF document generation, Aspose.PDF for .NET, Rectangle object, fill rectangle, gradient color fill, Z-Order control, alpha channel color, graph objects in PDF, create filled rectangle",
    "wordcount": "1263",
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
    "url": "/net/add-rectangle/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-rectangle/"
    },
    "dateModified": "2024-11-25",
    "description": "この記事では、Aspose.PDF for .NETを使用してPDFに矩形オブジェクトを作成する方法を説明します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも機能します。

## 矩形オブジェクトを追加

Aspose.PDF for .NETは、PDF文書にグラフオブジェクト（例えば、グラフ、線、矩形など）を追加する機能をサポートしています。また、特定の色で矩形オブジェクトを塗りつぶし、Z-オーダーを制御し、グラデーションカラー塗りを追加する機能も提供しています。

まず、矩形オブジェクトを作成する可能性を見てみましょう。

以下の手順に従ってください：

1. 新しいPDF [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)を作成します。
1. PDFファイルのページコレクションに[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)を追加します。
1. ページインスタンスの段落コレクションに[Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment)を追加します。
1. [Graph](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/graph)インスタンスを作成します。
1. [Drawing object](https://reference.aspose.com/pdf/net/aspose.pdf.drawing)の境界を設定します。
1. 矩形インスタンスを作成します。

1. [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトをGraphオブジェクトの形状コレクションに追加します。
1. グラフオブジェクトをページインスタンスの段落コレクションに追加します。
1. ページインスタンスの段落コレクションに[Text fragment](https://reference.aspose.com/pdf/net/aspose.pdf/texfragment)を追加します。

1. そして、PDFファイルを保存します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangle(Aspose.Pdf.Page page, float x, float y, float width, float height, Aspose.Pdf.Color color, int zIndex)
{
    // Create a Graph object with dimensions matching the specified rectangle
    var graph = new Aspose.Pdf.Drawing.Graph(width, height)
    {
        // Prevent the graph from repositioning automatically
        IsChangePosition = false,
        // Set the Left coordinate position for the Graph instance
        Left = x,
        // Set the Top coordinate position for the Graph instance
        Top = y
    };

    // Create a Rectangle object inside the Graph
    var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, width, height)
    {
        // Set the fill color of the rectangle
        GraphInfo =
        {
            FillColor = color,
            // Set the border color of the rectangle
            Color = color
        }
    };

    // Add the rectangle to the Shapes collection of the Graph
    graph.Shapes.Add(rect);

    // Set the Z-Index for the Graph object to control layering
    graph.ZIndex = zIndex;

    // Add the Graph object to the Paragraphs collection of the page
    page.Paragraphs.Add(graph);
}
```

![矩形を作成](create_rectangle.png)

## 塗りつぶされた矩形オブジェクトを作成

Aspose.PDF for .NETは、特定の色で矩形オブジェクトを塗りつぶす機能も提供しています。

以下のコードスニペットは、色で塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance with specified dimensions
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            // Specify fill color for the Rectangle object
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.Red 
            }
        };

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

塗りつぶされた単色の矩形の結果を見てください：

![塗りつぶされた矩形](fill_rectangle.png)

## グラデーション塗りで描画を追加

Aspose.PDF for .NETは、PDF文書にグラフオブジェクトを追加する機能をサポートしており、時にはグラフオブジェクトをグラデーションカラーで塗りつぶす必要があります。グラフオブジェクトをグラデーションカラーで塗りつぶすには、以下のようにsetPatterColorSpaceをgradientAxialShadingオブジェクトに設定する必要があります。

以下のコードスニペットは、グラデーションカラーで塗りつぶされた[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateFilledRectangleGradientFill()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(400, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create Rectangle instance
        var rect = new Aspose.Pdf.Drawing.Rectangle(0, 0, 300, 300);

        // Create a gradient fill color
        var gradientColor = new Aspose.Pdf.Color();
        var gradientSettings = new Aspose.Pdf.Drawing.GradientAxialShading(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.Blue)
        {
            Start = new Aspose.Pdf.Point(0, 0),
            End = new Aspose.Pdf.Point(350, 350)
        };
        gradientColor.PatternColorSpace = gradientSettings;

        // Apply gradient fill color to the rectangle
        rect.GraphInfo.FillColor = gradientColor;

        // Add rectangle object to shapes collection of Graph object
        graph.Shapes.Add(rect);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangleGradient_out.pdf");
    }
}
```

![グラデーション矩形](gradient.png)

## アルファカラー チャンネルを持つ矩形を作成

Aspose.PDF for .NETは、特定の色で矩形オブジェクトを塗りつぶす機能をサポートしています。矩形オブジェクトは、透明な外観を与えるためにアルファカラー チャンネルを持つこともできます。以下のコードスニペットは、アルファカラー チャンネルを持つ[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを追加する方法を示しています。

画像のピクセルは、色の値とともに不透明度に関する情報を保存できます。これにより、透明または半透明の領域を持つ画像を作成できます。

色を透明にする代わりに、各ピクセルはどれだけ不透明であるかに関する情報を保存します。この不透明度データはアルファチャネルと呼ばれ、通常はピクセルのカラー チャンネルの後に保存されます。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RectangleFilled_AlphaChannel()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create Graph instance
        var graph = new Aspose.Pdf.Drawing.Graph(100, 400);

        // Add graph object to paragraphs collection of page instance
        page.Paragraphs.Add(graph);

        // Create first rectangle with alpha channel fill color
        var rect = new Aspose.Pdf.Drawing.Rectangle(100, 100, 200, 120)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(128, 244, 180, 0) 
            }
        };

        // Add the first rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect);

        // Create second rectangle with different alpha channel fill color
        var rect1 = new Aspose.Pdf.Drawing.Rectangle(200, 150, 200, 100)
        {
            GraphInfo = 
            { 
                FillColor = Aspose.Pdf.Color.FromArgb(160, 120, 0, 120) 
            }
        };

        // Add the second rectangle to the shapes collection of the Graph object
        graph.Shapes.Add(rect1);

        // Save PDF document
        document.Save(dataDir + "CreateFilledRectangle_out.pdf");
    }
}
```

![矩形アルファチャネルカラー](rectangle_color.png)

## 矩形のZ-オーダーを制御

Aspose.PDF for .NETは、PDF文書にグラフオブジェクト（例えば、グラフ、線、矩形など）を追加する機能をサポートしています。同じオブジェクトのインスタンスをPDFファイル内に複数追加する場合、Z-オーダーを指定することで描画を制御できます。Z-オーダーは、オブジェクトを重ねて描画する必要がある場合にも使用されます。

以下のコードスニペットは、[Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.drawing/rectangle)オブジェクトを重ねて描画する手順を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRectangleZOrder()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Set size of PDF page
        page.SetPageSize(375, 300);

        // Set left and top margins for the page object as 0
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Top = 0;

        // Create rectangles with different colors and Z-Order values
        AddRectangle(page, 50, 40, 60, 40, Aspose.Pdf.Color.Red, 2);
        AddRectangle(page, 20, 20, 30, 30, Aspose.Pdf.Color.Blue, 1);
        AddRectangle(page, 40, 40, 60, 30, Aspose.Pdf.Color.Green, 0);

        // Save PDF document
        document.Save(dataDir + "ControlRectangleZOrder_out.pdf");
    }
}
```

![Zオーダーの制御](control.png)

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