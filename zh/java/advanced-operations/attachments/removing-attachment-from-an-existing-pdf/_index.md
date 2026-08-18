---
title: 使用 Java 从 PDF 中删除附件
linktitle: 从现有 PDF 中删除附件
type: docs
weight: 30
url: /java/removing-attachment-from-an-existing-pdf/
description: 了解如何使用 Aspose.PDF 从 Java 中的 PDF 文档中删除一个或所有嵌入附件。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 以编程方式删除 PDF 附件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从 PDF 文件中删除附件。这些示例演示了在保存更新的文档之前，通过按键删除一个嵌入式文件并清除整个 EmbeddedFiles 集合。
---
可以通过 `EmbeddedFiles` 集合单独或一次性删除 PDF 文档中存储的附件。

## 删除单个附件

当应从 PDF 中删除一个指定的嵌入文件时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 通过附件的密钥从嵌入文件集合中删除附件。
1. 保存更新的输出文档。

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## 删除所有附件

当应清除整个嵌入文件集合时，请使用此方法。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 从嵌入文件集合中删除所有项目。
1. 保存清理后的输出文档。

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
