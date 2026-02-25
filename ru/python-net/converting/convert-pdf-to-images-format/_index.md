---
title: Конвертировать PDF в различные форматы изображений на Python
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /ru/python-net/convert-pdf-to-images-format/
lastmod: "2025-09-27"
description: Узнайте, как конвертировать страницы PDF в изображения, такие как PNG, JPEG или TIFF, используя Aspose.PDF в Python через .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в форматы изображений на Python
Abstract: В этой статье представлено полное руководство по конвертации файлов PDF в различные форматы изображений с использованием Python, в частности библиотеки Aspose.PDF for Python. Документ описывает методы конвертации PDF в форматы изображений, включая TIFF, BMP, EMF, JPG, PNG, GIF и SVG. Обсуждаются два основных подхода к конвертации — использование подхода Device и SaveOption. Подход Device подразумевает использование классов, таких как `DocumentDevice` и `ImageDevice`, для конвертации всего документа или отдельных страниц. Предоставлены подробные шаги и примеры кода на Python для конвертации страниц PDF в различные форматы, такие как TIFF с помощью `TiffDevice`, а также BMP, EMF, JPEG, PNG и GIF с использованием соответствующих классов устройств (`BmpDevice`, `EmfDevice`, `JpegDevice`, `PngDevice`, `GifDevice`). Для конвертации в SVG вводится класс `SvgSaveOptions`. В статье также отмечены онлайн‑инструменты для пробования этих конвертаций.
---

## Конвертация PDF в изображение на Python

**Aspose.PDF for Python** использует несколько подходов для конвертации PDF в изображение. Как правило, мы используем два подхода: конвертация с использованием подхода Device и конвертация с использованием SaveOption. В этом разделе будет показано, как конвертировать документы PDF в форматы изображений, такие как BMP, JPEG, GIF, PNG, EMF, TIFF и SVG, используя один из этих подходов.

Существует несколько классов в библиотеке, которые позволяют использовать виртуальное устройство для преобразования изображений. DocumentDevice предназначен для конвертации всего документа, а ImageDevice — для отдельной страницы.

## Конвертация PDF с помощью класса DocumentDevice

**Aspose.PDF for Python** делает возможным конвертировать страницы PDF в изображения TIFF.

Класс [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) (основанный на DocumentDevice) позволяет конвертировать страницы PDF в изображения TIFF. Этот класс предоставляет метод с именем [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods), который позволяет преобразовать все страницы PDF‑файла в одно изображение TIFF.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF for Python через .NET предлагает вам бесплатное онлайн‑приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать изучить его функциональность и качество работы.

[![Конвертация Aspose.PDF PDF в TIFF с бесплатным приложением](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Конвертировать страницы PDF в одно изображение TIFF

Aspose.PDF for Python объясняет, как конвертировать все страницы PDF‑файла в одно изображение TIFF:

Шаги: Конвертировать PDF в TIFF на Python

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте объекты [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) и [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Вызовите метод [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) для конвертации PDF‑документа в TIFF.
1. Чтобы задать свойства выходного файла, используйте класс [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/).

Следующий фрагмент кода показывает, как конвертировать все страницы PDF в одно изображение TIFF.

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

## Конвертация PDF с помощью класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) позволяет конвертировать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) позволяет конвертировать страницы PDF в изображения <abbr title="Enhanced Meta File">EMF</abbr>.
- Класс [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) позволяет конвертировать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) позволяет конвертировать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.
- Класс [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) позволяет конвертировать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте посмотрим, как конвертировать страницу PDF в изображение.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) класс предоставляет метод с именем [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods), который позволяет конвертировать определённую страницу PDF‑файла в формат изображения BMP. Другие классы имеют тот же метод. Поэтому, если нам нужно конвертировать страницу PDF в изображение, мы просто создаём экземпляр необходимого класса.

Следующие шаги и фрагмент кода на Python демонстрируют эту возможность:

- [Конвертировать PDF в BMP на Python](#python-pdf-to-image)
- [Конвертировать PDF в EMF на Python](#python-pdf-to-image)
- [Конвертировать PDF в JPG на Python](#python-pdf-to-image)
- [Конвертировать PDF в PNG на Python](#python-pdf-to-image)
- [Конвертировать PDF в GIF на Python](#python-pdf-to-image)

Шаги: PDF в изображение (BMP, EMF, JPG, PNG, GIF) на Python

1. Загрузите PDF‑файл, используя класс [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте экземпляр подкласса [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/), т.е.
* [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (для преобразования PDF в BMP)
* [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (для преобразования PDF в Emf)
* [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (для преобразования PDF в JPG)
* [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (для преобразования PDF в PNG)
* [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (для преобразования PDF в GIF)
1. Вызовите метод [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) для выполнения преобразования PDF в изображение.

### Преобразовать PDF в BMP

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

### Преобразовать PDF в EMF

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


### Преобразовать PDF в PNG

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

### Преобразовать PDF в PNG с шрифтом по умолчанию

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

### Преобразовать PDF в GIF

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

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF for Python представляет вам онлайн бесплатное приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попробовать изучить функциональность и качество его работы.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразовать PDF с использованием класса SaveOptions

В этой части статьи показано, как преобразовать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr> с помощью Python и класса SaveOptions.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попробовать изучить функциональность и качество его работы.

[![Конвертация PDF в SVG с помощью бесплатного приложения Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Масштабируемая векторная графика (SVG)** — это семейство спецификаций XML‑основанного формата файлов для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается World Wide Web Consortium (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, скриптовать и при необходимости сжимать. Как XML‑файлы, изображения SVG могут создаваться и редактироваться любым текстовым редактором, но часто удобнее создавать их в графических программах, таких как Inkscape.

Aspose.PDF for Python поддерживает возможность конвертировать изображение SVG в формат PDF, а также предоставляет возможность преобразовывать файлы PDF в формат SVG. Для реализации этой задачи в пространство имён Aspose.PDF был введён класс [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/). Создайте объект SvgSaveOptions и передайте его в качестве второго аргумента методу [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает шаги по преобразованию PDF‑файла в формат SVG с помощью Python.

Шаги: Преобразование PDF в SVG на Python

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) с необходимыми настройками.
1. Вызовите метод [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods), передав ему объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/), чтобы преобразовать PDF‑документ в SVG.

### Преобразовать PDF в SVG

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

