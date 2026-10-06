---
title: 使用 Java 导入和导出批注
linktitle: 导入和导出批注
type: docs
weight: 80
url: /zh/java/pdfannotationeditor-class/import-export-annotations/
description: 了解如何使用 Java 将批注从一个 PDF 文档复制到另一个 PDF 文档。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中在文档之间转移 PDF 批注
Abstract: 本文解释了如何使用 Java 将批注从源 PDF 复制并导出到新 PDF 文档中。工作流加载源文件，创建目标文档，添加页面，从第一个源页面复制批注，并保存结果。
---
## 将批注从一个 PDF 复制到另一个 PDF

1. 打开源 PDF 并创建一个带有目标页的新目标文档。
2. 枚举第一页上的注释，并将每个注释添加到目标页。
3. 保存目标文档以保留已复制的注释。

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
