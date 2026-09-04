---
title: Импорт данных XML
linktitle: Импорт данных XML
type: docs
weight: 40
url: /ru/java/import-xml-data/
description: Узнайте, как импортировать данные формы XML в PDF-форму с помощью Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Импорт данных AcroForm из XML в Java
Abstract: Эта статья показывает, как привязать PDF-форму, импортировать значения полей из XML-потока и сохранить обновлённый документ с использованием фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.importXml(...)` заполнить форму данными из XML.

```java
public static void importXml(Path inputFile, Path dataFile, Path outputFile) throws Exception {
    Form form = new Form();
    try (InputStream inputStream = Files.newInputStream(dataFile)) {
        form.bindPdf(inputFile.toString());
        form.importXml(inputStream);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```


