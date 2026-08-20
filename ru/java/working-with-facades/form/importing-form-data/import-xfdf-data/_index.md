---
title: Импорт данных XFDF
linktitle: Импорт данных XFDF
type: docs
weight: 20
url: /ru/java/import-xfdf-data/
description: Узнайте, как импортировать данные формы XFDF в PDF-форму с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Импорт данных AcroForm из XFDF на Java
Abstract: В этой статье показано, как привязать PDF-форму, импортировать значения полей из потока XFDF и сохранить обновлённый документ с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.importXfdf(...)` заполнить форму данными XFDF.

```java
public static void importXfdf(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXfdf(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```


