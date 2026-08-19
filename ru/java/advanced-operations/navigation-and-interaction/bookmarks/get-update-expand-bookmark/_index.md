---
title: Получить, обновить и развернуть PDF‑закладки в Java
linktitle: Получить, обновить и развернуть закладку
type: docs
weight: 20
url: /ru/java/get-update-and-expand-bookmark/
description: Узнайте, как получать, обновлять и развертывать закладки в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверьте свойства закладок и разверните оглавление в PDF‑файлах с помощью Java
Abstract: В этой статье объясняется, как читать, обновлять и расширять закладки с помощью Aspose.PDF for Java. Рассматриваются перебор элементов оглавления, извлечение номеров страниц закладок с помощью PdfBookmarkEditor, чтение дочерних закладок, обновление заголовков и стиля закладок, а также принудительное открытие оглавления при отображении документа.
---
Aspose.PDF for Java предоставляет закладки как через модель оглавления документа, так и через `PdfBookmarkEditor` фасад.

## Получите свойства закладки

Используйте этот пример, когда необходимо просмотреть записи закладок верхнего уровня в оглавлении документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите коллекцию оглавлений.
1. Прочитайте и выведите названия закладок, стили и значения цвета.

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

В этом примере используется `PdfBookmarkEditor` извлекать заголовки закладок, уровни, номера страниц и действия.

1. Привяжите исходный PDF к [PdfBookmarkEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdfbookmarkeditor/).
1. Извлеките коллекцию закладок и пройдитесь по ней.
1. Выведите уровень, заголовок, номер страницы и информацию о действии для каждой закладки.

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

Используйте этот пример, когда нужно проанализировать как элементы верхнего уровня, так и вложенные элементы оглавления.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Пройдите по элементам верхнего уровня и выведите их свойства.
1. Обнаружьте дочерние закладки, затем пройдите по ним и выведите их свойства.

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

Используйте этот пример, когда необходимо изменить существующее название закладки и её стиль.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевому элементу оглавления и его дочерней закладке.
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

## Разворачивать закладки по умолчанию

Используйте этот пример, когда панель закладок должна открываться и показывать развернутые элементы оглавления при отображении документа.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Установите режим страницы на использование оглавления и пометьте каждый элемент оглавления как открытый.
1. Сохраните обновлённый документ.

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

