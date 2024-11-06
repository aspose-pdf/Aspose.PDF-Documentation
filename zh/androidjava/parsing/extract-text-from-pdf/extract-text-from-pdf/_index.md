---
title: 从PDF文件提取原始文本
linktitle: 从PDF中提取文本
type: docs
weight: 10
url: zh/androidjava/extract-text-from-all-pdf/
description: 本文介绍了使用Aspose.PDF for Android via Java从PDF文档中提取文本的各种方法。可以从整个页面、特定部分、基于列等提取。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从PDF文档的所有页面提取文本

从PDF文档提取文本是一个常见需求。在此示例中，您将看到Aspose.PDF for Java如何允许从PDF文档的所有页面提取文本。 要从所有PDF页面提取文本：

1. 创建一个[TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber)类的对象。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF，并调用 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 集合的 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 方法。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类从文档中吸收文本并返回到 **Text** 属性中。

以下代码片段向您展示如何从 PDF 文档的所有页面中提取文本。

```java
public static void ExtractFromAllPages() {
        // 文档目录的路径。

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // 打开文档
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // 创建 TextAbsorber 对象以提取文本
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // 接受所有页面的吸收器
        pdfDocument.getPages().accept(textAbsorber);

        // 获取提取的文本
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // 将一行文本写入文件
            writer.write(extractedText);
            // 关闭流
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```


## 从 PDF 文档中提取高亮文本

在从 PDF 文档提取文本的各种场景中，您可能会遇到只提取 PDF 文档中高亮文本的需求。为了实现此功能，我们在 API 中添加了 TextMarkupAnnotation.GetMarkedText() 和 TextMarkupAnnotation.GetMarkedTextFragments() 方法。您可以通过过滤 TextMarkupAnnotation 并使用上述方法从 PDF 文档中提取高亮文本。以下代码片段展示了如何从 PDF 文档中提取高亮文本。

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // 遍历所有注释
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // 过滤 TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // 检索高亮文本片段
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // 显示高亮文本
                    System.out.println(tf.getText());
                }
            }
        }
    }
```


## 访问 XML 中的文本片段和段元素

有时我们需要在处理从 XML 生成的 PDF 文档时访问 TextFragement 或 TextSegment 项。Aspose.PDF for Android via Java 提供了按名称访问这些项目的功能。下面的代码片段展示了如何使用此功能。

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
}
```