---
title: 将PDF转换为不同的图像格式在Python中
linktitle: 将PDF转换为图像
type: docs
weight: 70
url: zh/python-cpp/convert-pdf-to-images-format/
lastmod: "2023-06-23"
description: 本主题向您展示如何使用Aspose.PDF for Python将PDF转换为各种图像格式，例如TIFF、BMP、EMF、JPEG、PNG、GIF、SVG，只需几行代码。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概述

本文解释了如何使用Python将PDF转换为不同的图像格式。它涵盖了以下主题。

## Python将PDF转换为图像

### Python将PDF转换为PNG

1. 导入AsposePdfPython模块，它为Aspose.PDF库提供了一个Python封装。
2. 使用`document_open`函数打开PDF文档，该函数以文件名作为参数并返回一个Document对象。
3. 使用`document_get_pages`函数获取文档的页面，该函数以Document对象作为参数并返回一个PageCollection对象。

1. 使用 `page_collection_get_page` 函数获取文档所需的页面，该函数需要一个 PageCollection 对象和一个索引作为参数，并返回一个 Page 对象。
1. 使用 `png_device_create` 函数创建一个 PngDevice 对象，该函数不需要参数。此对象可以使用默认参数将 PDF 页面转换为 PNG 图像。
1. 使用 `png_device_save_page_to_file` 函数将文档所需的页面保存为 PNG 图像，该函数需要一个 PngDevice 对象、一个 Page 对象和一个文件名作为参数。
1. 使用 `close_handle` 函数关闭 PngDevice 和 Document 对象的句柄，该函数需要一个对象作为参数，并释放其资源。

```python

from AsposePdfPython import *

doc = document_open("blank_pdf_document.pdf")
pages = document_get_pages(doc)
page = page_collection_get_page(pages,1)

pngDevice = png_device_create()
png_device_save_page_to_file(pngDevice,page,"test.png")

```

### Python 将 PDF 转换为 JPEG

1. 使用 `document_open` 函数打开 PDF 文档，该函数以文件名作为参数并返回一个 Document 对象。
1. 使用 `document_get_pages` 函数获取文档的页面，该函数以 Document 对象作为参数并返回一个 PageCollection 对象。
1. 使用 `page_collection_get_page` 函数获取文档的所需页面，该函数以 PageCollection 对象和一个索引作为参数并返回一个 Page 对象。
1. 使用 `resolution_create` 函数创建一个 Resolution 对象，该函数以每英寸点数 (DPI) 的分辨率值作为参数。
1. 使用 `jpeg_device_create_from_width_height_resolution` 函数创建一个 JpegDevice 对象，该函数以宽度、高度和分辨率值作为参数。此对象可以使用指定的参数将 PDF 页面转换为 JPEG 图像。

1. 使用 `jpeg_device_save_page_to_file` 函数将文档的所需页面保存为 JPEG 图像，该函数以 JpegDevice 对象、Page 对象和文件名作为参数。
1. 使用 `close_handle` 函数关闭 JpegDevice 和 Document 对象的句柄，该函数以对象作为参数并释放其资源。

```python

    from AsposePdfPython import *

    doc = document_open("blank_pdf_document.pdf")
    pages = document_get_pages(doc)
    page = page_collection_get_page(pages,1)

    res = resolution_create(300)
    jpegDevice = jpeg_device_create_from_width_height_resolution(1239,1754,res)
    jpeg_device_save_page_to_file(jpegDevice,page,"test.jpeg")
```