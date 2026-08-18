---
title: Изменить настройки просмотра
linktitle: Изменить настройки просмотра
type: docs
weight: 20
url: /java/change-viewer-preferences/
description: Узнайте, как изменить настройки просмотра PDF-документа на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Изменить настройки просмотра PDF в Java
Abstract: В этой статье показано, как привязать PDF-файл, изменить текущее значение предпочтений средства просмотра и сохранить обновленный документ с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Изменение предпочтений зрителя

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Прочтите текущее значение предпочтений зрителя.
3. Объедините его с нужным дополнительным флагом и передайте результат `changeViewerPreference(...)`.
4. Сохраните обновленный PDF-документ.

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
