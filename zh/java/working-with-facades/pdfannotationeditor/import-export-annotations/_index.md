---
title: 使用 Java 导入和导出注释
linktitle: 导入和导出注释
type: docs
weight: 80
url: /java/pdfannotationeditor-class/import-export-annotations/
description: 了解如何使用 Java 将注释从一个 PDF 文档复制到另一个 PDF 文档中。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 用Java在文档之间传输PDF注释
Abstract: 本文介绍如何使用 Java 从源 PDF 复制注释并将其导出到新的 PDF 文档中。该工作流加载源文件，创建目标文档，添加页面，从第一个源页面复制注释，然后保存结果。
---
## 将注释从一个 PDF 复制到另一个 PDF

1. 打开源 PDF 并使用目标页面创建新的目标文档。
2. 枚举第一个源页面上的注释并将每个注释添加到目标页面。
3. 保存目标文档以保留复制的注释。

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
