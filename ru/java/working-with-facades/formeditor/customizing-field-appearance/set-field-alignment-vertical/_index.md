---
title: Установить вертикальное выравнивание поля
linktitle: Установить вертикальное выравнивание поля
type: docs
weight: 30
url: /java/set-field-alignment-vertical/
description: Узнайте, как установить вертикальное выравнивание для поля формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Установите вертикальное выравнивание для поля формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, установить вертикальное выравнивание полей и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Установите вертикальное выравнивание поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `setFieldAlignmentV(...)`, чтобы узнать целевое поле и желаемую константу вертикального выравнивания.
3. Сохраните обновленный документ.

```java
public static void setFieldAlignmentVertical(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setFieldAlignmentV("First Name", FormFieldFacade.ALIGN_BOTTOM);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
