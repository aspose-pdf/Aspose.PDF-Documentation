---
title: Конвертировать PDF в HTML на Java
linktitle: Конвертировать PDF в формат HTML
type: docs
weight: 50
url: /ru/java/convert-pdf-to-html/
lastmod: "2026-08-19"
description: Узнайте, как преобразовать PDF в HTML на Java с помощью Aspose.PDF, включая вывод многостраничных файлов, внешние папки с изображениями, обработку SVG и многоуровневую отрисовку HTML.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как преобразовать PDF в HTML на Java
Abstract: В этой статье объясняется, как преобразовать файлы PDF в HTML с помощью Aspose.PDF for Java. Описывается базовый экспорт в HTML вместе с вариантами для папок изображений, разбивки страниц, вывода SVG, сжатой графики SVG, фоновых изображений PNG, разметки только тела, прозрачного рендеринга текста и преобразования слоев документа.
---
Aspose.PDF for Java поддерживает экспорт в HTML с вариантами для изображений, SVG, разбиения страниц, прозрачности и рендеринга слоёв. Используйте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) для контроля того, как страницы PDF, ресурсы и разметка записываются в HTML‑вывод.

## Конвертировать PDF в HTML

Используйте этот пример, когда PDF должен быть экспортирован в стандартный HTML‑документ.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте по умолчанию [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) для стандартной сериализации HTML.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому содержимое страницы PDF экспортируется как HTML‑разметка.
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

## Преобразуйте PDF в HTML и сохранить изображения отдельно

Используйте этот пример, когда извлечённые изображения должны быть записаны в отдельные файлы при экспорте в HTML.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установить `setSpecialFolderForAllImages(...)` в отдельный каталог вывода изображений.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому растровые изображения выводятся как отдельные файлы ресурсов, а не только в виде встроенного вывода.
1. Сохраните HTML‑output вместе с сгенерированными графическими ресурсами.

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

## Преобразуйте PDF в многостраничный HTML

Используйте этот пример, когда каждая страница PDF должна быть представлена отдельно в HTML‑выводе.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включить `setSplitIntoPages(true)`.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому каждая страница PDF записывается как отдельный HTML‑вывод.
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

## Преобразуйте PDF в HTML и сохранить SVG отдельно

Используйте этот пример, когда векторный контент должен быть выведен как отдельные ресурсы SVG.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установить `setSpecialFolderForSvgImages(...)` во внешнюю директорию ресурсов SVG.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому векторная графика хранится вне основного HTML‑файла.
1. Сохраните вывод HTML и ресурсы SVG.

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

## Конвертировать PDF в HTML с сжатым SVG

Используйте этот пример, когда вывод SVG должен быть оптимизирован при экспорте в HTML.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и настройте отдельную папку для ресурсов SVG.
1. Включить `setCompressSvgGraphicsIfAny(true)` поэтому SVG‑ресурсы сжимаются при экспорте.
1. Вызов `document.save(outputFile.toString(), saveOptions)` и сохранить преобразованные HTML‑файлы.

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

## Конвертировать PDF в HTML с PNG‑фоновыми изображениями страниц

Используйте этот пример, когда фон страниц должен отображаться в виде PNG‑изображений в выводе HTML.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установить режим сохранения растрового изображения в PNG фон страниц.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому содержание фона страницы выводится в виде HTML‑слоёв на основе PNG.
1. Сохраните преобразованный HTML‑вывод.

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

## Преобразуйте PDF в HTML, только содержимое тела

Используйте этот пример, когда нужна только разметка тела, а не полная оболочка HTML‑документа.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и установить режим генерации разметки на `WriteOnlyBodyContent`.
1. Сохранять `setSplitIntoPages(true)` включено, когда вывод только тела должен оставаться разделённым по страницам.
1. Вызов `document.save(outputFile.toString(), saveOptions)` и сохранить вывод HTML.

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

## Конвертировать PDF в HTML с прозрачным отображением текста

Используйте этот пример, когда прозрачный текст должен быть сохранён при экспорте в HTML.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включить сохранение прозрачного и затенённого текста.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому внешний вид текста, связанный с прозрачностью, сохраняется в HTML‑результате.
1. Сохраните преобразованный HTML‑вывод.

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

## Преобразуйте PDF в HTML с рендерингом уровня документа

Используйте этот пример, когда видимость слоев PDF должна отображаться в HTML‑результате.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) и включить `setConvertMarkedContentToLayers(true)`.
1. Вызов `document.save(outputFile.toString(), saveOptions)` Итак, отмеченное PDF‑содержимое отображается в виде HTML‑слоев.
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

