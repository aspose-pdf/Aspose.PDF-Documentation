---
title: 在 Java 中将 PDF 表格与数据源集成
linktitle: 集成表格
type: docs
weight: 30
url: /zh/java/integrate-table/
description: 了解如何在 Java 中将 PDF 表格与结构化数据源（如 CSV 文件）集成。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 从结构化数据构建 PDF 表格
Abstract: 本文解释了如何使用 Aspose.PDF for Java 将 PDF 表格与外部数据集成。它涵盖了读取 CSV 数据、选择特定列、从解析的行构建样式化的 Table 对象，并将结果渲染到 PDF 文档中。
---
该 Java 示例在不依赖外部 dataframe 库的情况下，从 CSV 数据构建 PDF 表格。

## 从 CSV 行构建表格

当需要将选定的 CSV 列转换为样式化的 PDF 表格时，请使用此示例。

1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置其边框。
1. 从 CSV 标题行中检测所需的列索引。
1. 添加标题行和请求的指定数量的数据行，然后返回表格。

```java
public static Table createTableFromCsv(List<String[]> rows, int maxRows) {
    Table table = new Table();
    table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getLightGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Bottom, 1, Color.getLightGray()));

    String[] header = rows.get(0);
    int[] selectedColumns = findColumns(header, "city", "country", "population", "iso3");

    Row headerRow = table.getRows().add();
    headerRow.setRowBroken(false);
    for (int columnIndex : selectedColumns) {
        Cell cell = headerRow.getCells().add(header[columnIndex]);
        cell.setBackgroundColor(Color.getLightGray());
    }

    int limit = Math.min(maxRows, rows.size() - 1);
    for (int rowIndex = 1; rowIndex <= limit; rowIndex++) {
        Row row = table.getRows().add();
        String[] rowData = rows.get(rowIndex);
        for (int columnIndex : selectedColumns) {
            row.getCells().add(columnIndex < rowData.length ? rowData[columnIndex] : "");
        }
    }

    return table;
}
```

## 从 CSV 数据创建 PDF

当 CSV 输入应渲染为 PDF 表格文档时使用此示例。

1. 从输入文件中读取 CSV 行。
1. 在控制台预览解析后的一部分行。
1. 创建 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)，添加生成的表格，并保存输出文件。

```java
public static void createPdfFromCsv(Path inputFile, Path outputFile, int maxRows) throws Exception {
    List<String[]> rows = readCsv(inputFile);
    for (int i = 0; i < Math.min(20, rows.size()); i++) {
        System.out.println(String.join(" | ", rows.get(i)));
    }

    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(createTableFromCsv(rows, maxRows));
        document.save(outputFile.toString());
    }
}
```

## 按名称查找 CSV 列索引

当必须在 CSV 表头行中定位特定命名列时，请使用此辅助函数。

1. 遍历请求的列名。
1. 在表头行中搜索匹配的索引。
1. 返回收集的列位置。

```java
private static int[] findColumns(String[] header, String... names) {
    int[] indexes = new int[names.length];
    for (int i = 0; i < names.length; i++) {
        indexes[i] = 0;
        for (int j = 0; j < header.length; j++) {
            if (names[i].equals(header[j])) {
                indexes[i] = j;
                break;
            }
        }
    }
    return indexes;
}
```

## 从文件读取 CSV 行

当 CSV 源在生成表之前需要加载到内存中时，请使用此辅助工具。

1. 读取输入文件的所有行。
1. 使用 CSV 解析器帮助程序拆分每一行。
1. 返回收集的行值。

```java
private static List<String[]> readCsv(Path inputFile) throws Exception {
    List<String[]> rows = new ArrayList<>();
    for (String line : Files.readAllLines(inputFile)) {
        rows.add(splitCsvLine(line));
    }
    return rows;
}
```

## 将一行 CSV 拆分为值

当 CSV 行可能包含带引号的值和转义的引号字符时，请使用此辅助函数。

1. 遍历行中的字符。
1. 跟踪解析器当前是否位于引号文本内部。
1. 构建最终的值列表并将其作为数组返回。

```java
private static String[] splitCsvLine(String line) {
    List<String> values = new ArrayList<>();
    StringBuilder current = new StringBuilder();
    boolean inQuotes = false;
    for (int i = 0; i < line.length(); i++) {
        char ch = line.charAt(i);
        if (ch == '"') {
            if (inQuotes && i + 1 < line.length() && line.charAt(i + 1) == '"') {
                current.append('"');
                i++;
            } else {
                inQuotes = !inQuotes;
            }
        } else if (ch == ',' && !inQuotes) {
            values.add(current.toString());
            current.setLength(0);
        } else {
            current.append(ch);
        }
    }
    values.add(current.toString());
    return values.toArray(String[]::new);
}
```
