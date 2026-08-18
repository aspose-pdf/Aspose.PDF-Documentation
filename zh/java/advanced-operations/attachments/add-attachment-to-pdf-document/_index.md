---
title: 用 Java 添加 PDF 附件
linktitle: Adding Attachment to a PDF document
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: 了解如何使用 Aspose.PDF 将文件附件添加到 Java 中的 PDF 文档。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将嵌入文件添加到 PDF 文档
Abstract: 本文介绍如何使用 Aspose.PDF for Java 将外部文件附加到 PDF 文档。该示例打开现有 PDF，为附件创建 FileSpecification，将其添加到文档的 EmbeddedFiles 集合中，然后保存更新的文件。
---
要将文件附加到 PDF，请加载源文档，创建 `FileSpecification`，将其添加到嵌入文件集合，然后保存结果。

## 添加附件到 PDF 文档

当需要将外部文件嵌入到现有 PDF 中时，请使用此示例。

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 为要嵌入的文件创建一个 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)。
1. 将文件规范添加到`EmbeddedFiles` 集合并保存更新的文档。

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
