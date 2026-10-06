---
title: 在 Java 中向 PDF 添加表格
linktitle: 添加表格
type: docs
weight: 10
url: /zh/java/adding-tables/
description: 了解如何在 Java 中向现有的 PDF 文档添加和配置表格。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 添加并格式化 PDF 文档中的表格。
Abstract: 本文说明了如何使用 Aspose.PDF for Java 在 PDF 文档中添加和配置表格。它涵盖了表格创建、边框、边距、填充、行列跨越、AutoFit 行为、单元格中的图像插入、行列重复、HTML 和 LaTeX 片段以及多页渲染控制。
aliases:
    - "/zh/java/add-table-in-existing-pdf-document/"
---
Aspose.PDF for Java 提供了丰富的 `Table` 用于构建带有布局和内容自定义的表格的 API。

## 创建一个基本表格

当您需要添加一个具有统一边框和文本单元格的简易表格时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置其边框。
1. 添加行和单元格，将表格附加到页面，并保存文档。

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 5, Color.getLightGray()));
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 添加具有跨行和跨列的单元格

当表格需要跨行或跨列合并单元格时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并添加行。
1. 配置 `ColSpan` 和 `RowSpan` 在目标单元格上，然后保存 PDF。

```java
public static void addRowspanOrColspan(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));

        Row row1 = table.getRows().add();
        for (int cellCount = 1; cellCount < 5; cellCount++) {
            row1.getCells().add("Test 1" + cellCount);
        }

        Row row2 = table.getRows().add();
        row2.getCells().add("Test 2 1");
        Cell cell = row2.getCells().add("Test 2 2");
        cell.setColSpan(2);
        row2.getCells().add("Test 2 4");

        Row row3 = table.getRows().add();
        row3.getCells().add("Test 3 1");
        row3.getCells().add("Test 3 2");
        row3.getCells().add("Test 3 3");
        row3.getCells().add("Test 3 4");

        Row row4 = table.getRows().add();
        row4.getCells().add("Test 4 1");
        cell = row4.getCells().add("Test 4 2");
        cell.setRowSpan(2);
        row4.getCells().add("Test 4 3");
        row4.getCells().add("Test 4 4");

        Row row5 = table.getRows().add();
        row5.getCells().add("Test 5 1");
        row5.getCells().add("Test 5 3");
        row5.getCells().add("Test 5 4");

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 添加表格边框和单元格内边距

当您需要配置边框、填充和单元格换行行为时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置宽度、边框和填充。
1. 添加行并保存生成的文档。

```java
public static void addBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add();
        row1.getCells().get_Item(2).getParagraphs().add(new TextFragment("col3 with large text string"));
        row1.getCells().get_Item(2).setWordWrapped(false);

        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## 启用自动适配表格布局

当表格应自动调整以适应可用页面宽度时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并设置 `ColumnAdjustment.AutoFitToWindow`。
1. 添加示例行并保存 PDF。

```java
public static void autoFit(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        page.getParagraphs().add(table);
        table.setColumnWidths("50 50 50");
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToWindow);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.1f));
        table.setBorder(new BorderInfo(BorderSide.All, 1));
        table.setDefaultCellPadding(new MarginInfo(5, 5, 5, 5));

        Row row1 = table.getRows().add();
        row1.getCells().add("col1");
        row1.getCells().add("col2");
        row1.getCells().add("col3");
        Row row2 = table.getRows().add();
        row2.getCells().add("item1");
        row2.getCells().add("item2");
        row2.getCells().add("item3");
        document.save(outputFile.toString());
    }
}
```

## 在表格单元格中添加图像

当表格需要在其中一个单元格中显示光栅图像内容时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并添加一个包含文本和图像单元格的行。
1. 配置 [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 设置大小并保存文档。

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");

        Row row = table.getRows().add();
        row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
        Image image = new Image();
        image.setFile(imageFile.toString());
        image.setFixWidth(50);
        image.setFixHeight(50);
        row.getCells().add().getParagraphs().add(image);

        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 在表格单元格中添加 SVG 图像

在表格需要逐行渲染 SVG 文件时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并遍历 SVG 文件。
1. 为每个图像添加一行，配置 SVG [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/)，并保存 PDF。

```java
public static void addSvgImage(List<Path> imageFiles, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("200 100");
        for (Path imageFile : imageFiles) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment(imageFile.toString()));
            Image image = new Image();
            image.setFileType(ImageFileType.Svg);
            image.setFile(imageFile.toString());
            image.setFixWidth(50);
            image.setFixHeight(50);
            row.getCells().add().getParagraphs().add(image);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 向表格单元格添加 HTML 片段

当表格内容应包含内联 HTML 格式时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置边框。
1. 添加 [HtmlFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlfragment/) 将对象放入单元格并保存文档。

```java
public static void addHtmlFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <strong>(" + rowCount + ", 1)</strong>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='color:red'>(" + rowCount + ", 2)</span>"));
            row.getCells().add().getParagraphs().add(new HtmlFragment("Column <span style='text-decoration: underline'>(" + rowCount + ", 3)</span>"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 向表格单元格添加 LaTeX 片段

当表格内容需要渲染 TeX 或 LaTeX 表达式时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个带有边框的 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 添加 [TeXFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/texfragment/) 将对象放入单元格并保存输出文件。

```java
public static void addLatexFragments(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray()));
        for (int rowCount = 1; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\mathbf{(" + rowCount + ", 1)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\textcolor{red}{(" + rowCount + ", 2)}$"));
            row.getCells().add().getParagraphs().add(new TeXFragment("Column $\\underline{(" + rowCount + ", 3)}$"));
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 将表格强制放到新页面

在大型表格之后，如果第二个表格应在单独的页面上开始，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并配置页面设置。
1. 构建第一个大型 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并将其添加到页面。
1. 创建第二个表，设置 `InNewPage`，并保存文档。

```java
public static void addTableOnNewPage(Path outputFile) {
    try (Document document = new Document()) {
        document.getPageInfo().getMargin().setLeft(37);
        document.getPageInfo().getMargin().setRight(37);
        document.getPageInfo().getMargin().setTop(37);
        document.getPageInfo().getMargin().setBottom(37);
        document.getPageInfo().setLandscape(true);

        Page page = document.getPages().add();
        Table table = new Table();
        table.setColumnWidths("50 100");
        for (int i = 1; i < 121; i++) {
            Row row = table.getRows().add();
            row.setFixedRowHeight(15);
            row.getCells().add().getParagraphs().add(new TextFragment("Content 1"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 2"));
        }
        page.getParagraphs().add(table);

        Table table1 = new Table();
        table1.setColumnWidths("100 100");
        for (int i = 1; i < 11; i++) {
            Row row = table1.getRows().add();
            row.getCells().add().getParagraphs().add(new TextFragment("Content 3"));
            row.getCells().add().getParagraphs().add(new TextFragment("Content 4"));
        }
        table1.setInNewPage(true);
        page.getParagraphs().add(table1);
        document.save(outputFile.toString());
    }
}
```

## 构建一个垂直断裂且列重复的表格

当宽表需要纵向继续并重复关键列时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置垂直换行与重复列。
1. 添加标题行和数据行，然后保存文档。

```java
public static void addTableHideBorders(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All));
        table.setRepeatingColumnsCount(2);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        Cell cell = row.getCells().add("header 1");
        cell.setColSpan(2);
        cell.setBackgroundColor(Color.getLightGray());
        row.getCells().add("header 3");
        Cell cell2 = row.getCells().add("header 4");
        cell2.setColSpan(2);
        cell2.setBackgroundColor(Color.getLightBlue());
        row.getCells().add("header 6");
        Cell cell3 = row.getCells().add("header 7");
        cell3.setColSpan(2);
        cell3.setBackgroundColor(Color.getLightGreen());
        Cell cell4 = row.getCells().add("header 9");
        cell4.setColSpan(3);
        cell4.setBackgroundColor(Color.getLightCoral());
        for (int i = 12; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 0; rowCounter < 3; rowCounter++) {
            Row row1 = table.getRows().add();
            for (int i = 1; i < 18; i++) {
                row1.getCells().add("col " + rowCounter + ", " + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 复用边框和填充示例

当边距和填充场景应委托给共享的边框示例时，请使用此帮助程序。

1. 调用现有的表格边框和填充方法。
1. 在不重复代码的情况下复用相同的表格布局逻辑。

```java
public static void addMarginsOrPadding(Path outputFile) {
    addBorders(outputFile);
}
```

## 创建一个带圆角的表格

当表格应使用圆角样式而不是标准矩形边框时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置圆角边框设置。
1. 向表格中添加行并保存 PDF。

```java
public static void createTableWithRoundCorner(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        BorderInfo borderInfo = new BorderInfo(BorderSide.All);
        borderInfo.setRoundedBorderRadius(15);
        table.setCornerStyle(BorderCornerStyle.Round);
        table.setBorder(borderInfo);
        for (int rowCount = 0; rowCount < 10; rowCount++) {
            Row row = table.getRows().add();
            row.getCells().add("Column (" + rowCount + ", 1)");
            row.getCells().add("Column (" + rowCount + ", 2)");
            row.getCells().add("Column (" + rowCount + ", 3)");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 添加重复的标题行

当多页表格应在每个续页上重复其标题行时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个垂直断开的 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并配置重复行计数和样式。
1. 添加标题行和数据行，然后保存文档。

```java
public static void addRepeatingRows(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBroken(TableBroken.Vertical);
        table.setRepeatingRowsCount(2);
        TextState textState = new TextState();
        textState.setFontSize(12);
        textState.setFont(FontRepository.findFont("TimesNewRoman"));
        textState.setForegroundColor(Color.getRed());
        table.setRepeatingRowsStyle(textState);
        table.setColumnWidths("100 100 100");
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setBorder(new BorderInfo(BorderSide.All, 1, Color.getBlack()));

        Row headerRow1 = table.getRows().add();
        headerRow1.getCells().add("Header 1-1");
        headerRow1.getCells().add("Header 1-2");
        headerRow1.getCells().add("Header 1-3");
        for (Cell cell : headerRow1.getCells()) {
            cell.setBackgroundColor(Color.getLightGray());
        }
        Row headerRow2 = table.getRows().add();
        headerRow2.getCells().add("Header 2-1");
        headerRow2.getCells().add("Header 2-2");
        headerRow2.getCells().add("Header 2-3");
        for (Cell cell : headerRow2.getCells()) {
            cell.setBackgroundColor(Color.getLightBlue());
        }
        for (int i = 1; i < 101; i++) {
            Row row = table.getRows().add();
            row.getCells().add("Data " + i + "-1");
            row.getCells().add("Data " + i + "-2");
            row.getCells().add("Data " + i + "-3");
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 在宽表中添加重复列

当第一列需要重复且表格在同一页面上垂直换行时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并配置页面大小。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并设置重复列以及自动适应行为。
1. 添加标题行和数据行，然后保存 PDF。

```java
public static void addRepeatingColumns(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(PageSize.getA5().getHeight(), PageSize.getA5().getWidth());
        BorderInfo border = new BorderInfo(BorderSide.All, 0.5f, Color.getLightGray());
        Table table = new Table();
        table.setBroken(TableBroken.VerticalInSamePage);
        table.setColumnAdjustment(ColumnAdjustment.AutoFitToContent);
        table.setRepeatingColumnsCount(5);
        table.setBorder(border);
        table.setDefaultCellBorder(border);
        page.getParagraphs().add(table);

        Row row = table.getRows().add();
        for (int i = 1; i < 6; i++) {
            Cell cell = row.getCells().add("header " + i);
            cell.setBackgroundColor(Color.getLightGray());
        }
        for (int i = 6; i < 18; i++) {
            row.getCells().add("header " + i);
        }

        for (int rowCounter = 1; rowCounter < 6; rowCounter++) {
            row = table.getRows().add();
            for (int i = 1; i < 6; i++) {
                Cell cell = row.getCells().add("cell " + rowCounter + "," + i);
                cell.setBackgroundColor(Color.getLightGray());
            }
            for (int i = 6; i < 18; i++) {
                row.getCells().add("cell " + rowCounter + "," + i);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 在表格行之间插入分页符

当特定表格行应在新页面开始时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并填充多行。
1. 用...标记选定的行 `InNewPage` 并保存文档。

```java
public static void insertPageBreak(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, Color.getRed()));
        table.setColumnWidths("100 100");
        for (int counter = 0; counter < 201; counter++) {
            Row row = new Row();
            table.getRows().add(row);
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 0"));
            row.getCells().add().getParagraphs().add(new TextFragment("Cell " + counter + ", 1"));
            if (counter % 10 == 0 && counter != 0) {
                row.setInNewPage(true);
            }
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```

## 在表格单元格中旋转文本

当单元格文本需要以不同的旋转角度显示时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个页面。
1. 创建一个 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 并添加一行包含多个单元格。
1. 创建已旋转 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 对象，将它们添加到单元格中，然后保存 PDF。

```java
public static void rotatedTextTable(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Table table = new Table();
        table.setBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5f, Color.getBlack()));
        Row row = table.getRows().add();
        row.setMinRowHeight(200);
        for (int cellCount = 0; cellCount < 4; cellCount++) {
            Cell cell = row.getCells().add();
            TextFragment textFragment = new TextFragment("Cell 1 " + (cellCount - 1));
            textFragment.getTextState().setRotation(90 * cellCount);
            textFragment.setHorizontalAlignment(HorizontalAlignment.Center);
            cell.getParagraphs().add(textFragment);
        }
        page.getParagraphs().add(table);
        document.save(outputFile.toString());
    }
}
```
