---
title: Удалить вложения
linktitle: Удалить вложения
type: docs
weight: 50
url: /java/remove-attachments/
description: Узнайте, как удалить все вложения документов из PDF-файла на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Удалить все вложения PDF в Java
Abstract: В этой статье показано, как связать PDF-файл, удалить все вложения документов и сохранить обновленный файл с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Удалите все вложения

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Позвоните `deleteAttachments()`, чтобы удалить все встроенные вложения.
3. Сохраните обновленный PDF-документ.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
