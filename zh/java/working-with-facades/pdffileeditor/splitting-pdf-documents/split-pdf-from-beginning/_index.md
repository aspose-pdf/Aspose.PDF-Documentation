---
title: 从开头拆分 PDF
linktitle: 从开头拆分 PDF
type: docs
weight: 10
url: /zh/java/split-pdf-from-beginning/
description: 使用 PdfFileEditor 类在 Java 中从开头拆分 PDF。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 将 PDF 的前几页提取到新文档中。
Abstract: 了解如何使用 Aspose.PDF for Java 从开头拆分 PDF。该 Java 示例使用 PdfFileEditor 提取文档的前三页并将其保存为单独的 PDF。
---
## 从开头拆分 PDF

该 Java 示例从源文档中提取前三页。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 调用 `splitFromFirst` 使用源文件、要保留的页数以及输出文件。
3. 保存新的 PDF 文档。

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
