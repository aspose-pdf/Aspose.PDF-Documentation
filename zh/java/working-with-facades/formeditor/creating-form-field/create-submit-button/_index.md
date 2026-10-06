---
title: 创建提交按钮
linktitle: 创建提交按钮
type: docs
weight: 60
url: /zh/java/create-submit-button/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类向 PDF 文档添加提交按钮。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 在 Java 中创建 PDF 提交按钮
Abstract: 本文展示了如何绑定现有 PDF，使用 Aspose.PDF for Java 中的 FormEditor 类添加带有目标 URL 的提交按钮字段，并保存修改后的文档。
---

使用 `FormEditorExamples.createSubmitButton(...)` 创建一个提交表单数据的按钮。

## 创建提交按钮

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 调用 `addSubmitBtn(...)` 带有按钮名称、页面、标签、目标 URL 和矩形。
3. 保存更新后的文档。

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
