---
title: 在 Python 中添加 PDF 背景
linktitle: 添加背景
type: docs
weight: 20
url: /zh/python-net/add-backgrounds/
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 的 BackgroundArtifact 类向 PDF 页面添加背景图像。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 为 PDF 添加背景
Abstract: 本文讨论了在 PDF 文档中使用 Aspose.PDF for Python via .NET 添加背景图像的用法。它强调了通过利用 `BackgroundArtifact` 类，可向文档添加水印或细微设计的能力，该类允许将背景图像合并到各个页面对象中。文章提供了一个实用的代码示例，演示如何实现此功能。过程包括创建一个新的 PDF 文档、添加页面、创建 `BackgroundArtifact` 对象、设置背景图像，并将该背景工件追加到页面的 artifacts 集合中。最后，将修改后的文档保存为 PDF 文件。此技术可提升 PDF 文档的视觉呈现效果。
---

## 向 PDF 添加背景图像

背景图像可用于在文档中添加水印或其他细微的设计。在 Aspose.PDF for Python via .NET 中，每个 PDF 文档都是页面的集合，每个页面包含一组工件。该 [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/) 类可用于向页面对象添加背景图像。

当您需要在主 PDF 内容后面放置装饰性图像，而不将其转换为可搜索的文本文档时，此方法非常有用。

以下代码片段展示了如何使用 BackgroundArtifact 对象在 Python 中向 PDF 页面添加背景图像。

1. 加载 PDF 文档。
1. 创建背景 artifact。
1. 加载图像文件。
1. 将工件附加到页面。
1. 保存更新后的文档。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_to_pdf(infile, imagefile, outfile):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 向 PDF 添加带透明度的背景图像

使用 Aspose.PDF for Python 向 PDF 页面添加半透明背景图像。

通过应用不透明度，背景图像会变得部分透明，使原始页面内容（文字、图像等）仍然清晰可见。这在以下情况下尤其有用：

- 水印
- 品牌覆盖层
- 细微的设计增强

背景作为工件添加，确保它位于所有页面内容的后面。

1. 加载 PDF 文档。
1. 创建背景 artifact。
1. 加载图像文件。
1. 设置不透明度级别。
1. 将工件附加到页面。
1. 保存更新后的文档。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_image_with_opacity_to_pdf(infile, imagefile, outfile):
    """Add a background image with opacity to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = 0.5
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 为 PDF 添加背景颜色

使用 Aspose.PDF for Python 为 PDF 页面应用纯色背景。

1. 加载 PDF 文档。
1. 创建背景 artifact。
1. 设置背景颜色。
1. 将工件附加到页面。
1. 保存更新后的文档。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 从 PDF 中移除背景

使用 Aspose.PDF for Python 从 PDF 页面中移除背景伪影。
PDF 中的背景通常以伪影形式存储，此方法会选择性地识别并仅移除被分类为背景元素的伪影。

1. 加载 PDF 文档。
1. 访问页面伪影。
1. 过滤背景伪影。
1. 收集背景元素。
1. 删除背景伪影。
1. 保存更新后的文档。

```python

from os import path
from io import FileIO
import aspose.pdf as ap
import sys

def remove_background(infile, outfile):
    with ap.Document(infile) as document:
        backgrounds = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and artifact.subtype == ap.Artifact.ArtifactSubtype.BACKGROUND
        ]

        for background in backgrounds:
            document.pages[1].artifacts.delete(background)

        document.save(outfile)
```

## 相关工件主题

- [在 Python 中使用 PDF 工件](/pdf/zh/python-net/artifacts/)
- [在 Python 中为 PDF 添加水印](/pdf/zh/python-net/add-watermarks/)
- [在 Python 中为 PDF 添加 Bates 编号](/pdf/zh/python-net/add-bates-numbering/)
- [统计 PDF 文件中的工件类型](/pdf/zh/python-net/counting-artifacts/)