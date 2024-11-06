---
title: C++を使用してAcroFormsを作成する
linktitle: AcroFormsを作成する
type: docs
weight: 10
url: ja/cpp/create-form/
description: このセクションでは、Aspose.PDF for C++を使用してPDFドキュメントにAcroFormsをゼロから作成する方法を説明します。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントにフォームフィールドを追加する

[Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)クラスは、PDFドキュメント内のフォームフィールドを管理するのに役立つFormという名のコレクションを提供します。

フォームフィールドを追加するには：

1. 追加したいフォームフィールドを作成します。
2. [Form](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.forms)コレクションのaddメソッドを呼び出します。

この例では、[TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field)を追加する方法を示します。同じアプローチで任意のフォームフィールドを追加できます：

1. まず、フィールドオブジェクトを作成し、そのプロパティを設定します。
2. 次に、フィールドをFormコレクションに追加します。

### TextBoxFieldの追加

テキストフィールドは、受信者がフォームにテキストを入力できるようにするフォーム要素です。 ユーザーが自由に入力できるようにしたい場合に使用されます。

次のコードスニペットは、PDFドキュメントにTextBoxFieldを追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
void AddingTextBoxField()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"TextField.pdf");

    // フィールドを作成
    auto textBoxField = MakeObject<TextBoxField>(document->get_Pages()->idx_get(1), MakeObject<Aspose::Pdf::Rectangle>(100, 200, 300, 300));
    textBoxField->set_PartialName (u"textbox1");
    textBoxField->set_Value (u"Text Box");

    // TextBoxField.Border = new Border(
    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textBoxField);
    border->set_Width(5);
    border->set_Dash (MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textBoxField->set_Border(border);

    textBoxField->set_Color(Aspose::Pdf::Color::get_Green());

    // ドキュメントにフィールドを追加
    document->get_Form()->Add(textBoxField, 1);

    // 修正されたPDFを保存
    document->Save(_dataDir + u"TextBox_out.pdf");
}
```
## RadioButtonFieldの追加

ラジオボタンは、1つの回答のみ選択できる状況で、複数選択問題に最も一般的に使用されます。

次のコードスニペットは、PDFドキュメントに[RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)を追加する方法を示しています。

```cpp
void AddingRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto document = MakeObject<Document>();

    // PDFファイルにページを追加
    document->get_Pages()->Add();

    // 引数としてページ番号を持つRadioButtonFieldオブジェクトをインスタンス化

    auto radio = MakeObject<RadioButtonField>(document->get_Pages()->idx_get(1));

    // 最初のラジオボタンのオプションを追加し、Rectangleオブジェクトを使用してその位置を指定
    radio->AddOption(u"Option 1", MakeObject<Rectangle>(0, 0, 20, 20));
    // 2番目のラジオボタンのオプションを追加
    radio->AddOption(u"Option 2", MakeObject<Rectangle>(20, 20, 40, 40));
    // Documentオブジェクトのフォームオブジェクトにラジオボタンを追加
    document->get_Form()->Add(radio,1);

    // PDFファイルを保存
    document->Save(_dataDir + u"RadioButton_out.pdf");
}
```

以下のコードスニペットは、3つのオプションを持つ[RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field)を追加し、それらをテーブルのセル内に配置する手順を示しています。

```cpp
void AddRadioButtonFieldInsideTableCells()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto table = MakeObject<Aspose::Pdf::Table>();

    table->set_ColumnWidths(u"120 120 120");

    page->get_Paragraphs()->Add(table);

    auto r1 = table->get_Rows()->Add();
    auto c1 = r1->get_Cells()->Add();
    auto c2 = r1->get_Cells()->Add();
    auto c3 = r1->get_Cells()->Add();

    auto rf = MakeObject<RadioButtonField>(page);
    rf->set_PartialName(u"radio");
    document->get_Form()->Add(rf, 1);

    auto opt1 = MakeObject<RadioButtonOptionField>();
    auto opt2 = MakeObject<RadioButtonOptionField>();
    auto opt3 = MakeObject<RadioButtonOptionField>();

    opt1->set_OptionName(u"Item1");
    opt2->set_OptionName(u"Item2");
    opt3->set_OptionName(u"Item3");

    opt1->set_Width (15);
    opt1->set_Height(15);
    opt2->set_Width (15);
    opt2->set_Height(15);
    opt3->set_Width (15);
    opt3->set_Height(15);

    rf->Add(opt1);
    rf->Add(opt2);
    rf->Add(opt3);

    opt1->set_Border(MakeObject<Border>(opt1));
    opt1->get_Border()->set_Width(1);
    opt1->get_Border()->set_Style(BorderStyle::Solid);
    opt1->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt1->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt1->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item1"));
    opt2->set_Border(MakeObject<Border>(opt2));
    opt2->get_Border()->set_Width(1);
    opt2->get_Border()->set_Style(BorderStyle::Solid);
    opt2->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt2->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt2->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item2"));
    opt3->set_Border(MakeObject<Border>(opt3));
    opt3->get_Border()->set_Width(1);
    opt3->get_Border()->set_Style(BorderStyle::Solid);
    opt3->get_Characteristics()->set_Border(System::Drawing::Color::get_Black());
    opt3->get_DefaultAppearance()->set_TextColor(System::Drawing::Color::get_Red());
    opt3->set_Caption(MakeObject<Aspose::Pdf::Text::TextFragment>(u"Item3"));
    c1->get_Paragraphs()->Add(opt1);
    c2->get_Paragraphs()->Add(opt2);
    c3->get_Paragraphs()->Add(opt3);

    // PDFファイルを保存
    document->Save(_dataDir + u"RadioButtonWithOptions_out.pdf");
}
```

## ラジオボタンフィールドへのキャプションの追加

次のコードスニペットは、[RadioButtonField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.radio_button_field) に関連付けられるキャプションを追加する方法を示します:

```cpp
void AddingCaptionToRadioButtonField()
{
    String _dataDir("C:\\Samples\\");
    auto document = MakeObject<Document>();

    // ソースPDFフォームをロード
    auto form1 =
        MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"RadioButtonField.pdf");

    auto PDF_Template_PDF_HTML = MakeObject<Document>(_dataDir + u"RadioButtonField.pdf");

    for(auto item : form1->get_FieldNames())
    {
        System::Console::WriteLine(item);
        auto radioOptions = form1->GetButtonOptionValues(item);
        if (item.Contains(u"radio1"))
        {
            auto field0 = System::DynamicCast<RadioButtonField>(PDF_Template_PDF_HTML->get_Form()->idx_get(item));
            auto fieldoption = MakeObject<RadioButtonOptionField>();
            fieldoption->set_OptionName (u"Yes");
            fieldoption->set_PartialName (u"Yesname");

            auto updatedFragment = MakeObject<Aspose::Pdf::Text::TextFragment>(u"test123");
            updatedFragment->get_TextState()->set_Font (Aspose::Pdf::Text::FontRepository::FindFont(u"Arial"));
            updatedFragment->get_TextState()->set_FontSize(10);
            updatedFragment->get_TextState()->set_LineSpacing(6.32f);

            // TextParagraphオブジェクトを作成
            auto par = MakeObject<Aspose::Pdf::Text::TextParagraph>();

            // 段落の位置を設定
            par->set_Position(MakeObject<Aspose::Pdf::Text::Position>(field0->get_Rect()->get_LLX(), field0->get_Rect()->get_LLY() + updatedFragment->get_TextState()->get_FontSize()));
            // ワードラッピングモードを指定
        par->get_FormattingOptions()->set_WrapMode(Aspose::Pdf::Text::TextFormattingOptions::WordWrapMode::ByWords);

            // 段落に新しいTextFragmentを追加
            par->AppendLine(updatedFragment);

            // TextBuilderを使用してTextParagraphを追加
            auto textBuilder = MakeObject<Aspose::Pdf::Text::TextBuilder>(PDF_Template_PDF_HTML->get_Pages()->idx_get(1));
            textBuilder->AppendParagraph(par);

            field0->DeleteOption(u"item1");
        }
    }
    PDF_Template_PDF_HTML->Save(_dataDir + u"RadioButtonField_out.pdf");
}
```

## コンボボックスフィールドの追加

コンボボックスは、ドキュメントにドロップダウンメニューを追加するフォームフィールドです。

以下のコードスニペットは、PDFドキュメントに[ComboBox](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.combo_box_field)フィールドを追加する方法を示しています。

```cpp
void AddingComboBoxField()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントオブジェクトを作成
    auto document = MakeObject<Document>();
    // ドキュメントオブジェクトにページを追加
    document->get_Pages()->Add();
    // コンボボックスフィールドオブジェクトをインスタンス化
    auto combo = MakeObject<ComboBoxField>(document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(100, 600, 150, 616));

    // コンボボックスにオプションを追加
    combo->AddOption(u"Red");
    combo->AddOption(u"Yellow");
    combo->AddOption(u"Green");
    combo->AddOption(u"Blue");

    // ドキュメントオブジェクトのフォームフィールドコレクションにコンボボックスオブジェクトを追加
    document->get_Form()->Add(combo);

    // PDFドキュメントを保存
    document->Save(_dataDir + u"ComboBox_out.pdf");
}
```


## フォームにツールチップを追加

The Document クラスは、PDF ドキュメント内のフォームフィールドを管理する Form というコレクションを提供します。フォームフィールドにツールチップを追加するには、Field クラスの AlternateName を使用します。Adobe Acrobat は、「代替名」をフィールドのツールチップとして使用します。

以下のコードスニペットは、C++でフォームフィールドにツールチップを追加する方法を示しています。

```cpp
void AddTooltipToFormField()
{
    String _dataDir("C:\\Samples\\");
    // ソース PDF フォームをロード
    auto document = new Document(_dataDir + u"AddTooltipToField.pdf");

    // テキストフィールドのツールチップを設定
    //(doc.Form["textbox1"] as Field).AlternateName = "テキストボックスのツールチップ";

    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"AddTooltipToField_out.pdf");
}
```