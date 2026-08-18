---
title: Переименовать поле
linktitle: Переименовать поле
type: docs
weight: 50
url: /java/rename-field/
description: Узнайте, как переименовать существующее поле формы в PDF-документе на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Переименуйте поле формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, переименовать указанное поле и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Переименование поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `renameField(...)`, указав текущее имя поля и новое имя поля.
3. Сохраните обновленный документ.

```java
public static void renameField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.renameField("City", "Town");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
