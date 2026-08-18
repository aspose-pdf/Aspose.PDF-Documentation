---
title: Создать поле флажка
linktitle: Создать поле флажка
type: docs
weight: 20
url: /java/create-checkbox-field/
description: Узнайте, как добавить поле формы флажка в PDF-документ на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Создайте поле флажка в PDF-файле с помощью Java
Abstract: В этой статье показано, как связать существующий PDF-файл, добавить поле флажка в указанную позицию и сохранить измененный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
Используйте `FormEditorExamples.createCheckBoxField(...)`, чтобы добавить поле флажка в форму PDF.

## Создайте поле флажка

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Добавьте поле флажка с `FieldType.CheckBox`, именем поля, заголовком, страницей и прямоугольником.
3. Сохраните обновленный документ.

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
