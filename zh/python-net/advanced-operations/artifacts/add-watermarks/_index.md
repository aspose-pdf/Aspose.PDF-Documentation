---
title: 使用 Python 为 PDF 添加水印
linktitle: 添加水印
type: docs
weight: 30
url: /zh/python-net/add-watermarks/
description: 本文解释了使用 Python 编程方式处理文档中的工件并获取 PDF 水印的功能。
lastmod: "2025-11-21"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 为 PDF 添加水印
Abstract: 本文讨论了使用 Aspose.PDF for Python via .NET 通过管理工件向 PDF 文档添加水印。它介绍了处理工件的关键类——`Artifact` 和 `ArtifactCollection`，并描述了如何通过 `Page` 类的 `Artifacts` 属性访问它们。文章详细说明了 `Artifact` 类的属性，包括 `contents`、`form`、`image`、`text`、`rectangle`、`rotation` 和 `opacity` 等属性，这些属性使对 PDF 文件中的工件进行全面操作成为可能。此外，还提供了一个实用示例，演示如何使用 Python 编程方式在 PDF 的首页添加水印。代码片段展示了 `WatermarkArtifact` 的创建与配置，设置其文本、对齐方式、旋转角度和不透明度，然后将其附加到 PDF 文档并保存更改。
---

## 编程示例：如何在 PDF 文件上添加水印

使用 Aspose.PDF for Python via .NET 向 PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 添加水印工件。水印是一种在页面上用于品牌、安保或信息目的的视觉覆盖层。示例展示了如何配置 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 外观，使用 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 与 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) 进行定位，旋转和透明度设置，然后将水印应用到 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。

1. 创建水印工件（参见 [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)）。
1. 配置文本状态（参见 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/)）。
1. 将文本绑定到水印。
1. 使用 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 和 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/) 定义定位和样式。
1. 通过页面的 [`Artifacts`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 集合将水印附加到 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)（参见 [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)）。
1. 使用 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 保存已更新的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。

```python

import aspose.pdf as ap

def add_watermark(input_pdf, output_pdf):
    # Load the existing PDF document
    document = ap.Document(input_pdf)

    # Create a watermark artifact
    watermark = ap.WatermarkArtifact()

    # Configure text state for the watermark
    text_state = ap.text.TextState()
    text_state.font_size = 72
    text_state.foreground_color = ap.Color.blue
    text_state.font = ap.text.FontRepository.find_font("Courier")

    # Apply text and style to the watermark
    watermark.set_text_and_state("WATERMARK", text_state)

    # Position and style settings
    watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
    watermark.rotation = 45
    watermark.opacity = 0.5
    watermark.is_background = True

    # Add watermark to the first page
    document.pages[1].artifacts.append(watermark)

    # Save the updated PDF
    document.save(output_pdf)
```


