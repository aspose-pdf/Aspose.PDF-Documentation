---
title: 在 Python 中将图像格式转换为 PDF
linktitle: 将图像转换为 PDF
type: docs
weight: 60
url: /zh/python-net/convert-images-format-to-pdf/
lastmod: "2026-06-08"
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中将 BMP、CGM、DICOM、PNG、TIFF、EMF、SVG 等图像格式转换为 PDF。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: 如何在 Python 中将图像转换为 PDF
Abstract: 本文提供了一份关于使用 Python 将各种图像格式转换为 PDF 的综合指南，特别是利用 Aspose.PDF for Python via .NET 库。文章涵盖了 BMP、CGM、DICOM、EMF、GIF、PNG、SVG 和 TIFF 等多种图像格式。每个章节详细说明了执行转换所需的步骤，并提供代码片段以演示该过程。例如，将 BMP 转换为 PDF 包括创建一个新的 PDF 文档、定义图像位置、插入图像以及保存文档。类似地，对于 CGM、DICOM 等格式，文中列出了特定的加载选项和处理步骤。文章还强调了使用 Aspose.PDF 执行此类任务的优势，例如它对不同编码方式的支持以及能够处理单帧和多帧图像的能力。
---

## 相关转换

- [将 PDF 转换为图像格式](/pdf/zh/python-net/convert-pdf-to-images-format/) 当您需要反向工作流时。
- [将HTML转换为PDF](/pdf/zh/python-net/convert-html-to-pdf/) 用于网页内容和 MHTML 源。
- [将其他文件格式转换为 PDF](/pdf/zh/python-net/convert-other-files-to-pdf/) 针对 EPUB、XPS、文本以及其他非图像输入。

## Python 图像转 PDF 转换

**Aspose.PDF for Python via .NET** 允许您将不同格式的图像转换为 PDF 文件。我们的库展示了将最流行的图像格式转换为 PDF 的代码片段，例如 - BMP、CGM、DICOM、EMF、JPG、PNG、SVG 和 TIFF 格式。

## 将 BMP 转换为 PDF

使用 **Aspose.PDF for Python via .NET** 库将 BMP 文件转换为 PDF 文档。

<abbr title="Bitmap Image File">BMP</abbr> 图像是具有扩展名的文件。BMP 代表用于存储位图数字图像的位图图像文件。这些图像独立于图形适配器，也称为设备无关位图（DIB）文件格式。

您可以使用 Aspose.PDF for Python via .NET API 将 BMP 转换为 PDF 文件。因此，您可以按照以下步骤将 BMP 图像转换为 PDF：

在 Python 中将 BMP 转换为 PDF 的步骤：

1. 创建一个空的 PDF 文档。
1. 创建您需要的页面，例如，我们创建了 A4，但您可以指定自己的格式。
1. 将图像（来自 infile）放置在页面内，使用定义的矩形。
1. 将文档保存为 PDF。

因此，下面的代码片段遵循这些步骤，并展示了如何使用 Python 将 BMP 转换为 PDF：

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 BMP 转换为 PDF**

Aspose 为您呈现在线应用 ["BMP 转 PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 将 BMP 转换为 PDF 使用 App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## 将 CGM 转换为 PDF

使用 Aspose.PDF for Python via .NET 将 CGM（Computer Graphics Metafile）转换为 PDF（或其他受支持的格式）。

<abbr title="Computer Graphics Metafile">计算机图形元文件</abbr> 是计算机图形元文件（Computer Graphics Metafile）格式的文件扩展名，常用于 CAD（计算机辅助设计）和演示图形应用程序。CGM 是一种矢量图形格式，支持三种不同的编码方法：二进制（最适合程序读取速度）、基于字符的编码（产生最小的文件大小并允许更快的数据传输）或明文编码（允许用户使用文本编辑器读取和修改文件）。

检查下面的代码片段以将 CGM 文件转换为 PDF 格式。

在 Python 中将 CGM 转换为 PDF 的步骤：

1. 定义文件路径
1. 为 CGM 设置加载选项。
1. 将 CGM 转换为 PDF
1. 打印转换消息

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 DICOM 转换为 PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 格式是医学行业用于创建、存储、传输和可视化受检患者数字医学图像和文件的标准。

**Aspose.PDF for Python** 允许您转换 DICOM 和 SVG 图像，但由于技术原因，要向 PDF 添加图像，需要指定要添加的文件类型。

以下代码片段展示了如何使用 Aspose.PDF 将 DICOM 文件转换为 PDF 格式。您应加载 DICOM 图像，将图像放置在 PDF 文件的页面上并将输出保存为 PDF。我们使用额外的 pydicom 库来设置此图像的尺寸。如果您想在页面上定位图像，可以跳过此代码片段。

1. 加载 DICOM 文件。
1. 提取图像尺寸。
1. 打印图像大小。
1. 创建一个新的 PDF 文档。
1. 准备 DICOM 图像以用于 PDF。
1. 设置 PDF 页面大小和边距。
1. 将图像添加到页面。
1. 保存 PDF。
1. 打印转换消息。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 DICOM 转换为 PDF**

Aspose 为您呈现在线应用 ["DICOM 转 PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)，在此您可以尝试调查其功能以及其工作质量。

[![使用 App 将 DICOM 转换为 PDF 的 Aspose.PDF](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## 将 EMF 转换为 PDF

<abbr title="Enhanced metafile format">EMF</abbr> 以设备无关的方式存储图形图像。EMF 元文件由按时间顺序排列的可变长度记录组成，这些记录在任何输出设备上解析后都能渲染存储的图像。

以下代码片段展示了如何使用 Python 将 EMF 转换为 PDF：

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 EMF 转换为 PDF**

Aspose 为您呈现在线应用 ["EMF 转 PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)，在此您可以尝试调查其功能以及其工作质量。

[![Aspose.PDF 使用 App 将 EMF 转换为 PDF](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## 将 GIF 转换为 PDF

使用 **Aspose.PDF for Python via .NET** 库将 GIF 文件转换为 PDF 文档。

<abbr title="Graphics Interchange Format">GIF</abbr> 能够在不超过256种颜色的格式中存储压缩数据且不损失质量。硬件无关的 GIF 格式于 1987 年（GIF87a）由 CompuServe 开发，用于在网络上传输位图图像。

因此，下面的代码片段遵循这些步骤，并展示了如何使用 Python 将 BMP 转换为 PDF：

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 GIF 转换为 PDF**

Aspose 为您呈现在线应用 ["GIF 转 PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)，在此您可以尝试调查其功能以及其工作质量。

[![使用 App 将 GIF 转换为 PDF 的 Aspose.PDF](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## 将 PNG 转换为 PDF

**Aspose.PDF for Python via .NET** 支持将 PNG 图像转换为 PDF 格式的功能。请查看下面的代码片段以实现您的任务。

<abbr title="Portable Network Graphics">PNG</abbr> 指的是一种使用无损压缩的光栅图像文件格式，这使它在用户中很受欢迎。

您可以使用以下步骤将 PNG 转换为 PDF 图像：

1. 创建一个新的 PDF 文档。
1. 定义图像放置。
1. 保存 PDF。
1. 打印转换消息。

此外，下面的代码片段展示了如何使用 Python 将 PNG 转换为 PDF：

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**尝试在线将 PNG 转换为 PDF**

Aspose 为您呈现在线应用 ["PNG 转 PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)，在此您可以尝试调查其功能以及其工作质量。

[![使用 App 将 PNG 转换为 PDF 的 Aspose.PDF](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## 将 SVG 转换为 PDF

**Aspose.PDF for Python via .NET** 解释了如何将 SVG 图像转换为 PDF 格式，以及如何获取源 SVG 文件的尺寸。

可伸缩矢量图形（SVG）是一系列基于 XML 的文件格式规范，用于二维矢量图形，包括静态和动态图形（交互式或动画）。SVG 规范是一项开放标准，自 1999 年起由万维网联盟（W3C）进行开发。

<abbr title="Scalable Vector Graphics">可缩放矢量图形</abbr> 图像及其行为在 XML 文本文件中定义。这意味着它们可以被搜索、索引、脚本化，并在需要时进行压缩。作为 XML 文件，SVG 图像可以使用任何文本编辑器创建和编辑，但通常使用诸如 Inkscape 等绘图程序来创建会更方便。

{{% alert color="success" %}}
**尝试在线将 SVG 格式转换为 PDF**

Aspose.PDF for Python via .NET 为您呈现在线应用程序 ["SVG 转 PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)，在此您可以尝试调查其功能以及其工作质量。

[![使用 App 将 SVG 转换为 PDF（Aspose.PDF）](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

以下代码片段展示了使用 Aspose.PDF for Python 将 SVG 文件转换为 PDF 格式的过程。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 TIFF 转换为 PDF

**Aspose.PDF** 文件格式受支持，无论是单帧还是多帧的 TIFF 图像。这意味着您可以将 TIFF 图像转换为 PDF。

TIFF 或 TIF，标记图像文件格式，表示用于在符合此文件格式标准的各种设备上使用的光栅图像。TIFF 图像可以包含多个不同图像的帧。也支持 Aspose.PDF 文件格式，无论是单帧还是多帧 TIFF 图像。

您可以使用与其余光栅文件格式图形相同的方式将 TIFF 转换为 PDF：

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 CDR 转换为 PDF

下面的代码片段展示了如何使用 Aspose.PDF for Python via .NET 中的 'CdrLoadOptions' 加载 CorelDRAW (CDR) 文件并将其保存为 PDF。

1. 创建 'CdrLoadOptions()' 以配置 CDR 文件的加载方式。
1. 使用 CDR 文件和加载选项初始化 Document 对象。
1. 将文档保存为 PDF。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## 将 JPEG 转换为 PDF

此示例展示了如何使用 Aspose.PDF for Python via .NET 将 JPEG 转换为 PDF 文件。

1. 创建一个新的 PDF 文档。
1. 添加新页面。
1. 定义放置矩形（A4尺寸：595x842 点）。
1. 将图像插入页面。
1. 保存 PDF。

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
