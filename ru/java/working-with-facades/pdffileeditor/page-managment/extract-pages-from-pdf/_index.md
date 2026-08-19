---
title: Извлечь страницы из PDF
linktitle: Извлечь страницы из PDF
type: docs
weight: 30
url: /ru/java/extract-pages-from-pdf/
description: Извлечь выбранные страницы из PDF в Java с фасадом PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечь выбранные страницы PDF в новый документ с помощью Java
Abstract: Узнайте, как извлечь страницы из PDF с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor для сбора определённых номеров страниц и записи их в отдельный выходной PDF.
---
## Извлеките страницы из PDF

Пример на Java извлекает страницы 1, 4 и 3 в новый PDF‑документ.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Определите номера страниц для извлечения.
3. Вызов `extract` с исходным файлом, массивом страниц и выходным файлом.
4. Сохраните извлечённые страницы как новый PDF.

### Пример на Java

```java
public static void extractPagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.extract(inputFile.toString(), new int[] {1, 4, 3}, outputFile.toString());
}
```

