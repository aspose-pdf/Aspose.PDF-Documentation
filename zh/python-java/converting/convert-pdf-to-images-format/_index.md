---
title: 将PDF转换为不同的图像格式在Python中
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: zh/python-java/convert-pdf-to-images-format/
lastmod: "2023-04-06"
description: 本主题向您展示如何使用Aspose.PDF for Python将PDF转换为各种图像格式，例如TIFF、BMP、EMF、JPEG、PNG、GIF、SVG，只需几行代码即可实现。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概述

本文解释了如何使用Python将PDF转换为不同的图像格式。它涵盖了以下主题。

_图像格式_: **TIFF**
- [Python PDF到TIFF](#python-pdf-to-tiff)
- [Python将PDF转换为TIFF](#python-pdf-to-tiff)
- [Python将单个或特定页面的PDF转换为TIFF](#python-pdf-to-tiff-pages)

_图像格式_: **BMP**
- [Python PDF到BMP](#python-pdf-to-bmp)
- [Python将PDF转换为BMP](#python-pdf-to-bmp)
- [Python PDF到BMP转换器](#python-pdf-to-bmp)

_图像格式_: **EMF**
- [Python PDF到EMF](#python-pdf-to-emf)

- [Python将PDF转换为EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_图片格式_: **JPG** 
- [Python PDF 转换为 JPG](#python-pdf-to-jpg)
- [Python 将 PDF 转换为 JPG](#python-pdf-to-jpg)
- [Python PDF 转 JPG 转换器](#python-pdf-to-jpg)

_图片格式_: **PNG** 
- [Python PDF 转换为 PNG](#python-pdf-to-png)
- [Python 将 PDF 转换为 PNG](#python-pdf-to-png)
- [Python PDF 转 PNG 转换器](#python-pdf-to-png)

_图片格式_: **GIF** 
- [Python PDF 转换为 GIF](#python-pdf-to-gif)
- [Python 将 PDF 转换为 GIF](#python-pdf-to-gif)
- [Python PDF 转 GIF 转换器](#python-pdf-to-gif)

_图片格式_: **SVG** 
- [Python PDF 转换为 SVG](#python-pdf-to-svg)
- [Python 将 PDF 转换为 SVG](#python-pdf-to-svg)
- [Python PDF 转 SVG 转换器](#python-pdf-to-svg)

## Python 将 PDF 转换为图像

**Aspose.PDF for Python** 使用多种方法将 PDF 转换为图像。
 一般来说，我们使用两种方法：使用设备方法进行转换和使用SaveOption进行转换。本节将向您展示如何使用其中一种方法将PDF文档转换为BMP、JPEG、GIF、PNG、EMF、TIFF和SVG格式的图像格式。

库中有几个类允许您使用虚拟设备来转换图像。DocumentDevice用于转换整个文档，而ImageDevice用于特定页面。

## 使用DocumentDevice类转换PDF

**Aspose.PDF for Python** 使得将PDF页面转换为TIFF图像成为可能。

[TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/)（基于DocumentDevice）类允许您将PDF页面转换为TIFF图像。此类提供了一个名为[`Process`](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods)的方法，该方法允许您将PDF文件中的所有页面转换为单个TIFF图像。

{{% alert color="success" %}}

**尝试在线将PDF转换为TIFF**
Aspose.PDF for Python via .NET 提供了一个在线免费应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以在其中尝试调查其功能和工作质量。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### 将 PDF 页面转换为一个 TIFF 图像

Aspose.PDF for Python 说明如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

<a name="csharp-pdf-to-tiff"><strong>步骤: 在 Python 中将 PDF 转换为 TIFF</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 类的对象。
2. 创建 [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) 和 [TiffDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/) 对象。

3. 调用 [TiffDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffdevice/#methods) 方法将 PDF 文档转换为 TIFF。
4. 要设置输出文件的属性，请使用 [TiffSettings](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/tiffsettings/) 类。

以下代码片段展示了如何将所有 PDF 页面转换为单个 TIFF 图像。

```python


from asposepdf import Api, Device

# 初始化许可证
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# 打开 PDF 文档
DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "source.pdf"
output_image = DIR_OUTPUT + "image.tiff"
# 打开 PDF 文档
document = Api.Document(input_pdf)
# 创建 Resolution 对象
resolution = Device.Resolution(300)

# 创建 TiffSettings 对象
tiffSettings = Device.TiffSettings()
tiffSettings._CompressionType = Device.CompressionType.LZW
tiffSettings._ColorDepth = Device.ColorDepth.Default
tiffSettings._Skip_blank_pages = False

# 创建 TIFF 设备
tiffDevice = Device.TiffDevice(resolution, tiffSettings)

# 转换特定页面并将图像保存到流
tiffDevice.process(document, output_image)
```


## 使用 ImageDevice 类转换 PDF

`ImageDevice` 是 `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice` 和 `EmfDevice` 的祖先。

- [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/) 类允许您将 PDF 页面转换为 <abbr title="位图图像文件">BMP</abbr> 图像。
- [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/) 类允许您将 PDF 页面转换为 <abbr title="增强型图元文件">EMF</abbr> 图像。
- [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/) 类允许您将 PDF 页面转换为 JPEG 图像。
- [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/) 类允许您将 PDF 页面转换为 <abbr title="便携式网络图形">PNG</abbr> 图像。

- [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/) 类允许您将 PDF 页面转换为 <abbr title="图形交换格式">GIF</abbr> 图像。

让我们看看如何将PDF页面转换为图像。

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/)类提供了一个名为[Process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods)的方法，允许您将PDF文件的特定页面转换为BMP图像格式。其他类也有相同的方法。所以，如果我们需要将PDF页面转换为图像，我们只需实例化所需的类。

以下步骤和Python代码片段展示了这种可能性

- [在Python中将PDF转换为BMP](#python-pdf-to-image)
- [在Python中将PDF转换为EMF](#python-pdf-to-image)
- [在Python中将PDF转换为JPG](#python-pdf-to-image)
- [在Python中将PDF转换为PNG](#python-pdf-to-image)
- [在Python中将PDF转换为GIF](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>步骤：在Python中将PDF转换为图像（BMP，EMF，JPG，PNG，GIF）</strong></a>

1. 使用 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 类加载 PDF 文件。
2. 创建 [ImageDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/) 子类的实例，例如：
   * [BmpDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/bmpdevice/)（将 PDF 转换为 BMP）
   * [EmfDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/emfdevice/)（将 PDF 转换为 Emf）
   * [JpegDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/jpegdevice/)（将 PDF 转换为 JPG）
   * [PngDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/pngdevice/)（将 PDF 转换为 PNG）
   * [GifDevice](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/gifdevice/)（将 PDF 转换为 GIF）
3. 调用 [ImageDevice.Process()](https://reference.aspose.com/pdf/python-java/aspose.pdf.devices/imagedevice/#methods) 方法执行 PDF 到图像的转换。

### 将 PDF 转换为 BMP

```python
from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# 打开 PDF 文档
document = Api.Document(input_pdf)

# 创建分辨率对象
resolution = Device.Resolution(300)
device = Device.BmpDevice(resolution)

for i in range(0, document.getPages.size):
    # 创建保存的文件名
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.bmp"
    # 转换特定页面并将图像保存到文件
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```


### 将 PDF 转换为 EMF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# 打开 PDF 文档
document = Api.Document(input_pdf)

# 创建分辨率对象
resolution = Device.Resolution(300)
device = Device.EmfDevice(resolution)

for i in range(0, document.getPages.size):
    # 创建保存的文件名
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.emf"
    # 转换特定页面并将图像保存到文件
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
```  

### 将 PDF 转换为 JPEG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# 打开 PDF 文档
document = Api.Document(input_pdf)

# 创建分辨率对象
resolution = Device.Resolution(300)
device = Device.JpegDevice(resolution)

for i in range(0, document.getPages.size):
    # 创建保存的文件名
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.jpeg"
    # 转换特定页面并将图像保存到文件
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


### 将 PDF 转换为 PNG

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# 打开 PDF 文档
document = Api.Document(input_pdf)

# 创建分辨率对象
resolution = Device.Resolution(300)
device = Device.PngDevice(resolution)

for i in range(0, document.getPages.size):
    # 创建保存的文件名
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.png"
    # 转换特定页面并将图像保存到文件
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 

### 将 PDF 转换为 GIF

```python

from asposepdf import Api, Device

DIR_INPUT = "../../testdata/"
DIR_OUTPUT = "../../testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "image"
# 打开 PDF 文档
document = Api.Document(input_pdf)

# 创建分辨率对象
resolution = Device.Resolution(300)
device = Device.GifDevice(resolution)

for i in range(0, document.getPages.size):
    # 创建保存的文件名
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.gif"
    # 转换特定页面并将图像保存到文件
    device.process(document.getPages.getPage(i + 1), outputFileName=imageFileName)
``` 


{{% alert color="success" %}}
**尝试在线将PDF转换为PNG**

作为我们免费应用程序如何工作的示例，请查看下一个功能。

Aspose.PDF for Python为您提供在线免费应用程序["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试调查其功能和工作质量。

[![如何使用免费应用将PDF转换为PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用SaveOptions类转换PDF

本文的这一部分向您展示如何使用Python和SaveOptions类将PDF转换为<abbr title="可缩放矢量图形">SVG</abbr>。

{{% alert color="success" %}}
**尝试在线将PDF转换为SVG**

Aspose.PDF for Python via .NET为您提供在线免费应用程序["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF使用免费应用将PDF转换为SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是一种基于 XML 的文件格式的二维矢量图形规范，包括静态和动态（交互式或动画）的图形。SVG 规范是一个开放标准，自 1999 年以来由万维网联盟 (W3C) 开发。

SVG 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、脚本化，并在需要时被压缩。作为 XML 文件，SVG 图像可以用任何文本编辑器创建和编辑，但使用诸如 Inkscape 之类的绘图程序创建它们通常更为方便。

Aspose.PDF for Python 支持将 SVG 图像转换为 PDF 格式的功能，并且还提供将 PDF 文件转换为 SVG 格式的能力。
 为满足此要求，[SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 类已被引入到 Aspose.PDF 命名空间中。实例化一个 SvgSaveOptions 对象并将其作为第二个参数传递给 [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

以下代码片段展示了使用 Python 将 PDF 文件转换为 SVG 格式的步骤。

<a name="csharp-pdf-to-svg"><strong>步骤：在 Python 中将 PDF 转换为 SVG</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) 类的对象。
2. 使用需要的设置创建 [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) 对象。
3. 调用 [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) 方法并传递 [SvgSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/svgsaveoptions/) 对象将 PDF 文档转换为 SVG。

### 将 PDF 转换为 SVG

```python

from asposepdf import Api

documentName = "testdata/input.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.svg"
doc.save(documentOutName, Api.SaveFormat.Svg)
```