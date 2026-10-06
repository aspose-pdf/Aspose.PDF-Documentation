---
title: 在 Java 中将 PDF/A 和 PDF/UA 转换为 PDF
linktitle: 将 PDF/A 和 PDF/UA 转换为 PDF
type: docs
weight: 120
url: /zh/java/convert-pdf_x-to-pdf/
lastmod: "2026-10-06"
description: 了解如何在 Java 中从基于标准的 PDF 文件中移除 PDF/A 和 PDF/UA 合规性，并将其保存为标准 PDF 文档。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: 如何在 Java 中将 PDF/A 和 PDF/UA 转换为标准 PDF
Abstract: 本文说明了如何使用 Aspose.PDF for Java 从基于标准的 PDF 文档中移除 PDF/A 和 PDF/UA 合规性，然后将结果保存为标准 PDF 文件。
---
Aspose.PDF for Java 可以将符合标准的 PDF 变体转换回普通 PDF 文档。

## 将 PDF/A 转换为标准 PDF

当需要将归档的 PDF/A 文档降级为标准 PDF 时，请使用此示例。

1. 在 a 中打开源 PDF/A 文件 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 调用 `removePdfaCompliance()` 从已加载的文档中分离归档合规配置文件。
1. 保存生成的标准 PDF 文件，不设置 PDF/A 限制。

```java
public static void convertPdfAToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfaCompliance();
        document.save(outputFile.toString());
    }
}
```

## 将 PDF/UA 转换为标准 PDF

当需要将可访问的 PDF/UA 文档转换回标准 PDF 时，请使用此示例。

1. 在 a 中打开源 PDF/UA 文件 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 实例。
1. 调用 `removePdfUaCompliance()` 从文档元数据和结构要求中移除可访问性合规配置文件。
1. 将生成的 PDF 文档保存为常规 PDF 文件。

```java
public static void convertPdfUaToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.removePdfUaCompliance();
        document.save(outputFile.toString());
    }
}
```
