---
title: 在 Python 中添加 PDF 背景
linktitle: 添加背景
type: docs
weight: 20
url: /zh/python-net/add-backgrounds/
description: 在 Python 中向 PDF 页面添加图像和纯色背景，并调整背景图像的不透明度。
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 为 PDF 添加背景
Abstract: 在 Python 中向 PDF 页面添加图像和纯色背景，并调整背景图像的不透明度。
---

使用 `BackgroundArtifact` 在 PDF 页的内容后面放置图像或纯色。这些示例会修改第一页。

## 向 PDF 添加背景图像

将图像流赋给 `background_image` 属性，然后将工件添加到页面。

```python
from io import FileIO
import aspose.pdf as ap

def add_background_image_to_pdf(infile, imagefile, outfile, opacity=1.0):
    """Add a background image to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_image = FileIO(imagefile, "rb")
        artifact.opacity = opacity
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 向 PDF 添加半透明背景图像

将 0 到 1 之间的不透明度值传给同一个函数。要获得半透明图像，请使用 `0.5`。

```python
add_background_image_to_pdf("input.pdf", "background.png", "output.pdf", opacity=0.5)
```

## 为 PDF 添加背景颜色

设置工件的 `background_color` 属性以应用纯色背景。

```python
import aspose.pdf as ap

def add_background_color_to_pdf(infile, outfile):
    """Add a solid color background to a PDF document as an artifact."""
    with ap.Document(infile) as document:
        artifact = ap.BackgroundArtifact()
        artifact.background_color = ap.Color.dark_khaki
        document.pages[1].artifacts.append(artifact)
        document.save(outfile)
```

## 相关主题

- [删除背景](/pdf/zh/python-net/remove-backgrounds/)
- [在 Python 中处理 PDF 工件](/pdf/zh/python-net/artifacts/)
