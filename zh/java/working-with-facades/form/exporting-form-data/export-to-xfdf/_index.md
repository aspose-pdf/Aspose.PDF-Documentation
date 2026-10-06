---
title: 导出至 XFDF
linktitle: 导出至 XFDF
type: docs
weight: 20
url: /zh/java/export-to-xfdf/
description: 了解如何在 Java 中使用 Aspose.PDF 的 Form 类将 PDF 表单字段数据导出为 XFDF。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中将 AcroForm 数据导出为 XFDF
Abstract: 本文展示了如何绑定 PDF 表单，并使用 Aspose.PDF for Java 中的 Form 类将其字段值导出为 XFDF 流。
---
使用 `FormExamples.exportXfdf(...)` 将表单字段数据写入 XFDF。

```java
public static void exportXfdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXfdf(outputStream);
    } finally {
        form.close();
    }
}
```
