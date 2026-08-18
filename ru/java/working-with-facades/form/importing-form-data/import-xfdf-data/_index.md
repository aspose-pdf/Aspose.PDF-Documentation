---
title: Импортировать данные XFDF
linktitle: Импортировать данные XFDF
type: docs
weight: 20
url: /java/import-xfdf-data/
description: Узнайте, как импортировать данные формы XFDF в форму PDF с помощью Java, используя фасад формы в Aspose.PDF.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Импортируйте данные AcroForm из XFDF в Java
Abstract: В этой статье показано, как привязать форму PDF, импортировать значения полей из потока XFDF и сохранить обновленный документ с фасадом формы в Aspose.PDF для Java.
---
Используйте `FormExamples.importXfdf(...)`, чтобы заполнить форму данными XFDF.

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
