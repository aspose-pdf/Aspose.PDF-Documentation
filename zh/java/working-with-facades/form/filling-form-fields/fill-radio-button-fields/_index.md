---
title: 填写单选按钮字段
linktitle: 填写单选按钮字段
type: docs
weight: 30
url: /java/fill-radio-button-fields/
description: 了解如何使用 Aspose.PDF 中的表单外观通过 Java 选择 PDF 表单中的单选按钮值。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 在 Java 中选择单选按钮字段选项
Abstract: 本文介绍如何绑定 PDF 表单、按索引选择单选按钮选项以及如何在 Aspose.PDF for Java 中使用表单外观保存更新的文档。
---
使用`FormExamples.fillRadioButtonFields(...)` 选择单选按钮选项。

```java
public static void fillRadioButtonFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("gender", 0);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
