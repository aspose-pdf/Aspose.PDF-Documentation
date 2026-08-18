---
title: 导入 XML 数据
linktitle: 导入 XML 数据
type: docs
weight: 40
url: /java/import-xml-data/
description: 了解如何使用 Aspose.PDF 中的表单外观通过 Java 将 XML 表单数据导入 PDF 表单。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中从 XML 导入 AcroForm 数据
Abstract: 本文介绍如何绑定 PDF 表单、从 XML 流导入字段值以及使用 Aspose.PDF for Java 中的表单外观保存更新的文档。
---
使用`FormExamples.importXml(...)` 从 XML 数据填充表单。

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
