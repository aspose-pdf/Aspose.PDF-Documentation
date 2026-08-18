---
title: 导入 XFDF 数据
linktitle: 导入 XFDF 数据
type: docs
weight: 20
url: /java/import-xfdf-data/
description: 了解如何使用 Aspose.PDF 中的表单外观通过 Java 将 XFDF 表单数据导入 PDF 表单。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中从 XFDF 导入 AcroForm 数据
Abstract: 本文介绍如何绑定 PDF 表单、从 XFDF 流导入字段值以及使用 Aspose.PDF for Java 中的表单外观保存更新的文档。
---
使用 `FormExamples.importXfdf(...)` 从 XFDF 数据填充表单。

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
