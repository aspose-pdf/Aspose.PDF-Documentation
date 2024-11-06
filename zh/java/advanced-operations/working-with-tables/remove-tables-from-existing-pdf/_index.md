---
title: 从现有PDF中移除表格
linktitle: 移除表格
type: docs
weight: 40
url: zh/java/remove-tables-from-existing-pdf/
description: Aspose.PDF for Java允许您从PDF文档中移除表格和多个表格。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

Aspose.PDF for Java提供了在生成PDF文档时插入/创建表格的功能，或者您可以在任何现有PDF文档中添加表格对象。然而，您可能有一个需求是[在现有PDF中操作表格](https://docs.aspose.com/pdf/java/manipulate-tables-in-existing-pdf/)，可以更新现有表格单元格中的内容。然而，您可能会遇到需要从现有PDF文档中移除表格对象的需求。

{{% /alert %}}

为了移除表格，我们需要使用[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber)类来获取现有PDF中的表格，然后调用[Remove](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#remove-com.aspose.pdf.AbsorbedTable-)方法。

## 从 PDF 文档中移除表格

我们在现有的 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) 类中添加了新的函数，即 Remove()，以便从 PDF 文档中移除表格。一旦吸收器成功地在页面上找到表格，它就能够移除它们。请查看以下代码片段，展示如何从 PDF 文档中移除表格：

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleRemoveTable {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void RemoveTable() {
        // 加载现有的 PDF 文档
        Document pdfDocument = new Document(_dataDir + "Table_input.pdf");

        // 创建 TableAbsorber 对象以查找表格
        TableAbsorber absorber = new TableAbsorber();

        // 使用吸收器访问第一页
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // 获取页面上的第一个表格
        AbsorbedTable table = absorber.getTableList().get(0);

        // 移除表格
        absorber.remove(table);

        // 保存 PDF
        pdfDocument.save(_dataDir + "Table_out.pdf");
    }  
```


## 从 PDF 文档中移除多个表格

有时候，一个 PDF 文档可能包含多个表格，您可能需要从中移除多个表格。为了从 PDF 文档中移除多个表格，请使用以下代码片段：

```java
    public static void RemoveMultipleTable() {
        // 加载现有的 PDF 文档
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // 创建 TableAbsorber 对象以查找表格
        TableAbsorber absorber = new TableAbsorber();

        // 使用吸收器访问第二页
        absorber.visit(pdfDocument.getPages().get_Item(2));

        // 循环遍历集合的副本并移除表格
        for (AbsorbedTable table : absorber.getTableList())
            absorber.remove(table);

        // 保存文档
        pdfDocument.save(_dataDir + "Table2_out.pdf");
    }
}
```