---
title: PDFファイルへの曲線オブジェクトの追加
linktitle: 曲線の追加
type: docs
weight: 30
url: ja/cpp/add-curve/
description: この記事では、Aspose.PDF for C++を使用してPDFに曲線オブジェクトを作成する方法を説明します。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 曲線オブジェクトの追加

グラフ[曲線](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.curve/)は射影線の連結された集合であり、それぞれの線は通常の二重点で他の三本と交わります。

ベジェ曲線は、コンピュータグラフィックスで滑らかな曲線をモデル化するために広く使用されています。曲線は、その制御点の凸包に完全に含まれており、点はグラフィカルに表示され、曲線を直感的に操作するために使用されることがあります。
曲線全体は、与えられた4つの点（その凸包）の角を持つ四辺形に含まれています。

この記事では、PDFドキュメントで作成できる単純なグラフ曲線と塗りつぶし曲線を調査します。

以下の手順に従ってください：

1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) インスタンスを作成する

1. 特定の寸法で[Drawing object](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.drawing)を作成する

1. Drawing オブジェクトに[Border](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph#ab63dde9501441515b915fd68f66a01bd)を設定する

1. ページの段落コレクションに[Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph)オブジェクトを追加する

1. PDF ファイルを保存する

```cpp
void ExampleCurve() {

    // Create Document instance
    String _dataDir("C:\\Samples\\");
    // Create Document instance
    auto document = MakeObject<Document>();

    // Add page to pages collection of PDF file
    auto page = document->get_Pages()->Add();

    // Create Drawing object with certain dimensions
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Set border for Drawing object
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double> ({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // Add Graph object to paragraphs collection of page
    page->get_Paragraphs()->Add(graph);

    // Save PDF file
    document->Save(_dataDir + u"DrawingCurve1_out.pdf");
}
```
以下の画像は、私たちのコードスニペットで実行された結果を示しています。

![Drawing Curve](drawing_curve.png)

## 塗りつぶされた曲線オブジェクトを作成する

この例は、色で塗りつぶされたCurveオブジェクトを追加する方法を示しています。

```cpp
void ExampleFilledCurve() {

    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 200);
    
    // Drawingオブジェクトに境界線を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto curve1 = MakeObject<Aspose::Pdf::Drawing::Curve>(MakeArray<double>({ 10, 10, 50, 60, 70, 10, 100, 120}));
    curve1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(curve1);

    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingCurve2_out.pdf");
}
```

```
Look at the result of adding a filled Curve:

![Filled Curve](filled_curve.png)
```

見ると、塗りつぶされたカーブを追加した結果が表示されます。