---
title: 从现有 PDF 文档中删除表格
linktitle: 删除表格
description: 了解如何使用 Java 从现有 PDF 文档中删除一个或多个表格。
lastmod: "2026-06-09"
type: docs
weight: 50
url: /java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文件中删除一个或多个表格
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从现有 PDF 文档中删除表格。它介绍了用于定位表的TableAbsorber，并演示了如何删除单个表或从页面中删除所有检测到的表。
---
当您需要从现有 PDF 中删除一个或多个检测到的表格时，请使用`TableAbsorber`。

## 删除一张检测到的表

当仅应删除页面上第一个匹配的表时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)访问目标页面。
1. 删除第一个检测到的表格并保存文档。

```java
public static void removeOneTable(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        absorber.remove(absorber.getTableList().get(0));
        document.save(outputFile.toString());
    }
}
```

## 从页面中删除所有检测到的表格

当页面上的每个匹配表都应被删除时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 访问目标页面并将检测到的表复制到列表中。
1. 删除每个检测到的表格并保存更新的 PDF。

```java
public static void removeAllTables(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        List<AbsorbedTable> tables = new ArrayList<>(absorber.getTableList());
        for (AbsorbedTable table : tables) {
            absorber.remove(table);
        }
        document.save(outputFile.toString());
    }
}
```
