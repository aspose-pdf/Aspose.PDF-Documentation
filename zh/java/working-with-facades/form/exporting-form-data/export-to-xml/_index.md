---
title: 导出为 XML
linktitle: 导出为 XML
type: docs
weight: 40
url: /zh/java/export-to-xml/
description: 了解如何在 Java 中使用 Aspose.PDF 的 Form 类将 PDF 表单数据导出为 XML。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中将 AcroForm 数据导出为 XML
Abstract: 本文展示了如何绑定 PDF 表单，并使用 Aspose.PDF for Java 中的 Form 类将其字段值导出到 XML 流。
---
使用 `FormExamples.exportXml(...)` 将表单字段数据保存为 XML。

```java
public static void exportXml(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportXml(outputStream);
    } finally {
        form.close();
    }
}
```
