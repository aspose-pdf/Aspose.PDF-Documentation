---
title: Получение и установка свойств страницы PDF в Java
linktitle: Получение и настройка свойств страницы
type: docs
weight: 90
url: /java/get-and-set-page-properties/
description: Узнайте, как проверять свойства страницы PDF, такие как количество, поля, поворот и информацию о цвете, в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка количества страниц, полей и типа цвета в файлах PDF с помощью Java
Abstract: В этой статье объясняется, как проверить свойства страницы с помощью Aspose.PDF для Java. Он включает в себя считывание количества страниц, создание абзацев и проверку полученного количества перед сохранением, печать всех основных значений полей страниц и определение типа цвета каждой страницы.
---
Aspose.PDF для Java может проверять количество страниц, поля страниц, поворот и тип цвета страницы.

## Получите количество страниц

Используйте этот пример, когда вам нужно прочитать общее количество страниц в PDF-файле.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Прочтите размер коллекции страниц.
1. Выведите общее количество страниц.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Получите количество страниц перед сохранением

Используйте этот пример, когда вам нужно знать, сколько страниц будет создано сгенерированным контентом, прежде чем записывать файл.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте контент на страницу.
1. Обработайте абзацы, чтобы принудительно рассчитать макет.
1. Прочитайте полученное количество страниц и выведите его.

```java
public static void getPageCountWithoutSaving(Path inputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        for (int i = 0; i < 300; i++) {
            page.getParagraphs().add(new TextFragment("Pages count test"));
        }
        document.processParagraphs();
        System.out.println("Number of pages in document = " + document.getPages().size());
    }
}
```

## Получите свойства страничного блока

Используйте этот пример, когда вам нужно проверить все основные размеры поля и значения поворота страницы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите доступ к целевой странице.
1. Соберите значения страничных блоков на карте.
1. Выведите размеры и информацию о повороте страницы.

```java
public static void getPageProperties(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        Map<String, Rectangle> boxes = new LinkedHashMap<>();
        boxes.put("ArtBox", page.getArtBox());
        boxes.put("BleedBox", page.getBleedBox());
        boxes.put("CropBox", page.getCropBox());
        boxes.put("MediaBox", page.getMediaBox());
        boxes.put("TrimBox", page.getTrimBox());
        boxes.put("Rect", page.getRect());

        for (Map.Entry<String, Rectangle> entry : boxes.entrySet()) {
            Rectangle box = entry.getValue();
            System.out.println(entry.getKey() + " : Height=" + box.getHeight()
                    + ",Width=" + box.getWidth()
                    + ",LLX=" + box.getLLX()
                    + ",LLY=" + box.getLLY()
                    + ",URX=" + box.getURX()
                    + ",URY=" + box.getURY());
        }

        System.out.println("Page Number : " + page.getNumber());
        System.out.println("Rotate : " + page.getRotate());
    }
}
```

## Получите тип цвета каждой страницы

Используйте этот пример, когда вам нужно определить, являются ли страницы черно-белыми, оттенками серого или RGB.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать все страницы и прочитать каждую страницу [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
1. Преобразуйте значение перечисления в читаемый текст и выведите результат.

```java
public static void getPageColorType(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (int pageNumber = 1; pageNumber <= document.getPages().size(); pageNumber++) {
            ColorType pageColorType = document.getPages().get_Item(pageNumber).getColorType();
            String colorDescription = switch (pageColorType) {
                case BlackAndWhite -> "Black and white";
                case Grayscale -> "Gray Scale";
                case Rgb -> "RGB";
                case Undefined -> "undefined";
            };
            System.out.println("Page # " + pageNumber + " is " + colorDescription + ".");
        }
    }
}
```
