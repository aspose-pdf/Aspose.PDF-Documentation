---
title: 在 Python 中将 PDF 转换为图像格式
linktitle: 将 PDF 转换为图像
type: docs
weight: 70
url: /zh/python-net/convert-pdf-to-images-format/
lastmod: "2026-06-08"
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 将 PDF 页面渲染为 TIFF、BMP、EMF、JPEG、PNG、GIF 和 SVG 文件。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 在 Python 中将 PDF 页面转换为 TIFF、PNG、JPEG、GIF、BMP、EMF 和 SVG。
Abstract: 本文介绍如何使用 Aspose.PDF for Python via .NET 将 PDF 文件转换为常见的图像格式。内容包括使用 `TiffDevice` 对整篇文档进行 TIFF 导出，使用 `ImageDevice` 子类（如 `BmpDevice`、`JpegDevice`、`PngDevice`、`GifDevice` 和 `EmfDevice`）对每页生成光栅图像，以及使用 `SvgSaveOptions` 将向量导出为 SVG。每个章节都提供了核心步骤和所需的 Python 示例，以将 PDF 内容保存为图像输出。
---

## Python 将 PDF 转换为图像

**Aspose.PDF for Python via .NET** 支持多种将 PDF 内容转换为图像的方法。在实际中，大多数工作流使用以下两种选项之一：

- 用于将 PDF 页面渲染为光栅图像格式的设备方法
- 用于将 PDF 内容导出为 SVG 的 SaveOptions 方法

本文展示如何将 PDF 文件转换为 TIFF、BMP、EMF、JPEG、PNG、GIF 和 SVG。

该库包含多个渲染类。 `DocumentDevice` 旨在进行全文件转换，而 `ImageDevice` 针对单个页面。

## 使用 DocumentDevice 类转换 PDF

使用 `DocumentDevice` 当您想将整个 PDF 渲染为单个多页 TIFF 文件时。

这 [Tiff设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 类是基于 `DocumentDevice` 并提供 [处理](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) 将 PDF 文件中的所有页面转换为单个 TIFF 输出的方法。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 TIFF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["PDF 转 TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)，在此您可以尝试调查其功能以及其工作质量。

[![使用 App 将 PDF 转换为 TIFF 的 Aspose.PDF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### 将 PDF 页面转换为一个 TIFF 图像

Aspose.PDF for Python via .NET 可以将 PDF 文件中的每一页渲染为一个 TIFF 图像。

步骤：在 Python 中将 PDF 转换为 TIFF

1. 使用以下方式加载源 PDF [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 创建 [Tiff设置](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffsettings/) 和 [Tiff设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/) 对象。
1. 配置 TIFF 选项，例如压缩、色彩深度和空白页处理。
1. 调用 [处理](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/tiffdevice/#methods) 写入 TIFF 文件的方法。

以下代码片段展示了如何将所有 PDF 页面转换为单个 TIFF 图像。

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

## 使用 ImageDevice 类转换 PDF

使用 `ImageDevice` 当您需要以栅格图像格式逐页输出时。

`ImageDevice` 是...的基类 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`，和 `EmfDevice`.

- 这 [Bmp设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 类允许您将 PDF 页面转换为 BMP 图像。
- 这 [Emf设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) 类允许您将 PDF 页面转换为 EMF 图像。
- 这 [Jpeg设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) 类允许您将 PDF 页面转换为 JPEG 图像。
- 这 [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) 类允许您将 PDF 页面转换为 PNG 图像。
- 这 [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) 类允许您将 PDF 页面转换为 GIF 图像。

每种格式的工作流程相同：加载文档，创建相应的设备，然后处理所需的页面。

[Bmp设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) 公开了 [处理](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/#methods) 将特定页面渲染为 BMP 的方法。其他图像设备类遵循相同的模式，因此您可以通过更改设备类来切换格式。

以下链接和代码示例展示了如何将 PDF 页面渲染为常见的图像格式：

- [在 Python 中将 PDF 转换为 BMP](#convert-pdf-to-bmp)
- [在 Python 中将 PDF 转换为 EMF](#convert-pdf-to-emf)
- [在 Python 中将 PDF 转换为 JPEG](#convert-pdf-to-jpeg)
- [在 Python 中将 PDF 转换为 PNG](#convert-pdf-to-png)
- [在 Python 中将 PDF 转换为 GIF](#convert-pdf-to-gif)

步骤：在 Python 中将 PDF 转换为图像（BMP、EMF、JPG、PNG、GIF）

1. 使用 ... 加载 PDF 文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 创建所需的实例 [图像设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/) 子类:
    - [Bmp设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/bmpdevice/) (将 PDF 转换为 BMP)
    - [Emf设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/emfdevice/) (将 PDF 转换为 EMF)
    - [Jpeg设备](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/jpegdevice/) （将 PDF 转换为 JPG）
    - [PngDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/pngdevice/) (将 PDF 转换为 PNG)
    - [GifDevice](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/gifdevice/) (将 PDF 转换为 GIF)
1. 遍历您想要导出的页面。
1. 调用 [ImageDevice.process()](https://reference.aspose.com/pdf/python-net/aspose.pdf.devices/imagedevice/#methods) 将每页保存为图像的方法。

### 将 PDF 转换为 BMP

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

### 将 PDF 转换为 EMF

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

### 将 PDF 转换为 JPEG

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

### 将 PDF 转换为 PNG

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

### 将 PDF 转换为 PNG，使用默认字体

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

### 将 PDF 转换为 GIF

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
**尝试在线将 PDF 转换为 PNG**

作为我们的应用程序工作方式的示例，请查看下一个功能。

Aspose.PDF for Python 为您呈现在线应用 ["PDF 转 PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)，在此您可以尝试调查其功能以及其工作质量。

[![如何使用 App 将 PDF 转换为 PNG](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## 使用 SaveOptions 类转换 PDF

使用 `SaveOptions` 当您想要将 PDF 内容导出为 SVG 时。

{{% alert color="success" %}}
**尝试在线将 PDF 转换为 SVG**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["PDF 转 SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 PDF 转换为 SVG 的应用](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**可缩放矢量图形 (SVG)** 是一种基于 XML 的二维矢量图形格式。由于 SVG 保持矢量特性，当您需要为网页、UI 或设计工作流提供可缩放的输出时，它非常有用。

SVG 文件是基于文本的、可搜索的，并且易于在其他工具中进行后处理。

Aspose.PDF for Python via .NET 可以将 SVG 转换为 PDF，也可以将 PDF 页面导出为 SVG。对于 PDF 转 SVG 转换，创建一个 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 对象并将其传递给 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

以下步骤展示如何使用 Python 将 PDF 文件转换为 SVG。

步骤：在 Python 中将 PDF 转换为 SVG

1. 使用以下方式加载源 PDF [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 创建一个 [SvgSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/svgsaveoptions/) 对象并配置所需的选项。
1. 调用 [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 带有 the 的方法 `SvgSaveOptions` 用于写入 SVG 输出的实例。

### 将 PDF 转换为 SVG

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

## 相关转换

- [将图像格式转换为 PDF](/pdf/zh/python-net/convert-images-format-to-pdf/) 当您需要从 JPG、PNG、TIFF、SVG 或其他图像来源重建 PDF 时。
- [将 PDF 转换为 HTML](/pdf/zh/python-net/convert-pdf-to-html/) 用于生成对浏览器友好的输出，而不是光栅图像。
- [将 PDF 转换为其他格式](/pdf/zh/python-net/convert-pdf-to-other-files/) 用于 EPUB、Markdown、文本和 XPS 导出工作流。
