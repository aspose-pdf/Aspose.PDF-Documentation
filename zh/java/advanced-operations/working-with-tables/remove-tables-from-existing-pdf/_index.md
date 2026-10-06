---
title: 从现有 PDF 文档中移除表格
linktitle: 移除表格
description: 了解如何在 Java 中从现有 PDF 文档中移除一个或多个表格。
lastmod: "2026-10-06"
type: docs
weight: 50
url: /zh/java/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 删除 PDF 文件中的一个或多个表格
Abstract: 本文解释了如何使用 Aspose.PDF for Java 从现有 PDF 文档中移除表格。它介绍了用于定位表格的 TableAbsorber，并演示了如何删除单个表格或从页面中移除所有检测到的表格。
aliases:
    - "/zh/java/remove-tables-from-existing-pdf/"
---
当需要从现有 PDF 中删除一个或多个检测到的表格时，使用 `TableAbsorber`。

## 删除一个检测到的表格

仅在页面上应删除第一个匹配的表格时使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用以下方式访问目标页面 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)。
1. 删除检测到的第一个表格并保存文档。

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

当页面上的每个匹配的表格都应被删除时使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用以下方式访问目标页面 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 并将检测到的表格复制到列表中。
1. 删除每个检测到的表格并保存更新后的 PDF。

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
