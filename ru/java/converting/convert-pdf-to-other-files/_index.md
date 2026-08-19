---
title: Конвертировать PDF в EPUB, Text, XPS и другие форматы на Java
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /ru/java/convert-pdf-to-other-files/
lastmod: "2026-08-19"
description: Узнайте, как конвертировать PDF-файлы в EPUB, LaTeX, Markdown, текст, XPS и MobiXML на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в другие форматы на Java
Abstract: В этой статье объясняется, как преобразовать файлы PDF в форматы EPUB, TeX, Markdown, текст, XPS и MobiXML с использованием Aspose.PDF for Java, при необходимости используя параметры сохранения, специфичные для формата.
---
Aspose.PDF for Java может экспортировать PDF‑документы в форматы вывода, ориентированные на текст, электронные книги, печать и разметку.

## Конвертировать PDF в EPUB

Используйте этот пример, когда PDF‑документ должен быть экспортирован в формат электронной книги EPUB.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) и установить режим распознавания на `Flow`.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому содержимое PDF экспортируется как переливаемая разметка EPUB.
1. Сохраните преобразованный файл EPUB.

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## Конвертировать PDF в TeX

Используйте этот пример, когда содержимое PDF должно быть экспортировано в разметку TeX.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) для сериализации TeX.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому содержимое PDF выводится в виде разметки TeX.
1. Сохраните полученный файл TeX.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в обычный текст

Используйте этот пример, когда PDF‑документ должен быть экспортирован в текстовый файл.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) для извлечения текстового содержимого из страниц PDF.
1. Вызов `device.process(document.getPages().get_Item(1), outputFile.toString())` записать первую страницу в виде простого текста.
1. Сохраните файл вывода текста.

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Конвертировать PDF в XPS

Используйте этот пример, когда PDF‑документ должен быть преобразован в формат XPS.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) и включить встроенные шрифты TrueType.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому PDF сериализуется как XPS с встроенными ресурсами шрифтов.
1. Сохраните преобразованный файл XPS.

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте PDF в Markdown

Используйте этот пример, когда содержимое PDF должно быть экспортировано в Markdown.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) и настройте каталог ресурсов изображений, а также вывод HTML‑тега img.
1. Вызов `document.save(outputFile.toString(), saveOptions)` поэтому содержимое PDF выводится как Markdown с внешними ресурсами изображений.
1. Сохраните сгенерированный файл Markdown.

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразуйте PDF в Mobi XML

Используйте этот пример, когда содержимое PDF должно быть экспортировано в совместимый с Mobi XML.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Выбрать [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` в качестве целевого формата сериализации.
1. Вызов `document.save(outputFile.toString(), SaveFormat.MobiXml)` поэтому PDF экспортируется как совместимый с Mobi XML.
1. Сохраните преобразованный файл.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

