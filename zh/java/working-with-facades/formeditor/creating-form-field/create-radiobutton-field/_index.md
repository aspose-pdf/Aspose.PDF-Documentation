---
title: 创建单选按钮字段
linktitle: 创建单选按钮字段
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: 了解如何使用 Aspose.PDF 中的 FormEditor 外观向 Java 中的 PDF 文档添加单选按钮字段。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Create a radio button field in a PDF with Java
Abstract: This article shows how to bind an existing PDF, configure radio button layout settings, create a radio button field, and save the modified document using the FormEditor facade in Aspose.PDF for Java.
---
Use `FormEditorExamples.createRadioButtonField(...)` to create a radio button field with predefined options.

## Create a radio button field

1. Bind the source PDF to the `FormEditor` facade.
2. Configure the radio button gap, orientation, and item size.
3. Define the radio button items.
4. Add the radio button field with its default selection and rectangle.
5. Save the updated document.

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
