---
title: 使用 Java 提取 PDF 表格中的数据
linktitle: 提取表格数据
type: docs
weight: 40
url: /zh/java/extract-data-from-table-in-pdf/
description: 学习如何使用 Aspose.PDF for Java 从 PDF 文件中提取表格数据，并导出检测到的表格以进行进一步处理。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Java 在 PDF 中提取表格数据
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 从 PDF 文档中提取和处理表格数据。它展示了如何使用 `TableAbsorber` 扫描页面，读取检测到的表格中的行和单元格，将提取限制在特定的标注区域，并将结果导出为 Excel。
---
## 从 PDF 中提取表格

使用 `TableAbsorber` 在每页上查找表格并遍历行、单元格、文本片段和文本段。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 遍历文档 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 对象，因为表格是逐页检测的。
1. 创建一个 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 对每页进行调用 `visit(page)` 填充检测到的表格列表。
1. 遍历检测到的 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/), [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/), [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/), [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)，以及 `TextSegment` 对象。
1. 从片段内容构建提取的行文本并打印表格数据。

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

## 从特定标记区域提取表格

此示例查找方形注释，将其矩形与每个检测到的表格进行比较，并仅输出位于标记区域内的表格。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 获取目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 并定位方框 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 标记提取区域的。
1. 创建一个 [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber/) 并调用 `visit(page)` 检测该页上的表格。
1. 比较每个检测到的 [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedtable/) [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 与注释矩形的边界。
1. 遍历匹配的 [AbsorbedRow](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedrow/) 和 [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/absorbedcell/) 对象并重建行文本。
1. 仅打印标记区域的表格数据。

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

## 将表导出到 Excel

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建 [ExcelSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/excelsaveoptions/) 用于导出。
1. 将 Excel 输出格式设置为 `XLSX` 因此检测到的表布局被写入为 Excel 工作簿。
1. 呼叫 `document.save(outputFile.toString(), excelSave)` 将文档导出为 Excel 格式。

```java
public static void exportTablesToExcel(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ExcelSaveOptions excelSave = new ExcelSaveOptions();
        excelSave.setFormat(ExcelSaveOptions.ExcelFormat.XLSX);
        document.save(outputFile.toString(), excelSave);
    }
}
```
