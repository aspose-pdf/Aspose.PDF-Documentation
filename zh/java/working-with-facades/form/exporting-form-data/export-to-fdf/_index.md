---
title: 导出为 FDF
linktitle: 导出为 FDF
type: docs
weight: 10
url: /zh/java/export-to-fdf/
description: 了解如何在 Java 中使用 Aspose.PDF 的 Form Facade 将 PDF 表单字段值导出为 FDF。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中导出 AcroForm 数据为 FDF
Abstract: 本文展示了如何使用 Aspose.PDF for Java 的 Form Facade 绑定 PDF 表单并将其字段数据导出为 FDF 流。
---
当需要将 AcroForm 字段数据序列化为 FDF 时，使用 `FormExamples.exportFdf(...)`。

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
