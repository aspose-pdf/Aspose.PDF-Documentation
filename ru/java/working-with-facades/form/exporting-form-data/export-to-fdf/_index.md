---
title: Экспорт в FDF
linktitle: Экспорт в FDF
type: docs
weight: 10
url: /java/export-to-fdf/
description: Узнайте, как экспортировать значения полей формы PDF в FDF на Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Экспорт данных AcroForm в FDF в Java
Abstract: В этой статье показано, как связать форму PDF и экспортировать данные ее полей в поток FDF с помощью фасада формы в Aspose.PDF для Java.
---
Используйте `FormExamples.exportFdf(...)`, когда вам нужно сериализовать данные поля AcroForm как FDF.

```java
public static void exportFdf(Path inputFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (OutputStream outputStream = Files.newOutputStream(outputFile)) {
        form.bindPdf(inputFile.toString());
        form.exportFdf(outputStream);
    } finally {
        form.close();
    }
}
```
