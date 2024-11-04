---
title: 操作现有PDF中的表格
linktitle: 操作表格
type: docs
weight: 30
url: /java/manipulate-tables-in-existing-pdf/
description: 操作现有PDF文件中的表格，并使用Aspose.PDF for Java在PDF文档中用新表替换旧表。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 操作现有PDF中的表格

Aspose.PDF for Java 支持的最早功能之一就是处理表格的能力，它提供了在从头开始生成的PDF文件或任何现有PDF文件中添加表格的强大支持。
 你还可以将表格与数据库集成（DOM）来创建基于数据库内容的动态表格。在此新版本中，我们实现了搜索和解析PDF文档页面上已有简单表格的新功能。一个名为**Aspose.PDF.Text.TableAbsorber**的新类提供了这些功能。TableAbsorber的使用与现有的TextFragmentAbsorber类非常相似。

以下代码片段展示了更新特定表格单元格内容的步骤。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleManipulate {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ManipulateTables() {

        // 加载现有的PDF文件
        Document pdfDocument = new Document(_dataDir + "input.pdf");
        // 创建TableAbsorber对象以查找表格
        TableAbsorber absorber = new TableAbsorber();

        // 使用吸收器访问第一页
        absorber.visit(pdfDocument.getPages().get_Item(1));

        // 获取页面上第一个表格的访问权，它们的第一个单元格和其中的文本片段
        TextFragment fragment = absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1);

        // 更改单元格中第一个文本片段的文本
        fragment.setText("hi world");

        pdfDocument.save(_dataDir + "ManipulateTable_out.pdf");
    }
```

## 用新表替换PDF文档中的旧表

如果您需要找到特定的表并用所需的表替换它，可以使用 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber) 类的 Replace() 方法来实现。

以下示例演示了在PDF文档中替换表的功能：

```java
public static void ReplaceOldTableWithNew() {

        // 加载现有PDF文档
        Document pdfDocument = new Document(_dataDir + "Table_input2.pdf");

        // 创建TableAbsorber对象以查找表
        TableAbsorber absorber = new TableAbsorber();

        Page page = pdfDocument.getPages().get_Item(1);

        // 使用吸收器访问第一页
        absorber.visit(page);

        // 获取页面上的第一个表
        AbsorbedTable table = absorber.getTableList().get(0);

        // 创建新表
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder (new BorderInfo(BorderSide.All, 1F));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");

        // 用新表替换旧表
        absorber.replace(page, table, newTable);

        // 保存文档
        pdfDocument.save(_dataDir + "TableReplaced_out.pdf");
        
    }

}
```