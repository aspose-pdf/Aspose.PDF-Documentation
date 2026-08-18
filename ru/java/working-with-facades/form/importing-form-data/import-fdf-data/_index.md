---
title: Импортировать данные FDF
linktitle: Импортировать данные FDF
type: docs
weight: 10
url: /java/import-fdf-data/
description: Узнайте, как импортировать данные формы FDF в форму PDF с помощью Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Импортируйте данные AcroForm из FDF в Java
Abstract: В этой статье показано, как привязать форму PDF, импортировать значения полей из потока FDF и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.importFdf(...)`, чтобы применить значения полей из файла FDF.

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
