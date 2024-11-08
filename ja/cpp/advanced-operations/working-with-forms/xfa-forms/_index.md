---
title: C++を使用したXFAフォームの操作
linktitle: XFAフォーム
type: docs
weight: 20
url: /ja/cpp/xfa-forms/
description: Aspose.PDF for C++ APIを使用すると、PDFドキュメント内のXFAおよびXFA Acroformフィールドを操作できます。Aspose.PDF.Facades。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

XFAフォームはXML Forms Architectureであり、JetFormによって提案および開発されたプロプライエタリなXML仕様のファミリーであり、ウェブフォームの処理を改善するためのものです。PDF 1.5仕様から始まるPDFファイルでも使用できます。

XFAフィールドを[Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades)の[Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/)クラスで埋めます。

## XFAフィールドを埋める

次のコードスニペットは、XFAフォームのフィールドを埋める方法を示しています。

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Load XFA form
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Get names of XFA form fields
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Set field values

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Save the updated document
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```

## XFAをAcroFormに変換

{{% alert color="primary" %}}

オンラインで試す
Aspose.PDFの変換品質を確認し、オンラインで結果を表示するには、次のリンクをご覧ください: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

ダイナミックフォームは、XFA、「XMLフォームアーキテクチャ」として知られるXML仕様に基づいています。フォームに関する情報は（PDFに関しては）非常に曖昧で、フィールドが存在すること、プロパティ、JavaScriptイベントを指定していますが、レンダリングに関しては指定していません。

現在、PDFはデータとPDFフォームを統合するための2つの異なる方法をサポートしています:

- AcroForms（Acrobatフォームとも呼ばれます）、PDF 1.2フォーマット仕様に導入され、含まれています。
- Adobe XML Forms Architecture (XFA) フォーム、PDF 1.5フォーマット仕様でオプション機能として導入されました（XFA仕様はPDF仕様に含まれておらず、参照されるのみです）。

XFAフォームのページを抽出または操作することはできません。なぜなら、フォームのコンテンツは実行時に（XFAフォームの表示中に）XFAフォームを表示またはレンダリングしようとするアプリケーション内で生成されるからです。 Aspose.PDFには、開発者がXFAフォームを標準のAcroFormsに変換する機能があります。

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // XFAフォームを読み込む
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // フォームフィールドタイプを標準のAcroFormに設定する
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // 結果のPDFを保存する
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## XFAフィールドプロパティを取得する

フィールドプロパティにアクセスするには、まずDocument.Form.XFA.Teamplateを使用してフィールドテンプレートにアクセスします。次のコードスニペットは、XFAフォームフィールドのXおよびY座標を取得する手順を示しています。

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // XFAフォームを読み込む
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // フィールド値を設定する
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // フィールドの位置を取得する
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // フィールドの位置を取得する
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // 更新されたドキュメントを保存する
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```