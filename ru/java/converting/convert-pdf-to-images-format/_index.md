---
title: Преобразование PDF в форматы изображений в Java
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2026-06-16"
description: Узнайте, как визуализировать PDF-страницы в файлы TIFF, BMP, EMF, JPEG, PNG, GIF и SVG в Java с помощью Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Конвертируйте PDF-страницы в TIFF, PNG, JPEG, GIF, BMP, EMF и SVG в Java
Abstract: В этой статье объясняется, как конвертировать PDF-файлы в распространенные форматы изображений с помощью Aspose.PDF для Java. Он охватывает экспорт TIFF всего документа, постраничную генерацию растров с помощью устройств обработки изображений, дополнительную замену шрифтов во время экспорта PNG и вывод SVG с помощью `SvgSaveOptions`.
---
Aspose.PDF для Java может отображать PDF-страницы в форматы растровых и векторных изображений с помощью опций устройства, специфичных для формата.

## Конвертировать PDF в BMP

Используйте этот пример, когда страницы PDF должны отображаться как изображения BMP.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) с разрешением [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI.
1. Выполните итерацию `document.getPages()` и вызовите `device.process(...)` для каждой страницы.
1. Сохраните сгенерированные изображения BMP в пронумерованные пути вывода.

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

Используйте этот пример, когда страницы PDF необходимо экспортировать как векторные изображения EMF.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) с разрешением [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI.
1. Перебирайте страницы и вызывайте `device.process(...)` для каждой страницы.
1. Сохраните выходные данные EMF в пронумерованных путях к файлам.

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

## Конвертировать PDF в GIF

Используйте этот пример, когда страницы PDF необходимо преобразовать в изображения GIF.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) с разрешением [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI.
1. Перебирайте страницы и вызывайте `device.process(...)` для рендеринга каждой страницы.
1. Сохраните файлы GIF в пронумерованных выходных путях.

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

Используйте этот пример, когда страницы PDF необходимо экспортировать как изображения JPEG.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) с разрешением [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI.
1. Пройдитесь по страницам и вызовите `device.process(...)`, чтобы растрировать каждую страницу в JPEG.
1. Сохраните выходные файлы JPEG по пронумерованным путям.

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

## Конвертировать PDF в PNG

Используйте этот пример, когда страницы PDF необходимо преобразовать в изображения PNG.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с разрешением [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI.
1. Перебирайте страницы и вызывайте `device.process(...)` для каждой страницы PDF.
1. Сохраните выходные данные PNG по пронумерованным путям к файлам.

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

## Преобразование PDF в PNG с резервным шрифтом по умолчанию

Используйте этот пример, когда при рендеринге необходимо использовать запасной шрифт для отсутствующих глифов.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) с разрешением [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI.
1. Включите `document.setAbsentFontTryToSubstitute(true)`, чтобы отсутствующие глифы могли быть заменены шрифтами во время рендеринга.
1. Отобразите страницы и сохраните файлы PNG.

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

Используйте этот пример, когда страницы PDF необходимо экспортировать как графику SVG.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) и отключите сжатие ZIP, если требуется необработанный вывод `.svg`.
1. Включите `setTreatTargetFileNameAsDirectory(true)`, чтобы постраничный вывод SVG можно было организовать по целевому пути.
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

Используйте этот пример, когда одну или несколько страниц PDF необходимо экспортировать в TIFF.

1. Откройте исходный PDF-файл в экземпляре [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) и настройте сжатие, глубину цвета и поведение пустой страницы.
1. Создайте [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) с [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) разрешением 300 точек на дюйм и подготовленными настройками TIFF.
1. Отобразите страницы и сохраните результат в формате TIFF.

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
