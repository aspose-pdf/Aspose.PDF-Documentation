---
title: Создать поле ListBox
linktitle: Создать поле ListBox
type: docs
weight: 40
url: /ru/java/create-listbox-field/
description: Узнайте, как добавить поле списка в PDF‑документ на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Создать поле списка в PDF на Java
Abstract: В этой статье показано, как привязать существующий PDF, определить элементы списка, добавить поле списка и сохранить изменённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
Использовать `FormEditorExamples.createListBoxField(...)` создать поле списка с предопределёнными элементами.

## Создайте поле списка

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Определите доступные элементы списка с помощью `setItems(...)`.
3. Добавьте поле списка с его значением по умолчанию и прямоугольником.
4. Сохраните обновлённый документ.

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


