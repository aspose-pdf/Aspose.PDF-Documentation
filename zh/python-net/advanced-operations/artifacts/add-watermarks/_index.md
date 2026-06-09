---
title: 在 Python 中为 PDF 添加水印
linktitle: 添加水印
type: docs
weight: 30
url: /zh/python-net/add-watermarks/
description: 了解如何使用 Aspose.PDF for Python via .NET 在 Python 中向 PDF 文件添加水印。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 向 PDF 添加水印
Abstract: 本文讨论了使用 Aspose.PDF for Python via .NET 通过管理 artifacts 为 PDF 文档添加水印。它介绍了处理 artifacts 的关键类——`Artifact` 和 `ArtifactCollection`，并描述了如何通过 `Page` 类的 `Artifacts` 属性访问它们。本文详细说明了 `Artifact` 类的属性，包括 `contents`、`form`、`image`、`text`、`rectangle`、`rotation` 和 `opacity` 等属性，这些属性使得在 PDF 文件中对 artifacts 进行全面操作成为可能。此外，还提供了一个实用示例，演示如何使用 Python 编程方式向 PDF 的首页添加水印。代码片段展示了 `WatermarkArtifact` 的创建与配置，设置其文本、对齐方式、旋转角度和透明度，然后将其追加到 PDF 文档并保存更改。
---

向 PDF 添加水印工件 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 使用 Aspose.PDF for Python via .NET。水印是应用于页面的可视化覆盖层，用于品牌化、安全或信息目的。示例展示了如何配置 [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) 外观、定位与 [`HorizontalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/horizontalalignment/) 和 [`VerticalAlignment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/verticalalignment/)，旋转和透明度在将水印应用于 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).

## 从 PDF 中提取水印

1. 加载 PDF 文档。
1. 访问页面伪影。
1. 过滤水印伪影。
1. 收集水印元素。
1. 提取水印属性。
1. 输出水印信息。

```python
from os import path
import sys
import aspose.pdf as ap

def extract_watermark_from_pdf(infile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            print(f"{watermark.text} {watermark.rectangle}")
```

## 向 PDF 添加水印

使用 Aspose.PDF for Python 向 PDF 文档添加文本水印：

1. 加载 PDF 文档。
1. 创建文本状态。
1. 创建水印工件。
1. 设置水印文本和样式。
1. 配置位置和旋转。
1. 设置不透明度和背景行为。
1. 将水印附加到页面。
1. 保存更新后的文档。

```python
from os import path
import sys
import aspose.pdf as ap

def add_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        text_state = ap.text.TextState()
        text_state.font_size = 72
        text_state.foreground_color = ap.Color.blue_violet
        text_state.font_style = ap.text.FontStyles.BOLD
        text_state.font = ap.text.FontRepository.find_font("Arial")

        watermark = ap.WatermarkArtifact()
        watermark.set_text_and_state("WATERMARK", text_state)
        watermark.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
        watermark.artifact_vertical_alignment = ap.VerticalAlignment.CENTER
        watermark.rotation = 60
        watermark.opacity = 0.2
        watermark.is_background = True

        document.pages[1].artifacts.append(watermark)
        document.save(outfile)

```

## 删除 PDF 页面上的水印伪影 

使用 Aspose.PDF for Python API 从 PDF 文档的特定页面中删除水印伪影。该方法针对存储为页面伪影的水印元素（特别是被归类为分页水印子类型的元素），遍历它们并在保存更新后的文档之前将其删除。

1. 加载 PDF 文档。
1. 访问页面伪影。
1. 过滤水印伪影。
1. 删除水印伪影。
1. 保存更新后的文档。

```python
from os import path
import sys
import aspose.pdf as ap

def delete_watermark_artifact(infile, outfile):
    with ap.Document(infile) as document:
        watermarks = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.WATERMARK
        ]

        for watermark in watermarks:
            document.pages[1].artifacts.delete(watermark)

        document.save(outfile)
```

## 相关工件主题

- [在 Python 中使用 PDF 工件](/pdf/zh/python-net/artifacts/)
- [在 Python 中添加 PDF 背景](/pdf/zh/python-net/add-backgrounds/)
- [在 Python 中为 PDF 添加 Bates 编号](/pdf/zh/python-net/add-bates-numbering/)
- [统计 PDF 文件中的工件类型](/pdf/zh/python-net/counting-artifacts/)