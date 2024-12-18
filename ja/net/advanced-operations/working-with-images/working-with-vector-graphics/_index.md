---
title: ベクターグラフィックスの操作
linktitle: ベクターグラフィックスの操作
type: docs
weight: 120
url: /ja/net/working-with-vector-graphics/
description: この記事では、C#を使用してGraphicsAbsorberツールを使用する機能について説明します。
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "GraphicsAbsorberの操作",
    "alternativeHeadline": "PDFファイル内の画像の位置を取得する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDFドキュメント生成",
    "keywords": "PDF, C#, PDF内のGraphicsAbsorber",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "このセクションでは、C#ライブラリを使用してPDFファイルでGraphicsAbsorberを操作する機能について説明します。"
}
</script>
この章では、PDFドキュメント内のベクターグラフィックスと対話するために強力な`GraphicsAbsorber`クラスの使用方法について探求します。グラフィックを移動、削除、または追加する必要がある場合、このガイドはこれらのタスクを効果的に実行する方法を示します。さあ、始めましょう！

## はじめに<a name="introduction"></a>

ベクターグラフィックスは、多くのPDFドキュメントで重要なコンポーネントであり、画像、形状、その他のグラフィカル要素を表現するために使用されます。Aspose.PDFは`GraphicsAbsorber`クラスを提供しており、開発者がこれらのグラフィックスにプログラムでアクセスして操作できるようにします。`GraphicsAbsorber`の`Visit`メソッドを使用することで、指定されたページからベクターグラフィックスを抽出し、移動、削除、または他のページへのコピーなどのさまざまな操作を実行できます。

## 1. `GraphicsAbsorber`を使ったグラフィックの抽出<a name="extracting-graphics"></a>

ベクターグラフィックスを扱う最初のステップは、PDFドキュメントからそれらを抽出することです。ここでは`GraphicsAbsorber`クラスを使用してこれを行う方法を紹介します：

```csharp
public static void UsingGraphicsAbsorber()
{
    // ステップ 1: Documentオブジェクトを作成します。
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // ステップ 2: GraphicsAbsorberのインスタンスを作成します。
    var graphicsAbsorber = new GraphicsAbsorber();

    // ドキュメントの最初のページを選択します。
    var page = document.Pages[1];

    // ステップ 3: `Visit`メソッドを使用してページからグラフィックを抽出します。
    graphicsAbsorber.Visit(page);

    // 抽出された要素に関する情報を表示します。
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"ページ番号: {element.SourcePage.Number}");
        Console.WriteLine($"位置: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"オペレーターの数: {element.Operators.Count}");
    }
}
```
### 説明:

1. **ドキュメントオブジェクトを作成する**: 新しい`Document`オブジェクトがターゲットPDFファイルへのパスでインスタンス化されます。
2. **`GraphicsAbsorber`のインスタンスを作成する**: このクラスは指定されたページからすべてのグラフィック要素をキャプチャします。
3. **訪問方法**: `GraphicsAbsorber`がベクターグラフィックスを吸収することを可能にするために、最初のページで`Visit`メソッドが呼び出されます。
4. **抽出された要素を通して反復する**: コードは各抽出された要素をループし、ページ番号、位置、および関与する描画オペレータの数などの情報を印刷します。

## 2. グラフィックスの移動<a name="moving-graphics"></a>

グラフィックを抽出したら、同じページの異なる位置に移動できます。これを実現する方法は次のとおりです：

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // パフォーマンスを向上させるために一時的に更新を停止します。
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // XおよびY座標をシフトしてグラフィックを移動します。
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // 更新を再開して変更を適用します。
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### 主要なポイント:

- **SuppressUpdate**: このメソッドは、複数の変更を行う場合にパフォーマンスを向上させるために一時的に更新を停止します。
- **ResumeUpdate**: このメソッドは更新を再開し、グラフィックの位置に対して行われた変更を適用します。
- **要素の位置決め**: 各グラフィックの位置は、その `X` と `Y` 座標を変更することによって調整されます。

## 3. グラフィックの削除<a name="removing-graphics"></a>

特定のグラフィックをページから削除したい場合があります。Aspose.PDFはこれを実現するための2つの方法を提供しています:

### 方法 1: 矩形の境界を使用する

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // グラフィックの位置が矩形内にあるかどうかを確認します。
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // グラフィック要素を削除します。
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### 方法2：削除された要素のコレクションを使用する

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### 説明:

- **矩形の境界**: 削除するグラフィックスを指定する矩形エリアを定義する。
- **更新の抑制と再開**: 中間レンダリングなしで効率的な削除を保証する。

## 4. 別のページへのグラフィックスの追加<a name="adding-graphics"></a>

一つのページから吸収したグラフィックスは、同じドキュメント内の別のページに追加することができる。
1ページから取得したグラフィックを同じドキュメントの別のページに追加することができます。

### メソッド1：グラフィックを個別に追加

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // 各グラフィック要素を2ページ目に追加します。
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### メソッド2：グラフィックをコレクションとして追加

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // 一度にすべてのグラフィックを追加します。
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### 主要ポイント:

- **SuppressUpdate と ResumeUpdate**: これらのメソッドは、一括変更を行う際にパフォーマンスを維持するのに役立ちます。
- **AddOnPage と AddGraphics**: `AddOnPage` は個別の追加に使用し、`AddGraphics` は一括追加に使用します。

## 結論

この章では、Aspose.PDF を使用して PDF ドキュメント内のベクターグラフィックスを抽出、移動、削除、追加する方法を探りました。これらの技術をマスターすることで、PDF の視覚的プレゼンテーションを大幅に向上させ、ダイナミックで視覚的に魅力的なドキュメントを作成することができます。

コード例を実験して、特定のユースケースに合わせて適応させてください。ハッピーコーディング!

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


