---
title: 填写复选框字段
linktitle: 填写复选框字段
type: docs
weight: 20
url: /zh/java/fill-check-box-fields/
description: 了解如何使用 Aspose.PDF 中的 Form facade 用 Java 填写 PDF 表单的复选框字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 表单中设置复选框字段的值
Abstract: 本文展示了如何绑定 PDF 表单、按名称设置复选框字段，并使用 Aspose.PDF for Java 中的 Form facade 保存更新后的文档。
---
使用 `FormExamples.fillCheckBoxFields(...)` 设置表单中复选框的值。

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
