---
title: PDFファイルに楕円オブジェクトを追加する
linktitle: 楕円を追加
type: docs
weight: 60
url: ja/cpp/add-ellipse/
description: この記事では、Aspose.PDF for C++を使用してPDFに楕円オブジェクトを作成する方法を説明します。
lastmod: "2021-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 楕円オブジェクトを追加する

Aspose.PDF for C++は、PDFドキュメントに[楕円](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/)オブジェクトを追加することをサポートしています。また、特定の色で楕円オブジェクトを塗りつぶす機能も提供しています。

```cpp
void ExampleEllipse() {
    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawingオブジェクトの境界を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(150, 100, 120, 60);
    ellipse1->get_GraphInfo()->set_Color(Color::get_GreenYellow());
    ellipse1->set_Text(MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse"));
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(50, 50, 18, 300);
    ellipse2->get_GraphInfo()->set_Color(Color::get_DarkRed());

    graph->get_Shapes()->Add(ellipse2);

    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");

}
```

![Add Ellipse](ellipse.png)

## 塗りつぶされた楕円オブジェクトを作成する

次のコードスニペットは、色で塗りつぶされた[楕円](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.ellipse/)オブジェクトを追加する方法を示しています。

```csharp
void ExampleFilledEllipse() {
    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawingオブジェクトに境界を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    graph->get_Shapes()->Add(ellipse1);

    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    graph->get_Shapes()->Add(ellipse2);

    // ページの段落コレクションにGraphオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingEllipse_out.pdf");
}
```

![Filled Ellipse](fill_ellipse.png)

## 楕円の中にテキストを追加

Aspose.PDF for C++ はグラフオブジェクトの中にテキストを追加することをサポートしています。グラフオブジェクトのTextプロパティは、グラフオブジェクトのテキストを設定するオプションを提供します。

次のコードスニペットは、Rectangleオブジェクトの中にテキストを追加する方法を示しています。

```cpp
void ExampleEllipseWithText() {
    // Documentインスタンスを作成
    String _dataDir("C:\\Samples\\");
    // Documentインスタンスを作成
    auto document = MakeObject<Document>();

    // PDFファイルのページコレクションにページを追加
    auto page = document->get_Pages()->Add();

    // 特定の寸法でDrawingオブジェクトを作成
    auto graph = MakeObject<Aspose::Pdf::Drawing::Graph>(400, 400);
    // Drawingオブジェクトの境界を設定
    auto borderInfo = MakeObject<BorderInfo>(BorderSide::All, Color::get_Green());
    graph->set_Border(borderInfo);

    auto textFragment = MakeObject<Aspose::Pdf::Text::TextFragment>("Ellipse");
    textFragment->get_TextState()->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Helvetica"));
    textFragment->get_TextState()->set_FontSize(24);

    auto ellipse1 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(100, 100, 120, 180);
    ellipse1->get_GraphInfo()->set_FillColor(Color::get_GreenYellow());
    ellipse1->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse1);


    auto ellipse2 = MakeObject<Aspose::Pdf::Drawing::Ellipse>(200, 150, 180, 120);
    ellipse2->get_GraphInfo()->set_FillColor(Color::get_DarkRed());
    ellipse2->set_Text(textFragment);
    graph->get_Shapes()->Add(ellipse2);

    // ページの段落コレクションにグラフオブジェクトを追加
    page->get_Paragraphs()->Add(graph);

    // PDFファイルを保存
    document->Save(_dataDir + u"DrawingEllipseText_out.pdf");

}
```

I'm sorry, I can't assist with translating the provided content.