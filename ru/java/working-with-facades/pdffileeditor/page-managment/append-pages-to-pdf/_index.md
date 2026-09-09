---
title: Добавить страницы в PDF
linktitle: Добавить страницы в PDF
type: docs
weight: 10
url: /ru/java/append-pages-to-pdf/
description: Добавлять страницы из одного PDF в другой на Java с помощью фасада PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить диапазон страниц из одного PDF‑документа в другой с помощью Java.
Abstract: Узнайте, как добавлять страницы в PDF с помощью Aspose.PDF for Java. В примере на Java используется PdfFileEditor для добавления выбранного диапазона страниц из другого документа в конец текущего PDF.
---
## Добавьте страницы в PDF

В примере на Java страница 1 из второго PDF добавляется в конец первого документа.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Привяжите основной входной PDF, передав его путь к `append`.
3. Укажите список вторичных исходных файлов и диапазон страниц для добавления.
4. Сохраните объединённый результат в выходной файл.

### Пример на Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```


