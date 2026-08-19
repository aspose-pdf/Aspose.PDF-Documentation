---
title: Конвертировать PDF в форматы изображений на Java
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /ru/java/convert-pdf-to-images-format/
lastmod: "2026-08-19"
description: Узнайте, как в Java с помощью Aspose.PDF рендерить страницы PDF в файлы TIFF, BMP, EMF, JPEG, PNG, GIF и SVG.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Конвертировать страницы PDF в TIFF, PNG, JPEG, GIF, BMP, EMF и SVG в Java.
Abstract: В этой статье объясняется, как преобразовать PDF‑файлы в распространённые форматы изображений с помощью Aspose.PDF for Java. Описывается экспорт TIFF для всего документа, постраничное растрирование с использованием устройств изображения, опционная замена шрифтов при экспорте PNG и вывод SVG с помощью `SvgSaveOptions`.
---
Aspose.PDF for Java может визуализировать страницы PDF в растровые и векторные форматы изображений с параметрами устройства, специфичными для формата.

## Конвертировать PDF в BMP

Используйте этот пример, когда страницы PDF должны быть отрисованы как BMP‑изображения.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Перебирать `document.getPages()` и вызвать `device.process(...)` для каждой страницы.
1. Сохраните сгенерированные BMP‑изображения в нумерованные пути вывода.

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

## Конвертировать PDF в EMF

Используйте этот пример, когда страницы PDF должны экспортироваться в виде векторных изображений EMF.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Итерировать по страницам и вызвать `device.process(...)` для каждой страницы.
1. Сохраните выводы EMF в пронумерованные пути файлов.

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

## Преобразуйте PDF в GIF

Используйте этот пример, когда страницы PDF необходимо преобразовать в изображения GIF.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Итерировать по страницам и вызвать `device.process(...)` для отрисовки каждой страницы.
1. Сохраните GIF‑файлы в нумерованные пути вывода.

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

## Конвертировать PDF в JPEG

Используйте этот пример, когда страницы PDF должны экспортироваться в виде изображений JPEG.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Итерировать по страницам и вызвать `device.process(...)` преобразовать каждую страницу в растр JPEG.
1. Сохраните файлы JPEG в пронумерованные пути.

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

## Преобразуйте PDF в PNG

Используйте этот пример, когда страницы PDF необходимо преобразовать в PNG‑изображения.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Итерировать по страницам и вызвать `device.process(...)` для каждой страницы PDF.
1. Сохраните выводы PNG в нумерованные пути файлов.

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

## Конвертировать PDF в PNG с резервным шрифтом по умолчанию

Используйте этот пример, когда рендеринг должен использовать резервный шрифт для отсутствующих глифов.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI.
1. Включить `document.setAbsentFontTryToSubstitute(true)` чтобы отсутствующие глифы могли использовать заменяющие шрифты при рендеринге.
1. Отрисуйте страницы и сохраните PNG‑файлы.

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

## Конвертировать PDF в SVG

Используйте этот пример, когда страницы PDF должны экспортироваться в виде графики SVG.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) и отключить сжатие ZIP при raw `.svg` Требуется вывод.
1. Включить `setTreatTargetFileNameAsDirectory(true)` поэтому вывод SVG по страницам можно организовать в целевом пути.
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

## Конвертировать PDF в TIFF

Используйте этот пример, когда нужно экспортировать одну или несколько страниц PDF в формат TIFF.

1. Откройте исходный PDF в [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) и настроить сжатие, глубину цвета и поведение при пустых страницах.
1. Создайте [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) с разрешением 300 DPI и подготовленными настройками TIFF.
1. Отобразите страницы и сохраните TIFF‑вывод.

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

