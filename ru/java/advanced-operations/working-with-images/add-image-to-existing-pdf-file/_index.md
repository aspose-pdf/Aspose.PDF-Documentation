---
title: Добавить изображение в PDF с помощью Java
linktitle: Добавить изображение
type: docs
weight: 10
url: /ru/java/add-image-to-existing-pdf-file/
description: Узнайте, как добавить изображения в существующие PDF‑файлы на Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Добавить изображения в существующие PDF‑файлы с помощью Java
Abstract: В этой статье показано, как добавлять изображения в PDF‑документы с использованием Aspose.PDF for Java. Описывается размещение изображения по фиксированным координатам, добавление изображений через низкоуровневые операторы страницы, установка альтернативного текста для доступности и встраивание данных изображения с помощью сжатия Flate.
---
Aspose.PDF for Java поддерживает как размещение изображений на высоком уровне, так и рисование с использованием низкоуровневых операторов.

## Добавьте изображение с координатами страницы

Используйте этот пример, когда необходимо разместить изображение в фиксированном положении на странице PDF.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте страницу.
1. Вызов `page.addImage()` с путем к исходному изображению и целевым прямоугольником.
1. Сохраните сгенерированный PDF‑файл.

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

Используйте этот пример, когда вам нужен низкоуровневый контроль над размещением изображения и масштабированием с помощью операторов страницы.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и откройте поток исходного изображения.
1. Добавьте изображение в ресурсы страницы и вычислите целевой прямоугольник.
1. Запишите необходимые графические операторы и сохраните документ.

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

## Добавьте изображение и задайте альтернативный текст

Используйте этот пример, когда изображение должно включать метаданные доступности для программ чтения с экрана.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте изображение на страницу.
1. Получите вставленное [XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/ximage/) из ресурсов страницы.
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

## Добавьте изображение с сжатием Flate

Используйте этот пример, когда хотите встроить данные изображения, используя сжатие Flate.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и открыть поток изображения.
1. Добавьте изображение в ресурсы страницы с `ImageFilterType.Flate`.
1. Отрисуйте изображение с помощью операторов страницы и сохраните результат.

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

