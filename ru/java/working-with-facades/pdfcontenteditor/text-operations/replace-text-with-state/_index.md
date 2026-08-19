---
title: Заменить текст с помощью состояния
linktitle: Заменить текст с помощью состояния
type: docs
weight: 20
url: /ru/java/replace-text-with-state/
description: Узнайте, как заменять текст с пользовательским форматированием в Java, используя фасад `PdfContentEditor` в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Заменить текст в PDF с пользовательским форматированием в Java
Abstract: В этой статье показано, как привязать PDF, настроить пользовательский TextState, заменить все вхождения соответствующего текста и сохранить обновлённый документ, используя фасад `PdfContentEditor` в Aspose.PDF for Java.
---
## Заменить текст с пользовательским состоянием текста

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Создайте и настроить `TextState` с требуемым цветом и размером шрифта.
3. Установите область замены текста на `ReplaceAll`.
4. Вызов `replaceText(...)` с текстом поиска, текстом замены и настроенными `TextState`.
5. Сохраните обновлённый PDF‑документ.

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

