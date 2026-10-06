---
title: 在现有 PDF 文档中操作表格
linktitle: 操作表格
type: docs
weight: 40
url: /zh/java/manipulating-tables/
description: 学习如何使用 Java 检查并修改现有 PDF 文档中的表格。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 检查和修改现有 PDF 表格
Abstract: 本文说明了如何使用 Aspose.PDF for Java 操作 PDF 文档中已存在的表格。内容包括使用 TableAbsorber 定位表格、更新单元格内的文本，以及用新的 Table 对象替换检测到的表格。
aliases:
    - "/zh/java/manipulate-tables-in-existing-pdf/"
---
当需要定位现有表并更新其内容时，使用 `TableAbsorber`。

## 替换表格单元格中的文本

当需要在检测到的单元格中更新文本而无需重新构建整个表格时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并访问包含 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)。
1. 验证目标表格和单元格文本片段是否存在。
1. 替换单元格文本并保存更新后的文档。

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

## 用新表替换检测到的表格

当原始表格应完全被新构建的表格替换时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并在页面上检测表格。
1. 创建一个新 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 使用所需的结构。
1. 替换已吸收的表格并保存输出的 PDF。

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
