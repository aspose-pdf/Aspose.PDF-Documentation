---
title: 将PDF转换为不同图像格式的Python方法
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: /python-net/convert-pdf-to-images-format/
lastmod: "2022-12-23"
description: 本主题向您展示如何使用Aspose.PDF for Python将PDF转换为多种图像格式，例如TIFF、BMP、EMF、JPEG、PNG、GIF、SVG，只需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概述

本文解释了如何使用Python将PDF转换为不同的图像格式。它涵盖以下主题。

_图像格式_：**TIFF**
- [Python PDF 转 TIFF](#python-pdf-to-tiff)
- [Python 将 PDF 转换为 TIFF](#python-pdf-to-tiff)
- [Python 将单个或特定页面的 PDF 转换为 TIFF](#python-pdf-to-tiff-pages)

_图像格式_：**BMP**
- [Python PDF 转 BMP](#python-pdf-to-bmp)
- [Python 将 PDF 转换为 BMP](#python-pdf-to-bmp)
- [Python PDF 转 BMP 转换器](#python-pdf-to-bmp)

_图像格式_：**EMF**
- [Python PDF 转 EMF](#python-pdf-to-emf)
- [Python 将 PDF 转换为 EMF](#python-pdf-to-emf)
- [Python PDF to EMF Converter](#python-pdf-to-emf)

_图片格式_: **JPG**
- [Python PDF 转 JPG](#python-pdf-to-jpg)
- [Python 转换 PDF 到 JPG](#python-pdf-to-jpg)
- [Python PDF 到 JPG 转换器](#python-pdf-to-jpg)

_图片格式_: **PNG**
- [Python PDF 转 PNG](#python-pdf-to-png)
- [Python 转换 PDF 到 PNG](#python-pdf-to-png)
- [Python PDF 到 PNG 转换器](#python-pdf-to-png)

_图片格式_: **GIF**
- [Python PDF 转 GIF](#python-pdf-to-gif)
- [Python 转换 PDF 到 GIF](#python-pdf-to-gif)
- [Python PDF 到 GIF 转换器](#python-pdf-to-gif)

_图片格式_: **SVG**
- [Python PDF 转 SVG](#python-pdf-to-svg)
- [Python 转换 PDF 到 SVG](#python-pdf-to-svg)
- [Python PDF 到 SVG 转换器](#python-pdf-to-svg)

## Python 转换 PDF 到图像

**Aspose.PDF for Python** 使用几种方法将 PDF 转换为图像。
 通常情况下，我们使用两种方法：使用设备方法进行转换和使用保存选项进行转换。本节将向您展示如何使用其中一种方法将PDF文档转换为图像格式，如BMP、JPEG、GIF、PNG、EMF、TIFF和SVG格式。

库中有几类允许您使用虚拟设备来转换图像。DocumentDevice用于转换整个文档，而ImageDevice用于特定页面。

## 使用 DocumentDevice 类转换 PDF

**Aspose.PDF for Python**可以将PDF页面转换为TIFF图像。

[TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/)（基于DocumentDevice）类允许您将PDF页面转换为TIFF图像。此类提供了一个名为[process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods)的方法，允许您将PDF文件中的所有页面转换为单个TIFF图像。

{{% alert color="success" %}}

**尝试在线将PDF转换为TIFF**
Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 转换 PDF 到 TIFF 免费应用](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### 将 PDF 页面转换为一个 TIFF 图像

Aspose.PDF for Python 解释如何将 PDF 文件中的所有页面转换为单个 TIFF 图像：

<a name="csharp-pdf-to-tiff"><strong>步骤：在 Python 中将 PDF 转换为 TIFF</strong></a>

1. 创建一个 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的对象。
2. 创建 [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 和 [TiffDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 对象。

3. 调用 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) 方法将 PDF 文档转换为 TIFF。
4. 要设置输出文件的属性，请使用 [TiffSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 类。

以下代码片段展示了如何将所有 PDF 页面转换为单个 TIFF 图像。

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tiff.tiff"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 创建分辨率对象
    resolution = ap.devices.Resolution(300)

    # 创建 TiffSettings 对象
    tiffSettings = ap.devices.TiffSettings()
    tiffSettings.compression = ap.devices.CompressionType.LZW
    tiffSettings.depth = ap.devices.ColorDepth.DEFAULT
    tiffSettings.skip_blank_pages = False

    # 创建 TIFF 设备
    tiffDevice = ap.devices.TiffDevice(resolution, tiffSettings)

    # 转换特定页面并将图像保存到流
    tiffDevice.process(document, output_pdf)
```


## 使用 ImageDevice 类转换 PDF

`ImageDevice` 是 `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice` 和 `EmfDevice` 的祖先。

- [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 类允许您将 PDF 页面转换为 <abbr title="位图图像文件">BMP</abbr> 图像。
- [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) 类允许您将 PDF 页面转换为 <abbr title="增强型图元文件">EMF</abbr> 图像。
- [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) 类允许您将 PDF 页面转换为 JPEG 图像。
- [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) 类允许您将 PDF 页面转换为 <abbr title="可移植网络图形">PNG</abbr> 图像。

- [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) 类允许您将 PDF 页面转换为 <abbr title="图形交换格式">GIF</abbr> 图像。

让我们看看如何将 PDF 页面转换为图像。

[BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 类提供了一个名为 [process](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) 的方法，该方法允许您将 PDF 文件的特定页面转换为 BMP 图像格式。其他类也有相同的方法。因此，如果我们需要将 PDF 页面转换为图像，我们只需实例化所需的类。

以下步骤和 Python 中的代码片段展示了这种可能性

- [将 PDF 转换为 BMP 在 Python 中](#python-pdf-to-image)
- [将 PDF 转换为 EMF 在 Python 中](#python-pdf-to-image)
- [将 PDF 转换为 JPG 在 Python 中](#python-pdf-to-image)
- [将 PDF 转换为 PNG 在 Python 中](#python-pdf-to-image)
- [将 PDF 转换为 GIF 在 Python 中](#python-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>步骤：PDF 转换为图像（BMP、EMF、JPG、PNG、GIF）在 Python 中</strong></a>

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类加载 PDF 文件。
2. 创建 [ImageDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) 子类的实例，例如：
   * [BmpDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (将 PDF 转换为 BMP)
   * [EmfDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (将 PDF 转换为 Emf)
   * [JpegDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) (将 PDF 转换为 JPG)
   * [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (将 PDF 转换为 PNG)
   * [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (将 PDF 转换为 GIF)
3. 调用 [ImageDevice.Process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) 方法执行 PDF 到图像的转换。

### 将 PDF 转换为 BMP

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_bmp"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 创建分辨率对象
    resolution = ap.devices.Resolution(300)
    device = ap.devices.BmpDevice(resolution)

    for i in range(0, len(document.pages)):
        # 创建文件用于保存
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.bmp", 'x'
        )
        # 转换特定页面并将图像保存到流中
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```


### 将PDF转换为EMF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_emf"
    # 打开PDF文档
    document = ap.Document(input_pdf)

    # 创建Resolution对象
    resolution = ap.devices.Resolution(300)
    device = ap.devices.EmfDevice(resolution)

    for i in range(0, len(document.pages)):
        # 创建用于保存的文件
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.emf", 'x'
        )
        # 转换特定页面并将图像保存到流
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```  

### 将PDF转换为JPEG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_jpeg"
    # 打开PDF文档
    document = ap.Document(input_pdf)

    # 创建Resolution对象
    resolution = ap.devices.Resolution(300)
    device = ap.devices.JpegDevice(resolution)

    for i in range(0, len(document.pages)):
        # 创建用于保存的文件
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.jpeg", "x"
        )
        # 转换特定页面并将图像保存到流
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()  
``` 


### 将 PDF 转换为 PNG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_png"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 创建 Resolution 对象
    resolution = ap.devices.Resolution(300)
    device = ap.devices.PngDevice(resolution)

    for i in range(0, len(document.pages)):
        # 创建文件以保存
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.png", 'x'
        )
        # 转换特定页面并将图像保存到流
        device.process(document.pages[i + 1], imageStream)
        imageStream.close()
```

### 将 PDF 转换为 GIF

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "many_pages.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_gif"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 创建 Resolution 对象
    resolution = ap.devices.Resolution(300)

    device = ap.devices.GifDevice(resolution)

    for i in range(0, len(document.pages)):
        # 创建文件以保存
        imageStream = io.FileIO(
            output_pdf + "_page_" + str(i + 1) + "_out.gif", 'x'
        )
        # 转换特定页面并将图像保存到流
        device.process(document.pages[i + 1], imageStream)
        # 关闭流
        imageStream.close()  
```


{{% alert color="success" %}}
**尝试在线将 PDF 转换为 PNG**

作为我们免费应用程序如何工作的一个例子，请查看下一个功能。

Aspose.PDF for Python 为您提供在线免费应用程序 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，您可以尝试调查其功能和工作质量。

[![如何使用免费应用程序将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用 SaveOptions 类转换 PDF

本文的这一部分向您展示了如何使用 Python 和 SaveOptions 类将 PDF 转换为 <abbr title="Scalable Vector Graphics">SVG</abbr>。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for Python via .NET 为您提供在线免费应用程序 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，您可以尝试调查其功能和工作质量。

[![Aspose.PDF 使用免费应用程序将 PDF 转换为 SVG](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是一种基于 XML 的文件格式的规格家族，用于二维矢量图形，包括静态和动态（交互式或动画）。SVG 规范是一个开放标准，自 1999 年以来一直由万维网联盟 (W3C) 开发。

SVG 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、编写脚本，并在需要时进行压缩。作为 XML 文件，SVG 图像可以用任何文本编辑器创建和编辑，但通常使用绘图程序（如 Inkscape）创建它们更为方便。

Aspose.PDF for Python 支持将 SVG 图像转换为 PDF 格式的功能，并且还提供将 PDF 文件转换为 SVG 格式的功能。
 要实现此要求，[SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 类已被引入到 Aspose.PDF 命名空间中。实例化一个 SvgSaveOptions 对象，并将其作为第二个参数传递给 [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

以下代码片段展示了使用 Python 将 PDF 文件转换为 SVG 格式的步骤。

<a name="csharp-pdf-to-svg"><strong>步骤：在 Python 中将 PDF 转换为 SVG</strong></a>

1. 创建 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类的对象。
2. 使用所需的设置创建 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 对象。
3. 调用 [Document.Save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法并传递 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 对象，将 PDF 文档转换为 SVG。

### 将 PDF 转换为 SVG

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_svg.svg"
    # 打开 PDF 文档
    document = ap.Document(input_pdf)

    # 实例化一个 SvgSaveOptions 对象
    saveOptions = ap.SvgSaveOptions()

    # 不将 SVG 图像压缩到 Zip 压缩包
    saveOptions.compress_output_to_zip_archive = False
    saveOptions.treat_target_file_name_as_directory = True

    # 将输出保存为 SVG 文件
    document.save(output_pdf, saveOptions)
```