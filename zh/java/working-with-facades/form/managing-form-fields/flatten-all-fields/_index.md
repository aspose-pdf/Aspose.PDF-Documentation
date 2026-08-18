---
title: 展平所有字段
linktitle: 展平所有字段
type: docs
weight: 10
url: /java/flatten-all-fields/
description: 了解如何使用 Aspose.PDF 中的表单外观在 Java 中展平所有 PDF 表单字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 将所有交互式表单字段转换为 Java 中的静态内容
Abstract: 本文展示了如何在 Aspose.PDF for Java 中绑定 PDF 表单、展平每个表单字段以及使用表单外观保存更新的文档。
---
当您需要将所有交互字段转换为静态页面内容时，请使用`FormExamples.flattenAllFields(...)`。

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
