---
title: Конвертировать PDF в форматы изображений в Python
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /ru/python-net/convert-pdf-to-images-format/
lastmod: "2026-04-14"
description: Узнайте, как преобразовать страницы PDF в изображения, такие как PNG, JPEG или TIFF, используя Aspose.PDF в Python через .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в форматы изображений в Python
Abstract: Эта статья предоставляет исчерпывающее руководство по конвертации PDF‑файлов в различные форматы изображений с использованием Python, в частности с помощью библиотеки Aspose.PDF for Python. Документ описывает методы преобразования PDF в форматы изображений, включая TIFF, BMP, EMF, JPG, PNG, GIF и SVG. Рассмотрены два основных подхода к конвертации — использование подхода Device и SaveOption. Подход Device предполагает использование классов, таких как `DocumentDevice` и `ImageDevice`, для конвертации всего документа или отдельных страниц. Предоставлены подробные шаги и примеры кода на Python для преобразования страниц PDF в различные форматы, такие как TIFF с использованием `TiffDevice`, а также BMP, EMF, JPEG, PNG и GIF с помощью соответствующих классов устройств (`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). Для конвертации в SVG вводится класс `SvgSaveOptions`. В статье также отмечены онлайн‑инструменты для тестирования этих конвертаций.
---

## Python конвертировать PDF в изображение

**Aspose.PDF for Python** использует несколько подходов для преобразования PDF в изображение. Как правило, мы используем два подхода: преобразование с использованием подхода Device и преобразование с использованием SaveOption. В этом разделе будет показано, как преобразовать документы PDF в форматы изображений, такие как BMP, JPEG, GIF, PNG, EMF, TIFF и SVG, используя один из этих подходов.

В библиотеке есть несколько классов, позволяющих использовать виртуальное устройство для преобразования изображений. DocumentDevice ориентирован на преобразование всего документа, а ImageDevice — на отдельную страницу.

## Преобразовать PDF, используя класс DocumentDevice

**Aspose.PDF for Python** делает возможным конвертировать страницы PDF в изображения TIFF.

{"translatedText":""} [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (based on DocumentDevice) класс позволяет конвертировать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем [процесс](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) что позволяет конвертировать все страницы PDF‑файла в одно изображение TIFF.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["PDF в TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попытаться исследовать, как работает функция и качество.

[![Aspose.PDF конвертация PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Преобразовать страницы PDF в одно изображение TIFF

Aspose.PDF for Python объясняет, как преобразовать все страницы PDF‑файла в одно изображение TIFF:

Шаги: Конвертировать PDF в TIFF в Python

1. Создать объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Создать [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) и [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) объекты
1. Вызовите [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) метод преобразования PDF-документа в TIFF.
1. Чтобы установить свойства выходного файла, используйте [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) класс.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в одно изображение TIFF.

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    resolution = apdf.devices.Resolution(300)
    tiffSettings = apdf.devices.TiffSettings()
    tiffSettings.compression = apdf.devices.CompressionType.LZW
    tiffSettings.depth = apdf.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = apdf.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, path_outfile)

    print(infile + " converted into " + outfile)
```

## Преобразовать PDF с помощью класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- {"translatedText":""} [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) класс позволяет конвертировать страницы PDF в <abbr title="Bitmap Image File">BMP</abbr> изображения.
- {"translatedText":""} [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) класс позволяет конвертировать страницы PDF в <abbr title="Enhanced Meta File">EMF</abbr> изображения.
- {"translatedText":""} [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) Класс позволяет конвертировать страницы PDF в изображения JPEG.
- {"translatedText":""} [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) класс позволяет конвертировать страницы PDF в <abbr title="Portable Network Graphics">PNG</abbr> изображения.
- {"translatedText":""} [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) класс позволяет конвертировать страницы PDF в <abbr title="Graphics Interchange Format">GIF</abbr> изображения.

Давайте посмотрим, как преобразовать страницу PDF в изображение.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) класс предоставляет метод с именем [процесс](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) что позволяет конвертировать отдельную страницу PDF‑файла в формат изображения BMP. Другие классы имеют тот же метод. Таким образом, если нам нужно преобразовать страницу PDF в изображение, мы просто создаём экземпляр требуемого класса.

Следующие шаги и фрагмент кода на Python демонстрируют эту возможность:

 - [Конвертировать PDF в BMP на Python](#python-pdf-to-image)
 - [Конвертировать PDF в EMF на Python](#python-pdf-to-image)
 - [Преобразовать PDF в JPG с помощью Python](#python-pdf-to-image)
 - [Конвертировать PDF в PNG на Python](#python-pdf-to-image)
 - [Конвертировать PDF в GIF на Python](#python-pdf-to-image)

Шаги: PDF в изображение (BMP, EMF, JPG, PNG, GIF) на Python

1. Загрузите PDF-файл, используя [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Создать экземпляр подкласса [Устройство изображения](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) т.е.
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (для конвертации PDF в BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (для конвертации PDF в Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (для преобразования PDF в JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (для конвертации PDF в PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (для конвертации PDF в GIF)
1. Вызовите [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) метод для выполнения преобразования PDF в изображение.

### Конвертировать PDF в BMP

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в EMF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в JPEG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PNG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)

    device = apdf.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PNG с шрифтом по умолчанию

```python

    from os import path
    import aspose.pdf as ap
    from io import FileIO


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в GIF

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    resolution = apdf.devices.Resolution(300)
    device = apdf.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(path_outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, проверьте следующую функцию.

Aspose.PDF for Python предоставляет вам бесплатное онлайн‑приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попытаться исследовать, как работает функция и качество.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразовать PDF с использованием класса SaveOptions

Эта часть статьи показывает, как конвертировать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> используя Python и класс SaveOptions.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попытаться исследовать, как работает функция и качество.

[![Конвертация PDF в SVG с бесплатным приложением Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций XML‑формата файлов для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

SVG‑изображения и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, использовать в скриптах и, при необходимости, сжимать. Как файлы XML, SVG‑изображения можно создавать и редактировать с помощью любого текстового редактора, но часто удобнее создавать их в графических программах, таких как Inkscape.

Aspose.PDF for Python поддерживает функцию конвертации SVG‑изображения в формат PDF и также предлагает возможность конвертировать PDF‑файлы в формат SVG. Чтобы выполнить это требование, the [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) класс был введён в пространство имён Aspose.PDF. Создайте объект SvgSaveOptions и передайте его в качестве второго аргумента к [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод.

Следующий фрагмент кода показывает шаги по преобразованию PDF‑файла в формат SVG с помощью Python.

Шаги: Конвертировать PDF в SVG на Python

1. Создать объект [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) класс.
1. Создать [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) объект с необходимыми настройками.
1. Вызовите [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) метод и передать его [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) объект конвертирует PDF‑документ в SVG.

### Конвертировать PDF в SVG

```python

    from os import path
    import aspose.pdf as apdf
    from io import FileIO

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)

    save_options = apdf.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать форматы изображений в PDF](/pdf/ru/python-net/convert-images-format-to-pdf/) когда вам нужно воссоздавать PDF из JPG, PNG, TIFF, SVG или других источников изображений.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для вывода, удобного для браузера, вместо растровых изображений.
- [Конвертировать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) для рабочих процессов экспорта EPUB, Markdown, текста и XPS.
