---
title: Получить настройки зрителя
linktitle: Получить настройки зрителя
type: docs
weight: 10
url: /java/get-viewer-preferences/
description: Узнайте, как прочитать настройки просмотра PDF-документа на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Чтение настроек просмотра PDF-файлов в Java
Abstract: В этой статье показано, как связать PDF-файл и распечатать текущее значение предпочтений средства просмотра с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Получите текущие предпочтения зрителя

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Вызовите `getViewerPreference()`, чтобы прочитать текущее значение.
3. Проверьте или распечатайте возвращенный флаг предпочтений.

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
