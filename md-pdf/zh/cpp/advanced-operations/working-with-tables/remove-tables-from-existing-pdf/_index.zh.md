---
title: 从现有 PDF 中移除表格
linktitle: 移除表格
type: docs
weight: 50
url: /cpp/remove-tables-from-existing-pdf/
description: 本节介绍如何从 PDF 文档中移除表格。
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++ 允许您在从头生成 PDF 文档时插入和创建表格，或者您也可以在任何现有 PDF 文档中添加表格对象。但是，您可能需要[在现有 PDF 中操作表格](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/)，在这里您可以更新现有表格单元格中的内容。此外，您可能会遇到从现有 PDF 文档中移除表格对象的需求。

为了移除表格，我们需要使用 [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) 类来获取现有 PDF 中的表格，然后调用 'Remove' 方法。

## 从 PDF 文档中移除表格

我们添加了新功能，即。 [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) 到现有的 TableAbsorber 类中以从 PDF 文档中移除表格。一旦吸收器成功找到页面上的表格，它就能够将其移除。请查看以下代码片段，展示如何从 PDF 文档中移除表格：

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

    // 加载源 PDF 文档
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // 创建 TableAbsorber 对象以查找表格
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 使用吸收器访问第一页
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 获取页面上的第一个表格
    auto table = absorber->get_TableList()->idx_get(0);

    // 移除表格
    absorber->Remove(table);

    // 保存 PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## 从 PDF 文档中删除多个表格

有些任务将涉及在一个 PDF 文档中处理多个表格。您需要从中删除多个表格。要从 PDF 文档中删除多个表格，请使用以下代码片段：

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // 加载现有的 PDF 文档
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // 创建 TableAbsorber 对象以查找表格
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // 使用吸收器访问第一页
    absorber->Visit(document->get_Pages()->idx_get(1));

    // 获取表格集合的副本
    auto tables = absorber->get_TableList();

    // 遍历集合的副本并删除表格
    for(auto table : tables)
    absorber->Remove(table);

    // 保存文档
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

请注意，删除或替换表格会改变 TableList 集合。 因此，在循环中移除/替换表时，复制 TableList 集合是必不可少的。

{{% /alert %}}