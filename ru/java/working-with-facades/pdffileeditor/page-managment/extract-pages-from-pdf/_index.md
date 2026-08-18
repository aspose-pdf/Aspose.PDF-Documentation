---
title: Извлечь страницы из PDF
linktitle: Извлечь страницы из PDF
type: docs
weight: 30
url: /java/extract-pages-from-pdf/
description: Извлекайте выбранные страницы из PDF-файла на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлеките выбранные страницы PDF в новый документ с помощью Java
Abstract: Узнайте, как извлекать страницы из PDF-файла с помощью Aspose.PDF для Java. В примере Java PdfFileEditor используется для сбора определенных номеров страниц и записи их в отдельный выходной PDF-файл.
---
## Извлечение страниц из PDF-файла

Пример Java извлекает страницы 1, 4 и 3 в новый документ PDF.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Определите номера страниц для извлечения.
3. Вызовите `extract` с исходным файлом, массивом страниц и выходным файлом.
4. Сохраните извлеченные страницы как новый PDF-файл.

### Пример Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```
