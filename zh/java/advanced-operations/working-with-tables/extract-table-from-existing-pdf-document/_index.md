---
title: 在 Java 中从 PDF 提取表格
linktitle: 提取表格
type: docs
weight: 20
url: /zh/java/extracting-table/
description: 了解如何在 Java 中从现有 PDF 文档中提取表格数据。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从 PDF 文件中提取表格数据
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 从 PDF 文档中提取表格。它展示了如何使用 TableAbsorber 按页检测表格，遍历行和单元格，并收集单元格文本以进行后续处理。
aliases:
    - "/zh/java/extract-table-from-existing-pdf-document/"
---
当需要检测现有 PDF 中的表格结构并读取其内容时，使用 `TableAbsorber`。

## 提取检测到的表格文本

当您需要在每页定位表格并收集其单元格文本时，请使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 使用...访问每页 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)。
1. 遍历已吸收的表格、行和单元格，然后输出提取的文本。

```java
public static void extract(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);
            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table ----");
                for (AbsorbedRow row : table.getRowList()) {
                    System.out.println("Row:");
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            for (TextSegment segment : fragment.getSegments()) {
                                cellText.append(segment.getText());
                            }
                        }
                        rowText.append(" | ").append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```
