---
title: Преобразование PDF в различные форматы изображений на Python
linktitle: Преобразование PDF в изображения
type: docs
weight: 70
url: /ru/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: Эта тема показывает, как использовать Aspose.PDF для Python для преобразования PDF в различные форматы изображений, такие как TIFF, BMP, EMF, JPEG, PNG, GIF, SVG, с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Обзор

Эта статья объясняет, как преобразовывать PDF в различные форматы изображений с использованием Python. Она охватывает следующие темы.

_Формат изображения_: **TIFF**
- [Python PDF в TIFF](#python-pdf-to-tiff)
- [Python Преобразование PDF в TIFF](#python-pdf-to-tiff)
- [Python Преобразование отдельных или определенных страниц PDF в TIFF](#python-pdf-to-tiff-pages)

_Формат изображения_: **BMP**
- [Python PDF в BMP](#python-pdf-to-bmp)
- [Python Преобразование PDF в BMP](#python-pdf-to-bmp)
- [Конвертер PDF в BMP на Python](#python-pdf-to-bmp)

_Формат изображения_: **EMF**
- [Python PDF в EMF](#python-pdf-to-emf)
- [Python Преобразование PDF в EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_Формат изображения_: **JPG**
- [Python PDF в JPG](#python-pdf-to-jpg)
- [Python Конвертация PDF в JPG](#python-pdf-to-jpg)
- [Python PDF в JPG Конвертер](#python-pdf-to-jpg)

_Формат изображения_: **PNG**
- [Python PDF в PNG](#python-pdf-to-png)
- [Python Конвертация PDF в PNG](#python-pdf-to-png)
- [Python PDF в PNG Конвертер](#python-pdf-to-png)

_Формат изображения_: **GIF**
- [Python PDF в GIF](#python-pdf-to-gif)
- [Python Конвертация PDF в GIF](#python-pdf-to-gif)
- [Python PDF в GIF Конвертер](#python-pdf-to-gif)

_Формат изображения_: **SVG**
- [Python PDF в SVG](#python-pdf-to-svg)
- [Python Конвертация PDF в SVG](#python-pdf-to-svg)
- [Python PDF в SVG Конвертер](#python-pdf-to-svg)

## Python Конвертация PDF в Изображение

**Aspose.PDF для Python** использует несколько подходов для конвертации PDF в изображение.
 В общем, мы используем два подхода: преобразование с использованием устройства и преобразование с использованием SaveOption. В этом разделе показано, как преобразовать PDF-документы в форматы изображений, такие как BMP, JPEG, GIF, PNG, EMF, TIFF и SVG, с использованием одного из этих подходов.

В библиотеке есть несколько классов, которые позволяют использовать виртуальное устройство для преобразования изображений. DocumentDevice ориентирован на преобразование всего документа, а ImageDevice - для конкретной страницы.

## Преобразование PDF с использованием класса DocumentDevice

**Aspose.PDF для Python** позволяет конвертировать страницы PDF в изображения TIFF.

Класс [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) (основанный на DocumentDevice) позволяет преобразовывать страницы PDF в изображения TIFF. Этот класс предоставляет метод под названием [`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods), который позволяет преобразовать все страницы PDF-файла в одно изображение TIFF.

{{% alert color="success" %}}

**Попробуйте преобразовать PDF в TIFF онлайн**
Aspose.PDF для Python через .NET предлагает вам бесплатное онлайн-приложение ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF из PDF в TIFF с помощью бесплатного приложения](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Конвертация страниц PDF в одно изображение TIFF

Aspose.PDF для Python объясняет, как конвертировать все страницы в PDF-файле в одно изображение TIFF:

<a name="csharp-pdf-to-tiff"><strong>Шаги: Конвертация PDF в TIFF на Python</strong></a>

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Создайте объекты [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) и [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/).

3. Вызовите метод [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) для преобразования PDF документа в TIFF.
4. Чтобы установить свойства выходного файла, используйте класс [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/).

Следующий фрагмент кода показывает, как конвертировать все страницы PDF в одно изображение TIFF.

```python
from asposepdf import Api, Device

# инициализация лицензии
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Открыть PDF документ
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# Открыть PDF документ
document = Api.Document(input_pdf)
# Создать объект разрешения
resolution = Device.Resolution(300)

# Создать объект TiffSettings
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# Создать устройство TIFF
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# Конвертировать определенную страницу и сохранить изображение в поток
tiffDevice.process(document, output_image)
```


## Преобразование PDF с использованием класса ImageDevice

`ImageDevice` является предком для `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice` и `EmfDevice`.

- Класс [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Bitmap Image File">BMP</abbr>.
- Класс [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Enhanced Meta File">EMF</abbr>.
- Класс [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) позволяет преобразовывать страницы PDF в изображения JPEG.
- Класс [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Portable Network Graphics">PNG</abbr>.

- Класс [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) позволяет преобразовывать страницы PDF в изображения <abbr title="Graphics Interchange Format">GIF</abbr>.

Давайте рассмотрим, как конвертировать страницу PDF в изображение.

Класс [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) предоставляет метод под названием [Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods), который позволяет конвертировать определенную страницу PDF файла в формат изображения BMP. Другие классы имеют тот же метод. Таким образом, если нам нужно конвертировать страницу PDF в изображение, мы просто создаем экземпляр необходимого класса.

Следующие шаги и фрагмент кода на Python демонстрируют эту возможность

 - [Конвертировать PDF в BMP на Python](#python-pdf-to-image)
 - [Конвертировать PDF в EMF на Python](#python-pdf-to-image)
 - [Конвертировать PDF в JPG на Python](#python-pdf-to-image)
 - [Конвертировать PDF в PNG на Python](#python-pdf-to-image)
 - [Конвертировать PDF в GIF на Python](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>Шаги: PDF в изображение (BMP, EMF, JPG, PNG, GIF) на Python</strong></a>

1. Загрузите PDF файл, используя класс [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Создайте экземпляр подкласса [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/), например:
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) (для преобразования PDF в BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) (для преобразования PDF в Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) (для преобразования PDF в JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) (для преобразования PDF в PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) (для преобразования PDF в GIF)
3. Вызовите метод [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods), чтобы выполнить преобразование из PDF в изображение.

### Преобразование PDF в BMP

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Открыть PDF документ
document = Api.Document(input_pdf)

# Создать объект разрешения
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # Создать имя файла для сохранения
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # Преобразовать определенную страницу и сохранить изображение в файл
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### Преобразование PDF в EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Открыть PDF документ
document = Api.Document(input_pdf)

# Создать объект разрешения
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # Создать имя файла для сохранения
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # Конвертировать конкретную страницу и сохранить изображение в файл
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### Преобразование PDF в JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Открыть PDF документ
document = Api.Document(input_pdf)

# Создать объект разрешения
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # Создать имя файла для сохранения
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # Конвертировать конкретную страницу и сохранить изображение в файл
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### Конвертировать PDF в PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Открыть PDF-документ
document = Api.Document(input_pdf)

# Создать объект разрешения
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # Создать имя файла для сохранения
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # Конвертировать определенную страницу и сохранить изображение в файл
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 

### Конвертировать PDF в GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# Открыть PDF-документ
document = Api.Document(input_pdf)

# Создать объект разрешения
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # Создать имя файла для сохранения
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # Конвертировать определенную страницу и сохранить изображение в файл
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, ознакомьтесь со следующей функцией.

Aspose.PDF for Python предлагает вам бесплатное онлайн-приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), в котором вы можете исследовать функциональность и качество его работы.

[![Как преобразовать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## Преобразование PDF с использованием класса SaveOptions

Эта часть статьи показывает, как преобразовать PDF в <abbr title="Scalable Vector Graphics">SVG</abbr>, используя Python и класс SaveOptions.

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF for Python via .NET предлагает вам бесплатное онлайн-приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), в котором вы можете исследовать функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в SVG с помощью бесплатного приложения](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** - это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, скриптовать и, если необходимо, сжимать. Как XML-файлы, изображения SVG могут быть созданы и отредактированы с помощью любого текстового редактора, но чаще всего их удобнее создавать с помощью программ для рисования, таких как Inkscape.

Aspose.PDF для Python поддерживает функцию преобразования изображения SVG в формат PDF, а также предлагает возможность преобразования PDF-файлов в формат SVG.
 Для выполнения этого требования в пространство имен Aspose.PDF был введен класс [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/). Создайте объект SvgSaveOptions и передайте его в качестве второго аргумента методу [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Следующий фрагмент кода показывает шаги по преобразованию файла PDF в формат SVG с помощью Python.

<a name="csharp-pdf-to-svg"><strong>Шаги: Преобразование PDF в SVG на Python</strong></a>

1. Создайте объект класса [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/).
2. Создайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) с необходимыми настройками.
3. Вызовите метод [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) и передайте объект [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) для преобразования PDF-документа в SVG.

### Преобразование PDF в SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```