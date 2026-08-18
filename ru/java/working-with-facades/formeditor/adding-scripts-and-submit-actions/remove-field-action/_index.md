---
title: Удалить действие поля
linktitle: Удалить действие поля
type: docs
weight: 50
url: /java/remove-field-action/
description: Узнайте, как удалить действие поля из поля формы PDF в Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Удалить действие поля формы PDF в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, удалить действие, связанное с определенным полем, и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Удаление действия поля

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `removeFieldAction(...)` для целевого поля.
3. Сохраните обновленный документ.

```java
public static void removeFieldAction(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeFieldAction("Script_Demo_Button");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
