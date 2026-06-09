---
title: 获取并搜索 PDF 中的图像
linktitle: 获取并搜索图像
type: docs
weight: 40
url: /zh/python-net/search-and-get-images-from-pdf-document/
description: 了解如何在 Python 中搜索和检查 PDF 文档中的图像。
lastmod: "2026-06-08"
TechArticle: true
AlternativeHeadline: 使用 Python 搜索并检查 PDF 文件中的图像
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中搜索和检查图像。它涵盖了使用 ImagePlacementAbsorber 来分析图像的放置位置、大小、分辨率和替代文本。
---

## 检查 PDF 页面中的图像放置属性

本示例演示了如何使用 Aspose.PDF for Python via .NET 分析并显示特定 PDF 页面上所有图像的属性。

当您需要审计图像放置、检查图像分辨率或识别跨 PDF 页面嵌入的图像对象时，请使用此页面。

1. 创建一个 'ImagePlacementAbsorber' 来收集页面上的所有图像。
1. 调用 'document.pages[1].accept(absorber)' 来分析第一页上的图像布局。
1. 遍历 'absorber.image_placements' 并显示每个图像的关键属性：
    - 宽度和高度（点）。
    - 左下 X (LLX) 和 左下 Y (LLY) 坐标。
    - 水平 (X) 和 垂直 (Y) 分辨率 (DPI)。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_params(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## 提取并统计 PDF 中的图像类型

此函数分析 PDF 首页的所有图像，并统计其中的灰度图像和 RGB 图像数量。

1. 创建一个 'ImagePlacementAbsorber' 来收集页面上的所有图像。
1. 初始化灰度和 RGB 图像的计数器。
1. 调用 'document.pages[1].accept(absorber)' 来分析图像放置位置。
1. 打印找到的图像总数。
1. 遍历 'absorber.image_placements' 中的每个图像：
    - 使用 `image_placement.image.get_color_type()` 获取图像颜色类型。
    - 增加相应的计数器（灰度或 rgb）。
    - 为每个图像打印一条消息，指示它是灰度还是 RGB。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_types_from_pdf(infile):
    """
    Extract and count image types (grayscale/RGB) with resolution analysis.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_image_types_from_pdf("sample_extr.pdf")

    Note:
        Prints total images count, color type for each image, and resolution info.
    """

    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()

    # Counters for grayscale and RGB images
    grayscaled = 0
    rgb = 0

    document.pages[1].accept(absorber)

    print("--------------------------------")
    print("Total Images = " + str(len(absorber.image_placements)))

    image_counter = 1

    for image_placement in absorber.image_placements:
        # Determine the color type of the image
        colorType = image_placement.image.get_color_type()
        if colorType == ap.ColorType.GRAYSCALE:
            grayscaled += 1
            print(f"Image {image_counter} is Grayscale...")
        elif colorType == ap.ColorType.RGB:
            rgb += 1
            print(f"Image {image_counter} is RGB...")
        image_counter += 1

    print("--------------------------------")
    print("Grayscale Images = " + str(grayscaled))
    print("RGB Images = " + str(rgb))
```

## 从 PDF 中提取详细的图像信息

此函数分析 PDF 第一页上的所有图像，并根据页面的图形变换计算它们的缩放尺寸和有效分辨率。

1. 加载 PDF 并初始化变量
1. 收集图像资源
1. 处理页面内容操作符：
    - 'GSave' - 将当前 CTM 推入堆栈。
    - 'GRestore' - 从堆栈中弹出最后一个 CTM。
    - 'ConcatenateMatrix' - 通过与运算符的矩阵相乘来更新当前 CTM。
1. 打印图像名称、缩放后的尺寸和计算得到的分辨率。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_information_from_pdf(infile):
    with ap.Document(infile) as document:
        default_resolution = 72
        graphics_state = []

        image_names = list(document.pages[1].resources.images.names)

        graphics_state.append(
            drawing.drawing2d.Matrix(
                float(1), float(0), float(0), float(1), float(0), float(0)
            )
        )

        for op in document.pages[1].contents:
            if is_assignable(op, ap.operators.GSave):
                graphics_state.append(
                    cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone()
                )

            elif is_assignable(op, ap.operators.GRestore):
                graphics_state.pop()

            elif is_assignable(op, ap.operators.ConcatenateMatrix):
                op_cm = cast(ap.operators.ConcatenateMatrix, op)
                cm = drawing.drawing2d.Matrix(
                    float(op_cm.matrix.a),
                    float(op_cm.matrix.b),
                    float(op_cm.matrix.c),
                    float(op_cm.matrix.d),
                    float(op_cm.matrix.e),
                    float(op_cm.matrix.f),
                )

                graphics_state[-1].multiply(cm)
                continue

            elif is_assignable(op, ap.operators.Do):
                op_do = cast(ap.operators.Do, op)
                if op_do.name in image_names:
                    last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                    index = image_names.index(op_do.name) + 1
                    image = document.pages[1].resources.images[index]

                    scaled_width = math.sqrt(
                        last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2
                    )
                    scaled_height = math.sqrt(
                        last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2
                    )

                    original_width = image.width
                    original_height = image.height

                    res_horizontal = (
                        original_width * default_resolution / scaled_width
                    )
                    res_vertical = (
                        original_height * default_resolution / scaled_height
                    )

                    info = (
                        f"{infile} image {op_do.name} "
                        f"({scaled_width:.2f}:{scaled_height:.2f}): "
                        f"res {res_horizontal:.2f} x {res_vertical:.2f}\n"
                    )
                    print(info.rstrip())
```

## 从 PDF 中提取图像的替代文本

此函数从 PDF 第一页的所有图像中检索替代文本（alt text），对可访问性和 PDF/UA 合规性检查很有用。

1. 使用 'ap.Document()' 加载 PDF 文档。
1. 创建一个 'ImagePlacementAbsorber' 来收集页面上的所有图像。
1. 在第一页接受吸收器（page.accept(absorber)）。
1. 遍历 'absorber.image_placements' 中的每个图像：
    - 打印页面资源集合中图像的名称 (get_name_in_collection()).
    - 使用 'get_alternative_text(page)' 检索替代文本。
    - 打印 alt 文本的第一行。

```python
import math
import aspose.pdf as ap
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as drawing

def extract_image_alt_text(infile):
    document = ap.Document(infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: " + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```

## 相关图像主题

- [使用 Python 处理 PDF 中的图像](/pdf/zh/python-net/working-with-images/)
- [从 PDF 文件中提取图像](/pdf/zh/python-net/extract-images-from-pdf-file/)
- [替换现有 PDF 文件中的图像](/pdf/zh/python-net/replace-image-in-existing-pdf-file/)
- [向现有 PDF 文件添加图像](/pdf/zh/python-net/add-image-to-existing-pdf-file/)
