---
title: Установить ограничение поля
linktitle: Установить ограничение поля
type: docs
weight: 50
url: /java/set-field-limit/
description: Узнайте, как установить максимальное количество символов для поля формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установите ограничение на количество символов для поля формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, установить максимальное количество символов в поле и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите ограничение на количество символов в поле

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `setFieldLimit(...)`, чтобы узнать целевое поле и максимальное количество символов.
3. Сохраните обновленный документ.

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldLimit("First Name", 15);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
