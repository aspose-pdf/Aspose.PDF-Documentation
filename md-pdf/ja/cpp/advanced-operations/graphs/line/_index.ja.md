---
title: PDFファイルにラインオブジェクトを追加する
linktitle: ラインを追加
type: docs
weight: 40
url: /cpp/add-line/
description: この記事では、Aspose.PDF for C++を使用してPDFにラインオブジェクトを作成する方法を説明します。
lastmod: "2021-12-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## ラインオブジェクトを追加する

Aspose.PDF for C++は、PDFドキュメントにグラフオブジェクト（例えばグラフ、ライン、長方形など）を追加する機能をサポートしています。また、[Line](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.line/)オブジェクトを追加し、ダッシュパターン、色、および他のフォーマット設定を指定することもできます。

以下の手順に従ってください：

1. 新しいPDF [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) を作成します

1. PDFファイルのページコレクションに[Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/)を追加します

1. [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph/)インスタンスを作成します。

1. ページインスタンスの段落コレクションにグラフオブジェクトを追加します。

1. [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) インスタンスを作成します。

1. 線の幅を設定します。

1. [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) オブジェクトを Graph オブジェクトのシェイプコレクションに追加します。

1. PDF ファイルを保存します。

次のコードスニペットは、色で塗りつぶされた [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.rectangle/) オブジェクトを追加する方法を示しています。

```cpp

void AddLineObjectToPDF()
{

String _dataDir("C:\\Samples\\");

// Document インスタンスを作成します

auto document = MakeObject<Document>();


// PDF ファイルのページコレクションにページを追加します

auto page = document->get_Pages()->Add();


// Graph インスタンスを作成します

auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);


// ページインスタンスの段落コレクションにグラフオブジェクトを追加します

page->get_Paragraphs()->Add(graph);


// Rectangle インスタンスを作成します

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(new float[] { 100, 100, 200, 100 });



// Graph オブジェクトの塗りつぶし色を指定します

line->get_GraphInfo()->set_DashArray (MakeArray<int>({ 0, 1, 0 }));

line->get_GraphInfo()->set_DashPhase (1);



// Graph オブジェクトのシェイプコレクションに長方形オブジェクトを追加します

graph->get_Shapes()->Add(line);



// PDF ファイルを保存します

document->Save(_dataDir + u"AddLineObject_out.pdf");
}

```
![Add Line](add_line.png)

## PDFドキュメントに点線を追加する方法

```cpp
void DashLengthInBlackAndDashLengthInWhite()
{

String _dataDir("C:\\Samples\\");

// Documentインスタンスを作成

auto document = MakeObject<Document>();


// PDFファイルのページコレクションにページを追加

auto page = document->get_Pages()->Add();


// 特定の寸法でDrawingオブジェクトを作成

auto canvas = MakeObject<Aspose::Pdf::Drawing::Graph>(100, 400);

// ページインスタンスの段落コレクションに描画オブジェクトを追加

page->get_Paragraphs()->Add(canvas);



// Lineオブジェクトを作成

auto line = MakeObject<Aspose::Pdf::Drawing::Line>(MakeArray<float>({ 100, 100, 200, 100 }));

// Lineオブジェクトの色を設定

line->get_GraphInfo()->set_Color (Aspose::Pdf::Color::get_Red());

// lineオブジェクトのダッシュ配列を指定

line->get_GraphInfo()->set_DashArray(MakeArray<int>({ 0, 1, 0 }));

// Lineインスタンスのダッシュフェーズを設定

line->get_GraphInfo()->set_DashPhase(1);

// 描画オブジェクトのシェイプコレクションにラインを追加

canvas->get_Shapes()->Add(line);


// PDFファイルを保存

document->Save(_dataDir + u"DashLength_out.pdf");
}
```

結果を確認しましょう：

![Dashed Line](dash_line.png)

## ページ全体に線を引く

ラインオブジェクトを使用して、左下から右上の角、および左上の角から右下の角に向かってクロスを描画することもできます。

この要件を達成するために、以下のコードスニペットを確認してください。

```cpp
void ExampleLineAcrossPage() {

    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();
   
    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();
    // ページの余白をすべて0に設定

    page->get_PageInfo()->get_Margin()->set_Left(0);
    page->get_PageInfo()->get_Margin()->set_Right(0);
    page->get_PageInfo()->get_Margin()->set_Bottom(0);
    page->get_PageInfo()->get_Margin()->set_Top(0);

    // ページの寸法に等しい幅と高さでGraphオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(
        page->get_PageInfo()->get_Width(), 
        page->get_PageInfo()->get_Height());

    // ページの左下から右上の角に向かって始まる最初のラインオブジェクトを作成
    auto line = MakeObject<Aspose::Pdf::Drawing::Line>(
        MakeArray<double>({ 
                      page->get_Rect()->get_LLX(), 0, 
                      page->get_PageInfo()->get_Width(),
                      page->get_Rect()->get_URY() }));

    // Graphオブジェクトの形状コレクションにラインを追加
    graph->get_Shapes()->Add(line);
    // ページの左上の角から右下の角に向かってラインを描画
    auto line2 = MakeObject<Aspose::Pdf::Drawing::Line>( MakeArray<double>({0, 
        page->get_Rect()->get_URY(), page->get_PageInfo()->get_Width(), page->get_Rect()->get_LLX() }));

    // Graphオブジェクトの形状コレクションにラインを追加
    graph->get_Shapes()->Add(line2);
    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingLine_out.pdf");
}
```

![Drawing Line](draw_line.png)