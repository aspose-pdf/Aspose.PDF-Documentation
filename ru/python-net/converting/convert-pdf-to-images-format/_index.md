---
title: Конвертировать PDF в форматы изображений в Python
linktitle: Конвертировать PDF в изображения
type: docs
weight: 70
url: /ru/python-net/convert-pdf-to-images-format/
lastmod: "2026-05-08"
description: Узнайте, как рендерить страницы PDF в файлы TIFF, BMP, EMF, JPEG, PNG, GIF и SVG в Python с помощью Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Преобразуйте страницы PDF в TIFF, PNG, JPEG, GIF, BMP, EMF и SVG в Python.
Abstract: В этой статье объясняется, как преобразовать файлы PDF в распространённые форматы изображений с помощью Aspose.PDF for Python via .NET. В ней рассматривается экспорт TIFF на уровне всего документа с использованием `TiffDevice`, генерация растровых изображений постранично с помощью подклассов `ImageDevice`, таких как `BmpDevice`, `JpegDevice`, `PngDevice`, `GifDevice` и `EmfDevice`, а также векторный экспорт в SVG с использованием `SvgSaveOptions`. Каждый раздел содержит основные шаги и примеры на Python, необходимые для сохранения содержимого PDF в виде изображений.
---

## Преобразование PDF в изображения в Python

**Aspose.PDF for Python via .NET** поддерживает несколько способов конвертации содержимого PDF в изображения. На практике большинство рабочих процессов использует один из двух вариантов:

- подход Device для рендеринга страниц PDF в растровые форматы изображений
- подход SaveOptions для экспорта содержимого PDF в SVG

В этой статье показано, как конвертировать PDF‑файлы в TIFF, BMP, EMF, JPEG, PNG, GIF и SVG.

Библиотека включает несколько классов рендеринга. `DocumentDevice` разработан для конвертации всего документа, в то время как `ImageDevice` нацелено на отдельные страницы.

## Преобразовать PDF с помощью класса DocumentDevice

Используйте `DocumentDevice`, если хотите вывести весь PDF в один многостраничный TIFF-файл.

Класс [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) основан на `DocumentDevice` и предоставляет метод [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) для преобразования всех страниц PDF-файла в один TIFF-файл.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["PDF в TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попытаться изучить функциональность и качество его работы.

[![Конвертация PDF в TIFF с приложением Aspose.PDF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Преобразовать страницы PDF в одно изображение TIFF

Aspose.PDF for Python via .NET может рендерить каждую страницу PDF‑файла в одно TIFF‑изображение.

Шаги: Конвертировать PDF в TIFF в Python

1. Загрузите исходный PDF с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте объекты [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) и [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/).
1. Настройте параметры TIFF, такие как сжатие, глубина цвета и обработка пустых страниц.
1. Вызовите метод [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods), чтобы записать TIFF-файл.

Следующий фрагмент кода показывает, как преобразовать все страницы PDF в одно изображение TIFF.

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_TIFF(infile, outfile):
    document = ap.Document(infile)

    resolution = ap.devices.Resolution(300)
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)
    tiffDevice.process(document, f"{outfile}.tiff")

    print(infile + " converted into " + outfile)
```

## Конвертировать PDF с использованием класса ImageDevice

Используйте `ImageDevice`, если вам нужен постраничный вывод в растровом формате.

`ImageDevice` является базовым классом для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) позволяет преобразовывать страницы PDF в BMP-изображения.
- Класс [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) позволяет преобразовывать страницы PDF в изображения EMF.
- Класс [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) позволяет преобразовывать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) позволяет преобразовывать страницы PDF в изображения PNG.
- Класс [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) позволяет преобразовывать страницы PDF в изображения GIF.

Рабочий процесс одинаков для каждого формата: загрузите документ, создайте соответствующее устройство, затем обработайте требуемую страницу.

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) предоставляет метод [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) для рендеринга конкретной страницы в BMP. Остальные классы `ImageDevice` работают по тому же шаблону, поэтому формат можно сменить, просто заменив класс устройства.

Следующие примеры показывают, как рендерить страницы PDF в распространённые форматы изображений:

- Конвертация PDF в BMP
- Конвертация PDF в EMF
- Конвертация PDF в JPEG
- Конвертация PDF в PNG
- Конвертация PDF в GIF

Шаги: PDF в изображение (BMP, EMF, JPG, PNG, GIF) на Python

1. Загрузите PDF-файл с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте экземпляр нужного подкласса [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/):
    - [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (для конвертации PDF в BMP)
    - [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (для конвертации PDF в EMF)
    - [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (для конвертации PDF в JPG)
    - [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (для преобразования PDF в PNG)
    - [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (для преобразования PDF в GIF)
1. Переберите страницы, которые вы хотите экспортировать.
1. Вызовите метод [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods), чтобы сохранить каждую страницу как изображение.

### Преобразовать PDF в BMP

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_BMP(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.bmp", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в EMF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_EMF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.emf", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```  

### Конвертировать PDF в JPEG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_JPEG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)
    page_count = 1

    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.jpeg", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PNG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    device = ap.devices.PngDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Конвертировать PDF в PNG с шрифтом по умолчанию

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_PNG_with_default_font(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)

    rendering_options = ap.RenderingOptions()
    rendering_options.default_font_name = "Arial"

    device = ap.devices.PngDevice(resolution)
    device.rendering_options = rendering_options

    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.png", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1
```

### Конвертировать PDF в GIF

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_GIF(infile, outfile):
    document = ap.Document(infile)
    resolution = ap.devices.Resolution(300)
    device = ap.devices.GifDevice(resolution)
    page_count = 1
    while page_count <= len(document.pages):
        image_stream = FileIO(outfile + str(page_count) + "_out.gif", "w")
        device.process(document.pages[page_count], image_stream)
        image_stream.close()
        page_count = page_count + 1

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши приложения, пожалуйста, проверьте следующую функцию.

Aspose.PDF for Python представляет вам онлайн‑приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попытаться изучить функциональность и качество его работы.

[![Как конвертировать PDF в PNG с помощью App](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Конвертировать PDF с использованием класса SaveOptions

Используйте `SaveOptions`, если хотите экспортировать содержимое PDF в SVG.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попытаться изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в SVG с приложением](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это основанный на XML формат двумерной векторной графики. Поскольку SVG остаётся векторным, он полезен, когда вам нужен масштабируемый вывод для веба, пользовательского интерфейса или дизайнерских рабочих процессов.

Файлы SVG являются текстовыми, пригодными для поиска и их легко постобрабатывать в других инструментах.

Aspose.PDF for Python via .NET может как конвертировать SVG в PDF, так и экспортировать страницы PDF в SVG. Для конвертации PDF в SVG создайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) и передайте его в метод [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующие шаги показывают, как преобразовать файл PDF в SVG с помощью Python.

Шаги: Преобразовать PDF в SVG с помощью Python

1. Загрузите исходный PDF с помощью класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Создайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) и настройте нужные параметры.
1. Вызовите метод [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) с экземпляром `SvgSaveOptions`, чтобы записать выходной SVG-файл.

### Конвертировать PDF в SVG

```python
import aspose.pdf as ap
from io import FileIO
from os import path
import sys

def convert_PDF_to_SVG(infile, outfile):
    document = ap.Document(infile)

    save_options = ap.SvgSaveOptions()
    save_options.compress_output_to_zip_archive = False
    save_options.treat_target_file_name_as_directory = True

    document.save(f"{outfile}.svg", save_options)
```

## Связанные преобразования

- [Конвертировать форматы изображений в PDF](/pdf/ru/python-net/convert-images-format-to-pdf/) когда вам нужно воссоздать PDF из JPG, PNG, TIFF, SVG или других источников изображений.
- [Преобразовать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) для вывода, удобного для браузера, вместо растровых изображений.
- [Конвертировать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) для рабочих процессов экспорта в EPUB, Markdown, текст и XPS.
