---
title: Установить внешний вид поля
linktitle: Установить внешний вид поля
type: docs
weight: 40
url: /java/set-field-appearance/
description: Узнайте, как изменить флаги внешнего вида поля формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Изменить флаги внешнего вида полей формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, применить к полю флаг внешнего вида и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите флаги внешнего вида поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `setFieldAppearance(...)` для целевого поля и выбранного флага аннотации.
3. Сохраните обновленный документ.

```java
public static void setFieldAppearance(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAppearance("First Name", AnnotationFlags.Hidden);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
