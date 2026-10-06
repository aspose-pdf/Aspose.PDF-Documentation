---
title: 创建 N-Up PDF 文档
linktitle: 创建 N-Up PDF 文档
type: docs
weight: 10
url: /zh/java/create-n-up-pdf-document/
description: 在 Java 中使用 PdfFileEditor 类创建 2x2 N-Up PDF 布局。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中从现有文档生成 N-Up PDF 布局
Abstract: 了解如何使用 Aspose.PDF for Java 创建 N-Up PDF 文档。Java 示例使用 PdfFileEditor 将每个输出页放置四个源页面，并展示了用于检查失败的布尔返回变体。
---
## 创建 N-Up PDF 文档

Java 示例使用 `PdfFileEditor.makeNUp` 从现有 PDF 构建 2x2 布局。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 调用 `makeNUp` 使用输入文件、输出文件以及列数和行数。
3. 保存生成的文档。
4. 如果您想进行明确的成功检查，请调用返回布尔值的变体并处理 a `false` 结果。

### Java 示例

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
