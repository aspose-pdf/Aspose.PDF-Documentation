---
title: Добавить и Удалить Закладку
linktitle: Добавить и Удалить Закладку
type: docs
weight: 10
url: /java/add-and-delete-bookmark/
description: Вы можете добавить закладку в PDF-документ с помощью Java. Возможно удалить все или определенные закладки из PDF-документа.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавление Закладки в PDF-Документ

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) объекта Document, которая находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).

Чтобы добавить закладку в PDF:

1. Откройте PDF-документ, используя объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Создайте закладку и определите ее свойства.
1. Добавьте коллекцию [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в PDF-документ.

```java
package com.aspose.pdf.examples;

import java.io.IOException;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.Bookmark;
import com.aspose.pdf.facades.Bookmarks;
import com.aspose.pdf.facades.PdfBookmarkEditor;

public class ExampleBookmarks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Bookmarks/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Bookmarks\\";
        return _dataDir;
    }

    public static void AddBookmarks() throws IOException {

        Document pdfDocument = new Document(GetDataDir() + "AddBookmark.pdf");

        // Создать объект закладки
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Тестовая закладка");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Установить номер страницы назначения
        pdfOutline.setAction(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Добавить закладку в коллекцию закладок документа.
        pdfDocument.getOutlines().add(pdfOutline);

        // Сохранить обновленный документ
        pdfDocument.save(_dataDir + "AddBookmark_out.pdf");
    }
```


## Добавление дочерней закладки в PDF-документ

Закладки могут быть вложенными, что указывает на иерархическую связь с родительскими и дочерними закладками. В этой статье объясняется, как добавить дочернюю закладку, то есть закладку второго уровня, в PDF.

Чтобы добавить дочернюю закладку в PDF-файл, сначала добавьте родительскую закладку:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection), определив ее свойства.
1. Добавьте OutlineItemCollection в коллекцию [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) объекта Document.

Дочерняя закладка создается так же, как и родительская закладка, объясненная выше, но добавляется в коллекцию Outlines родительской закладки.

Следующие фрагменты кода показывают, как добавить дочернюю закладку в PDF-документ.

```java
    public static void AddChildBookmark() {
        // Открыть документ
        Document pdfDocument = new Document(GetDataDir() + "AddChildBookmark.pdf");

        // Создать объект родительской закладки
        OutlineItemCollection pdfOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfOutline.setTitle("Родительская закладка");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);

        // Создать объект дочерней закладки
        OutlineItemCollection pdfChildOutline = new OutlineItemCollection(pdfDocument.getOutlines());
        pdfChildOutline.setTitle("Дочерняя закладка");
        pdfChildOutline.setItalic(true);
        pdfChildOutline.setBold(true);

        // Добавить дочернюю закладку в коллекцию родительской закладки
        pdfOutline.add(pdfChildOutline);
        // Добавить родительскую закладку в коллекцию закладок документа.
        pdfDocument.getOutlines().add(pdfOutline);

        // Сохранить результат
        pdfDocument.save(_dataDir + "AddChildBookmark_out.pdf");
    }
```


## Удалить все закладки из PDF документа

Все закладки в PDF содержатся в коллекции [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). В этой статье объясняется, как удалить все закладки из PDF файла.

Чтобы удалить все закладки из PDF файла:

1. Вызовите метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
1. Сохраните измененный файл, используя метод Save объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующие фрагменты кода показывают, как удалить все закладки из PDF документа.

```java
    public static void DeleteAllBookmarksFromPDFDocument() {
        // Открыть документ
        Document pdfDocument = new Document(GetDataDir() + "DeleteAllBookmarks.pdf");

        // Удалить все закладки
        pdfDocument.getOutlines().delete();

        // Сохранить обновленный файл
        pdfDocument.save(_dataDir + "DeleteAllBookmarks_out.pdf");
    }
```


## Удалить определенную закладку из PDF документа

[Удалить все вложения из PDF документа](https://docs.aspose.com/pdf/java/working-with-attachments/) показано, как удалить все вложения из PDF файла. Также возможно удалять только определенные вложения.

Чтобы удалить конкретную закладку из PDF файла:

1. Передайте заголовок закладки в качестве параметра методу [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) коллекции [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection).
2. Затем сохраните обновленный файл с помощью метода Save объекта Document.

Класс [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) предоставляет коллекцию [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Метод [Delete](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection#delete--) удаляет любую закладку с заголовком, переданным методу.

Следующие фрагменты кода показывают, как удалить конкретную закладку из PDF документа.

```java
    public static void DeleteParticularBookmarkPDFDocument() {
        // Открыть документ
        Document pdfDocument = new Document(GetDataDir() + "DeleteParticularBookmark.pdf");

        // Удалить конкретный элемент по заголовку
        pdfDocument.getOutlines().delete("Child Outline");

        // Сохранить обновленный файл
        pdfDocument.save(_dataDir + "DeleteParticularBookmark_out.pdf");
    }
```