---
title: AcroFormの変更
linktitle: AcroFormの変更
type: docs
weight: 40
url: /ja/cpp/modifing-form/
description: Aspose.PDF for C++ライブラリを使用してPDFファイル内のフォームを変更します。既存のフォームにフィールドを追加または削除したり、フィールド制限を取得および設定したりすることができます。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## フィールド制限を取得または設定する

FormEditorクラスのSetFieldLimit(field, limit)メソッドは、フィールド制限を設定することを可能にします。これは、フィールドに入力できる文字数の最大値です。

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

同様に、Aspose.PDFにはDOMアプローチを使用してフィールド制限を取得するメソッドがあります。 以下のコードスニペットは手順を示しています。

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Limit: {0}", textBoxField->get_MaxLen());        
}
```

同じ値を*Aspose.PDF.Facades*名前空間を使用して設定および取得することもできます。次のコードスニペットを使用します。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // 制限付きフィールドを追加
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // 制限付きフィールドを追加
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Limit: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## フォームフィールドのカスタムフォントを設定する

Adobe PDFファイルのフォームフィールドは、特定のデフォルトフォントを使用するように設定できます。Aspose.PDFの初期バージョンでは、14種類のデフォルトフォントのみがサポートされていました。後のリリースでは、開発者が任意のフォントを適用できるようになりました。フォームフィールドで使用するデフォルトフォントを設定および更新するには、DefaultAppearance (Font font, double size, Color color) クラスを使用します。このクラスは、Aspose.PDF.InteractiveFeatures 名前空間の下にあります。このオブジェクトを使用するには、Field クラスの DefaultAppearance プロパティを使用します。

次のコードスニペットは、PDFフォームフィールドのデフォルトフォントを設定する方法を示しています。

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // ドキュメントから特定のフォームフィールドを取得
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // フォントオブジェクトを作成
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // フォームフィールドのフォント情報を設定

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## 既存のフォームからフィールドを削除する

すべてのフォームフィールドは、Document オブジェクトの Form コレクションに含まれています。このコレクションは、フィールドを管理するためのさまざまなメソッドを提供しており、Delete メソッドも含まれています。特定のフィールドを削除したい場合は、フィールド名を Delete メソッドのパラメーターとして渡し、更新された PDF ドキュメントを保存します。次のコードスニペットは、PDF ドキュメントから特定のフィールドを削除する方法を示しています。

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // 名前で特定のフィールドを削除する
    document->get_Form()->Delete(u"textbox1");
    
    // 変更されたドキュメントを保存する
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```