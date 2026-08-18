---
title: Конвертируйте PDF в EPUB, текст, XPS и другие форматы на Java
linktitle: Конвертируйте PDF в другие форматы
type: docs
weight: 90
url: /java/convert-pdf-to-other-files/
lastmod: "2026-06-16"
description: Узнайте, как конвертировать PDF-файлы в EPUB, LaTeX, Markdown, текст, XPS и MobiXML на Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в другие форматы в Java
Abstract: В этой статье объясняется, как конвертировать PDF-файлы в форматы EPUB, TeX, Markdown, текст, XPS и MobiXML с помощью Aspose.PDF для Java с параметрами сохранения для конкретного формата, где это необходимо.
---
Aspose.PDF для Java может экспортировать PDF-документы в текстовые, электронные книги, печатные форматы и форматы вывода, ориентированные на разметку.

## Конвертировать PDF в EPUB

Используйте этот пример, когда документ PDF необходимо экспортировать в формат электронной книги EPUB.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) и установите режим распознавания `Flow`.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое PDF было экспортировано в виде переформатируемой разметки EPUB.
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

Используйте этот пример, когда содержимое PDF необходимо экспортировать в разметку TeX.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) для сериализации TeX.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое PDF было создано как разметка TeX.
1. Сохраните полученный файл TeX.

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Преобразование PDF в обычный текст

Используйте этот пример, когда PDF-документ необходимо экспортировать в текстовый файл.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) для извлечения текстового содержимого со страниц PDF.
1. Позвоните `device.process(document.getPages().get_Item(1), outputFile.toString())`, чтобы записать первую страницу в виде обычного текста.
1. Сохраните текстовый выходной файл.

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

Используйте этот пример, когда документ PDF необходимо преобразовать в формат XPS.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) и включите встроенные шрифты TrueType.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы PDF-файл был сериализован как XPS со встроенными ресурсами шрифтов.
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

## Конвертировать PDF в Markdown

Используйте этот пример, когда содержимое PDF необходимо экспортировать в формате Markdown.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) и настройте каталог ресурсов изображения, а также вывод HTML-тега изображения.
1. Вызовите `document.save(outputFile.toString(), saveOptions)`, чтобы содержимое PDF было создано как Markdown с внешними ресурсами изображений.
1. Сохраните созданный файл Markdown.

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

## Конвертировать PDF в Mobi XML

Используйте этот пример, когда содержимое PDF необходимо экспортировать в Mobi-совместимый XML.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Выберите [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` в качестве целевого формата сериализации.
1. Вызовите `document.save(outputFile.toString(), SaveFormat.MobiXml)`, чтобы PDF-файл был экспортирован как Mobi-совместимый XML.
1. Сохраните преобразованный файл.

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
