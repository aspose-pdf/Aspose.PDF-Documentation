---
title: 创建复杂的 PDF
linktitle: 创建复杂的 PDF
type: docs
weight: 30
url: /zh/java/complex-pdf-example/
description: Aspose.PDF for Java 允许您创建包含图像、文本片段和表格的更复杂的 PDF 文档，所有内容位于同一个文件中。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 创建复杂的 PDF
Abstract: 本文展示了如何使用 Aspose.PDF 在 Java 中创建更复杂的 PDF。示例添加了一张图像、一个格式化的标题、一个描述性文本块，以及一个具有样式化表头单元格和生成的计划行的表格，然后将结果保存为 PDF 文档。
---
该 [你好，世界](/pdf/zh/java/hello-world-example/) 示例概述了最简的 PDF 创建路径。此示例基于该工作流，创建一个更丰富的文档，结合了图形、文本和表格内容。

在 Java 中创建更复杂的 PDF 文档：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 调用 `page.addImage(...)`，将图像添加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 中的目标 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 区域。
1. 创建标题 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/)，并设置其字体、大小、对齐方式和 [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/)。
1. 创建第二个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 用于描述段落。
1. 构建一个带有边框、内边距和标题样式的 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 将生成的计划行添加到 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/)。
1. 将 [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) 追加到 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 段落。
1. 保存输出 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

以下 Java 代码基于 `GetStartedExamples.java`。

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

相同的示例使用一个辅助方法来准备包含标题格式和生成的出发时间的时间表：

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
