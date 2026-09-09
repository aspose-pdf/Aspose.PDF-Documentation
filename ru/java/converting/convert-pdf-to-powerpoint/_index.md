---
title: Конвертировать PDF в PowerPoint на Java
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 30
url: /ru/java/convert-pdf-to-powerpoint/
description: Узнайте, как конвертировать PDF‑файлы в PowerPoint на Java с помощью Aspose.PDF, включая редактируемые слайды PPTX, слайды на основе изображений и настройку разрешения изображений.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в PowerPoint на Java
Abstract: В этой статье объясняется, как преобразовать PDF‑файлы в презентации PowerPoint с использованием Aspose.PDF for Java. Описывается стандартное преобразование в PPTX, вывод слайдов в виде изображений и контроль разрешения изображения с помощью `PptxSaveOptions`.
---
Aspose.PDF for Java поддерживает экспорт страниц PDF в редактируемые презентации PowerPoint с параметрами рендеринга слайдов. Используйте [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) для управления тем, как страницы PDF сопоставляются со слайдами PowerPoint.

## Конвертируйте PDF в PPTX

Используйте этот пример, когда PDF‑документ должен быть экспортирован как стандартная презентация PowerPoint.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте по умолчанию [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) для редактируемого экспорта PowerPoint.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` так что страницы PDF сериализуются как `.pptx` презентация.
1. Сохраните преобразованный файл PPTX.

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PDF в PPTX, где слайды являются изображениями

Используйте этот пример, когда каждая страница PDF должна стать слайдом PowerPoint на основе изображения.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) и включить `setSlidesAsImages(true)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому каждая страница PDF отображается как слайд, основанный на изображении, в презентации.
1. Сохраните сгенерированный файл PPTX.

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте PDF в PPTX с пользовательским разрешением изображения

Используйте этот пример, когда необходимо контролировать качество изображения слайдов при экспорте PDF в PPTX.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) и установить `setImageResolution(300)` для более высокой точности изображения слайда.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` поэтому растровое содержимое слайда генерируется с запрошенным разрешением.
1. Сохраните полученную презентацию.

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```


