---
title: Добавить и удалить закладку
linktitle: Добавить и удалить закладку
type: docs
weight: 10
url: ru/cpp/add-and-delete-bookmark/
description: Эта тема объясняет, как добавить закладку в PDF документ с помощью библиотеки C++. Также вы можете удалить все или определенные закладки из PDF документа.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Добавить закладку в PDF документ

Закладки находятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/) объекта Document, которая сама находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).

Чтобы добавить закладку в PDF:

1. Откройте PDF документ, используя объект [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).
1. Создайте закладку и определите её свойства.
1. Добавьте коллекцию [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) в коллекцию Outlines.

Следующий фрагмент кода показывает, как добавить закладку в PDF-документ.

```cpp
void AddBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddBookmark.pdf");


// Создайте объект закладки

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Test Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Установите номер страницы назначения

pdfOutline->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Добавьте закладку в коллекцию контура документа.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Сохраните обновленный документ

pdfDocument->Save(_dataDir + u"AddBookmark_out.pdf");
}
```

## Добавление дочерней закладки в PDF-документ

Закладки могут быть вложенными, что указывает на иерархическую связь с родительскими и дочерними закладками. Этот документ объясняет, как добавить закладку дочернего уровня, то есть закладку второго уровня, в PDF.

Чтобы добавить закладку дочернего уровня в PDF файл, сначала добавьте закладку родительского уровня:

1. Откройте документ.
1. Добавьте закладку в [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection/), определив её свойства.
1. Добавьте OutlineItemCollection в коллекцию [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/) объекта Document.

Закладка дочернего уровня создается так же, как и закладка родительского уровня, объясненная выше, но добавляется в коллекцию Outlines родительской закладки.

Следующие фрагменты кода показывают, как добавить закладку дочернего уровня в PDF документ.

```cpp
void AddChildBookmark() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Открыть документ

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddChildBookmark.pdf");


// Создать объект закладки родительского уровня

auto pdfOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfOutline->set_Title(u"Parent Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);


// Создать объект закладки дочернего уровня

auto pdfChildOutline = MakeObject<OutlineItemCollection>(pdfDocument->get_Outlines());

pdfChildOutline->set_Title(u"Child Outline");

pdfChildOutline->set_Italic(true);

pdfChildOutline->set_Bold(true);


// Добавить закладку дочернего уровня в коллекцию родительской закладки

pdfOutline->Add(pdfChildOutline);

// Добавить закладку родительского уровня в коллекцию закладок документа.

pdfDocument->get_Outlines()->Add(pdfOutline);


// Сохранить результат

pdfDocument->Save(_dataDir + u"AddChildBookmark_out.pdf");
}
```
## Удалить все закладки из PDF документа

Все закладки в PDF содержатся в коллекции [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Эта статья объясняет, как удалить все закладки из PDF файла.

Чтобы удалить все закладки из PDF файла:

1. Вызовите метод Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
1. Сохраните измененный файл, используя метод Save объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/).

Следующие фрагменты кода показывают, как удалить все закладки из PDF документа.

```cpp
void DeleteAllBookmarksFromPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Открыть документ

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteAllBookmarks.pdf");


// Удалить все закладки

pdfDocument->get_Outlines()->Delete();


// Сохранить обновленный файл

pdfDocument->Save(_dataDir + u"DeleteAllBookmarks_out.pdf");
}
```


## Удалить определенную закладку из PDF документа

[Удалить все вложения из PDF документа](https://docs.aspose.com/pdf/cpp/working-with-attachments/) показано, как удалить все вложения из PDF файла. Также возможно удалить только определенные вложения.

Чтобы удалить определенную закладку из PDF файла:

1. Передайте заголовок закладки в качестве параметра методу Delete коллекции [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/).
2. Затем сохраните обновленный файл с помощью метода Save объекта Document.

Класс [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) предоставляет коллекцию [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection/). Метод [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection#a04f36a1f4f7c4fde3189399eb046a98b) удаляет любую закладку с заголовком, переданным в метод.

Следующие примеры кода показывают, как удалить определенную закладку из PDF документа.

```cpp
void DeleteParticularBookmarkPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Открыть документ

auto pdfDocument = MakeObject<Document>(_dataDir + u"DeleteParticularBookmark.pdf");


// Удалить определенную закладку по заголовку

pdfDocument->get_Outlines()->Delete(u"Child Outline");


// Сохранить обновленный файл

pdfDocument->Save(_dataDir + u"DeleteParticularBookmark_out.pdf");
}
```