---
title: PDF内のテキストフォーマットをC++で行う
linktitle: PDF内のテキストフォーマット
type: docs
weight: 30
url: /cpp/text-formatting-inside-pdf/
description: このページでは、PDFファイル内のテキストをフォーマットする方法について説明します。行のインデントの追加、テキストの境界線の追加、下線の追加、追加したテキストの周囲に境界線を追加、フローティングボックスの内容のテキスト配置などがあります。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFに行インデントを追加する方法

PDFに行インデントを追加するには、Aspose.PDF for C++は[TextFormattingOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options/)クラスの[SubsequentLinesIndent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_formatting_options#a89b064ab1f39d56040625d7d98194ad3)プロパティを使用し、さらに[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)および[Paragraphs](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs)コレクションを活用します。

以下のコードスニペットを使用してプロパティを使用してください:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineIndent() {

    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("SubsequentIndent_out.pdf");


    // 新しいドキュメントオブジェクトの作成
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto text = MakeObject<TextFragment>("A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog. A quick brown fox jumped over the lazy dog.");

    // テキストフラグメントのTextFormattingOptionsを初期化し、SubsequentLinesIndent値を指定
    text->get_TextState()->set_FormattingOptions(MakeObject<Aspose::Pdf::Text::TextFormattingOptions>());
    text->get_TextState()->get_FormattingOptions()->set_SubsequentLinesIndent(20);

    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line2");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line3");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line4");
    page->get_Paragraphs()->Add(text);

    text = MakeObject<Aspose::Pdf::Text::TextFragment>(u"Line5");
    page->get_Paragraphs()->Add(text);

    document->Save(_dataDir + outputFileName);

}
```

## テキストボーダーの追加方法

以下のコードスニペットは、TextBuilderを使用してテキストにボーダーを追加し、[TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)のDrawTextRectangleBorderプロパティを設定する方法を示しています。

```cpp
void AddTextBorder() {

    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("PDFWithTextBorder_out.pdf");

    // 新しいドキュメントオブジェクトを作成
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();

    // テキストフラグメントを作成
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // テキストプロパティを設定
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // テキストの周りにボーダー（ストローク）を描画するためにStrokingColorプロパティを設定
    textFragment->get_TextState()->set_StrokingColor(Color::get_DarkRed());
    // DrawTextRectangleBorderプロパティの値をtrueに設定
    textFragment->get_TextState()->set_DrawTextRectangleBorder(true);
    auto tb = MakeObject<TextBuilder>(page);
    tb->AppendText(textFragment);
    // ドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## Underlineテキストを追加する方法

次のコードスニペットは、新しいPDFファイルを作成する際にUnderlineテキストを追加する方法を示しています。

```cpp
void AddUnderlineText() {
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名用の文字列
    String outputFileName("AddUnderlineText_out.pdf");

    // 新しいドキュメントオブジェクトを作成
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();

    // サンプルテキストを含むTextFragment
    auto fragment = MakeObject<TextFragment>("Text with underline decoration");
    // TextFragmentのフォントを設定
    fragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    fragment->get_TextState()->set_FontSize(10);

    // テキストの書式設定をUnderlineに設定
    fragment->get_TextState()->set_Underline(true);

    // TextFragmentを配置する位置を指定
    fragment->set_Position(MakeObject<Position>(10, 800));

    auto tb = MakeObject<TextBuilder>(page);
    // PDFファイルにTextFragmentを追加
    tb->AppendText(fragment);

    // 結果のPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## 追加されたテキストの周囲に境界線を追加する方法

追加するテキストの外観を自由にコントロールできます。以下の例では、追加したテキストの周囲に長方形を描いて境界線を追加する方法を示しています。[PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor/) クラスについて詳しく知ることができます。

```cpp
void AddBorderAroundAddedText() {

    String _dataDir("C:\\Samples\\");

    // 入力ファイル名用の文字列
    String inputFileName("sample.pdf");

    // 出力ファイル名用の文字列
    String outputFileName("AddingBorderAroundAddedText_out.pdf");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    editor->BindPdf(_dataDir + inputFileName);
    auto lineInfo = MakeObject<Aspose::Pdf::Facades::LineInfo>();

    lineInfo->set_LineWidth(2);
    lineInfo->set_VerticeCoordinate(MakeArray<float>({ 0, 0, 100, 100, 50, 100 }));
    lineInfo->set_Visibility(true);
    auto rect = MakeObject<System::Drawing::Rectangle>(0, 0, 0, 0);
    editor->CreatePolygon(lineInfo, 1, System::Drawing::Rectangle(0, 0, 0, 0), String::Empty);

    // 結果の PDF ドキュメントを保存します。
    editor->Save(_dataDir + outputFileName);
}
```

## NewLineフィードの追加方法

改行を含むテキストを追加するには、[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment)と[TextParagraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_paragraph)を使用してください。

以下のコードスニペットは、PDFファイルにNewLineフィードを追加する方法を示しています:

```cpp
void AddNewLineFeed() {
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("AddNewLineFeed_out.pdf");

    // 新しいドキュメントオブジェクトを作成
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();

    // 必要な改行マーカーを含むテキストで新しいTextFragmentを初期化
    auto textFragment = MakeObject<TextFragment>("Applicant Name: \r\n Joe Smoe");

    // 必要に応じてテキストフラグメントのプロパティを設定
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());

    // TextParagraphオブジェクトを作成
    auto par = MakeObject<TextParagraph>();

    // 新しいTextFragmentを段落に追加
    par->AppendLine(textFragment);

    // 段落の位置を設定
    par->set_Position(MakeObject<Position>(100, 600));

    // TextBuilderオブジェクトを作成
    auto textBuilder = new TextBuilder(page);
    // TextBuilderを使用してTextParagraphを追加
    textBuilder->AppendParagraph(par);

    // 結果のPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## StrikeOutテキストを追加する方法

[TextState](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_state)クラスを使用して、太字、斜体、下線などのテキストフォーマットを設定できます。また、APIはテキストフォーマットを打ち消し線としてマークする機能を提供しています。

次のコードスニペットを使用して、打ち消し線フォーマットでTextFragmentを追加してみてください。

```cpp
void AddStrikeOutText() {
    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("AddStrikeOutText_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();

    // テキストフラグメントを作成
    auto textFragment = MakeObject<TextFragment>("main text");
    textFragment->set_Position(MakeObject<Position>(100, 600));

    // テキストプロパティを設定
    textFragment->get_TextState()->set_FontSize(12);
    textFragment->get_TextState()->set_Font(FontRepository::FindFont(u"DejaVu Serif"));
    textFragment->get_TextState()->set_BackgroundColor(Color::get_LightGray());
    textFragment->get_TextState()->set_ForegroundColor(Color::get_Red());
    // 打ち消し線プロパティを設定
    textFragment->get_TextState()->set_StrikeOut(true);
    // テキストを太字としてマーク
    textFragment->get_TextState()->set_FontStyle(FontStyles::Bold);

    // TextBuilderオブジェクトを作成
    auto textBuilder = MakeObject<TextBuilder>(page);
    // テキストフラグメントをPDFページに追加
    textBuilder->AppendText(textFragment);

    // 結果として得られるPDFドキュメントを保存
    document->Save(_dataDir + outputFileName);
}
```

## テキストにグラデーションシェーディングを適用する

[Aspose.Pdf.Color](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color) クラスは、テキストのシェーディングカラーを指定するために使用できる新しいプロパティ [PatternColorSpace](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.color#a8be6d8ab626d2ba6935a13a9c5b0de54) を導入することにより、さらに強化されています。この新しいプロパティは、以下のコードスニペットに示すように、テキストに異なるグラデーションシェーディングを追加します。例えば、軸方向シェーディング、放射状（タイプ3）シェーディングなどです。

```cpp
void ApplyGradientShading() {

    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("sample.pdf");

    // 出力ファイル名の文字列
    String outputFileName("ApplyGradientShading_out.pdf");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>("always print correctly");

    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientAxialShading>(Color::get_Red(), Color::get_Blue()));

    // パターンカラー空間を持つ新しい色を作成
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);

}
```

>Radial Gradientを適用するには、上記のコードスニペットで‘PatternColorSpace’プロパティを‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’に設定することができます。

## フロートコンテンツにテキストを揃える方法

Aspose.PDFは、Floating Box要素内のコンテンツに対してテキストの配置を設定することをサポートしています。[Aspose.Pdf.FloatingBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.floating_box)インスタンスの配置プロパティを使用して、以下のコードサンプルのようにこれを達成できます。

```cpp
void ApplyGradientShadingRadial() {

    String _dataDir("C:\\Samples\\");

    // 入力ファイル名の文字列
    String inputFileName("sample.pdf");

    // 出力ファイル名の文字列
    String outputFileName("ApplyGradientShadingRadial_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto absorber = MakeObject<TextFragmentAbsorber>(u"always print correctly");
    document->get_Pages()->Accept(absorber);

    auto textFragment = absorber->get_TextFragments()->idx_get(1);

    auto foregroundColor = MakeObject<Aspose::Pdf::Color>();
    foregroundColor->set_PatternColorSpace(MakeObject<Aspose::Pdf::Drawing::GradientRadialShading>(Color::get_Red(), Color::get_Blue()));

    // パターンカラースペースを使って新しい色を作成
    textFragment->get_TextState()->set_ForegroundColor(foregroundColor);

    textFragment->get_TextState()->set_Underline(true);

    document->Save(_dataDir + outputFileName);
}
```