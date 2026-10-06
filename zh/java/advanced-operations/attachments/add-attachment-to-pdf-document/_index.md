---
title: 在 Java 中向 PDF 添加附件
linktitle: 向 PDF 文档添加附件
type: docs
weight: 10
url: /zh/java/add-attachment-to-pdf-document/
description: 了解如何使用 Aspose.PDF 在 Java 中向 PDF 文档添加文件附件。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 向 PDF 文档添加嵌入文件
Abstract: 本文展示了如何使用 Aspose.PDF for Java 将外部文件附加到 PDF 文档。示例打开一个现有的 PDF，创建一个 FileSpecification 来表示附件，将其添加到文档的 EmbeddedFiles 集合中，并保存更新后的文件。
---
要将文件附加到 PDF，加载源文档，创建一个 `FileSpecification`，将其添加到嵌入式文件集合中，然后保存结果。

## 将附件添加到 PDF 文档

当需要将外部文件嵌入到现有 PDF 时使用此示例。

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. 创建一个 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) 对于您想要嵌入的文件。
1. 将文件规范添加到 `EmbeddedFiles` 收集并保存更新后的文档。

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
