---
title: 创建列表框字段
linktitle: 创建列表框字段
type: docs
weight: 40
url: /java/create-listbox-field/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观向 Java 中的 PDF 文档添加列表框字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建列表框字段
Abstract: 本文介绍如何使用 Aspose.PDF for Java 中的 FormEditor 外观绑定现有 PDF、定义列表项、添加列表框字段以及保存修改后的文档。
---
使用`FormEditorExamples.createListBoxField(...)` 创建包含预定义项目的列表框。

## 创建列表框字段

1. 将源 PDF 绑定到 `FormEditor` 外观。
2. 使用`setItems(...)` 定义可用列表项。
3. 添加列表框字段及其默认值和矩形。
4. 保存更新的文档。

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
