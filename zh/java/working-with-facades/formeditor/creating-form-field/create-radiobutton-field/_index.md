---
title: 创建单选按钮字段
linktitle: 创建单选按钮字段
type: docs
weight: 50
url: /zh/java/create-radiobutton-field/
description: 了解如何在 Java 中使用 Aspose.PDF 的 FormEditor 类向 PDF 文档添加单选按钮字段。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 中创建单选按钮字段
Abstract: 本文展示了如何绑定现有 PDF，配置单选按钮布局设置，创建单选按钮字段，并使用 Aspose.PDF for Java 中的 FormEditor 类保存修改后的文档。
---
使用 `FormEditorExamples.createRadioButtonField(...)` 创建具有预定义选项的单选按钮字段。

## 创建单选按钮字段

1. 将源 PDF 绑定到 `FormEditor` 对象。
2. 配置单选按钮的间距、方向和项目大小。
3. 定义单选按钮项目。
4. 添加单选按钮字段并设置其默认选中项和矩形。
5. 保存更新后的文档。

```java
public static void createRadioButtonField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setRadioGap(4);
        editor.setRadioHoriz(false);
        editor.setRadioButtonItemSize(20);
        editor.setItems(new String[] {"Australia", "New Zealand", "Malaysia"});
        editor.addField(FieldType.Radio, "radiobutton1", "Malaysia", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
