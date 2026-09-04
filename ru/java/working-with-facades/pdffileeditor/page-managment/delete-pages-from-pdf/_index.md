---
title: Удалить страницы из PDF
linktitle: Удалить страницы из PDF
type: docs
weight: 20
url: /ru/java/delete-pages-from-pdf/
description: Удалить выбранные страницы из PDF в Java с помощью фасада PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить определённые страницы из PDF‑документа с помощью Java
Abstract: Узнайте, как удалить страницы из PDF с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor для удаления заданного набора номеров страниц и сохранения оставшихся страниц в новый документ.
---
## Удалите страницы из PDF

Пример на Java удаляет страницы 2 и 4 из исходного документа.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Создайте массив с номерами страниц для удаления.
3. Вызовите `delete` с входным файлом, массивом страниц и выходным файлом.
4. Сохраните полученный PDF.

### Пример на Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```


