---
title: Удалить поле
linktitle: Удалить поле
type: docs
weight: 40
url: /ru/java/remove-field/
description: Узнайте, как удалить существующее поле формы из PDF‑документа на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалить поле формы PDF на Java
Abstract: В этой статье показано, как привязать существующий PDF, удалить указанное поле и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Удалите поле

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызовите `removeField(...)` для имени целевого поля.
3. Сохраните обновлённый документ.

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


