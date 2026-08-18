---
title: Разделить PDF до конца
linktitle: Разделить PDF до конца
type: docs
weight: 40
url: /java/split-pdf-to-end/
description: Разделите PDF-файл от выбранной страницы до конца в Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение страниц от начальной точки до конца PDF-файла с помощью Java
Abstract: Узнайте, как разделить PDF-файл до конца с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor для извлечения всех страниц, начиная со страницы 2 и до конца исходного документа.
---
## Разделить PDF до конца

Образец Java извлекает все страницы, начиная со страницы 2.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Вызовите `splitToEnd`, указав исходный файл, номер начальной страницы и выходной файл.
3. Сохраните полученный PDF-документ.

```java
public static void splitPdfToEnd(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitToEnd(inputFile.toString(), 2, outputFile.toString());
}
```
