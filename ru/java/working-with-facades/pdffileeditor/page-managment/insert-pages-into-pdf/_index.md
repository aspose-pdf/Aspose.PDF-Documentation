---
title: Вставить страницы в PDF
linktitle: Вставить страницы в PDF
type: docs
weight: 40
url: /ru/java/insert-pages-into-pdf/
description: Вставить выбранные страницы из одного PDF в другой в Java с фасадом PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Вставить страницы из другого PDF в выбранную позицию с помощью Java
Abstract: Узнайте, как вставлять страницы в PDF с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor для вставки выбранных страниц из второго документа после указанного номера страницы в целевом PDF.
---
## Вставьте страницы в PDF

Пример на Java вставляет страницы 1 и 2 из вторичного документа после страницы 2 целевого PDF.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Выберите точку вставки в целевом документе.
3. Выберите номера страниц для копирования из исходного документа.
4. Вызовите `insert` с целевым файлом, точкой вставки, исходным файлом, массивом страниц и файлом вывода.
5. Сохраните обновлённый PDF.

### Пример Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```


