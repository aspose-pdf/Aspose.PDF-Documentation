---
title: 使用 Java 基于区域的提取
linktitle: 基于区域的提取
type: docs
weight: 20
url: /java/region-based-extraction/
description: 了解如何使用 Aspose.PDF for Java 从特定页面区域提取文本或检查 PDF 文档中的段落几何形状。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 从矩形页面区域中提取文本

将`TextSearchOptions` 与`Rectangle` 一起使用可将提取限制到页面上的定义区域。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 以从选定的页面区域收集文本。
1. 为目标 [矩形](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 创建 [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) 并启用 `setLimitToPageBounds(true)`，以便提取保留在可见页面框内。
1. 将配置的搜索选项应用于吸收器并访问目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 将提取的文本缓冲区写入输出文件。

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## 提取带有几何信息的段落

使用 `ParagraphAbsorber` 检查截面矩形和段落多边形以及提取的文本。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建[ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/)并访问目标[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)以构建页面标记信息。
1. 读取第一个页面标记结果并迭代其部分和段落。
1. 收集每个截面矩形、段落多边形以及从​​其 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 行重建的段落文本。
1. 使用几何图形和提取的文本详细信息构建输出报告。
1. 将提取的详细信息写入输出文件。

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
