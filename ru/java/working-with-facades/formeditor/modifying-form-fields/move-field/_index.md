---
title: Переместить поле
linktitle: Переместить поле
type: docs
weight: 30
url: /java/move-field/
description: Узнайте, как переместить существующее поле формы в PDF-документе на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Переместите поле формы PDF в новую позицию в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, переместить поле в новые координаты и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Переместить поле

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `moveField(...)`, указав имя целевого поля и координаты нового прямоугольника.
3. Сохраните обновленный документ.

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
