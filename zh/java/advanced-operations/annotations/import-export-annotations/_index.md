---
title: 使用 Java 导入和导出注释
linktitle: 导入和导出注释
type: docs
weight: 80
url: /java/import-export-annotations/
description: 了解如何使用 Aspose.PDF for Java 将注释从一个 PDF 文档复制到另一个 PDF 文档中。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在文档之间传输 PDF 注释。
Abstract: 本文介绍如何使用 Aspose.PDF for Java 从源 PDF 复制注释并将其导出到新的 PDF 文档中。该工作流加载源文件，创建目标文档，添加页面，从第一个源页面复制注释，然后保存结果。
---
## 将注释从一个 PDF 复制到另一个 PDF

1. 打开源 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)添加到目标[文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 将每个[注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 添加到目标[页面](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 读取或迭代目标页面上的[注释](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 项。
1. 保存更新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。
1. 枚举第一个源页面上的 [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) 项目并将每个项目添加到目标页面。

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
