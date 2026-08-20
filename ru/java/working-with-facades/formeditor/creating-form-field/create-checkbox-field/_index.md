---
title: Создать поле CheckBox
linktitle: Создать поле CheckBox
type: docs
weight: 20
url: /ru/java/create-checkbox-field/
description: Узнайте, как добавить поле формы с флажком в PDF‑документ на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Создать поле флажка в PDF с помощью Java
Abstract: В этой статье показано, как привязать существующий PDF, добавить поле с флажком в указанное положение и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
Использовать `FormEditorExamples.createCheckBoxField(...)` добавить поле чекбокса в PDF форму.

## Создайте поле с флажком

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Добавьте поле с флажком `FieldType.CheckBox`, название поля, заголовок, страница и прямоугольник.
3. Сохраните обновлённый документ.

```java
public static void createCheckBoxField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addField(FieldType.CheckBox, "checkbox1", "Check Box 1", 1, 240, 498, 256, 514);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```


