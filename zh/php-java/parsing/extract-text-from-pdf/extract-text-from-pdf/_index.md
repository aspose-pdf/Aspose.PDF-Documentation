---
title: 从PDF文件中提取原始文本
linktitle: 从PDF中提取文本
type: docs
weight: 10
url: zh/php-java/extract-text-from-all-pdf/
description: 本文介绍了使用Aspose.PDF for PHP从PDF文档中提取文本的各种方法。包括从整个页面、特定部分、基于列等提取。
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从PDF文档的所有页面提取文本

从PDF文档中提取文本是一个常见需求。在此示例中，您将看到Aspose.PDF for PHP如何允许从PDF文档的所有页面提取文本。
要从所有PDF页面提取文本：

1. 创建一个 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类的对象。

1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类打开 PDF，并调用 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 集合的 [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) 方法。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) 类从文档中吸收文本并在 [getText() 方法](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--) 中返回。

以下代码片段向您展示如何从 PDF 文档的所有页面中提取文本。

```php

    // 从输入 PDF 文件创建一个新的 Document 对象。
    $document = new Document($inputFile);

    // 创建一个新的 TextAbsorber 对象以从文档中提取文本。
    $textAbsorber = new TextAbsorber();

    // 从文档中提取文本。
    $textAbsorber->visit($document);

    // 获取提取的文本内容。
    $content = $textAbsorber->getText();

    // 将提取的文本保存到输出文件。
    file_put_contents($outputFile, $content);
```