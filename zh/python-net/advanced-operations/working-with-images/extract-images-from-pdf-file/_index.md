---
title: 使用 Python 从 PDF 文件中提取图像
linktitle: 提取图像
type: docs
weight: 30
url: /zh/python-net/extract-images-from-pdf-file/
description: 了解如何在 Python 中从 PDF 文件中提取嵌入的图像。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 使用 Python 从 PDF 文件中提取图像
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 从 PDF 文档中提取图像。内容涵盖提取单个嵌入图像以及导出页面上特定矩形区域内找到的图像。
---

当您需要复用嵌入的图形、归档图像资源或在 PDF 之外处理图像内容时，请使用此页面。

1. 使用加载源 PDF `ap.Document(infile)`.
1. 选择目标页面和图像资源索引。
1. 将图像对象保存到输出流。

```python
import aspose.pdf as ap
from io import FileIO


def extract_image(infile, outfile):
    document = ap.Document(infile)
    x_image = document.pages[1].resources.images[1]
    with FileIO(outfile, "wb") as output_image:
        x_image.save(output_image)
```

## 从 PDF 的特定区域提取图像

此示例提取位于 PDF 页面上指定矩形区域内的图像，并将它们另存为单独的文件。

1. 加载源 PDF。
1. 创建 `ImagePlacementAbsorber` 并在目标页面上接受它。
1. 定义目标矩形。
1. 遍历图像放置项，并检查每个图像的边界是否适合该区域。
1. 将匹配的图像保存到输出文件。

```python
import aspose.pdf as ap
from io import FileIO


def extract_image_from_specific_region(infile, outfile):
    document = ap.Document(infile)
    rectangle = ap.Rectangle(0, 0, 590, 590, True)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(image_placement.rectangle.llx, image_placement.rectangle.lly)
        point2 = ap.Point(image_placement.rectangle.urx, image_placement.rectangle.ury)

        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(outfile.replace("index", str(index)), "wb") as output_image:
                image_placement.image.save(output_image)
            index += 1
```

## 相关图像主题

- [使用 Python 处理 PDF 中的图像](/pdf/zh/python-net/working-with-images/)
- [替换现有 PDF 文件中的图像](/pdf/zh/python-net/replace-image-in-existing-pdf-file/)
- [从 PDF 文件中删除图像](/pdf/zh/python-net/delete-images-from-pdf-file/)
- [向现有 PDF 文件添加图像](/pdf/zh/python-net/add-image-to-existing-pdf-file/)
