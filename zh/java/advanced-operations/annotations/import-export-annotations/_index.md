---
title: 使用 Java 导入和导出批注
linktitle: 导入和导出批注
type: docs
weight: 80
url: /zh/java/import-export-annotations/
description: 了解如何使用 Aspose.PDF for Java 将批注从一个 PDF 文档复制到另一个 PDF 文档。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中在文档之间传输 PDF 批注。
Abstract: 本文解释了如何使用 Aspose.PDF for Java 将批注从源 PDF 复制并导出到新 PDF 文档。工作流加载源文件，创建目标文档，添加页面，从第一源页面复制批注，随后保存结果。
---
## 将批注从一个 PDF 复制到另一个 PDF

1. 打开源 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 添加到目标 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将每个 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 添加到目标 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 读取或遍历 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 目标页上的项目。
1. 保存更新后的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 枚举第一个源页面上的 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 对象，并将每个对象添加到目标页面。

```java
public static void importExport(Path inputFile, Path outputFile) {
    try (Document sourceDocument = new Document(inputFile.toString());
         Document destinationDocument = new Document()) {
        Page page = destinationDocument.getPages().add();

        for (Annotation annotation : sourceDocument.getPages().get_Item(1).getAnnotations()) {
            page.getAnnotations().add(annotation, true);
        }

        destinationDocument.save(outputFile.toString());
    }
}
```
