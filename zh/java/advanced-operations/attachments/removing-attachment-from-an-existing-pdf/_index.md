---
title: 在 Java 中移除 PDF 附件
linktitle: 从现有 PDF 中移除附件
type: docs
weight: 30
url: /zh/java/removing-attachment-from-an-existing-pdf/
description: 了解如何使用 Aspose.PDF 在 Java 中移除 PDF 文档中的一个或全部嵌入附件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 以编程方式删除 PDF 附件
Abstract: 本文展示了如何使用 Aspose.PDF for Java 从 PDF 文件中移除附件。示例演示了通过键删除单个嵌入文件以及在保存更新的文档之前清空整个 `EmbeddedFiles` 集合。
---
存储在 PDF 文档中的附件可以单独或一次性全部通过 `EmbeddedFiles` 集合。

## 删除单个附件

当需要从 PDF 中删除一个已命名的嵌入文件时使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 根据其键从嵌入文件集合中删除附件。
1. 保存更新后的输出文档。

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## 删除所有附件

当需要清除整个嵌入文件集合时，请使用此方法。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 删除嵌入文件集合中的所有项目。
1. 保存已清理的输出文档。

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
