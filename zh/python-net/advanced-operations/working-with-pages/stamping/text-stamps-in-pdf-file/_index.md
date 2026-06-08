---
title: 在 Python 中向 PDF 添加文本印章
linktitle: PDF 文件中的文本印章
type: docs
weight: 20
url: /zh/python-net/text-stamps-in-the-pdf-file/
description: 学习如何在 Python 中向 PDF 文档添加文本印章。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中添加文本印章
Abstract: 本文提供了使用 Aspose.PDF for Python 库向 PDF 文件添加文本印章的完整指南。它概述了使用 `TextStamp` 类创建可自定义的文本印章，具备字体大小、样式、颜色和对齐等属性。文章包含代码示例，演示如何添加简单的文本印章、配置文本对齐以及应用诸如填充描边文本等高级渲染模式。第一部分说明了创建 `Document` 和 `TextStamp` 对象、设置文本属性并将印章添加到特定页面的过程。第二部分介绍了 `text_alignment` 属性，用于水平和垂直对齐文本，并提供了在 PDF 页面上居中文本的代码示例。最后一部分讨论了渲染模式，演示如何使用 `TextState` 对象设置描边颜色和渲染模式后，再将其绑定到印章，从而实现填充描边文本。每个部分均配有实用示例，以帮助读者理解并实现相关功能。
---

## 使用 Python 添加文本印章

您可以使用 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类用于在 PDF 文件中添加文本印章。 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类提供创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了添加文本印章，您需要使用所需属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) Page 的方法，以在 PDF 中添加印章。以下代码片段展示了如何在 PDF 文件中添加文本印章。这对于向 PDF 页面添加注释、水印或标签非常有用。

1. 打开 PDF 文档。
1. 创建一个 TextStamp 对象。
1. 设置印章背景行为。
1. 在页面上定位印章。
1. 如有需要，旋转印章。
1. 设置文本属性。
1. 将印章添加到页面。
1. 保存修改后的 PDF 文档。

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## 相关的盖章主题

- [在 Python 中对 PDF 页面加盖印章](/pdf/zh/python-net/stamping/)
- [使用 Python 向 PDF 添加页面印章](/pdf/zh/python-net/page-stamps-in-the-pdf-file/)
- [使用 Python 向 PDF 添加图像印章](/pdf/zh/python-net/image-stamps-in-pdf-page/)
- [在 Python 中为 PDF 添加页码](/pdf/zh/python-net/add-page-number/)