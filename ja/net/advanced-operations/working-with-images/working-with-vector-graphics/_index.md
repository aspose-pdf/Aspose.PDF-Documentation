---
title: ベクターグラフィックスの操作
linktitle: ベクターグラフィックスの操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /ja/net/working-with-vector-graphics/
description: この文書では、C#を使用したGraphicsAbsorberツールの操作機能について説明します。
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics in PDF",
    "alternativeHeadline": "Programmatically manipulate PDF vector graphics",
    "abstract": "新しいGraphicsAbsorberクラスを使用して、PDF文書内のベクターグラフィックスをプログラムで操作します。Aspose.PDF for .NET C#ライブラリは、グラフィック要素を正確に制御できるようにし、グラフィックスを移動、削除、追加するなどのアクションを可能にします。このツールは、最適なパフォーマンスのために個別および一括操作メソッドを提供します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "GraphicsAbsorber, Vector Graphics, PDF Manipulation, C# library, Aspose.PDF, Move Graphics, Remove Graphics, Add Graphics, PDF Vector Graphics",
    "wordcount": "967",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "このセクションでは、C#ライブラリを使用したGraphicsAbsorber PDFファイルの操作機能について説明します。"
}
</script>

この章では、PDF文書内のベクターグラフィックスと対話するために強力な`GraphicsAbsorber`クラスを使用する方法を探ります。グラフィックスを移動、削除、または追加する必要がある場合でも、このガイドではこれらのタスクを効果的に実行する方法を示します。それでは始めましょう！

## はじめに<a name="introduction"></a>

ベクターグラフィックスは、多くのPDF文書の重要な要素であり、画像、形状、その他のグラフィカル要素を表現するために使用されます。Aspose.PDFは、開発者がこれらのグラフィックスにプログラムでアクセスし操作できる`GraphicsAbsorber`クラスを提供します。`GraphicsAbsorber`の`Visit`メソッドを使用することで、指定されたページからベクターグラフィックスを抽出し、移動、削除、または他のページにコピーするなどのさまざまな操作を実行できます。

## 1. `GraphicsAbsorber`を使用したグラフィックスの抽出<a name="extracting-graphics"></a>

ベクターグラフィックスを操作する最初のステップは、PDF文書からそれらを抽出することです。以下は、`GraphicsAbsorber`クラスを使用してこれを行う方法です：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Document-01.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}

```

### 説明：

1. **ドキュメントオブジェクトの作成**: 対象のPDFファイルへのパスを指定して新しい`Document`オブジェクトをインスタンス化します。
2. **`GraphicsAbsorber`のインスタンスを作成**: このクラスは、指定されたページからすべてのグラフィック要素をキャプチャします。
3. **Visitメソッド**: 最初のページで`Visit`メソッドを呼び出し、`GraphicsAbsorber`がベクターグラフィックスを吸収できるようにします。
4. **抽出された要素を反復処理**: コードは、抽出された各要素をループし、ページ番号、位置、関与する描画オペレーターの数などの情報を印刷します。

## 2. グラフィックスの移動<a name="moving-graphics"></a>

グラフィックスを抽出したら、同じページの別の位置に移動できます。以下は、これを達成する方法です：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "MoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Move graphics by shifting their X and Y coordinates
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "MoveGraphics_out.pdf");
        }
    }
}
```

### 重要なポイント：

- **SuppressUpdate**: このメソッドは、複数の変更を行う際にパフォーマンスを向上させるために更新を一時的に停止します。
- **ResumeUpdate**: このメソッドは、更新を再開し、グラフィックスの位置に対する変更を適用します。
- **要素の位置決め**: 各グラフィックの位置は、その`X`および`Y`座標を変更することで調整されます。

## 3. グラフィックスの削除<a name="removing-graphics"></a>

特定のグラフィックスをページから削除したい場合があります。Aspose.PDFは、これを達成するための2つのメソッドを提供します：

### メソッド1: 矩形境界を使用

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suppress updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove those inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                if (rectangle.Contains(element.Position))
                {
                    element.Remove(); // Remove the graphic element
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### メソッド2: 削除された要素のコレクションを使用

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle within which graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection to store the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Iterate through the extracted elements and add those inside the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the graphics elements from the page
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "RemoveGraphics_out.pdf");
        }
    }
}
```

### 説明：

- **矩形境界**: どのグラフィックスを削除するかを指定するために矩形領域を定義します。
- **更新の抑制と再開**: 中間レンダリングなしで効率的に削除を行うことを確認します。

## 4. 別のページにグラフィックスを追加<a name="adding-graphics"></a>

1ページから吸収されたグラフィックスは、同じ文書内の別のページに追加できます。これを達成するための2つの方法は次のとおりです：

### メソッド1: グラフィックスを個別に追加

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### メソッド2: グラフィックスをコレクションとして追加

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the documents directory directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddToAnotherPage.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the pages from the document
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphics from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics elements to the second page at once
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();

            // Save PDF document
            document.Save(dataDir + "AddToAnotherPage_out.pdf");
        }
    }
}
```

### 重要なポイント：

- **SuppressUpdateおよびResumeUpdate**: これらのメソッドは、一括変更を行う際のパフォーマンスを維持するのに役立ちます。
- **AddOnPageとAddGraphics**: 個別の追加には`AddOnPage`を使用し、一括追加には`AddGraphics`を使用します。

## 結論

この章では、Aspose.PDFを使用してPDF文書内のベクターグラフィックスを抽出、移動、削除、追加するために`GraphicsAbsorber`クラスを使用する方法を探りました。これらの技術を習得することで、PDFの視覚的プレゼンテーションを大幅に向上させ、動的で視覚的に魅力的な文書を作成できます。

コード例を試してみて、特定の使用ケースに合わせて適応させてください。コーディングを楽しんでください！

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