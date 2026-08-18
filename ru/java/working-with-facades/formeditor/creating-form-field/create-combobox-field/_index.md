---
title: Создать поле со списком
linktitle: Создать поле со списком
type: docs
weight: 30
url: /java/create-combobox-field/
description: Узнайте, как добавить поле со списком в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Создайте поле со списком в PDF-файле с помощью Java
Abstract: В этой статье показано, как связать существующий PDF-файл, добавить поле со списком, заполнить его элементами и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
Используйте `FormEditorExamples.createComboBoxField(...)`, чтобы создать поле со списком и добавить доступные для выбора элементы.

## Создайте поле со списком

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Добавьте поле со списком со значением по умолчанию и целевым прямоугольником.
3. Добавьте выбираемые элементы поля со списком.
4. Сохраните обновленный документ.

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
