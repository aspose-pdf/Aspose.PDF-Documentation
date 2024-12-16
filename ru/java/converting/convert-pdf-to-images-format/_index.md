---
title: Конвертация PDF в форматы изображений
linktitle: Конвертация PDF в изображения
type: docs
weight: 70
url: /ru/java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: Эта тема покажет вам, как Aspose.PDF позволяет конвертировать PDF в различные форматы изображений. Конвертируйте страницы PDF в изображения PNG, JPEG, BMP с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF для Java** позволяет конвертировать PDF-документы в форматы изображений, такие как BMP, JPEG, GIF, PNG, EMF, TIFF и SVG, используя два подхода. Конвертация выполняется с использованием устройства (Device) и с использованием опции сохранения (SaveOption).

В библиотеке есть несколько классов, которые позволяют использовать виртуальное устройство для преобразования изображений. DocumentDevice ориентирован на конвертацию всего документа, а ImageDevice - для конкретной страницы.

## Конвертация PDF с использованием класса DocumentDevice

**Aspose.PDF для Java** позволяет конвертировать страницы PDF в изображения TIFF.

Класс [TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) позволяет конвертировать страницы PDF в изображения TIFF.
 Этот класс предоставляет метод с именем Process, который позволяет конвертировать все страницы PDF-файла в одно изображение TIFF.

### Конвертация страниц PDF в одно изображение TIFF

Aspose.PDF для Java объясняет, как конвертировать все страницы PDF-файла в одно изображение TIFF:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
2. Вызовите метод [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-), чтобы конвертировать документ.
3. Для установки свойств выходного файла используйте класс [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

Следующий фрагмент кода показывает, как конвертировать все страницы PDF в одно изображение TIFF.

```java
// Открытие документа
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Создание объекта Resolution
Resolution resolution = new Resolution(300);

// Создание объекта TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// Создание устройства TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Конвертация определенной страницы и сохранение изображения в поток
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### Преобразование одной страницы в изображение TIFF

Aspose.PDF для Java позволяет преобразовать определенную страницу в PDF-файле в изображение TIFF, используя перегруженную версию метода Process(..), которая принимает номер страницы в качестве аргумента для преобразования. Следующий фрагмент кода показывает, как преобразовать первую страницу PDF в формат TIFF.

```java
// Открыть документ
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// Создать объект Resolution
Resolution resolution = new Resolution(300);

// Создать объект TiffSettings
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// Создать устройство TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// Преобразовать определенную страницу и сохранить изображение в поток
tiffDevice.process(document, 1, 1, tiffFileName);
```


### Использование алгоритма Брэдли во время конверсии

Aspose.PDF для Java поддерживает функцию преобразования PDF в TIFF с использованием сжатия LZW, а затем с использованием AForge может быть применена бинаризация. Однако один из клиентов запросил, чтобы для некоторых изображений им нужно было получать пороговое значение с использованием метода Оцу, поэтому они также хотели бы использовать метод Брэдли.

```java
// Открыть документ
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// Создать объект разрешения
Resolution resolution = new Resolution(300);
// Создать объект настроек TIFF
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// Создать устройство TIFF
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// Преобразовать конкретную страницу и сохранить изображение в поток
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// Создать объект потока для сохранения выходного изображения
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### Преобразование страниц PDF в пикселизированные изображения TIFF

Чтобы преобразовать все страницы PDF-файла в пикселизированный формат TIFF, используйте опцию Pixelated из IndexedConversionType

```java
// Преобразование страниц PDF в пикселизированные изображения TIFF
// Чтобы преобразовать все страницы PDF-файла в пикселизированный формат TIFF, используйте
// опцию Pixelated из IndexedConversionType.

// Открыть документ
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// Создать объект потока для сохранения выходного изображения
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// Создать объект Resolution
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// создать объект TiffSettings
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// установить сжатие результирующего изображения TIFF
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// установить глубину цвета для результирующего изображения
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// пропустить пустые страницы при рендеринге PDF в TIFF
tiffSettings.setSkipBlankPages(true);
// установить яркость изображения
tiffSettings.setBrightness(.5f);

// установить IndexedConversion Type, значение по умолчанию — простое
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// Создать объект TiffDevice с определенным разрешением
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// Преобразовать определенную страницу (страница 1) и сохранить изображение в поток
tiffDevice.process(document, 1, 1, imageStream);

// Закрыть поток
imageStream.close();
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF for Java предлагает вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете изучить функциональность и качество его работы.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Конвертация PDF с использованием класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Формат файла изображений Bitmap">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Формат Enhanced Meta File">EMF</abbr>.

- Класс [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) позволяет конвертировать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.
- Класс [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте рассмотрим, как конвертировать страницу PDF в изображение.

Класс [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) предоставляет метод с именем [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-), который позволяет конвертировать определенную страницу PDF-файла в формат изображения BMP. У других классов есть тот же метод. Таким образом, если нам нужно конвертировать страницу PDF в изображение, мы просто создаем экземпляр необходимого класса.

Следующий фрагмент кода демонстрирует эту возможность:

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Конвертация PDF в изображение.
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Создать объект Resolution
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // Конвертировать определенную страницу и сохранить изображение в поток
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Закрыть поток
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для Java предлагает вам бесплатное онлайн-приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать изучить функциональность и качество работы.

[![Как преобразовать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразование PDF с использованием класса SaveOptions

Эта часть статьи показывает, как преобразовать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> с помощью Java и класса SaveOptions.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF для Java предлагает вам бесплатное онлайн-приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать изучить функциональность и качество работы.

[![Aspose.PDF Преобразование PDF в SVG с помощью бесплатного приложения](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций формата файлов на основе XML для двухмерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML. Это означает, что они могут быть найдены, индексированы, скриптованы и, при необходимости, сжаты. Поскольку файлы XML, изображения SVG могут быть созданы и отредактированы с помощью любого текстового редактора, но чаще всего их удобнее создавать с помощью программ для рисования, таких как Inkscape.

### Преобразование страниц PDF в изображения SVG

Aspose.PDF для Java поддерживает функцию преобразования PDF файлов в формат SVG.
 Чтобы выполнить это требование, в пакет com.aspose.pdf был добавлен класс [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions). Создайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) и передайте его в качестве второго аргумента в метод [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Приведенный ниже фрагмент кода показывает шаги для конвертации PDF файла в формат SVG.

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Преобразование PDF в SVG.
 */
public class ConvertPDFtoSVG {
    // Путь к каталогу документов.
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // Загрузить PDF документ
        Document document = new Document(pdfFileName);

        // Создать объект SvgSaveOptions
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // Не сжимать SVG изображение в Zip архив
        saveOptions.setCompressOutputToZipArchive(false);

        // Сохранить вывод в файлы SVG
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```