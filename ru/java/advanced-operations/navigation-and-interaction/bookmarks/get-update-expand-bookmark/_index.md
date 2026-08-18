---
title: Получайте, обновляйте и расширяйте закладки PDF в Java
linktitle: Получить, обновить и расширить закладку
type: docs
weight: 20
url: /java/get-update-and-expand-bookmark/
description: Узнайте, как получать, обновлять и расширять закладки в документах PDF с помощью Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка свойств закладок и расширение контуров в файлах PDF с помощью Java
Abstract: В этой статье объясняется, как читать, обновлять и расширять закладки с помощью Aspose.PDF для Java. Он охватывает перебор элементов структуры, извлечение номеров страниц закладок с помощью PdfBookmarkEditor, чтение дочерних закладок, обновление заголовков и стилей закладок, а также принудительное открытие структур при отображении документа.
---
Aspose.PDF для Java предоставляет закладки как через модель структуры документа, так и через фасад `PdfBookmarkEditor`.

## Получите свойства закладки

Используйте этот пример, когда вам нужно проверить записи закладок верхнего уровня в структуре документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать коллекцию контуров.
1. Прочтите и распечатайте заголовок, стиль и значения цвета закладки.

```java
public static void getBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
        }
    }
}
```

## Получите номера страниц закладок

В этом примере `PdfBookmarkEditor` используется для извлечения заголовков, уровней, номеров страниц и действий закладок.

1. Привяжите исходный PDF-файл к [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Извлеките коллекцию закладок и просмотрите ее.
1. Распечатайте уровень, заголовок, номер страницы и информацию о действии для каждой закладки.

```java
public static void getBookmarkPageNumber(Path inputFile) {
    PdfBookmarkEditor bookmarkEditor = new PdfBookmarkEditor();
    try {
        bookmarkEditor.bindPdf(inputFile.toString());
        for (Bookmark bookmark : bookmarkEditor.extractBookmarks()) {
            String levelSeparator = "";
            for (int i = 0; i < bookmark.getLevel(); i++) {
                levelSeparator += "----";
            }

            System.out.println(levelSeparator + " Title: " + bookmark.getTitle());
            System.out.println(levelSeparator + " Page Number: " + bookmark.getPageNumber());
            System.out.println(levelSeparator + " Page Action: " + bookmark.getAction());
        }
    } finally {
        bookmarkEditor.close();
    }
}
```

## Получите дочерние закладки

Используйте этот пример, когда вам нужно проверить элементы структуры как верхнего уровня, так и вложенные.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите контуры верхнего уровня и распечатайте их свойства.
1. Обнаружьте дочерние закладки, затем просмотрите их и распечатайте их свойства.

```java
public static void getChildBookmarks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection outlineItem = document.getOutlines().get_Item(i);
            System.out.println(outlineItem.getTitle());
            System.out.println(outlineItem.getItalic());
            System.out.println(outlineItem.getBold());
            System.out.println(outlineItem.getColor());
            int count = outlineItem.size();
            if (count > 0) {
                System.out.println("Child Bookmarks");
                for (int j = 1; j <= outlineItem.size(); j++) {
                    OutlineItemCollection childOutlineItem = outlineItem.get_Item(j);
                    System.out.println(childOutlineItem.getTitle());
                    System.out.println(childOutlineItem.getItalic());
                    System.out.println(childOutlineItem.getBold());
                    System.out.println(childOutlineItem.getColor());
                }
            }
        }
    }
}
```

## Обновите закладки

Используйте этот пример, когда необходимо изменить заголовок и стиль существующей закладки.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевому элементу структуры и его дочерней закладке.
1. Обновите свойства закладки и сохраните документ.

```java
public static void updateBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OutlineItemCollection outline = document.getOutlines().get_Item(1);
        OutlineItemCollection childOutline = outline.get_Item(1);
        childOutline.setTitle("Updated Outline");
        childOutline.setItalic(true);
        childOutline.setBold(true);

        document.save(outputFile.toString());
    }
}
```

## Развернуть закладки по умолчанию

Используйте этот пример, когда панель закладок должна открыться и отображать развернутые элементы структуры при отображении документа.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Установите режим страницы для использования контуров и пометьте каждый элемент структуры как открытый.
1. Сохраните обновленный документ.

```java
public static void expandedBookmarks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setPageMode(PageMode.UseOutlines);
        for (int i = 1; i <= document.getOutlines().size(); i++) {
            OutlineItemCollection item = document.getOutlines().get_Item(i);
            item.setOpen(true);
        }
        document.save(outputFile.toString());
    }
}
```
