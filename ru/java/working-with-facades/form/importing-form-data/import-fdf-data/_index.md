---
title: Импорт данных FDF
linktitle: Импорт данных FDF
type: docs
weight: 10
url: /ru/java/import-fdf-data/
description: Узнайте, как импортировать данные формы FDF в PDF-форму с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Импорт данных AcroForm из FDF в Java
Abstract: В этой статье показано, как привязать PDF-форму, импортировать значения полей из потока FDF и сохранить обновлённый документ с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.importFdf(...)` применить значения полей из файла FDF.

```java
public static void importFdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importFdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

