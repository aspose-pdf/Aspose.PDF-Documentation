---
title: 填写复选框字段
linktitle: 填写复选框字段
type: docs
weight: 20
url: /java/fill-check-box-fields/
description: 了解如何使用 Aspose.PDF 中的表单外观使用 Java 填充 PDF 表单中的复选框字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 设置 PDF 表单中的复选框字段值
Abstract: 本文介绍如何绑定 PDF 表单、按名称设置复选框字段以及使用 Aspose.PDF for Java 中的表单外观保存更新的文档。
---
使用`FormExamples.fillCheckBoxFields(...)` 设置表单中的复选框值。

```java
public static void fillCheckBoxFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("subscribe_newsletter", "Yes");
        form.fillField("accept_terms", "Yes");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
