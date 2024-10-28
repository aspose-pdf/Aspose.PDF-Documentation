---
title: PDF内のテキストを回転させる方法 (C++使用)
linktitle: PDF内のテキストを回転させる
type: docs
weight: 50
url: /cpp/rotate-text-inside-pdf/
description: PDFにテキストを回転させるさまざまな方法を学びます。Aspose.PDFを使用すると、任意の角度にテキストを回転させたり、テキストフラグメントや段落全体を回転させたりできます。
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Rotationプロパティを使用してPDF内のテキストを回転させる

[TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/)クラスのRotationプロパティを使用すると、さまざまな角度でテキストを回転させることができます。テキストの回転は、ドキュメント生成のさまざまなシナリオで使用できます。必要に応じてテキストを回転させるために、回転角度を度で指定できます。以下の異なるシナリオを確認し、テキストの回転を実装できます。

## TextFragmentとTextBuilderを使用した回転の実装

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ImplementRotationUsingTextFragmentAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントオブジェクトを初期化
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();
    // テキストフラグメントを作成
    auto textFragment1 = MakeObject<TextFragment>("main text");
    textFragment1->set_Position(MakeObject<Position>(100, 600));

    // テキストのプロパティを設定
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 回転したテキストフラグメントを作成
    auto textFragment2 = MakeObject<TextFragment>("rotated text");
    textFragment2->set_Position(MakeObject<Position>(200, 600));
    // テキストのプロパティを設定
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment2->get_TextState()->set_Rotation(45);

    // 回転したテキストフラグメントを作成
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    textFragment3->set_Position(MakeObject<Position>(300, 600));

    // テキストのプロパティを設定
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    textFragment3->get_TextState()->set_Rotation(90);

    // TextBuilderオブジェクトを作成
    auto textBuilder = MakeObject<TextBuilder>(page);
    // テキストフラグメントをPDFページに追加
    textBuilder->AppendText(textFragment1);
    textBuilder->AppendText(textFragment2);
    textBuilder->AppendText(textFragment3);

    // ドキュメントを保存
    document->Save(_dataDir + u"TextFragmentTests_Rotated1_out.pdf");
}
```

## TextParagraphとTextBuilderを使用した回転の実装（回転されたフラグメント）

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder_RotatedFragments() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントオブジェクトを初期化
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();
    auto paragraph = MakeObject<TextParagraph>();
    paragraph->set_Position(MakeObject<Position>(200, 600));

    // テキストフラグメントを作成
    auto textFragment1 = MakeObject<TextFragment>("rotated text");
    // テキストプロパティを設定
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // 回転を設定
    textFragment1->get_TextState()->set_Rotation(45);

    // テキストフラグメントを作成
    auto textFragment2 = MakeObject<TextFragment>("main text");
    // テキストプロパティを設定
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // テキストフラグメントを作成
    auto textFragment3 = MakeObject<TextFragment>("another rotated text");
    // テキストプロパティを設定
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
    // 回転を設定
    textFragment3->get_TextState()->set_Rotation(-45);

    // テキストフラグメントを段落に追加
    paragraph->AppendLine(textFragment1);
    paragraph->AppendLine(textFragment2);
    paragraph->AppendLine(textFragment3);
    // TextBuilderオブジェクトを作成
    auto textBuilder = MakeObject<TextBuilder>(page);
    // PDFページにテキスト段落を追加
    textBuilder->AppendParagraph(paragraph);
    // ドキュメントを保存
    document->Save(_dataDir + u"TextFragmentTests_Rotated2_out.pdf");

}
```

## TextFragmentとPage.Paragraphsを使用した回転の実装

```cpp
void ImplementRotationUsingTextFragmentAndPageParagraphs() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントオブジェクトを初期化
    auto document = MakeObject<Document>();
    // 特定のページを取得
    auto page = document->get_Pages()->Add();
    // テキストフラグメントを作成
    auto textFragment1 = MakeObject<TextFragment>("main text");
    // テキストプロパティを設定
    textFragment1->get_TextState()->set_FontSize(12);
    textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // テキストフラグメントを作成
    auto textFragment2 = MakeObject<TextFragment>("rotated text");

    // テキストプロパティを設定
    textFragment2->get_TextState()->set_FontSize(12);
    textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 回転を設定
    textFragment2->get_TextState()->set_Rotation(315);

    // テキストフラグメントを作成
    auto textFragment3 = MakeObject<TextFragment>("rotated text");
    // テキストプロパティを設定
    textFragment3->get_TextState()->set_FontSize(12);
    textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));

    // 回転を設定
    textFragment3->get_TextState()->set_Rotation(270);
    page->get_Paragraphs()->Add(textFragment1);
    page->get_Paragraphs()->Add(textFragment2);
    page->get_Paragraphs()->Add(textFragment3);

    // ドキュメントを保存
    document->Save(_dataDir + u"TextFragmentTests_Rotated3_out.pdf");
}
```

## Implement Rotation using TextParagraph and TextBuilder (Whole Paragraph Rotated)

```cpp
void ImplementRotationUsingTextParagraphAndTextBuilder() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントオブジェクトを初期化する
    auto document = MakeObject<Document>();
    // 特定のページを取得する
    auto page = document->get_Pages()->Add();
    for (int i = 0; i < 4; i++) {
        auto paragraph = MakeObject<TextParagraph>();
        paragraph->set_Position(MakeObject<Position>(200, 600));
        // 回転を指定する
        paragraph->set_Rotation(i * 90 + 45);
        // テキストフラグメントを作成する
        auto textFragment1 = MakeObject<TextFragment>("Paragraph Text");
        // テキストフラグメントを作成する
        textFragment1->get_TextState()->set_FontSize(12);
        textFragment1->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment1->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment1->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // テキストフラグメントを作成する
        auto textFragment2 = MakeObject<TextFragment>("Second line of text");
        // テキストプロパティを設定する
        textFragment2->get_TextState()->set_FontSize(12);
        textFragment2->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment2->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment2->get_TextState()->set_ForegroundColor(Color::get_Blue());

        // テキストフラグメントを作成する
        auto textFragment3 = MakeObject<TextFragment>("And some more text...");
        // テキストプロパティを設定する
        textFragment3->get_TextState()->set_FontSize(12);
        textFragment3->get_TextState()->set_Font(FontRepository::FindFont(u"TimesNewRoman"));
        textFragment3->get_TextState()->set_BackgroundColor(Color::get_LightGray());
        textFragment3->get_TextState()->set_ForegroundColor(Color::get_Blue());
        textFragment3->get_TextState()->set_Underline(true);

        paragraph->AppendLine(textFragment1);
        paragraph->AppendLine(textFragment2);
        paragraph->AppendLine(textFragment3);
        // TextBuilderオブジェクトを作成する
        auto textBuilder = MakeObject<TextBuilder>(page);
        // テキストフラグメントをPDFページに追加する
        textBuilder->AppendParagraph(paragraph);
    }
    // ドキュメントを保存する
    document->Save(_dataDir + u"TextFragmentTests_Rotated4_out.pdf");
}
```