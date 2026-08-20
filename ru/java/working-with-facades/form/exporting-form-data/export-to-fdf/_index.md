---
title: Экспорт в FDF
linktitle: Экспорт в FDF
type: docs
weight: 10
url: /ru/java/export-to-fdf/
description: Узнайте, как экспортировать значения полей формы PDF в FDF на Java, используя фасад Form в Aspose.PDF.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Экспортировать данные AcroForm в FDF на Java
Abstract: В этой статье показано, как привязать форму PDF и экспортировать её данные полей в поток FDF с помощью фасада Form в Aspose.PDF for Java.
---
Использовать `FormExamples.exportFdf(...)` когда вам нужно сериализовать данные полей AcroForm в FDF.

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


