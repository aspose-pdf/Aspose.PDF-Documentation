---
title: Перемещение страниц PDF в Java
linktitle: Перемещение PDF-страниц
type: docs
weight: 100
url: /java/move-pages/
description: Узнайте, как перемещать страницы PDF внутри документа или между документами в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Перемещение страниц PDF между документами в Java
Abstract: В этой статье объясняется, как перемещать страницы в PDF-файлах с помощью Aspose.PDF для Java. Он охватывает перемещение одной или нескольких страниц в другой документ, а также изменение положения страницы внутри того же PDF-файла.
---
Aspose.PDF для Java позволяет перемещать страницы между документами или перемещать страницы в одном PDF-файле.

## Переместить страницу в другой документ

Используйте этот пример, когда одну страницу необходимо удалить из исходного PDF-файла и сохранить в отдельный документ.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Добавьте целевую страницу в место назначения и удалите ее из источника.
1. Сохраните оба документа.

```java
public static void movePageFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString());
         Document anotherDocument = new Document()) {
        anotherDocument.getPages().add(document.getPages().get_Item(2));
        document.getPages().delete(2);
        document.save(sourceOutputFile.toString());
        anotherDocument.save(outputFile.toString());
    }
}
```

## Переместить несколько страниц в другой документ

Используйте этот пример, когда необходимо перенести несколько страниц из исходного PDF-файла в новый документ.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Скопируйте выбранные страницы в целевой документ.
1. Удалите перемещенные страницы из источника и сохраните оба файла.

```java
public static void moveBunchPagesFromOneDocumentToAnother(Path inputFile, Path sourceOutputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString());
         Document dstDocument = new Document()) {
        Integer[] pages = {1, 2};
        for (Integer pageIndex : pages) {
            dstDocument.getPages().add(srcDocument.getPages().get_Item(pageIndex));
        }
        dstDocument.save(outputFile.toString());
        srcDocument.getPages().delete(pages);
        srcDocument.save(sourceOutputFile.toString());
    }
}
```

## Перемещение страницы в том же документе

Используйте этот пример, когда страницу необходимо переместить в новое место в том же PDF-файле.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Дублируйте целевую страницу в новом положении и удалите запись исходной страницы.
1. Сохраните переупорядоченный документ.

```java
public static void movePageInNewLocationInSameDocument(Path inputFile, Path outputFile) {
    try (Document srcDocument = new Document(inputFile.toString())) {
        srcDocument.getPages().add(srcDocument.getPages().get_Item(2));
        srcDocument.getPages().delete(2);
        srcDocument.save(outputFile.toString());
    }
}
```
