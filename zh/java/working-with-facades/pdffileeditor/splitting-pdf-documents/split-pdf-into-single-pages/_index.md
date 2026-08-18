---
title: Split PDF into Single Pages
linktitle: Split PDF into Single Pages
type: docs
weight: 30
url: /java/split-pdf-into-single-pages/
description: Split a PDF into single-page output files in Java with the PdfFileEditor facade.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export each page of a PDF to its own file with Java
Abstract: Learn how to split a PDF into single-page files with Aspose.PDF for Java. The Java example uses PdfFileEditor to write each page to an individual output PDF based on a filename pattern.
---
## 将 PDF 拆分为单页

当每个源页面必须成为其自己的 PDF 文件时，请使用此工作流程。

### 步骤

1. 创建一个 `PdfFileEditor` 实例。
2. 准备一个包含页面占位符（例如`%NUM%`）的输出文件模式。
3. 使用源文件和输出模式调用`splitToPages`。
4. 保存生成的单页文件。

```java
public static void splitPdfIntoSinglePages(Path inputFile, Path outputFilePattern) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToPages(inputFile.toString(), outputFilePattern.toString());
}
```
