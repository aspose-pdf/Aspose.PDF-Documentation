---
title: Изменение размера содержимого страницы PDF
linktitle: Изменение размера содержимого страницы PDF
type: docs
weight: 30
url: /java/resize-pdf-page-contents/
description: Измените размер содержимого на выбранных страницах PDF в Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Изменение размера существующего содержимого страницы в PDF-документе с помощью Java
Abstract: Узнайте, как изменить размер содержимого страницы с помощью Aspose.PDF для Java. В примере Java PdfFileEditor используется для ориентации на определенные страницы, применения новой ширины и высоты содержимого и остановки рабочего процесса в случае сбоя операции изменения размера.
---
## Изменение размера содержимого страницы PDF

В примере Java изменяется размер области содержимого на страницах 1 и 3 и проверяется возвращаемое логическое значение.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Выберите страницы, размер содержимого которых необходимо изменить.
3. Вызовите `resizeContents`, указав целевую ширину и высоту.
4. Прежде чем продолжить, проверьте возвращаемое значение и обработайте ошибку.
5. Сохраните обновленный документ.

### Пример Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
