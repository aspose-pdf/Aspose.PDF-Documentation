---
title: 使用 Python 在 PDF 中添加文字印章
linktitle: PDF 文件中的文字印章
type: docs
weight: 20
url: /zh/python-net/text-stamps-in-the-pdf-file/
description: 使用 Aspose.PDF for Python 库的 TextStamp 类向 PDF 文档添加文字印章。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 在 PDF 中添加文字印章
Abstract: 本文提供了使用 Aspose.PDF for Python 库向 PDF 文件添加文字印章的全面指南。它概述了使用 `TextStamp` 类创建可定制的文字印章，包含字体大小、样式、颜色和对齐方式等属性。文章包含代码片段，演示如何添加简单的文字印章、配置文字对齐以及应用诸如填充描边文字的高级渲染模式。第一部分解释了创建 `Document` 和 `TextStamp` 对象、设置文字属性并将印章添加到特定页面的过程。第二部分介绍了 `text_alignment` 属性，用于水平和垂直对齐文字，并提供了在 PDF 页面居中文本的代码示例。最后一部分讨论了渲染模式，展示如何使用 `TextState` 对象设置描边颜色和渲染模式后，通过印章添加填充描边文字。每个部分均附有实用示例，以帮助理解和实现。
---

## 使用 Python 添加文字印章

您可以使用 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类在 PDF 文件中添加文字印章。 [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) 类提供创建基于文字的印章所需的属性，如字体大小、字体样式和字体颜色等。要添加文字印章，您需要使用所需属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) 方法将印章添加到 PDF 中。以下代码片段展示了如何在 PDF 文件中添加文字印章。这对于向 PDF 页面添加注释、水印或标签非常有用。

1. 打开 PDF 文档。
1. 创建 TextStamp 对象。
1. 设置印章背景行为。
1. 将印章定位到页面上。
1. 如有需要，旋转印章。
1. 设置文字属性。
1. 将印章添加到页面。
1. 保存修改后的 PDF 文档。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

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
    text_stamp.text_state.font_style = ap.text.FontStyles.BOLD
    text_stamp.text_state.font_style = ap.text.FontStyles.ITALIC
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

