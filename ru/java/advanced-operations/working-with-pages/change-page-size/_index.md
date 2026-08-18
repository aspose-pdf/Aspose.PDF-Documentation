---
title: Изменить размер страницы PDF в Java
linktitle: Изменение размера страницы
type: docs
weight: 40
url: /java/change-page-size/
description: Узнайте, как читать и изменять размеры страниц PDF в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Чтение и обновление размеров и полей страницы с помощью Java
Abstract: В этой статье показано, как читать и изменять размеры страницы PDF с помощью Aspose.PDF для Java. Он охватывает получение размера страницы, измерение размера страницы с применением поворота и обновление первой страницы до нового размера при печати размеров коробки до и после изменения.
---
Aspose.PDF для Java может как сообщать о размерах страниц, так и обновлять их.

## Изменить размер страницы

Используйте этот пример, когда вам нужно изменить размер существующей страницы и проверить поля страницы до и после изменения.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и распечатайте текущие значения ее поля.
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

## Получите размер страницы

Используйте этот пример, когда вам нужно прочитать видимые размеры страницы.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите прямоугольник страницы с включенной обработкой поворота.
1. Выведите ширину и высоту страницы.

```java
public static void getPageSize(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Rectangle rectangle = document.getPages().get_Item(1).getPageRect(true);
        System.out.println(rectangle.getWidth() + " : " + rectangle.getHeight());
    }
}
```

## Получите размер страницы с примененным поворотом

Используйте этот пример, если вам нужно сравнить размеры страницы до и после учета поворота.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Поверните целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Считайте прямоугольник страницы с обработкой поворота и без нее и выведите оба значения.

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
