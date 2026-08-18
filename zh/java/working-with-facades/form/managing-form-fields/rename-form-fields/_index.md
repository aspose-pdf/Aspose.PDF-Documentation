---
title: 重命名表单字段
linktitle: 重命名表单字段
type: docs
weight: 30
url: /java/rename-form-fields/
description: 了解如何使用 Aspose.PDF 中的表单外观在 Java 中重命名 PDF 表单字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 重命名 PDF 文档中的表单字段
Abstract: 本文介绍如何在 Aspose.PDF for Java 中绑定 PDF 表单、重命名现有字段以及使用表单外观保存更新的文档。
---
使用`FormExamples.renameFormFields(...)` 重命名交互式 PDF 表单中的字段。

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
