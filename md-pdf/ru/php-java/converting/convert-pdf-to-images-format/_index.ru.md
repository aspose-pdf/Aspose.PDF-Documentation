---
title: Конвертировать PDF в форматы изображений
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /php-java/convert-pdf-to-images-format/
lastmod: "2024-05-20"
description: Эта тема показывает, как Aspose.PDF позволяет конвертировать PDF в различные форматы изображений. Конвертируйте страницы PDF в изображения PNG, JPEG, BMP с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for PHP** позволяет конвертировать PDF-документы в форматы изображений, такие как BMP, JPEG, GIF, PNG, EMF, TIFF и SVG, используя два подхода. Конвертация выполняется с использованием `Device` и `SaveOption`.

В библиотеке есть несколько классов, которые позволяют использовать виртуальное устройство для преобразования изображений. `DocumentDevice` ориентирован на конвертацию всего документа, а `ImageDevice` - для конкретной страницы.

## Конвертация PDF с использованием класса DocumentDevice

**Aspose.PDF for PHP** позволяет конвертировать страницы PDF в изображения TIFF.

Класс [TiffDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice) позволяет конвертировать страницы PDF в изображения TIFF.
 Этот класс предоставляет метод с именем Process, который позволяет конвертировать все страницы PDF файла в одно изображение TIFF.

### Конвертация страниц PDF в одно изображение TIFF

Aspose.PDF для PHP объясняет, как конвертировать все страницы PDF файла в одно изображение TIFF:

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Вызовите метод [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) для конвертации документа.
1. Чтобы установить свойства выходного файла, используйте класс [TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings).

Следующий фрагмент кода показывает, как конвертировать все страницы PDF в одно изображение TIFF.

```php
// Загрузить PDF документ
$document = new Document($inputFile);

// Создать новый объект TiffSettings
$tiffSettings = new devices_TiffSettings();

// Раскомментируйте следующие строки для настройки параметров TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Установить разрешение для изображения TIFF
$resolution = new devices_Resolution(300);

// Создать новый объект TiffDevice с указанным разрешением и настройками
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Конвертировать PDF документ в TIFF с использованием TiffDevice
$tiffDevice->process($document, $outputFile);
```

### Конвертация одной страницы в изображение TIFF

Aspose.PDF для PHP позволяет конвертировать определенную страницу PDF файла в изображение TIFF, используя перегруженную версию метода Process(..), который принимает номер страницы в качестве аргумента для конвертации. Следующий фрагмент кода показывает, как конвертировать первую страницу PDF в формат TIFF.

```php
// Загрузить PDF документ
$document = new Document($inputFile);

// Создать новый объект TiffSettings
$tiffSettings = new devices_TiffSettings();

// Раскомментируйте следующие строки, чтобы настроить параметры TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

// Установить разрешение для изображения TIFF
$resolution = new devices_Resolution(300);

// Создать новый объект TiffDevice с указанным разрешением и настройками
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Конвертировать PDF документ в TIFF, используя TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);
```


### Используйте алгоритм Брэдли во время конверсии

Aspose.PDF для PHP поддерживает функцию преобразования PDF в TIFF с использованием сжатия LZW, а затем с использованием AForge можно применить бинаризацию. Однако один из клиентов запросил, чтобы для некоторых изображений им нужно было получить пороговое значение, используя алгоритм Отсу, поэтому они также хотели бы использовать Брэдли.

```php
// Создать новый объект TiffSettings
$tiffSettings = new devices_TiffSettings();

// Раскомментируйте следующие строки, чтобы настроить параметры TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);

$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Установить разрешение для изображения TIFF
$resolution = new devices_Resolution(300);

// Создать новый объект TiffDevice с заданным разрешением и настройками
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Преобразовать документ PDF в TIFF с использованием TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Создать объект потока для сохранения выходного изображения
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


### Преобразование страниц PDF в пикселированные изображения TIFF

Чтобы преобразовать все страницы в PDF-файле в пикселированный формат TIFF, используйте опцию Pixelated типа IndexedConversionType

```php
// Создайте новый объект TiffSettings
$tiffSettings = new devices_TiffSettings();

// Раскомментируйте следующие строки, чтобы настроить параметры TIFF
// $tiffSettings->setCompression(devices_CompressionType::$NoneNone);
// $tiffSettings->setDepth(devices_ColorDepth::$DefaultDefault);
// $tiffSettings->setShape(devices_ShapeType::$Portrait);
// $tiffSettings->setSkipBlankPages(false);
// установите яркость изображения
$tiffSettings->setBrightness(0.5f);
// установите индексированный тип преобразования, значение по умолчанию - простое
$tiffSettings->setIndexedConversionType(IndexedConversionType::Pixelated);


$outputImageFile = new java("java.io.FileOutputStream", $outputImageFileName);
$outputBinImageFile = new java("java.io.FileOutputStream", $outputBinImageFileName);

// Установите разрешение для изображения TIFF
$resolution = new devices_Resolution(300);

// Создайте новый объект TiffDevice с указанным разрешением и настройками
$tiffDevice = new devices_TiffDevice($resolution, $tiffSettings);

// Преобразуйте PDF-документ в TIFF с использованием TiffDevice
$tiffDevice->process($document, 1, 1, $outputFile);

// Создайте объект потока для сохранения выходного изображения
$inStream = new java("java.io.FileInputStream",$outputImageFileName);
$tiffDevice->binarizeBradley($inStream, $outputBinImageFile, 0.1);
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF для PHP предлагает вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете опробовать функциональность и качество работы.

[![Aspose.PDF конвертация PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Конвертация PDF с использованием класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Enhanced Meta File">EMF</abbr>.

- Класс [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) позволяет конвертировать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.
- Класс [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) позволяет конвертировать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте посмотрим, как конвертировать страницу PDF в изображение.

Класс [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) предоставляет метод с именем [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-), который позволяет конвертировать определённую страницу PDF-файла в формат изображения BMP. Другие классы имеют такой же метод. Таким образом, если нам нужно конвертировать страницу PDF в изображение, мы просто создаём экземпляр нужного класса.

Следующий фрагмент кода демонстрирует эту возможность:

```php
// Загрузить PDF-документ
$document = new Document($inputFile);

// Получить коллекцию страниц в документе
$pages = $document->getPages();

// Получить общее количество страниц в документе
$count = $pages->size();

// Установить разрешение для PNG изображений
$resolution = new devices_Resolution(300);

// Создать новое устройство PNG с указанным разрешением
$imageDevice = new devices_PngDevice($resolution);

// Перебрать каждую страницу в документе
for ($pageCount = 1; $pageCount <= $document->getPages()->size(); $pageCount++) {
    // Установить имя выходного файла изображения для текущей страницы
    $imageFileName = $imageFileNameTemplate . $pageCount . '.png';

    // Получить текущую страницу из коллекции
    $page = $document->getPages()->get_Item($pageCount);

    // Обработать текущую страницу и сохранить её как изображение PNG
    $imageDevice->process($page, $imageFileName);
}
```


{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для PHP представляет вам бесплатное онлайн-приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать изучить функциональность и качество работы.

[![Как конвертировать PDF в PNG, используя бесплатное приложение](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Конвертация PDF с использованием класса SaveOptions

Эта часть статьи показывает, как конвертировать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr>, используя Java и класс SaveOptions.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF для PHP представляет вам бесплатное онлайн-приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать изучить функциональность и качество работы.

[![Конвертация PDF в SVG с бесплатным приложением Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статичной, так и динамичной (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

SVG-изображения и их поведение определяются в текстовых файлах XML. Это означает, что они могут быть найдены, индексированы, скриптованы и, если необходимо, сжаты. Как и XML-файлы, SVG-изображения могут быть созданы и отредактированы с помощью любого текстового редактора, но чаще всего их удобнее создавать с помощью программ для рисования, таких как Inkscape.

### Конвертирование страниц PDF в изображения SVG

Aspose.PDF для PHP поддерживает функцию преобразования PDF-файлов в формат SVG.
 Для выполнения этого требования в пакет com.aspose.pdf был введен класс [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions). Создайте экземпляр объекта [SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) и передайте его в качестве второго аргумента методу [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Следующий фрагмент кода показывает шаги для преобразования PDF-файла в формат SVG.

```php
// Загрузить PDF-документ
$document = new Document($inputFile);

// Создать экземпляр класса SvgSaveOptions
$saveOption = new SvgSaveOptions();

// Сохранить PDF-документ как SVG
$document->save($outputFile, $saveOption);
```