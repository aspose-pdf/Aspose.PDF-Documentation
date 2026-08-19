---
title: Создать поле TextBox
linktitle: Создать поле TextBox
type: docs
weight: 10
url: /ru/java/create-textbox-field/
description: Узнайте, как добавить поля TextBox в PDF‑документ на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Создайте текстовые поля формы в PDF с Java.
Abstract: В этой статье показано, как привязать существующий PDF, добавить текстовые поля с значениями по умолчанию и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
Использовать `FormEditorExamples.createTextBoxField(...)` добавить текстовые поля в форму PDF.

## Создайте поля TextBox

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Добавьте каждое текстовое поле с `FieldType.Text`, имя поля, значение по умолчанию, номер страницы и прямоугольник.
3. Сохраните обновлённый документ.

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

