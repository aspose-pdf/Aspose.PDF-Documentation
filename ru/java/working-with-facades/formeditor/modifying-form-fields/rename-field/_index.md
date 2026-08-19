---
title: Переименовать поле
linktitle: Переименовать поле
type: docs
weight: 50
url: /ru/java/rename-field/
description: Узнайте, как переименовать существующее поле формы в PDF‑документе на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Переименовать поле формы PDF на Java
Abstract: В этой статье показано, как привязать существующий PDF, переименовать указанное поле и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Переименовать поле

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `renameField(...)` с текущим именем поля и новым именем поля.
3. Сохраните обновлённый документ.

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

