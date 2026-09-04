---
title: Создать поле ComboBox
linktitle: Создать поле ComboBox
type: docs
weight: 30
url: /ru/java/create-combobox-field/
description: Узнайте, как добавить поле combo box в PDF‑документ на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Создать поле combo box в PDF на Java
Abstract: Эта статья демонстрирует, как привязать существующий PDF, добавить поле combo box, заполнить его элементами и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
Использовать `FormEditorExamples.createComboBoxField(...)` создать комбобокс и добавить выбираемые элементы.

## Создайте поле combo box

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Добавьте поле combo box с его значением по умолчанию и целевым прямоугольником.
3. Добавьте выбираемые элементы combo box.
4. Сохраните обновлённый документ.

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


