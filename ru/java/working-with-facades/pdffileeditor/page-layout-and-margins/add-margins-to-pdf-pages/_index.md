---
title: Добавьте поля на страницы PDF
linktitle: Добавьте поля на страницы PDF
type: docs
weight: 10
url: /java/add-margins-to-pdf-pages/
description: Добавьте поля к выбранным страницам PDF в Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте поля к определенным страницам PDF-документа с помощью Java
Abstract: Узнайте, как добавить поля к выбранным страницам с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor для определения отдельных номеров страниц и применения одинаковых значений верхнего, нижнего, левого и правого полей.
---
## Добавление полей на страницы PDF

В примере Java к страницам 1 и 3 исходного документа добавляются поля толщиной 36 пунктов.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Выберите номера страниц, для которых должны быть новые поля.
3. Вызовите `addMargins`, указав входной файл, выходной файл, список страниц и значения полей.
4. Сохраните обновленный PDF-файл.

### Пример Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```
