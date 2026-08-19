---
title: Извлечение страниц PDF в Java
linktitle: Извлечение страниц PDF
type: docs
weight: 80
url: /ru/java/extract-pages/
description: Узнайте, как извлекать отдельные или несколько страниц PDF в новые файлы на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлекать страницы PDF в новые документы с Java
Abstract: В этой статье объясняется, как извлекать страницы из PDF‑файлов с помощью Aspose.PDF for Java. Описывается копирование одной страницы и извлечение нескольких страниц в отдельный конечный документ с использованием нумерации страниц, начинающейся с 1.
---
Aspose.PDF for Java позволяет копировать выбранные страницы в новый конечный документ.

## Извлеките одну страницу

Используйте этот пример, когда необходимо сохранить одну страницу из исходного PDF в отдельный документ.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Скопируйте целевую страницу в коллекцию страниц назначения.
1. Сохраните новый PDF.

```java
public static void extractPage(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        dstDocument.getPages().add(srcDocument.getPages().get_Item(2));
        dstDocument.save(outputFile.toString());
    }
}
```

## Извлеките несколько страниц

Используйте этот пример, когда нужно скопировать несколько страниц в отдельный PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Пройдите по выбранным индексам страниц и добавьте их в конечный документ.
1. Сохраните документ с извлечёнными страницами.

```java
public static void extractBunchPages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        Integer[] pages = {2, 3};
        for (Integer pageIndex : pages) {
            anotherDocument.getPages().add(document.getPages().get_Item(pageIndex));
        }
        anotherDocument.save(outputFile.toString());
    }
}
```

