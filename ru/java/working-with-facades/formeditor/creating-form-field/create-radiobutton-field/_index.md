---
title: Создать поле RadioButton
linktitle: Создать поле RadioButton
type: docs
weight: 50
url: /java/create-radiobutton-field/
description: Узнайте, как добавить поле переключателя в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Создайте поле переключателя в PDF-файле с помощью Java
Abstract: В этой статье показано, как связать существующий PDF-файл, настроить параметры макета переключателя, создать поле переключателя и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
Используйте `FormEditorExamples.createRadioButtonField(...)`, чтобы создать поле переключателя с предопределенными параметрами.

## Создайте поле переключателя

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Настройте зазор переключателя, ориентацию и размер элемента.
3. Определите элементы переключателя.
4. Добавьте поле переключателя с выбором по умолчанию и прямоугольником.
5. Сохраните обновленный документ.

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
