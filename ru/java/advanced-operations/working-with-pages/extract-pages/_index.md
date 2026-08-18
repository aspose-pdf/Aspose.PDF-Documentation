---
title: Извлечение PDF-страниц в Java
linktitle: Извлечение PDF-страниц
type: docs
weight: 80
url: /java/extract-pages/
description: Узнайте, как извлечь одну или несколько страниц PDF в новые файлы на Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлекайте страницы PDF в новые документы с помощью Java
Abstract: В этой статье объясняется, как извлекать страницы из файлов PDF с помощью Aspose.PDF для Java. Он охватывает копирование одной страницы и извлечение нескольких страниц в отдельный целевой документ с использованием индексации по одной странице.
---
Aspose.PDF для Java позволяет копировать выбранные страницы в новый целевой документ.

## Извлеките одну страницу

Используйте этот пример, когда вам нужно сохранить одну страницу из исходного PDF-файла в отдельный документ.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Скопируйте целевую страницу в целевую коллекцию страниц.
1. Сохраните новый PDF-файл.

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

Используйте этот пример, если вам нужно скопировать несколько страниц в отдельный PDF-файл.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Переберите выбранные индексы страниц и добавьте их в место назначения.
1. Сохраните документ извлеченных страниц.

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
