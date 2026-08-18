---
title: Добавить действие документа
linktitle: Добавить действие документа
type: docs
weight: 10
url: /java/add-document-action/
description: Узнайте, как добавить действие открытия документа в PDF-файл на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Добавление действия открытия документа в PDF-файл на Java
Abstract: В этой статье показано, как привязать PDF-файл, прикрепить действие JavaScript к событию открытия документа и сохранить обновленный документ с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Добавьте действие открытия документа

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Вызовите `addDocumentAdditionalAction(...)` с событием `DOCUMENT_OPEN` и текстом действия JavaScript.
3. Сохраните обновленный PDF-документ.

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
