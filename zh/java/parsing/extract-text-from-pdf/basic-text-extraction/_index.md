---
title: 使用 Java 的基本文本提取
linktitle: 基本文本提取
type: docs
weight: 10
url: /zh/java/basic-text-extraction/
description: 了解如何使用 Aspose.PDF 在 Java 中从 PDF 文档中提取文本，可从所有页面、特定页面或按段落结构提取。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
基本文本提取是 Java 中读取 PDF 内容的起点。Aspose.PDF 提供了两种常见方法：

- 当需要从文档或页面获取纯文本结果时，使用 `TextAbsorber`。
- 当需要保留页面、章节、段落、行以及片段的分组时，使用 `ParagraphAbsorber`。

PDF 页面不像文字处理文档那样存储文本，因此提取的顺序取决于页面内容流和布局。若需进行区域特定的提取、几何细节、多列布局、注释、高亮文本或上标和下标检测，请使用本节中的相关提取文章。

## 从所有页面提取文本

使用 `TextAbsorber` 从整个文档收集平面文本流并将其写入文件。当您只需要可读的文本内容且不需要段落边界或坐标时，这是最简单的选项。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 以在整个文档中累积文本。
1. 调用 `document.getPages().accept(textAbsorber)` 所以每个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 被吸收器访问。
1. 将提取的文本缓冲区写入输出文件。

```java
public static void extractTextFromAllPages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 从特定页面提取文本

仅将吸收器应用于您需要的页面。页面编号在 `Document` 页面集合是从 1 开始计数的，所以 `get_Item(1)` 读取第一页。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 用于单页提取。
1. 调用 `accept(textAbsorber)` 在目标上 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 按页码选择。
1. 将提取的文本缓冲区写入输出文件。

```java
public static void extractTextFromPage(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        document.getPages().get_Item(pageNumber).accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```

## 按段落结构提取文本

当需要结构分组而不是单个纯文本流时，使用 `ParagraphAbsorber`。它返回包含章节、段落、行和 `TextFragment` 对象的页面标记，这在输出必须保留逻辑文本块时很有用。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例打开源 PDF。
1. 创建一个 [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) 并访问整个文档以构建页面标记结果。
1. 遍历页面标记、章节、段落、行和 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 吸收器公开的对象。
1. 构建输出文本时使用明确的页面、章节和段落编号，以保留结构分组。
1. 将提取的段落文本写入输出文件。

```java
public static void extractParagraphsFromPdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document);

        StringBuilder text = new StringBuilder();
        for (PageMarkup pageMarkup : absorber.getPageMarkups()) {
            int sectionIndex = 1;
            for (MarkupSection section : pageMarkup.getSections()) {
                int paragraphIndex = 1;
                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();
                    for (List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    text.append("Page ").append(pageMarkup.getNumber())
                            .append(", Section ").append(sectionIndex)
                            .append(", Paragraph ").append(paragraphIndex)
                            .append(":\n");
                    text.append(paragraphText).append("\n");
                    paragraphIndex++;
                }
                sectionIndex++;
            }
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
