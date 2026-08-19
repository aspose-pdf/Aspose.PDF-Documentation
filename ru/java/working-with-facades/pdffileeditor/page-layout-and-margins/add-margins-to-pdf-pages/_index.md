---
title: Добавить поля к страницам PDF
linktitle: Добавить поля к страницам PDF
type: docs
weight: 10
url: /ru/java/add-margins-to-pdf-pages/
description: Добавить поля к выбранным страницам PDF в Java с фасадом PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить поля к определённым страницам в PDF‑документе с помощью Java
Abstract: Узнайте, как добавить поля к выбранным страницам с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor для указания отдельных номеров страниц и применения одинаковых значений полей сверху, снизу, слева и справа.
---
## Добавьте поля к страницам PDF

Пример на Java добавляет поля в 36 пунктов к страницам 1 и 3 исходного документа.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Выберите номера страниц, которым следует добавить новые отступы.
3. Вызов `addMargins` с входным файлом, выходным файлом, списком страниц и значениями полей.
4. Сохраните обновлённый PDF.

### Пример на Java

```java
public static void addMarginsToPdfPages(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addMargins(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 36, 36, 36, 36);
}
```

