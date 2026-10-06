---
title: 展平所有字段
linktitle: 展平所有字段
type: docs
weight: 10
url: /zh/java/flatten-all-fields/
description: 了解如何在 Java 中使用 Aspose.PDF 的 Form 门面将所有 PDF 表单字段展平。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中将所有交互式表单字段转换为静态内容。
Abstract: 本文展示了如何绑定 PDF 表单、展平每个表单字段，并使用 Aspose.PDF for Java 中的 Form 门面保存更新后的文档。
---
使用 `FormExamples.flattenAllFields(...)` 当您需要将所有交互式字段转换为静态页面内容时。

```java
public static void flattenAllFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.flattenAllFields();
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
