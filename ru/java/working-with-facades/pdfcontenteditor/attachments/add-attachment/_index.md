---
title: Добавить вложение
linktitle: Добавить вложение
type: docs
weight: 10
url: /java/add-attachment/
description: Узнайте, как прикрепить внешний файл к PDF-документу на Java с помощью фасада PdfContentEditor в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Добавить вложение файла в PDF в Java
Abstract: В этой статье показано, как связать PDF-файл, открыть вложение в виде потока, добавить вложение документа с описанием и сохранить обновленный файл с помощью фасада PdfContentEditor в Aspose.PDF для Java.
---
## Добавьте вложение документа

1. Привяжите исходный PDF-файл к фасаду `PdfContentEditor`.
2. Откройте вложенный файл как входной поток.
3. Вызовите `addDocumentAttachment(...)`, указав поток, имя файла и описание.
4. Сохраните обновленный PDF-документ.

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
