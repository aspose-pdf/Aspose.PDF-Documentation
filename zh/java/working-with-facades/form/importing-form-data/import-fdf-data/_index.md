---
title: 导入 FDF 数据
linktitle: 导入 FDF 数据
type: docs
weight: 10
url: /zh/java/import-fdf-data/
description: 了解如何使用 Aspose.PDF 中的 Form facade 在 Java 中将 FDF 表单数据导入 PDF 表单。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中从 FDF 导入 AcroForm 数据
Abstract: 本文展示了如何绑定 PDF 表单、从 FDF 流中导入字段值，并使用 Aspose.PDF for Java 中的 Form facade 保存更新的文档。
---
使用 `FormExamples.importFdf(...)` 从 FDF 文件中应用字段值。

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
