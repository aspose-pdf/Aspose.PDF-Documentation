---
title: Удалить страницы из PDF
linktitle: Удалить страницы из PDF
type: docs
weight: 20
url: /java/delete-pages-from-pdf/
description: Удалите выбранные страницы из PDF-файла на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удаление определенных страниц из PDF-документа с помощью Java
Abstract: Узнайте, как удалять страницы из PDF-файла с помощью Aspose.PDF для Java. В примере Java PdfFileEditor используется для удаления определенного набора номеров страниц и сохранения оставшихся страниц как нового документа.
---
## Удаление страниц из PDF-файла

В примере Java из исходного документа удалены страницы 2 и 4.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Создайте массив с номерами страниц, которые нужно удалить.
3. Вызовите `delete` с входным файлом, массивом страниц и выходным файлом.
4. Сохраните полученный PDF-файл.

### Пример Java

```java
public static void deletePagesFromPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.delete(inputFile.toString(), new int[] {2, 4}, outputFile.toString());
}
```
