---
title: Создание поля RadioButton
linktitle: Создание поля RadioButton
type: docs
weight: 50
url: /ru/java/create-radiobutton-field/
description: Узнайте, как добавить поле радиокнопки в документ PDF на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-09-17"
TechArticle: true
AlternativeHeadline: Создать поле радиокнопки в PDF с помощью Java
Abstract: В этой статье показано, как привязать существующий PDF, настроить параметры расположения радиокнопок, создать поле радиокнопки и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
Используйте `FormEditorExamples.createRadioButtonField(...)`, чтобы создать поле переключателя с предопределёнными вариантами.

## Создание поля радиокнопки

1. Привяжите исходный PDF к фасаду `FormEditor`.
2. Настройте зазор радиокнопки, ориентацию и размер элемента.
3. Определите элементы радиокнопки.
4. Добавьте поле радиокнопки с его выбранным по умолчанию элементом и прямоугольником.
5. Сохраните обновлённый документ.

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


