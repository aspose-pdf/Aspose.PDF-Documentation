---
title: Добавить страницы в PDF
linktitle: Добавить страницы в PDF
type: docs
weight: 10
url: /java/append-pages-to-pdf/
description: Добавляйте страницы из одного PDF-файла в другой на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте диапазон страниц из одного PDF-документа в другой с помощью Java
Abstract: Узнайте, как добавлять страницы в PDF-файл с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor для добавления выбранного диапазона страниц из другого документа в конец текущего PDF-файла.
---
## Добавьте страницы в PDF

В примере Java страница 1 из второго PDF-файла добавляется в конец первого документа.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Привяжите основной входной PDF-файл, передав его путь к `append`.
3. Укажите список файлов вторичного источника и диапазон страниц для добавления.
4. Сохраните объединенный результат в выходной файл.

### Пример Java

```java
public static void appendPagesToPdf(Path inputFile, Path sampleFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.append(inputFile.toString(), new String[] {sampleFile.toString()}, 1, 1, outputFile.toString());
}
```
