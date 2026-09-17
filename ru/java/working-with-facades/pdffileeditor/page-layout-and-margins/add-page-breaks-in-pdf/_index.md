---
title: Добавление разрывов страниц в PDF
linktitle: Добавление разрывов страниц в PDF
type: docs
weight: 20
url: /ru/java/add-page-breaks-in-pdf/
description: Вставить разрывы страниц в PDF на Java с фасадом PdfFileEditor.
lastmod: "2026-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Вставить разрывы страниц в фиксированных позициях в документе PDF с помощью Java
Abstract: Узнайте, как добавить разрывы страниц с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor.PageBreak для разбиения страницы в определённой вертикальной позиции и сохранения результата как нового PDF.
---
## Добавление разрывов страниц в PDF

Используйте этот Workflow, когда страницу необходимо разбить на несколько страниц в известной позиции Y.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Создайте одну или несколько записей `PdfFileEditor.PageBreak` с номером страницы и позицией разрыва.
3. Передайте массив разрывов страниц в `addPageBreak`.
4. Сохраните обновлённый PDF‑документ.

### Пример на Java

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```


