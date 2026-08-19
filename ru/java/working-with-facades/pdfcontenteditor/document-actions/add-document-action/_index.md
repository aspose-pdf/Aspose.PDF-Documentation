---
title: Добавить действие к документу
linktitle: Добавить действие к документу
type: docs
weight: 10
url: /ru/java/add-document-action/
description: Узнайте, как добавить действие открытия документа к PDF в Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Добавьте действие открытия документа к PDF в Java
Abstract: В этой статье показано, как привязать PDF, прикрепить действие JavaScript к событию открытия документа и сохранить обновлённый документ, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Добавьте действие открытия документа

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызов `addDocumentAdditionalAction(...)` с `DOCUMENT_OPEN` событие и текст действия JavaScript.
3. Сохраните обновлённый PDF‑документ.

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

