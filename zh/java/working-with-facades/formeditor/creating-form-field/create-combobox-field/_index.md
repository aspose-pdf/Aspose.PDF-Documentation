---
title: 创建 ComboBox 字段
linktitle: 创建 ComboBox 字段
type: docs
weight: 30
url: /zh/java/create-combobox-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类向 PDF 文档添加 combo box 字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建 combo box 字段
Abstract: 本文展示了如何绑定现有 PDF，添加 combo box 字段，为其填充项目，并使用 Aspose.PDF for Java 中的 FormEditor 类保存修改后的文档。
---
使用 `FormEditorExamples.createComboBoxField(...)` 创建组合框并添加可选择的项。

## 创建 combo box 字段

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 添加组合框字段及其默认值和目标矩形。
3. 添加可选择的组合框项目。
4. 保存更新后的文档。

```java
public static void createComboBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.ComboBox, "combobox1", "Australia", 1, 230, 498, 350, 514);
        editor.addListItem("combobox1", new String[] {"Australia", "Australia"});
        editor.addListItem("combobox1", new String[] {"New Zealand", "New Zealand"});
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
