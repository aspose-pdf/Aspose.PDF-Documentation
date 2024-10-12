---
title: C++ を使用して AcroForm データを抽出する
linktitle: データ AcroForm を抽出する
type: docs
weight: 30
url: /cpp/extract-form/
description: このセクションでは、Aspose.PDF for C++ を使用して PDF ドキュメントからフォームを抽出する方法を説明します。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントのすべてのフィールドから値を取得する

PDF ドキュメントのすべてのフィールドから値を取得するには、すべてのフォーム フィールドをナビゲートして、Value プロパティを使用して値を取得する必要があります。Form コレクションから各フィールドを取得し、Field と呼ばれる基本フィールド タイプでその Value プロパティにアクセスします。

次のコードスニペットは、PDF ドキュメントのすべてのフィールドの値を取得する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // すべてのフィールドから値を取得する
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"フィールド名 : {0} ", formField->get_PartialName());
        Console::WriteLine(u"値 : {0} ", formField->get_Value());
    }
}
```

## PDFドキュメントの個々のフィールドから値を取得する

フォームフィールドのValueプロパティを使用して、特定のフィールドの値を取得できます。値を取得するには、DocumentオブジェクトのFormコレクションからフォームフィールドを取得します。この例では、[TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field)を選択し、Valueプロパティを使用してその値を取得します。

次のコードスニペットは、PDFドキュメント内の個々のフィールドの値を取得する方法を示しています。

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // フィールドを取得する
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // フィールド値を取得する
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

送信ボタンのURLを取得するには、以下のコード行を使用します。

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## PDFファイルの特定の領域からフォームフィールドを取得する

時々、ドキュメント内のどこにフォームフィールドがあるかは分かっていても、その名前が分からないことがあります。例えば、印刷されたフォームの設計図しか持っていない場合です。Aspose.PDF for C++を使用すれば、これは問題ではありません。PDFファイルの特定の領域にどのフィールドがあるかを調べることができます。PDFファイルの特定の領域からフォームフィールドを取得するには：

1. Documentオブジェクトを使用してPDFファイルを開く。
1. その領域のフィールドを取得するために矩形オブジェクトを作成する。
1. ドキュメントのFormsコレクションからフォームを取得する。
1. フィールド名と値を表示する。

次のコードスニペットは、PDFファイルの特定の矩形領域内のフォームフィールドを取得する方法を示しています。
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // PDFファイルを開く
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // そのエリアのフィールドを取得するために長方形オブジェクトを作成
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // 長方形エリア内のフィールドを取得
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // フィールド名と値を表示
    for(auto field : fields)
    {
        // すべての配置の画像配置プロパティを表示
        Console::WriteLine(u"Field Name: {0} - Field Value: {1}", field->get_FullName(), field->get_Value());
    }
}
```