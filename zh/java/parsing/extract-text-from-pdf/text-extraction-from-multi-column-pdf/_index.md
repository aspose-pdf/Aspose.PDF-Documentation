---
title: 改进多列 PDF 中的文本提取
linktitle: 从多列 PDF 中提取文本
type: docs
weight: 30
url: /java/text-extraction-from-multi-column-pdf/
description: 了解使用 Aspose.PDF for Java 改进多列 PDF 布局文本提取的技术。
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
多列布局通常需要额外的处理来提高阅读顺序和提取质量。

## 缩小字体大小后提取文本

该技术更新文本片段字体大小，将调整后的文档保存到内存中，然后从转换后的结果中提取文本。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建一个 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) 并访问所有文档页面以收集 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) 对象。
1. 迭代片段并按请求的比例减小每个字体大小，以便在提取之前可以对密集的列布局进行标准化。
1. 将调整后的[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)保存到内存字节流中。
1. 从该内存缓冲区重新打开第二个[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/)，访问转换后文档的所有页面，并将提取的文本写入输出文件。

```java
public static void extractTextReduceFont(Path inputFile, Path outputFile, double reduceRatio) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber fragmentAbsorber = new TextFragmentAbsorber();
        document.getPages().accept(fragmentAbsorber);
        for (TextFragment fragment : fragmentAbsorber.getTextFragments()) {
            fragment.getTextState().setFontSize((float) (fragment.getTextState().getFontSize() * reduceRatio));
        }

        ByteArrayOutputStream stream = new ByteArrayOutputStream();
        document.save(stream);
        try (Document document2 = new Document(new ByteArrayInputStream(stream.toByteArray()))) {
            TextAbsorber textAbsorber = new TextAbsorber();
            document2.getPages().accept(textAbsorber);
            Files.writeString(outputFile, textAbsorber.getText());
        }
    }
}
```

## 使用比例因子提取文本

在纯格式化模式下使用 `TextExtractionOptions` 并调整列布局的比例因子。

1. 在 [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例中打开源 PDF。
1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) 用于完整文档提取。
1. 在纯格式模式下创建 [TextExtractionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textextractionoptions/)，以便使用布局敏感的提取行为。
1. 在访问页面之前，设置比例因子并将提取选项应用到吸收器。
1. 访问所有文档页面并将提取的文本写入输出文件。

```java
public static void extractTextScaleFactor(Path inputFile, Path outputFile, double scaleFactor) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber textAbsorber = new TextAbsorber();
        TextExtractionOptions extractionOptions =
                new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        extractionOptions.setScaleFactor(scaleFactor);
        textAbsorber.setExtractionOptions(extractionOptions);
        document.getPages().accept(textAbsorber);
        Files.writeString(outputFile, textAbsorber.getText());
    }
}
```
