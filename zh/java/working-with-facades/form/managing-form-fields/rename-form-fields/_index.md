---
title: 重命名表单字段
linktitle: 重命名表单字段
type: docs
weight: 30
url: /zh/java/rename-form-fields/
description: 学习如何在 Java 中使用 Aspose.PDF 的 Form facade 重命名 PDF 表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文档中重命名表单字段
Abstract: 本文展示了如何绑定 PDF 表单、重命名现有字段，并使用 Aspose.PDF for Java 中的 Form facade 保存更新后的文档。
---
使用 `FormExamples.renameFormFields(...)` 在交互式 PDF 表单中重命名字段。

```java
public static void renameFormFields(Path inputFile, Path outputFile) {
    Form form = new Form();
    try {
        form.bindPdf(inputFile.toString());
        form.renameField("First Name", "NewFirstName");
        form.renameField("Last Name", "NewLastName");
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```
