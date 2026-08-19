---
title: Добавить вложение
linktitle: Добавить вложение
type: docs
weight: 10
url: /ru/java/add-attachment/
description: Узнайте, как прикрепить внешний файл к документу PDF на Java, используя фасад PdfContentEditor в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Добавить файловое вложение в PDF на Java
Abstract: В этой статье показано, как привязать PDF, открыть вложение как поток, добавить документное вложение с описанием и сохранить обновлённый файл, используя фасад PdfContentEditor в Aspose.PDF for Java.
---
## Добавьте документное вложение

1. Привяжите исходный PDF к `PdfContentEditor` фасад.
2. Откройте файл вложения как поток ввода.
3. Вызов `addDocumentAttachment(...)` с потоком, именем файла и описанием.
4. Сохраните обновлённый PDF‑документ.

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

