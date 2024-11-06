---
title: PDF Tooltip using using C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: ja/cpp/pdf-tooltip/
description: C++とAspose.PDFを使用してPDFのテキストフラグメントにツールチップを追加する方法を学びます
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 見えないボタンを追加して検索されたテキストにツールチップを追加

この記事では、C++で既存のPDFドキュメントのテキストにツールチップを追加する方法を示します。Aspose.PDFは、PDFファイルから検索されたテキストの上に見えないボタンを追加することでツールチップを作成することをサポートしています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void AddTooltipToSearchedText() {

    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("Tooltip_out.pdf");

    // テキストを含むサンプルドキュメントを作成
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("ここにマウスカーソルを移動するとツールチップが表示されます"));

    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(MakeObject<TextFragment>("ここにマウスカーソルを移動すると非常に長いツールチップが表示されます"));

    document->Save(outputFileName);

    // テキストを含むドキュメントを開く
    auto document = MakeObject<Document>(outputFileName);
    // 正規表現に一致するすべてのフレーズを見つけるためにTextAbsorberオブジェクトを作成
    auto absorber = MakeObject<TextFragmentAbsorber>("ここにマウスカーソルを移動するとツールチップが表示されます");
    // ドキュメントページに対してアブソーバーを受け入れる
    document->get_Pages()->Accept(absorber);

    // 抽出されたテキストフラグメントを取得
    auto textFragments = absorber->get_TextFragments();

    // フラグメントをループする
    for(auto fragment : textFragments)
    {
        // テキストフラグメントの位置に見えないボタンを作成
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // AlternateNameの値はビューアーアプリケーションによってツールチップとして表示されます
        field->set_AlternateName (u"テキストのツールチップ。");
        // ドキュメントにボタンフィールドを追加
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // 次は非常に長いツールチップのサンプルです
    absorber = MakeObject<TextFragmentAbsorber>("ここにマウスカーソルを移動すると非常に長いツールチップが表示されます");
    document->get_Pages()->Accept(absorber);
    textFragments = absorber->get_TextFragments();

    for(auto fragment : textFragments)
    {
        auto field = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        // 非常に長いテキストを設定
        field->set_AlternateName(String("Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
            sed do eiusmod tempor incididunt ut labore et dolore magna\
            aliqua. Ut enim ad minim veniam, quis nostrud exercitation\
            ullamco laboris nisi ut aliquip ex ea commodo consequat.\
            Duis aute irure dolor in reprehenderit in voluptate velit\
            esse cillum dolore eu fugiat nulla pariatur. Excepteur sint\
            occaecat cupidatat non proident, sunt in culpa qui officia\
            deserunt mollit anim id est laborum."));
        document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(field));
    }

    // ドキュメントを保存
    document->Save(outputFileName);

}
```

## マウスオーバーで表示される隠しテキストブロックを作成する

Aspose.PDF for C++は非表示アクション機能を実装しており、これを使用して、見えないボタンの上でマウスが入出した際にテキストフィールド（または他のタイプの注釈）を表示/非表示にすることができます。これを行うには、Aspose.Pdf.Annotations.HideActionクラスを使用して、テキストブロックに非表示/表示アクションを割り当てます。次のコードスニペットを使用して、マウス入出力時にテキストブロックを表示/非表示にします。

また、ドキュメント上のPDFアクションは、それぞれのリーダー（Adobe Readerなど）では正常に動作しますが、他のPDFリーダー（ウェブブラウザプラグインなど）では保証されないことに注意してください。私たちは短い調査を行い、以下のことを発見しました：

- PDFドキュメントにおける非表示アクションのすべての実装は、Internet Explorer v.11.0で正常に動作します。
- 非表示アクションのすべての実装はOpera v.12.14でも動作しますが、ドキュメントを初めて開いた際に応答の遅延が見られます。

- HideActionコンストラクタを使用する実装のみがGoogle Chrome v.61.0でドキュメントを閲覧する場合に動作します。Google Chromeでの閲覧が重要な場合は、対応するコンストラクタを使用してください。

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```cpp
void CreateHiddenTextBlock() {

    String _dataDir("C:\\Samples\\");

    // 出力ファイル名の文字列
    String outputFileName("TextBlock_HideShow_MouseOverOut_out.pdf");

    // テキスト付きのサンプルドキュメントを作成
    auto document = MakeObject<Document>();

    document->get_Pages()->Add()->get_Paragraphs()->Add(MakeObject<TextFragment>("マウスカーソルをここに移動して浮動テキストを表示"));
    document->Save(outputFileName);

    // テキスト付きのドキュメントを開く
    auto document = MakeObject<Document>(outputFileName);

    // 正規表現に一致するすべてのフレーズを見つけるためのTextAbsorberオブジェクトを作成
    auto absorber = MakeObject<TextFragmentAbsorber>("マウスカーソルをここに移動して浮動テキストを表示");
    // ドキュメントページにアブソーバーを適用
    document->get_Pages()->Accept(absorber);
    // 抽出された最初のテキストフラグメントを取得
    auto textFragments = absorber->get_TextFragments();
    auto fragment = textFragments->idx_get(1);

    // ページの指定された矩形に浮動テキスト用の非表示テキストフィールドを作成
    auto floatingField = MakeObject<Aspose::Pdf::Forms::TextBoxField>(fragment->get_Page(), MakeObject<Rectangle>(100, 700, 220, 740));
    // フィールド値として表示されるテキストを設定
    floatingField->set_Value(u"これは「浮動テキストフィールド」です。");
    // このシナリオではフィールドを「読み取り専用」にすることをお勧めします
    floatingField->set_ReadOnly(true);
    // ドキュメントを開く際にフィールドを非表示にするための「非表示」フラグを設定
    floatingField->set_Flags(floatingField->get_Flags() | Aspose::Pdf::Annotations::AnnotationFlags::Hidden);

    // フィールドの一意の名前を設定する必要はありませんが、許可されています
    floatingField->set_PartialName (u"FloatingField_1");

    // フィールドの外観特性を設定する必要はありませんが、設定したほうが見栄えが良くなります
    floatingField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>("Helv", 10, Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background (System::Drawing::Color::get_LightBlue());
    floatingField->get_Characteristics()->set_Border (System::Drawing::Color::get_DarkBlue());
    floatingField->set_Border(MakeObject<Aspose::Pdf::Annotations::Border>(floatingField));
    floatingField->get_Border()->set_Width (1);
    floatingField->set_Multiline (true);

    // ドキュメントにテキストフィールドを追加
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(floatingField));

    // テキストフラグメントの位置に見えないボタンを作成
    auto buttonField = MakeObject<Aspose::Pdf::Forms::ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    // 指定されたフィールド（注釈）と不可視フラグのための新しい非表示アクションを作成。
    // （上記で名前を指定した場合、浮動フィールドを名前で参照することもできます。）
    // 見えないボタンフィールドでマウスの入出時にアクションを追加
    buttonField->get_Actions()->set_OnEnter(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<Aspose::Pdf::Annotations::HideAction>(floatingField));

    // ドキュメントにボタンフィールドを追加
    document->get_Form()->Add(System::DynamicCast<Aspose::Pdf::Forms::Field>(buttonField));

    // ドキュメントを保存
    document->Save(outputFileName);
}
```