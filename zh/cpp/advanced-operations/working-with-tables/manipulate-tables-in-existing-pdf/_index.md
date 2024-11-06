---
title: 操作现有 PDF 中的表格
linktitle: 操作表格
type: docs
weight: 40
url: zh/cpp/manipulate-tables-in-existing-pdf/
description: 本节涵盖使用 Aspose.PDF for C++ 进行表格修改的各种方法
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 操作现有 PDF 中的表格

Aspose.PDF for C++ 允许您快速高效地处理表格，即从头创建表格或添加到现有的 PDF 文档中。

您还可以将表格与数据库 (DOM) 集成，以根据数据库内容创建动态表格。

[Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) 类允许您搜索和解析 PDF 文档页面上已存在的简单表格。以下代码片段展示了更新表格中特定单元格内容的步骤。

>Headers:

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

    // 加载现有的PDF文件
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // 创建TableAbsorber对象以查找表格
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 用吸收器访问第一页
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 访问页面上的第一个表格，它们的第一个单元格和其中的文本片段
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // 更改单元格中第一个文本片段的文本
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## 在PDF文档中用新表替换旧表

如果需要查找特定表格并将其替换为所需的表格，可以使用[TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table)类的Replace()方法来实现。

以下示例演示了替换 PDF 文档中表格的功能：

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // 加载现有的 PDF 文件
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // 创建 TableAbsorber 对象以查找表格
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 使用吸收器访问第一页
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 获取页面上的第一个表格
    auto table = absorber->get_TableList()->idx_get(0);

    // 创建新表格
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Col 1");
    row->get_Cells()->Add(u"Col 2");
    row->get_Cells()->Add(u"Col 3");

    // 用新表替换旧表
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // 保存文档
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```