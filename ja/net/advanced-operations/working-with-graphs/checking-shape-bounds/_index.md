---
title: シェイプコレクションの形状境界をチェックする
type: docs
weight: 70
url: /ja/net/aspose-pdf-drawing-graph-shapes-bounds-check/
description: シェイプがシェイプコレクションに挿入されたときの境界をチェックして、親コンテナ内に収まることを確認する方法を学びます。
lastmod: "2025-02-28"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Checking Element Bounds in Shapes Collection",
    "alternativeHeadline": "Configurable Bounds Checking for Aspose.PDF Shapes with Exception Mode",
    "abstract": "Aspose.PDF for .NETの新しい境界チェック機能は、`Drawing.Graph.Shapes`コレクション内の要素の寸法を親コンテナに対して自動的に検証し、レイアウトのオーバーフローを防ぎます。要素がコンテナの制限を超えると例外が発生し、挿入時に厳密なサイズ制約を強制して、正確なPDFフォーマットを確保し、デザインの精度を向上させます。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1000",
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
    "url": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/aspose-pdf-drawing-graph-shapes-bounds-check/"
    },
    "dateModified": "2025-02-28",
    "description": ""
}
</script>

## はじめに
このドキュメントは、シェイプコレクションにおける境界チェック機能の使用に関する詳細なガイドを提供します。この機能は、要素が親コンテナ内に収まることを保証し、コンポーネントが収まらない場合に例外をスローするように構成できます。この機能を実装する手順を説明し、完全な例を提供します。

## 前提条件
以下が必要です：
* Visual Studio 2019以降
* Aspose.PDF for .NET 25.3以降
* ページを含むサンプルPDFファイル

Aspose.PDF for .NETライブラリは公式ウェブサイトからダウンロードするか、Visual StudioのNuGetパッケージマネージャーを使用してインストールできます。

## 手順
タスクを完了するための手順は以下の通りです：
1. 新しいドキュメントを作成し、ページを追加します。
2. 指定された寸法で`Graph`オブジェクトを作成します。
3. 指定された寸法で`Shape`オブジェクトを作成します。
4. `BoundsCheckMode`を`ThrowExceptionIfDoesNotFit`に設定します。
5. シェイプをグラフに追加しようとします。

これらの手順をC#コードで実装する方法を見てみましょう。

### ステップ1: 新しいドキュメントを作成し、ページを追加する
まず、新しいPDFドキュメントを作成し、それにページを追加します。

```csharp
using (var doc = new Aspose.Pdf.Document())
{
    Aspose.Pdf.Page page = doc.Pages.Add();
}
```

### ステップ2: 指定された寸法でグラフオブジェクトを作成する
次に、幅と高さが100ユニットの`Graph`オブジェクトを作成します。グラフをページの上から10ユニット、左から15ユニットの位置に配置します。グラフに黒い境界を追加します。

```csharp
var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
{
    Top = 10,
    Left = 15,
    Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
};
page.Paragraphs.Add(graph);
```

### ステップ3: 指定された寸法でAspose.Pdf.Drawing.Shapeオブジェクト（例えば、Aspose.Pdf.Drawing.Rectangle）を作成する
幅と高さが50ユニットの長方形オブジェクトを作成します。長方形を(-1, 0)に配置します。これはグラフの境界の外側です。

```csharp
Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
{
    GraphInfo =
    {
        FillColor = Aspose.Pdf.Color.Tomato
    }
};
```

### ステップ4: BoundsCheckModeをThrowExceptionIfDoesNotFitに設定する
長方形がグラフ内に収まらない場合に例外がスローされるように、`BoundsCheckMode`を`ThrowExceptionIfDoesNotFit`に設定します。

```csharp
graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
```

### ステップ5: 長方形をグラフに追加しようとする
長方形をグラフに追加しようとします。これは、長方形がグラフの寸法内に収まらないため、`Aspose.Pdf.BoundsOutOfRangeException`をスローします。

```csharp
graph.Shapes.Add(rect);
```

## 出力
コードを実行した後、期待される出力は、次のメッセージを持つ`Aspose.Pdf.BoundsOutOfRangeException`になります：

```
Bounds not fit. Container dimensions: 100x100
```

## トラブルシューティング
問題が発生した場合、以下のいくつかのヒントがあります：
* `BoundsCheckMode`が正しく設定されていることを確認してください。
* 要素とコンテナの寸法が正確であることを確認してください。
* コンテナ内の要素の位置を確認してください。

## 完全な例
以下は、すべての手順を組み合わせた完全な例です：

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using (var doc = new Aspose.Pdf.Document())
    {
        Aspose.Pdf.Page page = doc.Pages.Add();
        
        // Create a Graph Object with Specified Dimensions
        var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
        {
            Top = 10,
            Left = 15,
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
        };
        page.Paragraphs.Add(graph);
        
        // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
        Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
        {
            GraphInfo =
            {
                FillColor = Aspose.Pdf.Color.Tomato
            }
        };
        
        // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
        graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);
        
        // Attempt to add the rectangle to the graph
        graph.Shapes.Add(rect);
    }
}```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckShapeBounds()
{
    // Create a new document and add a page
    using var doc = new Aspose.Pdf.Document();
    Aspose.Pdf.Page page = doc.Pages.Add();

    // Create a Graph Object with Specified Dimensions
    var graph = new Aspose.Pdf.Drawing.Graph(100d, 100d)
    {
        Top = 10,
        Left = 15,
        Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1F, Aspose.Pdf.Color.Black)
    };
    page.Paragraphs.Add(graph);

    // Create a Aspose.Pdf.Drawing.Shape object (for example, Aspose.Pdf.Drawing.Rectangle) with specified dimensions
    Aspose.Pdf.Drawing.Rectangle rect = new Aspose.Pdf.Drawing.Rectangle(-1, 0, 50, 50)
    {
        GraphInfo =
        {
            FillColor = Aspose.Pdf.Color.Tomato
        }
    };

    // Set the BoundsCheckMode to ThrowExceptionIfDoesNotFit
    graph.Shapes.UpdateBoundsCheckMode(Aspose.Pdf.BoundsCheckMode.ThrowExceptionIfDoesNotFit);

    // Attempt to add the rectangle to the graph
    graph.Shapes.Add(rect);
}
```
{{< /tab >}}
{{< /tabs >}}

## 結論
シェイプコレクションの境界チェック機能は、要素が親コンテナ内に収まることを保証するための強力なツールです。`BoundsCheckMode`を`ThrowExceptionIfDoesNotFit`に設定することで、PDFドキュメント内のレイアウトの問題を防ぐことができます。この機能は、要素の正確な配置とサイズが重要なシナリオで特に便利です。詳細については、[公式ドキュメント](https://docs.aspose.com/pdf/net/)を訪れてください。