---
title: Удалить вложения
linktitle: Удалить вложения
type: docs
weight: 50
url: /ru/java/remove-attachments/
description: Узнайте, как удалить все вложения документов из PDF на Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Удалить все вложения PDF на Java
Abstract: В этой статье показано, как привязать PDF, удалить все вложения документов и сохранить обновлённый файл, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Удалите все вложения

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Вызовите `deleteAttachments()` удалить каждое встроенное вложение.
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


