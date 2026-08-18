---
title: Создать PDF-документ N-Up
linktitle: Создать PDF-документ N-Up
type: docs
weight: 10
url: /java/create-n-up-pdf-document/
description: Создайте макет PDF размером 2x2 N-Up на Java с помощью фасада PdfFileEditor.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создайте макет PDF N-Up из существующего документа на Java.
Abstract: Узнайте, как создать PDF-документ N-Up с помощью Aspose.PDF для Java. В примере Java используется PdfFileEditor для размещения четырех исходных страниц на каждом выходном листе, а также показан вариант с логическим возвратом для проверки ошибок.
---
## Создайте PDF-документ N-Up

В примере Java используется `PdfFileEditor.makeNUp` для создания макета 2x2 из существующего PDF-файла.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Вызовите `makeNUp`, указав входной файл, выходной файл и количество столбцов и строк.
3. Сохраните созданный документ.
4. Если вам нужна явная проверка успеха, вызовите вариант с логическим возвратом и обработайте результат `false`.

### Пример Java

```java
public static void createNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2);
}

public static void tryCreateNupPdfDocument(Path inputFile, Path outputFile) {
    PdfFileEditor nupMaker = new PdfFileEditor();
    if (!nupMaker.makeNUp(inputFile.toString(), outputFile.toString(), 2, 2)) {
        System.out.println("Failed to create N-Up PDF document.");
    }
}
```
