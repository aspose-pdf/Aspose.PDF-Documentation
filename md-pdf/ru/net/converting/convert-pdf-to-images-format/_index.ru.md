---
title: Конвертация PDF в различные форматы изображений в C#
linktitle: Конвертация PDF в изображения
type: docs
weight: 70
url: /net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: Эта тема показывает, как использовать Aspose.PDF для конвертации PDF в различные форматы изображений, такие как TIFF, BMP, EMF, JPEG, PNG, GIF, SVG, с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Обзор

Эта статья объясняет, как конвертировать PDF в различные форматы изображений с помощью C#. Она охватывает следующие темы.

_Формат изображения_: **TIFF**
- [C# PDF в TIFF](#csharp-pdf-to-tiff)
- [C# Конвертация PDF в TIFF](#csharp-pdf-to-tiff)
- [C# Конвертация одной или определенных страниц PDF в TIFF](#csharp-pdf-to-tiff-pages)

_Формат изображения_: **BMP**
- [C# PDF в BMP](#csharp-pdf-to-bmp)
- [C# Конвертация PDF в BMP](#csharp-pdf-to-bmp)
- [C# Конвертер PDF в BMP](#csharp-pdf-to-bmp)

_Формат изображения_: **EMF**
- [C# PDF в EMF](#csharp-pdf-to-emf)
- [C# Конвертация PDF в EMF](#csharp-pdf-to-emf)
- [C# Конвертер PDF в EMF](#csharp-pdf-to-emf)
- [C# Конвертер PDF в EMF](#csharp-pdf-to-emf)

_Формат изображения_: **JPG**
- [C# PDF в JPG](#csharp-pdf-to-jpg)
- [C# Конвертировать PDF в JPG](#csharp-pdf-to-jpg)
- [C# Конвертер PDF в JPG](#csharp-pdf-to-jpg)

_Формат изображения_: **PNG**
- [C# PDF в PNG](#csharp-pdf-to-png)
- [C# Конвертировать PDF в PNG](#csharp-pdf-to-png)
- [C# Конвертер PDF в PNG](#csharp-pdf-to-png)

_Формат изображения_: **GIF**
- [C# PDF в GIF](#csharp-pdf-to-gif)
- [C# Конвертировать PDF в GIF](#csharp-pdf-to-gif)
- [C# Конвертер PDF в GIF](#csharp-pdf-to-gif)

_Формат изображения_: **SVG**
- [C# PDF в SVG](#csharp-pdf-to-svg)
- [C# Конвертировать PDF в SVG](#csharp-pdf-to-svg)
- [C# Конвертер PDF в SVG](#csharp-pdf-to-svg)

## C# Конвертация PDF в изображение

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

**Aspose.PDF для .NET** использует несколько подходов для конвертации PDF в изображение.
**Aspose.PDF для .NET** использует несколько подходов для конвертации PDF в изображение.

В библиотеке есть несколько классов, которые позволяют использовать виртуальное устройство для преобразования изображений. DocumentDevice ориентирован на конвертацию всего документа, а ImageDevice - на конвертацию конкретной страницы.

## Конвертация PDF с использованием класса DocumentDevice

**Aspose.PDF для .NET** позволяет конвертировать страницы PDF в изображения TIFF.

Класс TiffDevice (основанный на DocumentDevice) позволяет конвертировать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем `Process`, который позволяет конвертировать все страницы в файле PDF в одно изображение TIFF.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн-приложение ["PDF в TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете изучить функциональность и качество его работы.

[![Конвертация Aspose.PDF PDF в TIFF с использованием бесплатного приложения](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Конвертирование страниц PDF в один TIFF файл

Aspose.PDF для .NET объясняет, как конвертировать все страницы PDF файла в одно изображение TIFF:

<a name="csharp-pdf-to-tiff"><strong>Шаги: Конвертация PDF в TIFF на C#</strong></a>

1. Создайте объект класса **Document**.
2. Создайте объекты **TiffSettings** и **TiffDevice**.
3. Вызовите метод **TiffDevice.Process()** для конвертации PDF документа в TIFF.
4. Для настройки свойств выходного файла используйте класс **TiffSettings**.

Следующий пример кода показывает, как конвертировать все страницы PDF в одно изображение TIFF.

```csharp
public static void ConvertPDFtoTIFF()
{
    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Создать объект Resolution
    Resolution resolution = new Resolution(300);

    // Создать объект TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // Создать устройство TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Конвертировать определенную страницу и сохранить изображение в поток
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### Конвертирование одной страницы в изображение TIFF

Aspose.PDF для .NET позволяет конвертировать конкретную страницу PDF файла в изображение TIFF, используя перегруженную версию метода Process(..), который принимает номер страницы в качестве аргумента для конвертации. Следующий код показывает, как конвертировать первую страницу PDF в формат TIFF.

<a name="csharp-pdf-to-tiff-pages"><strong>Шаги: Конвертация одной или конкретных страниц PDF в TIFF в C#</strong></a>

1. Создайте объект класса **Document**.
2. Создайте объекты **TiffSettings** и **TiffDevice**.
3. Вызовите перегруженный метод **TiffDevice.Process()** с параметрами **fromPage** и **toPage** для конвертации страниц документа PDF в TIFF.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // Открыть документ
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Создать объект Resolution
    Resolution resolution = new Resolution(300);

    // Создать объект TiffSettings
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // Создать устройство TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // Конвертировать конкретную страницу и сохранить изображение в поток
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### Используйте алгоритм Брэдли при конвертации

Aspose.PDF для .NET поддерживает функцию конвертации PDF в TIF с использованием сжатия LZW, а затем с использованием AForge можно применить бинаризацию. Однако один из клиентов запросил, чтобы для некоторых изображений получить порог с использованием Отсу, поэтому они также хотели бы использовать Брэдли.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // Открыть документ
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Создать объект разрешения
    Resolution resolution = new Resolution(300);
    // Создать объект настроек TIFF
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // Создать устройство TIFF
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // Конвертировать определенную страницу и сохранить изображение в поток
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## Конвертация PDF с использованием класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) позволяет конвертировать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) позволяет конвертировать страницы PDF в изображения <abbr title="Enhanced Meta File">EMF</abbr>.
- Класс [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) позволяет конвертировать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) позволяет конвертировать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.
- Класс [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) позволяет конвертировать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте рассмотрим, как конвертировать страницу PDF в изображение.
Давайте посмотрим, как конвертировать страницу PDF в изображение.

Класс `BmpDevice` предоставляет метод под названием [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process), который позволяет конвертировать определенную страницу PDF файла в формат изображения BMP. Другие классы имеют тот же метод. Таким образом, если нам нужно конвертировать страницу PDF в изображение, мы просто создаем экземпляр необходимого класса.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>
    
Следующие шаги и фрагмент кода на C# демонстрируют эту возможность

 - [Конвертировать PDF в BMP на C#](#csharp-pdf-to-image)
 - [Конвертировать PDF в EMF на C#](#csharp-pdf-to-image)
 - [Конвертировать PDF в JPG на C#](#csharp-pdf-to-image)
 - [Конвертировать PDF в PNG на C#](#csharp-pdf-to-image)
 - [Конвертировать PDF в GIF на C#](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Шаги: PDF в Изображение (BMP, EMF, JPG, PNG, GIF) на C#</strong></a>

1.
1.
2. Создайте экземпляр подкласса **ImageDevice**, например:
   * **BmpDevice** (для конвертации PDF в BMP)
   * **EmfDevice** (для конвертации PDF в Emf)
   * **JpegDevice** (для конвертации PDF в JPG)
   * **PngDevice** (для конвертации PDF в PNG)
   * **GifDevice** (для конвертации PDF в GIF)
3. Вызовите метод **ImageDevice.Process()** для выполнения конвертации PDF в изображение.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // Создание объекта Resolution            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // Конвертация конкретной страницы и сохранение изображения в поток
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // Закрытие потока
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете исследовать функциональность и качество его работы.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Конвертация PDF с использованием класса SaveOptions

Эта часть статьи показывает, как конвертировать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> с использованием C# и класса SaveOptions.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF для .NET представляет вам бесплатное онлайн приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в SVG с помощью бесплатного приложения](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Масштабируемая векторная графика (SVG)** представляет собой семейство спецификаций основанного на XML формата файла для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, программировать и при необходимости сжимать. Как файлы XML, изображения SVG могут быть созданы и отредактированы в любом текстовом редакторе, однако часто более удобно создавать их с помощью программ для рисования, таких как Inkscape.

Aspose.PDF для .NET поддерживает функцию конвертации изображения SVG в формат PDF, а также предлагает возможность конвертации файлов PDF в формат SVG.
Aspose.PDF для .NET поддерживает функцию конвертации изображений SVG в формат PDF, а также предлагает возможность конвертировать файлы PDF в формат SVG.

Следующий фрагмент кода показывает шаги для конвертации файла PDF в формат SVG с помощью .NET.

<a name="csharp-pdf-to-svg"><strong>Шаги: Конвертация PDF в SVG на C#</strong></a>

1. Создайте объект класса **Document**.
2. Создайте объект **SvgSaveOptions** с необходимыми настройками.
3. Вызовите метод **Document.Save()** и передайте ему объект **SvgSaveOptions** для конвертации документа PDF в SVG.

```csharp
public static void ConvertPDFtoSVG()
{
    // Загрузка документа PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // Создание объекта SvgSaveOptions
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // Не сжимать изображение SVG в архив Zip
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // Сохранение результата в файлы SVG
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

