---
title: 既存のPDFからテーブルを削除
linktitle: テーブルを削除
type: docs
weight: 50
url: /ja/cpp/remove-tables-from-existing-pdf/
description: このセクションでは、PDFドキュメントからテーブルを削除する方法について説明します。
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++を使用すると、ゼロから生成されているPDFドキュメント内にテーブルを挿入および作成することができます。また、既存のPDFドキュメントにもテーブルオブジェクトを追加することができます。しかし、既存のPDFで[テーブルを操作する](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/)必要がある場合、既存のテーブルセルの内容を更新できます。また、既存のPDFドキュメントからテーブルオブジェクトを削除する必要があるかもしれません。

テーブルを削除するために、既存のPDF内のテーブルを取得するために[TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table)クラスを使用し、その後に'Remove'メソッドを呼び出す必要があります。

## PDFドキュメントからテーブルを削除

新しい関数を追加しました。すなわち、 [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) 既存のTableAbsorberクラスに、PDFドキュメントからテーブルを削除するために追加します。吸収器がページ上のテーブルを正常に見つけると、それらを削除することが可能になります。以下のコードスニペットを確認して、PDFドキュメントからテーブルを削除する方法を示しています:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // ソースPDFドキュメントをロード
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // テーブルを見つけるためにTableAbsorberオブジェクトを作成
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 吸収器で最初のページを訪問
    absorber->Visit(document->get_Pages()->idx_get(1));

    // ページ上の最初のテーブルを取得
    auto table = absorber->get_TableList()->idx_get(0);

    // テーブルを削除
    absorber->Remove(table);

    // PDFを保存
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## PDFドキュメントから複数のテーブルを削除する

いくつかのタスクは、1つのPDFドキュメントに複数のテーブルを含む作業に関連します。
そして、そこからいくつかのテーブルを削除する必要があります。PDFドキュメントから複数のテーブルを削除するには、次のコードスニペットを使用します:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // 既存のPDFドキュメントをロード
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // テーブルを見つけるためのTableAbsorberオブジェクトを作成
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // アブソーバーで最初のページを訪問
    absorber->Visit(document->get_Pages()->idx_get(1));

    // テーブルコレクションのコピーを取得
    auto tables = absorber->get_TableList();


    // コレクションのコピーをループし、テーブルを削除
    for(auto table : tables)
    absorber->Remove(table);

    // ドキュメントを保存
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

テーブルを削除または置き換えると、TableListコレクションが変更されることを考慮してください。 Therefore, in case removing/replacing tables in a loop the copying of TableList collection is essential.

したがって、ループ内でテーブルを削除/置換する場合、TableList コレクションのコピーが不可欠です。

{{% /alert %}}