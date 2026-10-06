---
title: 创建复选框字段
linktitle: 创建复选框字段
type: docs
weight: 20
url: /zh/java/create-checkbox-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类向 PDF 文档添加复选框表单字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建复选框字段
Abstract: 本文展示了如何绑定现有 PDF，在指定位置添加复选框字段，并使用 Aspose.PDF for Java 中的 FormEditor 类保存修改后的文档。
---
使用 `FormEditorExamples.createCheckBoxField(...)` 向 PDF 表单添加复选框字段。

## 创建复选框字段

1. 将源 PDF 绑定到 `FormEditor` 立面。
2. 添加复选框字段 `FieldType.CheckBox`, 字段名称、标题、页面和矩形。
3. 保存更新后的文档。

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
