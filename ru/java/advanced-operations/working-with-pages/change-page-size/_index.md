---
title: Изменение размера страницы PDF в Java
linktitle: Изменение размера страницы
type: docs
weight: 40
url: /ru/java/change-page-size/
description: Узнайте, как читать и изменять размеры страниц PDF в Java.
lastmod: "2026-09-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Читать и обновлять размеры страниц и области с помощью Java
Abstract: В этой статье демонстрируется, как считывать и изменять размеры страниц PDF с помощью Aspose.PDF for Java. Рассматриваются получение размера страницы, измерение размера страницы с учётом вращения и обновление первой страницы до нового размера при выводе размеров коробки до и после изменения.
---
Aspose.PDF for Java может как сообщать размеры страниц, так и обновлять их.

## Изменение размера страницы

Используйте этот пример, когда необходимо изменить размер существующей страницы и проверить параметры границ страницы до и после изменения.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите нужную страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и выведите текущие значения её границ.
1. Установите новый размер страницы и сохраните документ.

```java
public static void setPageSize(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        printBoxes("Before set", page);
        page.setPageSize(597.6, 842.4);
        printBoxes("After set", page);
        document.save(outputFile.toString());
    }
}
```

## Получение размера страницы

Используйте этот пример, когда вам нужно прочитать видимые размеры страницы.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите прямоугольник страницы с включенной обработкой вращения.
1. Выведите ширину и высоту страницы.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## Получение размера страницы с учётом поворота

Используйте этот пример, когда необходимо сравнить размеры страниц до и после учёта поворота.

1. Откройте исходный PDF в объекте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Поверните нужную страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Прочитайте прямоугольник страницы с учётом вращения и без учёта вращения и выведите оба значения.

```java
public static void getPageSizeRotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.setRotate(Rotation.on90);
        Rectangle rectangle = page.getPageRect(false);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
        rectangle = page.getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```


