---
title: 导出到 XFDF
linktitle: 导出到 XFDF
type: docs
weight: 20
url: /java/export-to-xfdf/
description: 了解如何使用 Aspose.PDF 中的表单外观将 PDF 表单字段数据导出到 Java 中的 XFDF。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中将 AcroForm 数据导出到 XFDF
Abstract: 本文展示了如何使用 Aspose.PDF for Java 中的表单外观绑定 PDF 表单并将其字段值导出到 XFDF 流。
---
使用`FormExamples.exportXfdf(...)` 将表单字段数据写入XFDF。

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
