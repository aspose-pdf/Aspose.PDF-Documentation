---
title: Удаление вложений
linktitle: Удаление вложений
type: docs
weight: 50
url: /ru/java/remove-attachments/
description: Узнайте, как удалить все вложения документов из PDF на Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-09-17"
TechArticle: true
AlternativeHeadline: Удалить все вложения PDF на Java
Abstract: В этой статье показано, как привязать PDF, удалить все вложения документов и сохранить обновлённый файл, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Удаление всех вложений

1. Привяжите исходный PDF к фасаду `PdfContentEditor`.
2. Вызовите `deleteAttachments()`, чтобы удалить каждое встроенное вложение.
3. Сохраните обновлённый PDF‑документ.

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


