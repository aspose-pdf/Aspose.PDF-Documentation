---
title: Удалить открытое действие
linktitle: Удалить открытое действие
type: docs
weight: 20
url: /java/remove-open-action/
description: Узнайте, как удалить действие открытия документа из PDF-файла на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Удалить действие открытия PDF-документа в Java
Abstract: В этой статье показано, как связать PDF-файл, удалить действие открытия документа и сохранить обновленный документ с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Удалите действие открытия документа

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Позвоните `removeDocumentOpenAction()`.
3. Сохраните обновленный PDF-документ.

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
