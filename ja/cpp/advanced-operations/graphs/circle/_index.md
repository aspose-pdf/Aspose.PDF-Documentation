---
title: PDFファイルに円オブジェクトを追加
linktitle: 円を追加
type: docs
weight: 20
url: /ja/cpp/add-circle/
description: この記事では、Aspose.PDF for C++を使用してPDFに円オブジェクトを作成する方法を説明します。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 円オブジェクトを追加

棒グラフのように、円グラフは複数の異なるカテゴリのデータを表示するために使用できます。しかし、棒グラフとは異なり、円グラフは全体を構成するすべてのカテゴリのデータがある場合にのみ使用できます。それでは、Aspose.PDF for C++を使用して[Circle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.circle/)オブジェクトを追加する方法を見てみましょう。

以下の手順に従います：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)インスタンスを作成

1. 特定の寸法を持つ[Drawingオブジェクト](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)を作成

1. Set [Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd) for Drawing object

1. ページの段落コレクションに[Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph)オブジェクトを追加

1. PDFファイルを保存

```cpp
void ExampleCircle() {

    // ドキュメントインスタンスの作成
    String _dataDir("C:\\Samples\\");
    // ドキュメントインスタンスの作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法で描画オブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    // 描画オブジェクトの枠線を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);

    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(circle);

    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingCircle1_out.pdf");
}
```
私たちの描いた円は次のようになります：

![円を描く](drawing_circle.png)

## 塗りつぶされた円オブジェクトを作成

この例は、色で塗りつぶされた円オブジェクトを追加する方法を示しています。

```cpp
void ExampleFilledCircle() {
    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Drawingオブジェクトに境界を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto circle = MakeObject<Aspose::Pdf::Drawing::Circle>(100, 100, 40);
    circle->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    circle->get_GraphInfo()->set_FillColor(Color::get_Green());

    circle->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Circle"));

    graph->get_Shapes()->Add(circle);

    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingCircle2_out.pdf");
}
```

```
Let's see the result of adding a filled Circle:

![塗りつぶされた円](filled_circle.png)
```