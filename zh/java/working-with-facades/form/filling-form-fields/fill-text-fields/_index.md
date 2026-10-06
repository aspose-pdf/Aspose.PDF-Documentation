---
title: 填写文本字段
linktitle: 填写文本字段
type: docs
weight: 10
url: /zh/java/fill-text-fields/
description: 了解如何使用 Java 在 Aspose.PDF 中的 Form 门面填充 PDF 表单中的文本字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 填充 PDF 中的文本表单字段
Abstract: 本文展示了如何绑定 PDF 表单、按名称设置文本字段值，并使用 Aspose.PDF for Java 中的 Form 门面保存更新后的文档。
---
使用 `FormExamples.fillTextFields(...)` 填充基于文本的表单字段。

```java
public static void fillTextFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.fillField("name", "John Doe");
        form.fillField("address", "123 Main St, Anytown, USA");
        form.fillField("email", "john.doe@example.com");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
