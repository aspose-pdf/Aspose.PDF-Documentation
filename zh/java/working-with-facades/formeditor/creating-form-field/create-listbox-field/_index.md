---
title: 创建 ListBox 字段
linktitle: 创建 ListBox 字段
type: docs
weight: 40
url: /zh/java/create-listbox-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 门面向 PDF 文档添加 list box 字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建 list box 字段
Abstract: 本文展示了如何绑定现有 PDF、定义列表项、添加 list box 字段，并使用 Aspose.PDF for Java 中的 FormEditor 门面保存修改后的文档。
---
使用 `FormEditorExamples.createListBoxField(...)` 创建一个带有预定义项的列表框。

## 创建 list box 字段

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 使用以下方式定义可用的列表项 `setItems(...)`.
3. 添加带有默认值和矩形的列表框字段。
4. 保存更新后的文档。

```java
public static void createListBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.ListBox, "listbox1", "Australia", 1, 230, 398, 350, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
