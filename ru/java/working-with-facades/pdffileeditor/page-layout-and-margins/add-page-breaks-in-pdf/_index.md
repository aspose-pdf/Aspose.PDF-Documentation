---
title: Добавить разрывы страниц в PDF
linktitle: Добавить разрывы страниц в PDF
type: docs
weight: 20
url: /java/add-page-breaks-in-pdf/
description: Вставка разрывов страниц в PDF-файл на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Вставка разрывов страниц в фиксированных позициях в PDF-документе с помощью Java
Abstract: Узнайте, как добавлять разрывы страниц с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor.PageBreak для разделения страницы в определенном вертикальном положении и сохранения результата в виде нового PDF-файла.
---
## Добавьте разрывы страниц в PDF

Используйте этот рабочий процесс, когда страницу необходимо разделить на несколько страниц в известной позиции Y.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Создайте одну или несколько записей `PdfFileEditor.PageBreak` с номером страницы и местом разрыва.
3. Передайте массив разрывов страниц в `addPageBreak`.
4. Сохраните обновленный PDF-документ.

### Пример Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
