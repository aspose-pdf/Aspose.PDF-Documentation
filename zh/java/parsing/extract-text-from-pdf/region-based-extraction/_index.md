---
title: 使用 Java 的基于区域的提取
linktitle: 基于区域的提取
type: docs
weight: 20
url: /zh/java/region-based-extraction/
description: 了解如何使用 Aspose.PDF for Java 从 PDF 文档的特定页面区域提取文本或检查段落几何形状。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 从矩形页面区域提取文本

使用 `TextSearchOptions` 带有一个 `Rectangle` 将提取限制在页面的指定区域。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 用于从选定的页面区域收集文本。
1. 创建 [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) 针对目标 [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 并启用 `setLimitToPageBounds(true)` 因此，提取保持在可见页面框内。
1. 将配置好的搜索选项应用于吸收器并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
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

使用 `ParagraphAbsorber` 检查节矩形和段落多边形以及提取的文本。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建一个 [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) 并访问目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 以构建页面标记信息。
1. 读取第一个页面标记结果并遍历其章节和段落。
1. 收集每个章节矩形、段落多边形，以及从中重建的段落文本。 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 行。
1. 构建带有几何和提取文本详细信息的输出报告。
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
