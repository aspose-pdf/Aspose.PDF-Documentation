---
title: Добавить резиновый штамп
linktitle: Добавить резиновый штамп
type: docs
weight: 10
url: /java/add-rubber-stamp/
description: Узнайте, как добавить аннотацию штампа в PDF-документ на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Добавление штампа в PDF-файл на Java
Abstract: В этой статье показано, как связать PDF-файл, создать штамп с текстом и цветом метки и сохранить обновленный документ с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Добавьте штамп

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Позвоните `createRubberStamp(...)` и сообщите номер страницы, прямоугольник, заголовок, содержание и цвет.
3. Сохраните обновленный PDF-документ.

```java
public static void addRubberStamp(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.createRubberStamp(1, new Rectangle(120, 450, 180, 60), "Approved", "Approved by reviewer", Color.GREEN);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
