---
title: PDFファイルにアークオブジェクトを追加する
linktitle: アークを追加
type: docs
weight: 10
url: /ja/cpp/add-arc/
description: 本記事では、Aspose.PDF for C++を使用してPDFにアークオブジェクトを作成する方法を説明します。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## アークオブジェクトを追加する

Aspose.PDF for C++は、グラフオブジェクト（例えばグラフ、線、長方形など）をPDFドキュメントに追加する機能をサポートしています。また、特定の色で[アーク](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc)オブジェクトを塗りつぶす機能も提供しています。

以下の手順に従います：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)インスタンスを作成します

1. 特定の寸法で[Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)を作成します

1. Drawingオブジェクトに[Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd)を設定します

1. [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) オブジェクトをページの段落コレクションに追加する

1. PDFファイルを保存する

以下のコードスニペットは、[Arc](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.arc/) オブジェクトの追加方法を示しています。

```cpp
void ExampleArc() {
    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // ページをPDFファイルのページコレクションに追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawingオブジェクトに境界線を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc1 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc1);

    auto arc2 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 90, 70, 180);
    arc2->get_GraphInfo()->set_Color(Color::get_DarkBlue());
    graph->get_Shapes()->Add(arc2);

    auto arc3 = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 85, 120, 210);
    arc3->get_GraphInfo()->set_Color(Color::get_Red());
    graph->get_Shapes()->Add(arc3);

    // Graphオブジェクトをページの段落コレクションに追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```
## 塗りつぶされた弧オブジェクトを作成する

次の例は、特定の寸法で色で塗りつぶされた弧オブジェクトを追加する方法を示しています。

```cpp
void ExampleFilledArc() {

    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawingオブジェクトに境界線を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto arc = MakeObject<Aspose::Pdf::Drawing::Arc>(100, 100, 95, 0, 90);
    arc->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(arc);

    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<double>({ 195, 100, 100, 100, 100, 195 }));
    line->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(line);

    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingArc_out.pdf");

}
```

```
Let's see the result of adding a filled Arс:

![Filled Arc](filled_arc.png)
```

追加された塗りつぶしアークの結果を見てみましょう。