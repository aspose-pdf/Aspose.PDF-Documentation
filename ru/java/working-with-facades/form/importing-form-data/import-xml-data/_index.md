---
title: Импортировать XML-данные
linktitle: Импортировать XML-данные
type: docs
weight: 40
url: /java/import-xml-data/
description: Узнайте, как импортировать данные формы XML в форму PDF с помощью Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Импортируйте данные AcroForm из XML в Java
Abstract: В этой статье показано, как привязать форму PDF, импортировать значения полей из потока XML и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.importXml(...)`, чтобы заполнить форму данными XML.

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
