---
title: Преобразование PDF в HTML на Java
linktitle: Преобразование PDF в формат HTML
type: docs
weight: 50
url: /ru/java/convert-pdf-to-html/
lastmod: "2026-09-16"
description: Узнайте, как преобразовать PDF в HTML на Java с помощью Aspose.PDF, включая вывод многостраничных документов, внешние папки изображений, обработку SVG и многослойную генерацию HTML.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как преобразовать PDF в HTML на Java
Abstract: В этой статье объясняется, как преобразовать файлы PDF в HTML с помощью Aspose.PDF for Java. Описывается базовый экспорт HTML вместе с параметрами для папок изображений, разбиения страниц, вывода SVG, сжатой графики SVG, фоновых изображений PNG, разметки только тела, прозрачного рендеринга текста и преобразования слоёв документа.
---
Aspose.PDF for Java поддерживает экспорт в HTML с параметрами для изображений, SVG, разбиения страниц, прозрачности и рендеринга слоёв. Используйте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) для контроля того, как страницы PDF, ресурсы и разметка записываются в HTML‑вывод.

## Преобразование PDF в HTML

Используйте этот пример, когда PDF должен быть экспортирован в стандартный HTML‑документ.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) с параметрами по умолчанию для стандартной сериализации HTML.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом содержимое страницы PDF экспортируется как HTML‑разметка.
1. Сохраните сгенерированный HTML‑вывод.

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в HTML с отдельным сохранением изображений

Используйте этот пример, когда извлечённые изображения должны записываться в отдельные файлы при экспорте в HTML.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и задайте отдельный каталог для изображений с помощью `setSpecialFolderForAllImages(...)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом растровые изображения генерируются как отдельные файлы ресурсов вместо встраивания в HTML.
1. Сохраните HTML-вывод вместе со сгенерированными изображениями.

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

## Преобразование PDF в многостраничный HTML

Используйте этот пример, когда каждая страница PDF должна быть представлена отдельно в выводе HTML.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включите `setSplitIntoPages(true)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом каждая страница PDF записывается как отдельный HTML‑вывод.
1. Сохраните сгенерированные HTML‑файлы.

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

## Преобразование PDF в HTML с отдельным сохранением SVG

Используйте этот пример, когда векторный контент должен быть вынесен в отдельные SVG‑ресурсы.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и задайте внешний каталог для ресурсов SVG с помощью `setSpecialFolderForSvgImages(...)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом векторная графика хранится вне основного HTML‑файла.
1. Сохраните HTML‑вывод и SVG‑ресурсы.

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

## Преобразование PDF в HTML со сжатием SVG

Используйте этот пример, когда вывод SVG должен быть оптимизирован при экспорте в HTML.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и настройте отдельную папку для ресурсов SVG.
1. Включите `setCompressSvgGraphicsIfAny(true)`, при этом ресурсы SVG сжимаются при экспорте.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните преобразованные HTML‑файлы.

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

## Преобразование PDF в HTML с фоном страниц в формате PNG

Используйте этот пример, когда фон страниц должен отображаться в виде PNG‑изображений в HTML‑выводе.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установите режим сохранения растровых изображений в PNG для фонов страниц.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом фон страницы выводится в виде HTML‑слоёв на основе PNG.
1. Сохраните преобразованный HTML-вывод.

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

## Преобразование PDF только в содержимое body HTML

Используйте этот пример, когда нужна только разметка тела вместо полной оболочки HTML‑документа.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установите режим генерации разметки `WriteOnlyBodyContent`.
1. Оставьте `setSplitIntoPages(true)` включённым, если содержимое body должно быть разделено на страницы.
1. Вызовите `document.save(outputFile.toString(), saveOptions)` и сохраните HTML‑вывод.

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

## Преобразование PDF в HTML с сохранением прозрачности текста

Используйте этот пример, когда прозрачный текст должен сохраняться при экспорте в HTML.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включите сохранение прозрачного и затенённого текста.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом отображение текста, связанное с прозрачностью, сохраняется в HTML‑результате.
1. Сохраните преобразованный HTML-вывод.

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

## Преобразование PDF в HTML с отображением слоёв документа

Используйте этот пример, когда видимость слоёв PDF должна отображаться в результате HTML.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включите `setConvertMarkedContentToLayers(true)`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, при этом отмеченный контент PDF отображается в слоях HTML.
1. Сохраните экспортированные HTML‑файлы.

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
