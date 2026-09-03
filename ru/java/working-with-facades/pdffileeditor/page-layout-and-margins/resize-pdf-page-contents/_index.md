---
title: Изменить размер содержимого страниц PDF
linktitle: Изменить размер содержимого страниц PDF
type: docs
weight: 30
url: /ru/java/resize-pdf-page-contents/
description: Изменить размер содержимого на выбранных страницах PDF в Java с помощью фасада PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Изменить размер существующего содержимого страниц в документе PDF с помощью Java
Abstract: Узнайте, как изменить размер содержимого страниц с помощью Aspose.PDF for Java. В примере на Java используется PdfFileEditor для выбора конкретных страниц, применения новой ширины и высоты содержимого и прекращения Workflow, если операция изменения размера не удалась.
---
## Измените размер содержимого страниц PDF

Пример на Java изменяет размер области содержимого на страницах 1 и 3 и проверяет булево возвращаемое значение.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Выберите страницы, содержимое которых должно быть изменено в размере.
3. Вызовите `resizeContents` с целевой шириной и высотой.
4. Проверьте возвращаемое значение и обработайте сбой перед продолжением.
5. Сохраните обновлённый документ.

### Пример Java

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```


