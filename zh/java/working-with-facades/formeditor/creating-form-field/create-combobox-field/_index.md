---
title: 创建组合框字段
linktitle: 创建组合框字段
type: docs
weight: 30
url: /java/create-combobox-field/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观向 Java 中的 PDF 文档添加组合框字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建组合框字段
Abstract: 本文介绍如何绑定现有 PDF、添加组合框字段、用项目填充它以及使用 Aspose.PDF for Java 中的 FormEditor 外观保存修改后的文档。
---
使用`FormEditorExamples.createComboBoxField(...)` 创建组合框并添加可选项目。

## 创建组合框字段

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 添加组合框字段及其默认值和目标矩形。
3. 添加可选择的组合框项目。
4. 保存更新的文档。

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
