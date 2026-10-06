---
title: 创建 TextBox 字段
linktitle: 创建 TextBox 字段
type: docs
weight: 10
url: /zh/java/create-textbox-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 门面向 PDF 文档添加文本框字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建文本表单字段
Abstract: 本文展示了如何绑定已有的 PDF，使用 Aspose.PDF for Java 中的 FormEditor 门面添加带默认值的文本字段，并保存修改后的文档。
---
使用 `FormEditorExamples.createTextBoxField(...)` 向 PDF 表单添加文本字段。

## 创建文本框字段

1. 将源 PDF 绑定到 `FormEditor` 外立面。
2. 为每个文本字段添加 `FieldType.Text`, 字段名称、默认值、页码和矩形。
3. 保存更新后的文档。

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
