---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: ja/cpp/posting-acroform-data/
description: Aspose.PDF for C++ の Aspose.Pdf.Facades 名前空間を使用して、フォームデータを XML ファイルにインポートおよびエクスポートできます。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm は PDF ドキュメントの重要なタイプです。  [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades)を使用してAcroFormを作成および編集するだけでなく、フォームデータをXMLファイルにインポートおよびエクスポートすることもできます。Aspose.PDF for C++のAspose.Pdf.Facades namespaceでは、AcroFormの別の機能を実装することができ、AcroFormデータを外部のウェブページに投稿することができます。このウェブページは、その後、投稿された変数を読み取り、このデータをさらに処理するために使用します。この機能は、データをPDFファイルに保持するだけでなく、サーバーに送信してデータベースなどに保存したい場合に便利です。

{{% /alert %}}

## 実装の詳細

この記事では、[Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades)と[FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/)クラスを使用してAcroFormを作成しようとしました。また、送信ボタンを追加し、そのターゲットURLを設定しました。

以下のコードスニペットは、フォームを作成し、その後ウェブページで投稿されたデータを受け取る方法を示しています。
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // FormEditorクラスのインスタンスを作成し、入力および出力PDFファイルをバインドする
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // AcroFormフィールドを作成 - 簡潔さのために2つのフィールドのみ作成しました
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // 送信ボタンを追加し、ターゲットURLを設定
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // 出力PDFファイルを保存
    editor->Save();
}
```