---
title: Вставить страницы в PDF
linktitle: Вставить страницы в PDF
type: docs
weight: 40
url: /java/insert-pages-into-pdf/
description: Вставляйте выбранные страницы из одного PDF-файла в другой на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Вставьте страницы из другого PDF-файла в выбранную позицию с помощью Java
Abstract: Узнайте, как вставлять страницы в PDF-файл с помощью Aspose.PDF для Java. В примере Java PdfFileEditor используется для вставки выбранных страниц из второго документа после заданного номера страницы в целевой PDF-файл.
---
## Вставка страниц в PDF

В примере Java страницы 1 и 2 из вторичного документа вставляются после страницы 2 целевого PDF-файла.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Выберите точку вставки в целевой документ.
3. Выберите номера страниц для копирования из исходного документа.
4. Вызовите `insert` с целевым файлом, точкой вставки, исходным файлом, массивом страниц и выходным файлом.
5. Сохраните обновленный PDF-файл.

### Пример Java

```java
public static void insertPagesIntoPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.insert(inputFile.toString(), 2, sampleFile.toString(), new int[] {1, 2}, outputFile.toString());
}
```
