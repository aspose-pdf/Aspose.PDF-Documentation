---
title: Преобразование PDF в форматы изображений в Java
linktitle: Преобразование PDF в изображения
type: docs
weight: 70
url: /ru/java/convert-pdf-to-images-format/
lastmod: "2026-09-16"
description: Узнайте, как рендерить страницы PDF в файлы TIFF, BMP, EMF, JPEG, PNG, GIF и SVG в Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Конвертируйте страницы PDF в TIFF, PNG, JPEG, GIF, BMP, EMF и SVG в Java
Abstract: В этой статье объясняется, как преобразовать файлы PDF в распространённые графические форматы с помощью Aspose.PDF for Java. Описывается экспорт TIFF для всего документа, генерация растровых изображений по страницам с использованием графических устройств, необязательная подстановка шрифтов при экспорте PNG и вывод SVG с помощью `SvgSaveOptions`.
---
Aspose.PDF for Java может рендерить страницы PDF в растровые и векторные форматы изображений с опциями устройства, специфичными для формата.

## Преобразование PDF в BMP

Используйте этот пример, когда страницы PDF должны быть отрисованы как BMP‑изображения.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Переберите страницы в `document.getPages()` и вызовите `device.process(...)` для каждой страницы.
1. Сохраните созданные BMP-изображения в файлы с номерами страниц в именах.

```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## Преобразование PDF в EMF

Используйте этот пример, когда страницы PDF должны экспортироваться в виде векторных изображений EMF.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Переберите страницы и вызовите `device.process(...)` для каждой страницы.
1. Сохраните изображения EMF в файлы с номерами страниц в именах.

```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Преобразование PDF в GIF

Используйте этот пример, когда страницы PDF необходимо преобразовать в изображения GIF.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Переберите страницы и вызовите `device.process(...)` для отображения каждой страницы.
1. Сохраните файлы GIF с номерами страниц в именах.

```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Преобразование PDF в JPEG

Используйте этот пример, когда страницы PDF должны экспортироваться как изображения JPEG.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Переберите страницы и вызовите `device.process(...)`, чтобы преобразовать каждую страницу в растровый формат JPEG.
1. Сохраните файлы JPEG с номерами страниц в именах.

```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Преобразование PDF в PNG

Используйте этот пример, когда страницы PDF нужно преобразовать в изображения PNG.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Переберите страницы и вызовите `device.process(...)` для каждой страницы PDF.
1. Сохраните файлы PNG с номерами страниц в именах.

```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Преобразование PDF в PNG с заменой отсутствующих шрифтов

Используйте этот пример, когда при рендеринге следует использовать резервный шрифт для отсутствующих глифов.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Включите `document.setAbsentFontTryToSubstitute(true)`, чтобы недостающие глифы могли использовать резервные шрифты при рендеринге.
1. Визуализируйте страницы и сохраните PNG‑файлы.

```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Преобразование PDF в SVG

Используйте этот пример, когда страницы PDF должны экспортироваться в виде графики SVG.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) и отключите сжатие ZIP, если нужны отдельные файлы `.svg`.
1. Включите `setTreatTargetFileNameAsDirectory(true)`, так что вывод SVG постранично может быть организован в целевом пути.
1. Сохраните вывод SVG.

```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## Преобразование PDF в TIFF

Используйте этот пример, когда нужно экспортировать одну или несколько страниц PDF в TIFF.

1. Откройте исходный PDF в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) и настройте сжатие, глубину цвета и поведение пустых страниц.
1. Создайте [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI и подготовленными настройками TIFF.
1. Отрисуйте страницы и сохраните вывод в формате TIFF.

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```
