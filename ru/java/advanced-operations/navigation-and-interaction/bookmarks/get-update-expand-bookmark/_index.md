---
title: Получение, обновление и расширение закладки
linktitle: Получение, обновление и расширение закладки
type: docs
weight: 20
url: ru/java/get-update-and-expand-bookmark/
description: В этой статье описывается, как использовать закладки в PDF-файле. С нашей библиотекой Java вы можете получить закладки из PDF-файла, получить номер страницы закладки, обновить закладки в PDF-документе и развернуть закладки при просмотре документа.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Получение закладок

Коллекция [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) объекта [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) содержит все закладки PDF-файла. В этой статье объясняется, как получить закладки из PDF-файла и как определить, на какой странице находится конкретная закладка.

Чтобы получить закладки, пройдите по коллекции [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection) и получите каждую закладку в OutlineItemCollection.
 The OutlineItemCollection предоставляет доступ ко всем атрибутам закладки. Следующий фрагмент кода показывает, как получить закладки из PDF-файла.

```java
    public static void GettingBookmarks() {
        // Открыть документ
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Перебор всех закладок
        for (OutlineItemCollection outlineItem : (Iterable<OutlineItemCollection>) pdfDocument.getOutlines()) {
            System.out.println("Заголовок :- " + outlineItem.getTitle());
            System.out.println("Курсив :- " + outlineItem.getItalic());
            System.out.println("Жирный :- " + outlineItem.getBold());
            System.out.println("Цвет :- " + outlineItem.getColor());
        }
    }
```

## Получение номера страницы закладки

Как только вы добавили закладку, вы можете узнать, на какой странице она находится, получив ассоциированный с объектом закладки номер страницы назначения.

```java
    public static void GettingBookmarksPageNumber() {
        // Создать PdfBookmarkEditor
        PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
        // Открыть PDF-файл
        bookmarkEditor.bindPdf(GetDataDir() + "UpdateBookmarks.pdf");
        // Извлечь закладки
        Bookmarks bookmarks = bookmarkEditor.extractBookmarks();
        for (Bookmark bookmark : (Iterable<Bookmark>) bookmarks) {
            String strLevelSeprator = "";
            for (int i = 1; i < bookmark.getLevel(); i++) {
                strLevelSeprator += "---- ";
            }
            System.out.println("Заголовок :- " + strLevelSeprator + bookmark.getTitle());
            System.out.println("Номер страницы :- " + strLevelSeprator + bookmark.getPageNumber());
            System.out.println("Действие на странице :- " + strLevelSeprator + bookmark.getAction());
        }
    }
```

## Обновление закладок в PDF-документе

Чтобы обновить закладку в PDF-файле, сначала получите конкретную закладку из коллекции OutlineCollection объекта Document, указав индекс закладки. Получив закладку в объект [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection), вы можете обновить ее свойства и затем сохранить обновленный PDF-файл, используя метод Save. Следующие фрагменты кода показывают, как обновить закладки в PDF-документе.

```java
    public static void UpdateBookmarksInPDFDocument() {
        // Открыть документ
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Получить объект закладки
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);

        // Обновить объект закладки
        pdfOutline.setTitle("Обновленный контур");
        pdfOutline.setItalic(true);
        pdfOutline.setBold(true);
        // Установить целевую страницу как 2
        pdfOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Сохранить вывод
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Обновление дочерних закладок в PDF-документе

Чтобы обновить дочернюю закладку:

1. Извлеките дочернюю закладку, которую вы хотите обновить, из PDF-файла, сначала получив родительскую закладку, а затем дочернюю закладку, используя соответствующие значения индекса.
1. Сохраните обновленный PDF-файл, используя метод Save.

{{% alert color="primary" %}}

Получите закладку из коллекции OutlineCollection объекта Document, указав индекс закладки, а затем получите дочернюю закладку, указав индекс этой родительской закладки.

{{% /alert %}}

Следующий фрагмент кода показывает, как обновить дочерние закладки в PDF-документе.

```java
    public static void UpdateChildBookmarksInPDFDocument() {
        // Открыть документ
        Document pdfDocument = new Document(GetDataDir() + "UpdateBookmarks.pdf");
        // Получить объект закладки
        OutlineItemCollection pdfOutline = pdfDocument.getOutlines().get_Item(1);
        // Получить объект дочерней закладки
        OutlineItemCollection childOutline = pdfOutline.get_Item(1);

        // Обновить объект закладки
        childOutline.setTitle("Обновленная закладка");
        childOutline.setItalic(true);
        childOutline.setBold(true);
        // Установить целевую страницу как 2
        childOutline.setDestination(new GoToAction(pdfDocument.getPages().get_Item(2)));

        // Сохранить результат
        pdfDocument.save(GetDataDir() + "Bookmarkupdated_output.pdf");
    }
```


## Раскрытые закладки при просмотре документа

Закладки хранятся в коллекции [OutlineItemCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineItemCollection) объекта Document, которая, в свою очередь, находится в коллекции [OutlineCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/OutlineCollection). Однако может возникнуть необходимость, чтобы все закладки были раскрыты при просмотре PDF-файла.

Для выполнения этого требования мы можем установить открытый статус для каждого элемента контура/закладки как Open. Следующий фрагмент кода показывает, как установить открытый статус для каждой закладки как расширенной в PDF-документе.

```java
    public static void ExpandedBookmarks() {    
        Document doc = new Document(GetDataDir()+"UpdateBookmarks.pdf");
        // установить режим просмотра страницы, т.е. показать миниатюры, на весь экран, показать панель вложений
        doc.setPageMode(PageMode.UseOutlines);
        // вывести общее количество закладок в PDF-файле
        System.out.println(doc.getOutlines().size());
        // пройти через каждый элемент Outline в коллекции outlines PDF-файла
        for (int counter = 1; counter <= doc.getOutlines().size(); counter++) {
            // установить открытый статус для элемента контура
            doc.getOutlines().get_Item(counter).setOpen(true);
        }
        // сохранить PDF-файл
        doc.save(_dataDir+"Bookmarks_Expanded.pdf");
    }
```