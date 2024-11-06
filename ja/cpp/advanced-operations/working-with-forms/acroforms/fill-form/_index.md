---
title: フィルアクロフォーム
linktitle: フィルアクロフォーム
type: docs
weight: 20
url: ja/cpp/fill-form/
description: このセクションでは、Aspose.PDF for C++ を使用して PDF ドキュメントのフォームフィールドを記入する方法を説明します。
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF ドキュメントは、フォームを作成するための最良で、実際に好まれるファイルタイプです。

このトピックでは、Aspose.PDF for C++ を使用して PDF フォームを記入する方法を説明します。

Aspose.PDF for C++ を使用すると、フォームフィールドを記入し、Document オブジェクトの Form コレクションからフィールドを取得できます。

次の例を見て、このタスクを解決する方法を確認してください。

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // ドキュメントを開く
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // フィールドを取得
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // フィールド値を変更
    textBoxField->set_Value(u"フィールドに記入する値");

    // 更新されたドキュメントを保存
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```