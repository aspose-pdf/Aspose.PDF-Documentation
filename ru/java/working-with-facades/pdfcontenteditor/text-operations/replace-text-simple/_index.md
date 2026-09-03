---
title: Простая замена текста
linktitle: Простая замена текста
type: docs
weight: 10
url: /ru/java/replace-text-simple/
description: Узнайте, как заменять текст во всём PDF‑документе на Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Замена текста в PDF на Java
Abstract: В этой статье показано, как привязать PDF, настроить область замены текста, заменить все соответствующие вхождения текста и сохранить обновлённый документ, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Замените текст во всём документе

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Установите область действия replace-text в `ReplaceAll`.
3. Вызовите `replaceText(...)` с текстом поиска и текстом замены.
4. Сохраните обновлённый PDF‑документ.

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


