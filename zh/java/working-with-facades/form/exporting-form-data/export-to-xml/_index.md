---
title: 导出为 XML
linktitle: 导出为 XML
type: docs
weight: 40
url: /java/export-to-xml/
description: 了解如何使用 Aspose.PDF 中的表单外观将 PDF 表单数据导出到 Java 中的 XML。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中将 AcroForm 数据导出为 XML
Abstract: 本文展示了如何使用 Aspose.PDF for Java 中的表单外观绑定 PDF 表单并将其字段值导出到 XML 流。
---
使用`FormExamples.exportXml(...)` 将表单字段数据保存为 XML。

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
