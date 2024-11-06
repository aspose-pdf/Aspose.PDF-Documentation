---
title: Преобразование файла PDF в формат HTML
linktitle: Преобразование файла PDF в формат HTML
type: docs
weight: 50
url: ru/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать файл PDF в формат HTML с использованием Java библиотеки.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF for Java предоставляет множество функций для преобразования различных форматов файлов в документы PDF и преобразования PDF файлов в различные выходные форматы. В этой статье обсуждается, как преобразовать файл PDF в формат HTML и сохранить изображения из файла PDF в определенной папке.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в HTML онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), где вы можете попробовать исследовать функциональность и качество работы.

[![Aspose.PDF Преобразование PDF в HTML с бесплатным приложением](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

При конвертации большого PDF-файла с несколькими страницами в формат HTML, вывод появляется в виде одной HTML-страницы. Она может оказаться очень длинной. Чтобы контролировать размер страницы, можно разделить вывод на несколько страниц во время преобразования PDF в HTML.

## Преобразование страниц PDF в HTML

Aspose.PDF для Java предоставляет множество функций для преобразования различных форматов файлов в PDF-документы и преобразования PDF-файлов в различные выходные форматы. В этой статье обсуждается, как преобразовать PDF-файл в формат HTML и сохранить изображения из PDF-файла в определенной папке.

Следующий фрагмент кода показывает все возможные варианты, которые вы можете использовать при преобразовании PDF в HTML.

```java
// Открыть исходный PDF-документ
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// Сохранить файл в формате документа MS
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## Преобразование PDF в HTML - Разделение вывода на многостраничный HTML

Aspose.PDF для Java поддерживает функцию преобразования PDF-документов в различные выходные форматы, включая HTML.
 Однако при преобразовании больших PDF-файлов (состоящих из нескольких страниц) может возникнуть необходимость сохранить отдельную страницу PDF в отдельный HTML-файл.

При преобразовании большого PDF-файла с несколькими страницами в формат HTML вывод отображается как одна HTML-страница. Она может оказаться очень длинной. Чтобы контролировать размер страницы, можно разделить вывод на несколько страниц во время преобразования PDF в HTML. Пожалуйста, попробуйте использовать следующий фрагмент кода.

```java
// Открыть исходный PDF-документ
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// Создать экземпляр объекта HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Указать разделение вывода на несколько страниц
htmlOptions.setSplitIntoPages(true);

// Сохранить документ
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## Преобразование PDF в HTML - Избегайте сохранения изображений в формате SVG

Формат вывода по умолчанию для сохранения изображений при преобразовании из PDF в HTML - это SVG. Во время преобразования некоторые изображения из PDF преобразуются в векторные изображения SVG. Это может быть медленным. Вместо этого изображения могут быть преобразованы в PNG. Для этого Aspose.PDF имеет возможность использовать SVG для векторов или создавать PNG.

Чтобы полностью удалить рендеринг изображений в формате SVG при преобразовании PDF файлов в формат HTML, попробуйте использовать следующий фрагмент кода.

```java
 // Загрузить PDF файл
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Создать объект параметров сохранения HTML
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Указать папку, где сохраняются SVG изображения во время преобразования PDF в HTML
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// Сохранить выходной файл
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## Сжатие SVG изображений во время преобразования

Чтобы сжать SVG изображения во время преобразования PDF в HTML, попробуйте использовать следующий код:

```java
// Загрузить PDF файл
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Создать HtmlSaveOption с протестированной функцией
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Сжать SVG изображения, если таковые имеются
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Преобразование PDF в HTML - Указание папки для изображений

По умолчанию, при преобразовании PDF файла в HTML, изображения в PDF сохраняются в отдельной папке, созданной в той же директории, где создан выходной HTML. Но иногда необходимо указать другую папку для сохранения изображений при генерации HTML файлов. Для этого мы ввели [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).
Метод [SpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) используется для указания целевой папки для хранения изображений.

```java
// Загрузить PDF файл
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Указать отдельную папку для сохранения изображений
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```


## Создание последующих файлов только с содержимым Body

С помощью следующего простого фрагмента кода вы можете разделить выходной HTML на страницы. На выходных страницах все HTML-объекты должны находиться точно там, где они находятся сейчас (обработка и вывод шрифтов, создание и вывод CSS, создание и вывод изображений), за исключением того, что выходной HTML будет содержать содержимое, которое в настоящее время размещено внутри тегов (теперь теги «body» будут опущены).

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## Прозрачный рендеринг текста

В случае, если исходный/входной PDF-файл содержит прозрачный текст, затененный на переднем плане изображениями, могут возникнуть проблемы с рендерингом текста. Поэтому для таких сценариев можно использовать методы `setSaveShadowedTextsAsTransparentTexts` и `setSaveTransparentTexts`.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Создать экземпляр объекта HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// Сохранить документ
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## Отображение слоев PDF-документа

Мы можем отображать слои PDF-документа в отдельном элементе типа слоя во время конвертации PDF в HTML:

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// Создание объекта HtmlSaveOptions

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Указать отображение слоев PDF-документа отдельно в выходном HTML
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// Сохранить документ
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

Конвертация PDF в HTML является одной из самых популярных функций Aspose.PDF, потому что она позволяет просматривать содержание PDF-файлов на различных платформах без использования просмотрщика PDF-документов. Выходной HTML соответствует стандартам WWW и может легко отображаться во всех веб-браузерах. Используя эту функцию, PDF-файлы могут просматриваться на портативных устройствах, так как вам не нужно устанавливать приложение для просмотра PDF, а можно использовать простой веб-браузер.

## PDF в HTML - Исключение ресурсов шрифтов

Если вы хотите исключить все или некоторые шрифтовые ресурсы при преобразовании PDF в HTML, Aspose.PDF для Java API позволяет вам достичь этого с помощью класса HtmlSaveOptions. API предлагает два варианта для этой цели.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - чтобы предотвратить экспорт всех шрифтов
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - для предотвращения экспорта конкретных шрифтов (имена шрифтов должны быть указаны без хэша)

Чтобы преобразовать PDF в HTML с исключением шрифтовых ресурсов, используйте следующие шаги:

1. Определите новый объект класса HtmlSaveOptions
2. Определите и установите имена шрифтов, которые следует исключить из экспорта, в HtmlSaveOptions.ExcludeFontNameList
3. Преобразуйте PDF в HTML, используя метод сохранения

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```