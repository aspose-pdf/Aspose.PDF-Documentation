---
title: Создание N-Up PDF документа
linktitle: Создание N-Up PDF документа
type: docs
weight: 10
url: /ru/java/create-n-up-pdf-document/
description: Создать 2x2 N-Up PDF макет в Java с фасадом PdfFileEditor.
lastmod: "2026-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать N-Up PDF макет из существующего документа на Java
Abstract: Узнайте, как создать N-Up PDF документ с помощью Aspose.PDF for Java. В примере на Java используется PdfFileEditor для размещения четырёх исходных страниц на каждом листе вывода, а также показан вариант с возвращаемым булевым значением для проверки ошибок.
---
## Создание PDF-документа с компоновкой N-Up

В примере на Java используется `PdfFileEditor.makeNUp`, чтобы создать макет 2x2 из существующего PDF.

### Шаги

1. Создайте экземпляр `PdfFileEditor`.
2. Вызовите `makeNUp` с входным файлом, выходным файлом и количеством столбцов и строк.
3. Сохраните сгенерированный документ.
4. Вызовите вариант, возвращающий булево значение, если требуется явная проверка успешности операции, и обработайте результат `false`.

### Пример на Java

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


