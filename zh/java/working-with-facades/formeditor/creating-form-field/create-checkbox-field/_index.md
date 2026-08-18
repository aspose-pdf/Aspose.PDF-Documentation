---
title: 创建复选框字段
linktitle: 创建复选框字段
type: docs
weight: 20
url: /java/create-checkbox-field/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观向 Java 中的 PDF 文档添加复选框表单字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建复选框字段
Abstract: 本文介绍如何绑定现有 PDF、在指定位置添加复选框字段以及使用 Aspose.PDF for Java 中的 FormEditor 外观保存修改后的文档。
---
使用`FormEditorExamples.createCheckBoxField(...)` 将复选框字段添加到 PDF 表单。

## 创建复选框字段

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 添加带有`FieldType.CheckBox`、字段名称、标题、页面和矩形的复选框字段。
3. 保存更新的文档。

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
