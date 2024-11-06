---
title: Конвертация PDF в различные форматы изображений на Python
linktitle: Конвертация PDF в изображения
type: docs
weight: 70
url: ru/python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: Эта тема показывает, как использовать Aspose.PDF для Python для конвертации PDF в различные форматы изображений, такие как TIFF, BMP, EMF, JPEG, PNG, GIF, SVG, с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Обзор

В этой статье объясняется, как конвертировать PDF в различные форматы изображений с использованием Python. Она охватывает следующие темы.

_Формат изображения_: **TIFF**
- [Python PDF в TIFF](#python-pdf-to-tiff)
- [Python Конвертация PDF в TIFF](#python-pdf-to-tiff)
- [Python Конвертация отдельных или конкретных страниц PDF в TIFF](#python-pdf-to-tiff-pages)


_Формат изображения_: **BMP**
- [Python PDF в BMP](#python-pdf-to-bmp)
- [Python Конвертация PDF в BMP](#python-pdf-to-bmp)
- [Python PDF в BMP Конвертер](#python-pdf-to-bmp)

_Формат изображения_: **EMF**
- [Python PDF в EMF](#python-pdf-to-emf)

- [Python Конвертация PDF в EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_Формат изображения_: **JPG**
- [Python PDF в JPG](#python-pdf-to-jpg)
- [Python Конвертировать PDF в JPG](#python-pdf-to-jpg)
- [Python Конвертер PDF в JPG](#python-pdf-to-jpg)

_Формат изображения_: **PNG**
- [Python PDF в PNG](#python-pdf-to-png)
- [Python Конвертировать PDF в PNG](#python-pdf-to-png)
- [Python Конвертер PDF в PNG](#python-pdf-to-png)

_Формат изображения_: **GIF**
- [Python PDF в GIF](#python-pdf-to-gif)
- [Python Конвертировать PDF в GIF](#python-pdf-to-gif)
- [Python Конвертер PDF в GIF](#python-pdf-to-gif)

_Формат изображения_: **SVG**
- [Python PDF в SVG](#python-pdf-to-svg)
- [Python Конвертировать PDF в SVG](#python-pdf-to-svg)
- [Python Конвертер PDF в SVG](#python-pdf-to-svg)

## Python Конвертировать PDF в изображение

**Aspose.PDF для Python** использует несколько подходов для конвертации PDF в изображение.
 В общем, мы используем два подхода: преобразование с использованием Device подхода и преобразование с использованием SaveOption. Этот раздел покажет вам, как преобразовать PDF-документы в форматы изображений, такие как BMP, JPEG, GIF, PNG, EMF, TIFF и SVG, используя один из этих подходов.

В библиотеке имеется несколько классов, которые позволяют использовать виртуальное устройство для преобразования изображений. DocumentDevice ориентирован на преобразование всего документа, а ImageDevice - для определённой страницы.

## Преобразование PDF с использованием класса DocumentDevice

**Aspose.PDF для Python** позволяет преобразовывать страницы PDF в изображения TIFF.

Класс [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (основанный на DocumentDevice) позволяет преобразовывать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods), который позволяет преобразовать все страницы в PDF-файле в одно изображение TIFF.

{{% alert color="success" %}}

**Попробуйте преобразовать PDF в TIFF онлайн**
Aspose.PDF для Python через .NET представляет вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Преобразование страниц PDF в одно изображение TIFF

Aspose.PDF для Python объясняет, как преобразовать все страницы в PDF-файле в одно изображение TIFF:

<a name="csharp-pdf-to-tiff"><strong>Шаги: Преобразование PDF в TIFF на Python</strong></a>

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Создайте объекты [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) и [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).

3. Вызовите метод [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods), чтобы преобразовать PDF-документ в TIFF.
4. Чтобы задать свойства выходного файла, используйте класс [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в одно изображение TIFF.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    # Создать объект разрешения
    resolution = ap.devices.Resolution(300)

    # Создать объект TiffSettings
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # Создать устройство TIFF
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # Преобразовать конкретную страницу и сохранить изображение в поток
    tiffDevice.process(document, output_pdf)
```


## Преобразование PDF с использованием класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Enhanced Meta File">EMF</abbr>.
- Класс [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) позволяет преобразовывать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.

- Класс [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте рассмотрим, как преобразовать страницу PDF в изображение.

Класс [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) предоставляет метод под названием [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods), который позволяет преобразовать определенную страницу PDF файла в формат изображения BMP. Другие классы имеют тот же метод. Таким образом, если нам нужно преобразовать страницу PDF в изображение, мы просто создаем экземпляр необходимого класса.

Следующие шаги и фрагмент кода на Python демонстрируют эту возможность

 - [Преобразовать PDF в BMP на Python](#python-pdf-to-image)
 - [Преобразовать PDF в EMF на Python](#python-pdf-to-image)
 - [Преобразовать PDF в JPG на Python](#python-pdf-to-image)
 - [Преобразовать PDF в PNG на Python](#python-pdf-to-image)
 - [Преобразовать PDF в GIF на Python](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Шаги: PDF в изображение (BMP, EMF, JPG, PNG, GIF) на Python</strong></a>

1. Загрузите PDF-файл, используя класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Создайте экземпляр подкласса [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/), например:
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (для конвертации PDF в BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (для конвертации PDF в Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (для конвертации PDF в JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (для конвертации PDF в PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (для конвертации PDF в GIF)
3. Вызовите метод [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) для выполнения конвертации PDF в изображение.

### Конвертировать PDF в BMP

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    # Создать объект разрешения
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # Создать файл для сохранения
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # Конвертировать конкретную страницу и сохранить изображение в поток
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### Конвертация PDF в EMF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    # Создать объект разрешения
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # Создать файл для сохранения
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # Конвертировать определенную страницу и сохранить изображение в поток
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### Конвертация PDF в JPEG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    # Создать объект разрешения
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # Создать файл для сохранения
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # Конвертировать определенную страницу и сохранить изображение в поток
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### Преобразование PDF в PNG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    # Создать объект разрешения
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # Создать файл для сохранения
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # Конвертировать определенную страницу и сохранить изображение в поток
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```

### Преобразование PDF в GIF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # Открыть PDF документ
    document = ap.Document(input_pdf)

    # Создать объект разрешения
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # Создать файл для сохранения
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # Конвертировать определенную страницу и сохранить изображение в поток
        device.process(document.pages[i + 1], imageStream)
        # Закрыть поток
        imageStream.close()
```


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете изучить функциональные возможности и качество его работы.

[![Как преобразовать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразование PDF с использованием класса SaveOptions

Эта часть статьи показывает, как преобразовать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> с использованием Python и класса SaveOptions.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF для Python через .NET предлагает вам бесплатное онлайн-приложение ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете изучить функциональные возможности и качество его работы.

[![Aspose.PDF Преобразование PDF в SVG с помощью бесплатного приложения](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** - это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

SVG-изображения и их поведение определяются в текстовых файлах XML. Это означает, что они могут быть найдены, индексированы, скриптованы и, если необходимо, сжаты. Как XML-файлы, SVG-изображения могут быть созданы и отредактированы с помощью любого текстового редактора, но чаще всего их удобнее создавать с помощью программ для рисования, таких как Inkscape.

Aspose.PDF for Python поддерживает функцию конвертации изображений SVG в формат PDF, а также предлагает возможность конвертации PDF-файлов в формат SVG.
 Чтобы выполнить это требование, в пространство имен Aspose.PDF был введен класс [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/). Создайте объект SvgSaveOptions и передайте его как второй аргумент в метод [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает шаги по преобразованию PDF-файла в формат SVG с помощью Python.

<a name="csharp-pdf-to-svg"><strong>Шаги: Преобразование PDF в SVG на Python</strong></a>

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Создайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) с необходимыми настройками.
3. Вызовите метод [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) и передайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/), чтобы конвертировать PDF-документ в SVG.

### Конвертация PDF в SVG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)

    # Создать экземпляр объекта SvgSaveOptions
    saveOptions = ap.SvgSaveOptions()

    # Не сжимать изображение SVG в Zip-архив
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # Сохранить вывод в файлы SVG
    document.save(output_pdf, saveOptions)
```