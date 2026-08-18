---
title: Установить выравнивание поля
linktitle: Установить выравнивание поля
type: docs
weight: 20
url: /java/set-field-alignment/
description: Узнайте, как настроить горизонтальное выравнивание текста для поля формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установить выравнивание полей формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, установить горизонтальное выравнивание полей и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите горизонтальное выравнивание поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `setFieldAlignment(...)`, чтобы узнать целевое поле и желаемую константу выравнивания.
3. Сохраните обновленный документ.

```java
public static void setFieldAlignment(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignment("First Name", FormFieldFacade.ALIGN_CENTER);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
