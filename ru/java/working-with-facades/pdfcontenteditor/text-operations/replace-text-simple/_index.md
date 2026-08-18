---
title: Заменить текст просто
linktitle: Заменить текст просто
type: docs
weight: 10
url: /java/replace-text-simple/
description: Узнайте, как заменить текст в PDF-документе на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Заменить текст в PDF в Java
Abstract: В этой статье показано, как связать PDF-файл, настроить область замены текста, заменить все соответствующие вхождения текста и сохранить обновленный документ с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Заменить текст по всему документу

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Установите область замены текста на `ReplaceAll`.
3. Позвоните `replaceText(...)`, указав текст поиска и текст замены.
4. Сохраните обновленный PDF-документ.

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
