---
title: Удалить действие поля
linktitle: Удалить действие поля
type: docs
weight: 50
url: /ru/java/remove-field-action/
description: Узнайте, как удалить действие поля из PDF-формы в Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалить действие поля PDF-формы в Java
Abstract: В этой статье показано, как привязать существующий PDF, удалить действие, связанное с конкретным полем, и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Удалите действие поля

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызовите `removeFieldAction(...)` для целевого поля.
3. Сохраните обновлённый документ.

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


