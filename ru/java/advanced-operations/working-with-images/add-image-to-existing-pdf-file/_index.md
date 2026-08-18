---
title: Добавить изображение в PDF с помощью Java
linktitle: Добавить изображение
type: docs
weight: 10
url: /java/add-image-to-existing-pdf-file/
description: Узнайте, как добавлять изображения в существующие файлы PDF в Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Добавляйте изображения в существующие PDF-файлы с помощью Java
Abstract: В этой статье показано, как добавлять изображения в PDF-документы с помощью Aspose.PDF для Java. Он охватывает размещение изображения в фиксированных координатах, добавление изображений с помощью операторов страниц низкого уровня, настройку альтернативного текста для обеспечения доступности и встраивание данных изображения со сжатием Flate.
---
Aspose.PDF для Java поддерживает как высокоуровневое размещение изображений, так и низкоуровневое рисование с помощью оператора.

## Добавьте изображение с координатами страницы

Используйте этот пример, когда вам нужно разместить изображение в фиксированном положении на странице PDF.

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте страницу.
1. Вызовите `page.addImage()`, указав путь к исходному изображению и целевой прямоугольник.
1. Сохраните созданный PDF-файл.

```java
public static void addImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));
        document.save(outputFile.toString());
    }
}
```

## Добавьте изображение с помощью операторов страницы

Используйте этот пример, если вам нужен низкоуровневый контроль над размещением и масштабированием изображений с помощью операторов страницы.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте поток исходного изображения.
1. Добавьте изображение в ресурсы страницы и рассчитайте целевой прямоугольник.
1. Напишите необходимые графические операторы и сохраните документ.

```java
public static void addImageUsingOperators(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream);
        XImage xImage = resourcesImages.get_Item(resourcesImages.size());

        Rectangle rectangle = new Rectangle(
                0,
                0,
                page.getMediaBox().getWidth(),
                (page.getMediaBox().getWidth() * xImage.getHeight()) / xImage.getWidth(),
                true);

        page.getContents().add(new GSave());

        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLX() + (page.getMediaBox().getHeight() - rectangle.getHeight()) / 2);
        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```

## Добавьте изображение и установите альтернативный текст

Используйте этот пример, когда изображение должно включать метаданные доступности для программ чтения с экрана.

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте изображение на страницу.
1. Получите вставленный [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) из ресурсов страницы.
1. Установите альтернативный текст и сохраните PDF.

```java
public static void addImageSetAlternativeTextForImage(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(842, 595);

        page.addImage(imageFile.toString(), new Rectangle(0, 0, 842, 595, true));

        XImage xImage = page.getResources().getImages().get_Item(1);
        boolean result = xImage.trySetAlternativeText("Alternative text for image", page);
        if (result) {
            System.out.println("Text has been added successfuly");
        }
        document.save(outputFile.toString());
    }
}
```

## Добавьте изображение со сжатием Flate

Используйте этот пример, если вы хотите внедрить данные изображения с помощью сжатия Flate.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте поток изображений.
1. Добавьте изображение в ресурсы страницы с помощью `ImageFilterType.Flate`.
1. Нарисуйте изображение через операторы страницы и сохраните результат.

```java
public static void addImageToPdfWithFlateCompression(Path imageFile, Path outputFile) throws Exception {
    try (Document document = new Document();
         InputStream imageStream = Files.newInputStream(imageFile)) {
        Page page = document.getPages().add();
        XImageCollection resourcesImages = page.getResources().getImages();
        String imageId = resourcesImages.add(imageStream, ImageFilterType.Flate);

        page.getContents().add(new GSave());

        Rectangle rectangle = new Rectangle(0, 0, 600, 600, true);
        Matrix matrix = new Matrix(
                rectangle.getURX() - rectangle.getLLX(),
                0,
                0,
                rectangle.getURY() - rectangle.getLLY(),
                rectangle.getLLX(),
                rectangle.getLLY());

        page.getContents().add(new ConcatenateMatrix(matrix));
        page.getContents().add(new Do(imageId));
        page.getContents().add(new GRestore());

        document.save(outputFile.toString());
    }
}
```
