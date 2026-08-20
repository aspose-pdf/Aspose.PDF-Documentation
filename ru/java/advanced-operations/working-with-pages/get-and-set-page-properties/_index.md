---
title: Получить и установить свойства страниц PDF в Java
linktitle: Получение и установка свойств страниц
type: docs
weight: 90
url: /ru/java/get-and-set-page-properties/
description: Узнайте, как проверять свойства страниц PDF, такие как количество, рамки, вращение и информация о цвете, в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверьте количество страниц, рамки и тип цвета в PDF‑файлах с помощью Java
Abstract: В этой статье объясняется, как проверять свойства страниц с помощью Aspose.PDF for Java. Она охватывает чтение количества страниц, генерацию абзацев и проверку полученного количества перед сохранением, вывод всех основных значений боксов страниц и определение типа цвета каждой страницы.
---
Aspose.PDF for Java может проверять количество страниц, боксы страниц, вращение и тип цвета страницы.

## Получите количество страниц

Используйте этот пример, когда нужно узнать общее количество страниц в PDF.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Прочитайте размер коллекции страниц.
1. Выведите общее количество страниц.

```java
public static void getPageCount(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Page Count: " + document.getPages().size());
    }
}
```

## Получите количество страниц перед сохранением

Используйте этот пример, когда необходимо узнать, сколько страниц сгенерированный контент создаст до записи файла.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте содержимое на страницу.
1. Обработайте абзацы, чтобы принудительно выполнить расчет разметки.
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

## Получите свойства коробки страницы

Используйте этот пример, когда необходимо проверить все основные размеры коробок и значения поворота страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получить доступ к целевой странице.
1. Соберите значения рамок страницы в карту.
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

Используйте этот пример, когда необходимо определить, являются ли страницы черно‑белыми, градациями серого или RGB.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Переберите все страницы и прочитайте каждую страницу [ColorType](https://reference.aspose.com/pdf/java/com.aspose.pdf/colortype/).
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


