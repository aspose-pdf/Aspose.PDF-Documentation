---
title: Переместить страницы PDF в Java
linktitle: Перемещение страниц PDF
type: docs
weight: 100
url: /ru/java/move-pages/
description: Узнайте, как перемещать страницы PDF внутри документа или между документами в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Переместить страницы PDF между документами в Java
Abstract: В этой статье объясняется, как перемещать страницы в PDF с помощью Aspose.PDF for Java. Описывается перемещение одной страницы или нескольких страниц в другой документ, а также переустановка страницы внутри того же PDF.
---
Aspose.PDF for Java позволяет перемещать страницы между документами или переустанавливать страницы внутри того же PDF.

## Переместить страницу в другой документ

Используйте этот пример, когда одну страницу следует удалить из исходного PDF и сохранить в отдельный документ.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Добавьте целевую страницу в назначение и удалите её из источника.
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

Используйте этот пример, когда несколько страниц должны быть перенесены из исходного PDF в новый документ.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и создайте целевой документ.
1. Скопируйте выбранные страницы в целевой документ.
1. Удалите перемещённые страницы из исходного документа и сохраните оба файла.

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

## Переместить страницу внутри того же документа

Используйте этот пример, когда страницу нужно переместить в новое место в том же PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Дублируйте целевую страницу в новое положение и удалите исходный элемент страницы.
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


