---
title: Получить, обновить и расширить закладку
linktitle: Получить, обновить и расширить закладку
type: docs
weight: 20
url: /cpp/get-update-and-expand-bookmark/
description: Aspose.PDF для библиотеки C++ позволяет вам получать, обновлять в PDF файле с нашим.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получить закладки

Коллекция [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) объекта [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) содержит все закладки PDF файла. Эта статья объясняет, как получить закладки из PDF файла и как узнать, на какой странице находится конкретная закладка.

Чтобы получить закладки, выполните перебор коллекции [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) и получите каждую закладку в OutlineItemCollection. The OutlineItemCollection предоставляет доступ ко всем атрибутам закладки. Следующий фрагмент кода показывает, как получить закладки из PDF файла.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Open document

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Loop through all the bookmarks

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"Title :- " + outlineItem->get_Title());


Console::WriteLine(u"Is Italic :- " + outlineItem->get_Italic());


Console::WriteLine(u"Is Bold :- " + outlineItem->get_Bold());


Console::WriteLine(u"Color :- {0}", outlineItem->get_Color());

}
}
```

## Получение номера страницы закладки

После добавления закладки вы можете узнать, на какой странице она находится, получив номер страницы назначения, связанный с объектом закладки.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Create PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// Open PDF file

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// Extract bookmarks

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"Title :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"Page Number :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"Page Action :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## Обновление закладок в PDF документе

Чтобы обновить закладку в PDF файле, сначала получите конкретную закладку из коллекции OutlineCollection объекта Document, указав индекс закладки. Получив закладку в объект [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection), вы можете обновить её свойства, а затем сохранить обновленный PDF файл, используя метод Save. Примеры кода ниже показывают, как обновить закладки в PDF документе.

```cpp
void UpdateBookmarksInPDFDocument() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Открыть документ

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Получить объект закладки

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);


// Обновить объект закладки

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// Установить целевую страницу как 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Сохранить результат

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Обновление дочерних закладок в PDF-документе

Чтобы обновить дочернюю закладку:

1. Извлеките дочернюю закладку, которую вы хотите обновить, из PDF-файла, сначала получив родительскую закладку, а затем дочернюю закладку, используя соответствующие индексные значения.
1. Сохраните обновленный PDF-файл, используя метод Save.

{{% alert color="primary" %}}

Получите закладку из коллекции OutlineCollection объекта Document, указав индекс закладки, а затем получите дочернюю закладку, указав индекс этой родительской закладки.

{{% /alert %}}

Следующий фрагмент кода показывает, как обновить дочерние закладки в PDF-документе.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Open document

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Get a bookmark object

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// Get child bookmark object

auto childOutline = pdfOutline->idx_get(1);


// Update the bookmark object

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// Set the target page as 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Save output

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Расширенные закладки при просмотре документа

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) объекта Document, которая, в свою очередь, находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection). Однако у нас может возникнуть необходимость, чтобы все закладки были развернуты при просмотре PDF файла.

Чтобы выполнить это требование, мы можем установить открытый статус для каждого элемента плана/закладки как Open. Следующий фрагмент кода показывает, как установить открытый статус для каждой закладки как развернутой в PDF документе.

```cpp
void ExpandedBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");


auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// установить режим просмотра страницы, т.е. показать миниатюры, полноэкранный режим, показать панель вложений

doc->set_PageMode(PageMode::UseOutlines);

// вывести общее количество закладок в PDF файле

Console::WriteLine(doc->get_Outlines()->get_Count());

// пройти через каждый элемент Outline в коллекции планов PDF файла

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {


// установить открытый статус для элемента Outline


doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// сохранить PDF файл

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```