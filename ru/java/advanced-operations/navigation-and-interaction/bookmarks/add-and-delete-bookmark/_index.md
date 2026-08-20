---
title: Добавление и удаление закладок PDF в Java
linktitle: Добавить и удалить закладку
type: docs
weight: 10
url: /ru/java/add-and-delete-bookmark/
description: Узнайте, как добавлять и удалять закладки в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте или удаляйте закладки в PDF‑документах с помощью Java
Abstract: В этой статье показано, как создавать и удалять закладки с помощью Aspose.PDF for Java. Примеры демонстрируют добавление закладки верхнего уровня, создание иерархии дочерних закладок, удаление всех закладок и удаление конкретной закладки по заголовку.
---
Используйте коллекцию оглавления документа для программного управления закладками.

## Добавьте закладку верхнего уровня

Используйте этот пример, когда документ должен содержать единственную запись оглавления верхнего уровня.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) и настройте его заголовок, стиль и действие.
1. Добавьте закладку в оглавление документа и сохраните файл.

```java
public static void addBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Test Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        pdfOutline.setAction(new GoToAction(document.getPages().get_Item(1)));

        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Добавьте дочернюю закладку

В этом примере создаётся родительская закладка, а дочерняя закладка помещается под ней.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте родительскую и дочернюю [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) объекты.
1. Добавьте дочерний элемент к родительскому, добавьте родительский элемент в коллекцию оглавления и сохраните документ.

```java
public static void addChildBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection pdfOutline = new OutlineItemCollection(document.getOutlines());
        pdfOutline.setTitle("Parent Outline");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(document.getOutlines());
        pdfChildOutline.setTitle("Child Outline");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        pdfOutline.add(pdfChildOutline);
        document.getOutlines().add(pdfOutline);
        document.save(outputFile.toString());
    }
}
```

## Удалите все закладки

Используйте этот подход, когда всю коллекцию оглавления следует удалить из документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите полную коллекцию оглавления.
1. Сохраните очищенный выходной файл.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Удалите конкретную закладку

Используйте этот пример, когда необходимо удалить одну именованную закладку, не очищая всё дерево оглавления.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите закладку по названию из коллекции оглавлений.
1. Сохраните обновлённый документ.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```


