---
title: 在 PDF 中获取和搜索图像
linktitle: 获取和搜索图像
type: docs
weight: 40
url: /zh/python-net/search-and-get-images-from-pdf-document/
description: 了解如何使用 Aspose.PDF 在 Python 中搜索并获取 PDF 文档中的图像。
lastmod: "2025-09-17"
TechArticle: true
AlternativeHeadline: 在 PDF 中搜索和提取图像
Abstract: Aspose.PDF for Python via .NET 库提供了强大的功能，用于在 PDF 文档中搜索和提取图像。利用 'ImagePlacementAbsorber' 类，开发人员可以高效定位并访问 PDF 所有页面中嵌入的图像。
---

## 检查 PDF 页面中的图像位置属性

本示例演示如何使用 Aspose.PDF for Python via .NET 分析并显示特定 PDF 页面上所有图像的属性。

1. 创建一个 'ImagePlacementAbsorber' 以收集页面上的所有图像。
1. 调用 'document.pages[1].accept(absorber)' 来分析第一页上的图像位置。
1. 遍历 'absorber.image_placements' 并显示每个图像的关键属性：
- 宽度和高度（点）。
- 左下角 X（LLX）和左下角 Y（LLY）坐标。
- 水平（X）和垂直（Y）分辨率（DPI）。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    for image_placement in absorber.image_placements:
        # Display image placement properties for all placements
        print("image width: " + str(image_placement.rectangle.width))
        print("image height: " + str(image_placement.rectangle.height))
        print("image LLX: " + str(image_placement.rectangle.llx))
        print("image LLY: " + str(image_placement.rectangle.lly))
        print("image horizontal resolution: " + str(image_placement.resolution.x))
        print("image vertical resolution: " + str(image_placement.resolution.y))
```

## 提取并计数 PDF 中的图像类型

此函数分析 PDF 第一页的所有图像，并统计其中有多少是灰度图像和 RGB 图像。

1. 创建一个 'ImagePlacementAbsorber' 以收集页面上的所有图像。
1. 初始化灰度和 RGB 图像的计数器。
1. 调用 'document.pages[1].accept(absorber)' 来分析图像位置。
1. 打印找到的图像总数。
1. 遍历 'absorber.image_placements' 中的每个图像：
- 使用 'image_placement.image.get_color_type()' 获取图像颜色类型。
- 增加相应的计数器（灰度或 rgb）。
- 为每个图像打印一条消息，指出它是灰度还是 RGB。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
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
```

## 从 PDF 中提取详细的图像信息

此函数分析 PDF 第一页的所有图像，并根据页面的图形变换计算它们的缩放尺寸和有效分辨率。

1. 加载 PDF 并初始化变量
1. 收集图像资源
1. 处理页面内容操作符：
- 'GSave' - 将当前 CTM 推入堆栈。
- 'GRestore' - 从堆栈弹出最近的 CTM。
- 'ConcatenateMatrix' - 通过与操作符的矩阵相乘来更新当前 CTM。
1. 打印图像名称、缩放尺寸和计算的分辨率。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)

    default_resolution = 72
    graphics_state = []

    image_names = list(document.pages[1].resources.images.names)

    graphics_state.append(drawing.drawing2d.Matrix(float(1), float(0), float(0), float(1), float(0), float(0)))

    for op in document.pages[1].contents:
        if is_assignable(op, ap.operators.GSave):
            graphics_state.append(cast(drawing.drawing2d.Matrix, graphics_state[-1]).clone())

        elif is_assignable(op, ap.operators.GRestore):
            graphics_state.pop()

        elif is_assignable(op, ap.operators.ConcatenateMatrix):
            opCM = cast(ap.operators.ConcatenateMatrix, op)
            cm = drawing.drawing2d.Matrix(
                float(opCM.matrix.a),
                float(opCM.matrix.b),
                float(opCM.matrix.c),
                float(opCM.matrix.d),
                float(opCM.matrix.e),
                float(opCM.matrix.f),
            )

            graphics_state[-1].multiply(cm)
            continue

        elif is_assignable(op, ap.operators.Do):
            opDo = cast(ap.operators.Do, op)
            if opDo.name in image_names:
                last_ctm = cast(drawing.drawing2d.Matrix, graphics_state[-1])
                index = image_names.index(opDo.name) + 1
                image = document.pages[1].resources.images[index]

                scaled_width = math.sqrt(last_ctm.elements[0] ** 2 + last_ctm.elements[1] ** 2)
                scaled_height = math.sqrt(last_ctm.elements[2] ** 2 + last_ctm.elements[3] ** 2)

                original_width = image.width
                original_height = image.height

                res_horizontal = original_width * default_resolution / scaled_width
                res_vertical = original_height * default_resolution / scaled_height

                print(
                    f"{self.data_dir}image {opDo.name} "
                    f"({scaled_width:.2f}:{scaled_height:.2f}): "
                    f"res {res_horizontal:.2f} x {res_vertical:.2f}"
                )
```

## 从 PDF 中的图像提取替代文本

此函数从 PDF 第一页的所有图像检索替代文本（alt text），对可访问性和 PDF/UA 合规性检查很有用。

1. 使用 'ap.Document()' 加载 PDF 文档。
1. 创建一个 'ImagePlacementAbsorber' 以收集页面上的所有图像。
1. 在第一页接受吸收器（page.accept(absorber)）。
1. 遍历 'absorber.image_placements' 中的每个图像：
- 打印页面资源集合中图像的名称（get_name_in_collection()）。
- 使用 'get_alternative_text(page)' 检索替代文本。
- 打印 alt 文本的第一行。

```python

    import math
    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable
    from os import path

    path_infile = path.join(self.data_dir, infile)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    page = document.pages[1]
    page.accept(absorber)

    for image_placement in absorber.image_placements:
        print(
            "Name in collection: "
            + str(image_placement.image.get_name_in_collection())
        )
        lines = image_placement.image.get_alternative_text(page)
        print("Alt Text: " + lines[0])
```
