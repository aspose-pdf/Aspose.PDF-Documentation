---
title: 操作现有 PDF 文档中的表格
linktitle: 操作表格
type: docs
weight: 40
url: /java/manipulating-tables/
description: 了解如何使用 Java 检查和修改现有 PDF 文档中的表格。
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 检查和修改现有 PDF 表格
Abstract: 本文介绍如何使用 Aspose.PDF for Java 操作 PDF 文档中已有的表格。它涵盖使用 TableAbsorber 定位表、更新单元格内的文本以及用新的 Table 对象替换检测到的表。
---
当您需要查找现有表并更新其内容时，请使用`TableAbsorber`。

## 替换表格单元格内的文本

当应更新检测到的单元格中的文本而不重建整个表格时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并使用 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 访问页面。
1. 验证目标表和单元格文本片段是否存在。
1. 替换单元格文本并保存更新的文档。

```java
public static void replaceCells(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }
        if (absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0).getTextFragments().size() == 0) {
            throw new IllegalStateException("The target cell has no text fragments.");
        }

        absorber.getTableList().get(0).getRowList().get(0).getCellList().get(0)
                .getTextFragments().get_Item(1).setText("New Value");
        document.save(outputFile.toString());
    }
}
```

## 用新表替换检测到的表

当原始表应完全替换为新建表时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并检测页面上的表格。
1. 使用所需的结构创建一个新的[表](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 替换吸收的表格并保存输出 PDF。

```java
public static void replaceTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        if (absorber.getTableList().isEmpty()) {
            throw new IllegalStateException("No tables were found on page 1.");
        }

        AbsorbedTable oldTable = absorber.getTableList().get(0);
        Table newTable = new Table();
        newTable.setColumnWidths("100 100 100");
        newTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1.0f));

        Row row = newTable.getRows().add();
        row.getCells().add("Col 1");
        row.getCells().add("Col 2");
        row.getCells().add("Col 3");
        row = newTable.getRows().add();
        row.getCells().add("Col 12");
        row.getCells().add("Col 22");
        row.getCells().add("Col 32");

        absorber.replace(document.getPages().get_Item(1), oldTable, newTable);
        document.save(outputFile.toString());
    }
}
```
