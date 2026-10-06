---
title: 创建 PDF 小册子
linktitle: 创建 PDF 小册子
type: docs
weight: 20
url: /zh/java/create-pdf-booklet/
description: 使用 PdfFileEditor 门面在 Java 中从现有文档创建适用于小册子的 PDF。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中从 PDF 文档生成小册子输出。
Abstract: 了解如何使用 Aspose.PDF for Java 创建 PDF 小册子。该 Java 示例使用 PdfFileEditor 重新排序页面以进行小册子打印，并且还包含一个返回布尔值的变体，用于简单的成功检查。
---
## 创建 PDF 小册子

使用 `PdfFileEditor.makeBooklet` 将现有 PDF 的页面重新排列成小册子顺序。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 呼叫 `makeBooklet` 使用源 PDF 和输出文件。
3. 保存小册子文档。
4. 如果要检查返回状态，请使用布尔返回的变体并处理失败的结果。

### Java 示例

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```
