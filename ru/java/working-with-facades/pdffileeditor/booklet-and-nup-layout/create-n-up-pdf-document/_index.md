---
title: Создать N-Up PDF документ
linktitle: Создать N-Up PDF документ
type: docs
weight: 10
url: /ru/java/create-n-up-pdf-document/
description: Создать 2x2 N-Up PDF макет в Java с фасадом PdfFileEditor.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создать N-Up PDF макет из существующего документа на Java
Abstract: Узнайте, как создать N-Up PDF документ с помощью Aspose.PDF for Java. В примере на Java используется PdfFileEditor для размещения четырёх исходных страниц на каждом листе вывода, а также показан вариант с возвращаемым булевым значением для проверки ошибок.
---
## Создайте N-Up PDF документ

В примере на Java используется `PdfFileEditor.makeNUp` создать макет 2x2 из существующего PDF.

### Шаги

1. Создайте `PdfFileEditor` экземпляр.
2. Вызов `makeNUp` с входным файлом, выходным файлом и количеством столбцов и строк.
3. Сохраните сгенерированный документ.
4. Если вы хотите явную проверку успеха, вызовите вариант, возвращающий булево значение, и обработайте a `false` результат.

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

