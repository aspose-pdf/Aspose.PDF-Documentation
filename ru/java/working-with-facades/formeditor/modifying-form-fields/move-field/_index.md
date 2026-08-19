---
title: Переместить поле
linktitle: Переместить поле
type: docs
weight: 30
url: /ru/java/move-field/
description: Узнайте, как переместить существующее поле формы в PDF‑документе на Java, используя фасад FormEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Переместить поле формы PDF в новое положение на Java
Abstract: В этой статье показано, как привязать существующий PDF, переместить поле к новым координатам и сохранить обновлённый документ, используя фасад FormEditor в Aspose.PDF for Java.
---
## Переместить поле

1. Привяжите исходный PDF к `FormEditor` фасад.
2. Вызов `moveField(...)` с именем целевого поля и новыми координатами прямоугольника.
3. Сохраните обновлённый документ.

```java
public static void moveField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.moveField("Country", 200, 600, 280, 620);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

