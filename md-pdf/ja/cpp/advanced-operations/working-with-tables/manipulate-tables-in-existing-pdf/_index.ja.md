---
title: 既存のPDFでテーブルを操作する
linktitle: テーブルを操作する
type: docs
weight: 40
url: /cpp/manipulate-tables-in-existing-pdf/
description: このセクションでは、Aspose.PDF for C++を使用したテーブルの修正方法について説明します
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 既存のPDFでテーブルを操作する

Aspose.PDF for C++を使用すると、テーブルを迅速かつ効率的に操作できます。具体的には、ゼロから作成するか、既存のPDFドキュメントに追加することができます。

また、データベース（DOM）とテーブルを統合して、データベースの内容に基づいた動的なテーブルを作成することができます。

[Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table)クラスを使用すると、PDFドキュメントページ上に既に存在する簡単なテーブルを検索および解析することができます。以下のコードスニペットは、テーブル内の特定のセルの内容を更新する手順を示しています。

>ヘッダー:

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // 既存のPDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // テーブルを見つけるためにTableAbsorberオブジェクトを作成
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 吸収器で最初のページを訪問
    absorber->Visit(document->get_Pages()->idx_get(1));

    // ページ上の最初のテーブル、最初のセルおよびその中のテキストフラグメントにアクセス
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // セル内の最初のテキストフラグメントのテキストを変更
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## PDFドキュメント内の古いテーブルを新しいテーブルに置き換える

特定のテーブルを見つけて希望するテーブルに置き換える必要がある場合は、[TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) クラスのReplace()メソッドを使用してそれを行うことができます。

以下の例は、PDFドキュメント内のテーブルを置き換える機能を示しています:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // 既存のPDFファイルを読み込む
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // テーブルを見つけるためのTableAbsorberオブジェクトを作成
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 最初のページを訪問して吸収する
    absorber->Visit(document->get_Pages()->idx_get(1));

    // ページ上の最初のテーブルを取得
    auto table = absorber->get_TableList()->idx_get(0);

    // 新しいテーブルを作成
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // 新しいテーブルでテーブルを置き換える
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // ドキュメントを保存
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```