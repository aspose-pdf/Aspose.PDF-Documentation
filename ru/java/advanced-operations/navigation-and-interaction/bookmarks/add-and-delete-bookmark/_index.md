---
title: Добавление и удаление закладок PDF в Java
linktitle: Добавить и удалить закладку
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Узнайте, как добавлять и удалять закладки в документах PDF с помощью Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавляйте или удаляйте закладки в PDF-документах с помощью Java
Abstract: В этой статье показано, как создавать и удалять закладки с помощью Aspose.PDF для Java. В примерах показано добавление закладки верхнего уровня, создание иерархии дочерних закладок, удаление всех закладок и удаление определенной закладки по заголовку.
---
Используйте коллекцию структур документов для программного управления закладками.

## Добавьте закладку верхнего уровня

Используйте этот пример, когда документ должен включать одну запись структуры верхнего уровня.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/) и настройте его заголовок, стиль и действие.
1. Добавьте закладку в контуры документа и сохраните файл.

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

В этом примере создается родительская закладка и вкладывается под нее дочерняя закладка.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте родительский и дочерний объекты [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/outlineitemcollection/).
1. Добавьте дочерний элемент к родительскому, добавьте родительский элемент в коллекцию структур и сохраните документ.

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

Используйте этот подход, когда из документа необходимо удалить всю коллекцию структур.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите полную коллекцию контуров.
1. Сохраните очищенный выходной файл.

```java
public static void deleteBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete();
        document.save(outputFile.toString());
    }
}
```

## Удалите определенную закладку

Используйте этот пример, когда необходимо удалить одну именованную закладку без очистки всего дерева структуры.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Удалите закладку по заголовку из коллекции контуров.
1. Сохраните обновленный документ.

```java
public static void deleteBookmark(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getOutlines().delete("Child Outline");
        document.save(outputFile.toString());
    }
}
```
