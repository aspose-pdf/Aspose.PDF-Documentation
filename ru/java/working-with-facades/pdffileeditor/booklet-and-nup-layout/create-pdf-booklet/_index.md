---
title: Создать PDF-буклет
linktitle: Создать PDF-буклет
type: docs
weight: 20
url: /java/create-pdf-booklet/
description: Создайте готовый PDF-файл из существующего документа на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создание буклета из PDF-документа на Java
Abstract: Узнайте, как создать PDF-буклет с помощью Aspose.PDF для Java. В примере Java PdfFileEditor используется для изменения порядка страниц для печати буклета, а также включает вариант с логическим возвратом для простой проверки успеха.
---
## Создайте PDF-буклет

Используйте `PdfFileEditor.makeBooklet`, чтобы переупорядочить страницы существующего PDF-файла в порядке буклета.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Вызовите `makeBooklet` и передайте исходный PDF-файл и выходной файл.
3. Сохраните документ буклета.
4. Если вы хотите проверить статус возврата, используйте вариант логического возврата и обработайте неудачный результат.

### Пример Java

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
