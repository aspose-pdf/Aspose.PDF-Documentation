---
title: Создание PDF-брошюры
linktitle: Создание PDF-брошюры
type: docs
weight: 20
url: /ru/java/create-pdf-booklet/
description: Создать PDF, готовый к печати в виде брошюры, из существующего документа на Java с фасадом PdfFileEditor.
lastmod: "2026-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать вывод в виде брошюры из PDF-документа на Java.
Abstract: Узнайте, как создать PDF-брошюру с помощью Aspose.PDF for Java. Пример на Java использует PdfFileEditor для переупорядочивания страниц для печати брошюры и также включает вариант, возвращающий булево значение, для простой проверки успеха.
---
## Создание PDF-брошюры

Используйте `PdfFileEditor.makeBooklet`, чтобы переставить страницы существующего PDF в порядок буклета.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Вызовите `makeBooklet` с исходным PDF и выходным файлом.
3. Сохраните документ брошюры.
4. Используйте вариант, возвращающий boolean, если требуется проверить результат операции, и обработайте неуспешный результат.

### Пример на Java

```java
public static void createPdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString());
}

public static void tryCreatePdfBooklet(Path inputFile, Path outputFile) {
    PdfFileEditor bookletMaker = new PdfFileEditor();
    if (!bookletMaker.makeBooklet(inputFile.toString(), outputFile.toString())) {
        System.out.println("Failed to create booklet.");
    }
}
```


