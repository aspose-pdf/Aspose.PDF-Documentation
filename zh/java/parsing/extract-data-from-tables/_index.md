---
title: 使用 Java 从 PDF 表格中提取数据
linktitle: 从表中提取数据
type: docs
weight: 40
url: /java/extract-data-from-table-in-pdf/
description: 了解如何使用 Aspose.PDF for Java 从 PDF 文件中提取表格数据并导出检测到的表格以进行进一步处理。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何通过Java从PDF表格中提取数据
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文档中提取和处理表​​格数据。它展示了如何使用`TableAbsorber`扫描页面，从检测到的表中读取行和单元格，将提取限制到特定的注释区域，以及将结果导出到Excel。
---
## 从 PDF 中提取表格

使用`TableAbsorber` 查找每个页面上的表格并迭代行、单元格、文本片段和文本段。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 迭代文档 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 对象，因为表是逐页检测的。
1. 为每个页面创建一个[TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/)，并调用`visit(page)`来填充检测到的表列表。
1. 迭代检测到的 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/)、[AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/)、[AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/)、[TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 和 `TextSegment` 对象。
1. 从片段内容构建提取的行文本并打印表数据。

```java
public static void extractTablesFromPdf(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            TableAbsorber absorber = new TableAbsorber();
            absorber.visit(page);

            for (AbsorbedTable table : absorber.getTableList()) {
                System.out.println("Table");
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## 从特定标记区域中提取表格

此示例找到一个方形注释，将其矩形与每个检测到的表格进行比较，并仅输出标记区域内的表格。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 获取目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)并找到标记提取区域的正方形[注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/)。
1. 创建一个 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 并调用 `visit(page)` 来检测该页面上的表。
1. 将每个检测到的 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 与注释矩形边界进行比较。
1. 迭代匹配的 [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) 和 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) 对象并重建行文本。
1. 仅打印标记区域的表数据。

```java
public static void extractTableFromSpecificArea(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Annotation squareAnnotation = null;
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                squareAnnotation = annotation;
                break;
            }
        }

        if (squareAnnotation == null) {
            System.out.println("No square annotation found.");
            return;
        }

        TableAbsorber absorber = new TableAbsorber();
        absorber.visit(page);

        for (AbsorbedTable table : absorber.getTableList()) {
            Rectangle tableRect = table.getRectangle();
            Rectangle annotationRect = squareAnnotation.getRect();

            boolean isInRegion = annotationRect.getLLX() < tableRect.getLLX()
                    && annotationRect.getLLY() < tableRect.getLLY()
                    && annotationRect.getURX() > tableRect.getURX()
                    && annotationRect.getURY() > tableRect.getURY();

            if (isInRegion) {
                for (AbsorbedRow row : table.getRowList()) {
                    StringBuilder rowText = new StringBuilder();
                    for (AbsorbedCell cell : row.getCellList()) {
                        if (rowText.length() > 0) {
                            rowText.append("|");
                        }
                        StringBuilder cellText = new StringBuilder();
                        for (TextFragment fragment : cell.getTextFragments()) {
                            StringBuilder fragmentText = new StringBuilder();
                            for (TextSegment segment : fragment.getSegments()) {
                                fragmentText.append(segment.getText());
                            }
                            if (cellText.length() > 0) {
                                cellText.append("|");
                            }
                            cellText.append(fragmentText);
                        }
                        rowText.append(cellText);
                    }
                    System.out.println(rowText);
                }
            }
        }
    }
}
```

## 将表格导出到 Excel

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 用于导出。
1. 将 Excel 输出格式设置为`XLSX`，以便将检测到的表布局写入 Excel 工作簿。
1. 调用`document.save(outputFile.toString(), excelSave)`将文档导出为Excel格式。

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
