---
title: Создать поле ListBox
linktitle: Создать поле ListBox
type: docs
weight: 40
url: /java/create-listbox-field/
description: Узнайте, как добавить поле списка в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Создайте поле списка в PDF-файле с помощью Java
Abstract: В этой статье показано, как связать существующий PDF-файл, определить элементы списка, добавить поле списка и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
Используйте `FormEditorExamples.createListBoxField(...)`, чтобы создать список с предопределенными элементами.

## Создайте поле списка

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Определите доступные элементы списка с помощью `setItems(...)`.
3. Добавьте поле списка со значением по умолчанию и прямоугольником.
4. Сохраните обновленный документ.

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
