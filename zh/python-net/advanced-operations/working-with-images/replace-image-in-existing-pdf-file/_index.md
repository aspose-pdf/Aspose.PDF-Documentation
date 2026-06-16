---
title: 使用 Python 在已有 PDF 文件中替换图像
linktitle: 替换图像
type: docs
weight: 70
url: /zh/python-net/replace-image-in-existing-pdf-file/
description: 了解如何在 Python 中替换已有 PDF 文件中的嵌入图像。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 使用 Python 替换已有 PDF 文件中的图像
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中替换图像。它涵盖了通过资源索引替换图像以及使用 ImagePlacementAbsorber 替换特定找到的图像。
---

## 在 PDF 中替换图像

当您需要在 PDF 中更新徽标、图表或其他嵌入式图形且无需重新构建文档布局时，请使用此页面。

1. 使用加载源 PDF `ap.Document(infile)`.
1. 将替换图像以二进制流的形式打开。
1. 按索引在页面上替换图像资源。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap
from io import FileIO


def replace_image(infile, image_file, outfile):
    document = ap.Document(infile)

    with FileIO(image_file, "rb") as image_stream:
        document.pages[1].resources.images.replace(1, image_stream)

    document.save(outfile)
```

## 替换特定图像

此示例替换由...找到的特定图像放置 `ImagePlacementAbsorber`.

1. 加载源 PDF。
1. 创建 `ImagePlacementAbsorber` 并收集页面上的图像放置位置。
1. 检查页面上是否存在任何图像位置。
1. 用新的图像流替换所选位置。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap
from io import FileIO


def replace_image_with_absorber(infile, image_file, outfile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        image_placement = absorber.image_placements[1]
        with FileIO(image_file, "rb") as image_stream:
            image_placement.replace(image_stream)

    document.save(outfile)
```

## 相关图像主题

- [使用 Python 处理 PDF 中的图像](/pdf/zh/python-net/working-with-images/)
- [从 PDF 文件中删除图像](/pdf/zh/python-net/delete-images-from-pdf-file/)
- [从 PDF 文件中提取图像](/pdf/zh/python-net/extract-images-from-pdf-file/)
- [向现有 PDF 文件添加图像](/pdf/zh/python-net/add-image-to-existing-pdf-file/)
