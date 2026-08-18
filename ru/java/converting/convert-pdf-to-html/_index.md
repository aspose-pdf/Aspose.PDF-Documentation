---
title: Конвертируйте PDF в HTML в Java
linktitle: Конвертировать PDF в формат HTML
type: docs
weight: 50
url: /java/convert-pdf-to-html/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать PDF в HTML на Java с помощью Aspose.PDF, включая многостраничный вывод, внешние папки изображений, обработку SVG и многоуровневый рендеринг HTML.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в HTML в Java
Abstract: В этой статье объясняется, как конвертировать PDF-файлы в HTML с помощью Aspose.PDF для Java. Он охватывает базовый экспорт HTML вместе с опциями для папок с изображениями, разделения страниц, вывода SVG, сжатой графики SVG, фона страниц PNG, разметки только тела, рендеринга прозрачного текста и преобразования слоев документа.
---
Aspose.PDF для Java поддерживает экспорт HTML с опциями для изображений, SVG, разделения страниц, прозрачности и рендеринга слоев. Используйте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/), чтобы контролировать запись PDF-страниц, ресурсов и разметки в вывод HTML.

## Конвертировать PDF в HTML

Используйте этот пример, когда PDF-файл необходимо экспортировать в стандартный HTML-документ.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте по умолчанию [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) для стандартной сериализации HTML.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое страницы PDF было экспортировано в виде разметки HTML.
1. Сохраните сгенерированный вывод HTML.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PDF в HTML и храните изображения отдельно.

Используйте этот пример, когда извлеченные изображения необходимо записать в отдельные файлы во время экспорта HTML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установите для `setSpecialFolderForAllImages(...)` выделенный каталог вывода изображений.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы растровые изображения создавались как отдельные файлы ресурсов, а не как встроенный вывод.
1. Сохраните выходные данные HTML вместе со сгенерированными графическими ресурсами.

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PDF в многостраничный HTML

Используйте этот пример, когда каждая страница PDF должна быть представлена ​​отдельно в выводе HTML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включите `setSplitIntoPages(true)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы каждая страница PDF была записана как отдельный вывод HTML.
1. Сохраните созданные HTML-файлы.

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PDF в HTML и храните SVG отдельно.

Используйте этот пример, когда векторный контент должен быть создан как отдельные ресурсы SVG.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установите `setSpecialFolderForSvgImages(...)` во внешний каталог ресурсов SVG.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы векторная графика хранилась вне основного файла HTML.
1. Сохраните выходные данные HTML и ресурсы SVG.

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PDF в HTML со сжатым SVG

Используйте этот пример, когда вывод SVG необходимо оптимизировать во время экспорта HTML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и настройте специальную папку для ресурсов SVG.
1. Включите `setCompressSvgGraphicsIfAny(true)`, чтобы ресурсы SVG сжимались во время экспорта.
1. Позвоните `document.save(outputFile.toString(), saveOptions)` и сохраните преобразованные файлы HTML.

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертируйте PDF в HTML с фоном страниц PNG

Используйте этот пример, когда фон страницы должен отображаться в виде изображений PNG при выводе HTML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установите режим сохранения растрового изображения на фон страницы PNG.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы фоновое содержимое страницы было создано в виде слоев HTML в формате PNG.
1. Сохраните преобразованный вывод HTML.

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в HTML только содержимое тела

Используйте этот пример, когда требуется только разметка тела вместо полной оболочки HTML-документа.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установите режим создания разметки `WriteOnlyBodyContent`.
1. Оставьте `setSplitIntoPages(true)` включенным, если вывод только основного текста по-прежнему должен быть разделен на страницы.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните вывод HTML.

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в HTML с прозрачной визуализацией текста

Используйте этот пример, если при экспорте HTML необходимо сохранить прозрачный текст.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включите сохранение прозрачного и затененного текста.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы в результате HTML сохранялся внешний вид текста, связанный с прозрачностью.
1. Сохраните преобразованный вывод HTML.

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в HTML с рендерингом слоев документа

Используйте этот пример, когда видимость слоя PDF должна быть отражена в результате HTML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включите `setConvertMarkedContentToLayers(true)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы отмеченное содержимое PDF было преобразовано в слои HTML.
1. Сохраните экспортированные файлы HTML.

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
