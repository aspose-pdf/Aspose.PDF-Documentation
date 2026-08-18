---
title: 导出到 FDF
linktitle: 导出到 FDF
type: docs
weight: 10
url: /java/export-to-fdf/
description: 了解如何使用 Aspose.PDF 中的表单外观将 PDF 表单字段值导出到 Java 中的 FDF。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中将 AcroForm 数据导出到 FDF
Abstract: 本文介绍如何使用 Aspose.PDF for Java 中的 Form Facade 绑定 PDF 表单并将其字段数据导出到 FDF 流。
---
当您需要将 AcroForm 字段数据序列化为 FDF 时，请使用 `FormExamples.exportFdf(...)`。

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
