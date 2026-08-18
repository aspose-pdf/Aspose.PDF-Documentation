---
title: От одного к нескольким
linktitle: От одного к нескольким
type: docs
weight: 60
url: /java/single-to-multiple/
description: Узнайте, как преобразовать однострочное текстовое поле в многострочное поле в PDF-документе на Java с помощью фасада FormEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Преобразование однострочного поля PDF в многострочное в Java
Abstract: В этой статье показано, как связать существующий PDF-файл, преобразовать однострочное поле в многострочное и сохранить обновленный документ с помощью фасада FormEditor в Aspose.PDF для Java.
---
## Преобразование однострочного поля в несколько строк

1. Привяжите исходный PDF-файл к фасаду `FormEditor`.
2. Вызовите `single2Multiple(...)`, чтобы узнать имя целевого поля.
3. Сохраните обновленный документ.

```java
public static void singleToMultiple(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.single2Multiple("City");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
