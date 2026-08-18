---
title: Установить номер гребенки поля
linktitle: Установить номер гребенки поля
type: docs
weight: 60
url: /java/set-field-comb-number/
description: Узнайте, как установить гребенчатый номер для поля формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установите номер гребенки для поля формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, установить номер гребенки для поля и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите номер гребенки поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `setFieldCombNumber(...)`, чтобы узнать целевое поле и значение гребенки.
3. Сохраните обновленный документ.

```java
public static void setFieldCombNumber(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldCombNumber("textCombField", 5);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
