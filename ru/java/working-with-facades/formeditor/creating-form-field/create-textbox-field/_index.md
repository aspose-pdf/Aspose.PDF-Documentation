---
title: Создать поле текстового поля
linktitle: Создать поле текстового поля
type: docs
weight: 10
url: /java/create-textbox-field/
description: Узнайте, как добавить поля текстового поля в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Создание полей текстовых форм в PDF-файле с помощью Java
Abstract: В этой статье показано, как связать существующий PDF-файл, добавить текстовые поля со значениями по умолчанию и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
Используйте `FormEditorExamples.createTextBoxField(...)`, чтобы добавить текстовые поля в форму PDF.

## Создание полей текстового поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Добавьте в каждое текстовое поле `FieldType.Text`, имя поля, значение по умолчанию, номер страницы и прямоугольник.
3. Сохраните обновленный документ.

```java
public static void createTextBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.Text, "first_name", "Alexander", 1, 50, 570, 150, 590);
        editor.addField(FieldType.Text, "last_name", "Smith", 1, 235, 570, 330, 590);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
