---
title: 创建复杂的 PDF
linktitle: 创建复杂的 PDF
type: docs
weight: 30
url: /java/complex-pdf-example/
description: Aspose.PDF for Java 允许您创建更复杂的 PDF 文档，其中在一个文件中包含图像、文本片段和表格。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 创建复杂的 PDF
Abstract: 本文介绍如何使用 Aspose.PDF 在 Java 中创建更复杂的 PDF。该示例添加图像、格式化标题、描述性文本块以及带有样式标题单元格和生成的明细表行的表格，然后将结果保存为 PDF 文档。
---
[Hello World](/pdf/java/hello-world-example/) 示例涵盖了最简单的 PDF 创建路径。此示例建立在该工作流程的基础上，创建了一个结合了图形、文本和表格内容的更丰富的文档。

要使用 Java 创建更复杂的 PDF 文档：

1. 创建[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)并添加[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 使用`page.addImage(...)` 和目标[矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 将图像添加到[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 创建标题 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 并设置其字体、大小、对齐方式和 [位置](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/)。
1. 为描述段落创建第二个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)。
1. 构建一个带有边框、填充和标题样式的[表格](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 将生成的计划行添加到[表](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 将[表](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 附加到[页](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 段落。
1. 保存输出 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

以下Java代码基于`GetStartedExamples.java`。

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

同一个示例使用辅助方法来准备带有标题格式和生成的出发时间的时间表：

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```
