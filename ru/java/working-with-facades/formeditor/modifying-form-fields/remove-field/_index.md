---
title: Удалить поле
linktitle: Удалить поле
type: docs
weight: 40
url: /java/remove-field/
description: Узнайте, как удалить существующее поле формы из PDF-документа на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Удалить поле формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, удалить указанное поле и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Удалите поле

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `removeField(...)`, чтобы узнать имя целевого поля.
3. Сохраните обновленный документ.

```java
public static void removeField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeField("Country");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
