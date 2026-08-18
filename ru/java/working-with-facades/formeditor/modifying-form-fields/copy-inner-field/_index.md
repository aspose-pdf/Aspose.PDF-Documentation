---
title: Копировать внутреннее поле
linktitle: Копировать внутреннее поле
type: docs
weight: 70
url: /java/copy-inner-field/
description: Узнайте, как скопировать поле формы в новую позицию в том же PDF-документе на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Скопируйте поле формы PDF в том же документе в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, дублировать поле на другую страницу и в другом месте и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Скопируйте поле внутри того же PDF-файла

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `copyInnerField(...)`, указав имя исходного поля, имя нового поля, страницу и координаты.
3. Сохраните обновленный документ.

```java
public static void copyInnerField(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.copyInnerField("First Name", "First Name Copy", 2, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
