---
title: 从 PDF 文件提取原始文本
linktitle: 从 PDF 提取文本
type: docs
weight: 10
url: /zh/androidjava/extract-text-from-all-pdf/
description: 本文介绍了使用 Aspose.PDF for Android via Java 从 PDF 文档提取文本的各种方法。包括整页提取、特定部分提取、基于列的提取等。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

从 PDF 文档中提取文本是一项常见需求。在本示例中，您将看到 Aspose.PDF for Java 如何实现从 PDF 文档的所有页面提取文本。
从所有 PDF 页面提取文本：

1. 创建一个对象的 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类。
1. 使用打开 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类并调用 [接受](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 方法的 [页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 集合。
1. 该 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类从文档中吸收文本并在 **Text** 属性中返回。

以下代码片段演示了如何从 PDF 文档的所有页面提取文本。

```java
public static void ExtractFromAllPages() {
        // The path to the documents directory.

        String filePath = _dataDir + "ExtractTextAll.pdf";

        // Open document
        Document pdfDocument = new com.aspose.pdf.Document(filePath);

        // Create TextAbsorber object to extract text
        TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();

        // Accept the absorber for all the pages
        pdfDocument.getPages().accept(textAbsorber);

        // Get the extracted text
        String extractedText = textAbsorber.getText();
        try {
            java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
            // Write a line of text to the file
            writer.write(extractedText);
            // Close the stream
            writer.close();
        } catch (java.io.IOException e) {
            e.printStackTrace();
        }

    }
```

## 从 PDF 文档中提取突出显示的文本

在从 PDF 文档提取文本的各种场景中，您可能会需要仅提取 PDF 文档中被突出显示的文本。为实现此功能，我们在 API 中添加了 TextMarkupAnnotation.GetMarkedText() 和 TextMarkupAnnotation.GetMarkedTextFragments() 方法。您可以通过筛选 TextMarkupAnnotation 并使用上述方法来提取 PDF 文档中的突出显示文本。以下代码片段展示了如何从 PDF 文档中提取突出显示的文本。

```java
public static void ExtractHighlightedText() {
        Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
        // Loop through all the annotations
        for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations()) {
            // Filter TextMarkupAnnotation
            if (annotation.getAnnotationType() == AnnotationType.Highlight) {
                HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
                // Retrieve highlighted text fragments
                TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
                for (TextFragment tf : collection) {
                    // Display highlighted text
                    System.out.println(tf.getText());
                }
            }
        }
    }
```

## 从 XML 访问 Text Fragment 和 Segment 元素

有时在处理由 XML 生成的 PDF 文档时，需要访问 TextFragement 或 TextSegment 项。Aspose.PDF for Android via Java 提供了按名称访问此类项的功能。下面的代码片段展示了如何使用此功能。

  public static void AccessTextFragmentAndSegmentElements() {
        String inXml = \u002240014.xml\u0022;
        Document doc = new Document();
        doc.bindXml(_dataDir \u002B inXml);

        TextSegment segment = (TextSegment) doc.getObjectById(\u0022boldHtml\u0022);
        segment = (TextSegment) doc.getObjectById("strongHtml");

        System.out.println(segment.getText());
        
    }
```

