---
title: Заменить текст состоянием
linktitle: Заменить текст состоянием
type: docs
weight: 20
url: /java/replace-text-with-state/
description: Узнайте, как заменить текст пользовательским форматированием в Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Замените текст PDF пользовательским форматированием в Java
Abstract: В этой статье показано, как связать PDF-файл, настроить собственный TextState, заменить все соответствующие вхождения текста и сохранить обновленный документ с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Заменить текст пользовательским текстовым состоянием

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Создайте и настройте `TextState` с необходимым цветом и размером шрифта.
3. Установите область замены текста на `ReplaceAll`.
4. Вызовите `replaceText(...)`, указав текст поиска, текст замены и настроенный `TextState`.
5. Сохраните обновленный PDF-документ.

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
