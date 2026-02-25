---
title: 使用 Python 从 PDF 文件提取图像
linktitle: 提取图像
type: docs
weight: 30
url: /zh/python-net/extract-images-from-pdf-file/
description: 本节展示如何使用 Python 库从 PDF 文件中提取图像。
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: 使用 Python 从 PDF 中提取图像
Abstract: 本文讨论了使用 Aspose.PDF for Python 从 PDF 文件中提取图像的过程。它强调了将图像分离用于管理、归档、分析或共享等目的的实用性。文章说明，PDF 中的图像存储在每页的资源集合中，具体位于 XImage 集合中。要提取图像，用户可以访问特定页面并通过其在 Images 集合中的索引检索图像。索引返回的 XImage 对象提供 `save()` 方法以保存提取的图像。文中提供了代码片段，演示打开 PDF 文档、使用索引从第二页提取特定图像并将其保存到文件的步骤。
---

您是否需要将 PDF 文件中的图像分离出来？为了简化管理、归档、分析或共享文档中的图像，请使用 **Aspose.PDF for Python** 并从 PDF 文件中提取图像。

1. 使用 'ap.Document()' 加载 PDF 文档。
1. 访问文档中所需的页面（document.pages[1]）。
1. 从页面资源中选择图像（例如，resources.images[1]）。
1. 为目标文件创建输出流（FileIO）。
1. 使用 'xImage.save(output_image)' 保存提取的图像。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    xImage = document.pages[1].resources.images[1]
    with FileIO(path_outfile, "w") as output_image:
        xImage.save(output_image)
```

## 从 PDF 的特定区域提取图像

此示例提取 PDF 页面上位于指定矩形区域内的图像，并将其保存为单独的文件。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 创建 'ImagePlacementAbsorber' 以收集首页上的所有图像。
1. 调用 'document.pages[1].accept(absorber)' 分析图像位置。
1. 遍历 'absorber.image_placements' 中的所有图像：
- 获取图像的边界框（llx, lly, urx, ury）。
- 检查图像矩形的两个角是否都位于目标矩形内部（rectangle.contains()）。
- 如果为真，使用 FileIO 将图像保存到文件中，用顺序编号替换文件名中的 'index'。
1. 为每个保存的图像递增索引。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    rectangle = ap.Rectangle(0, 0, 590, 590, True)

    document = ap.Document(path_infile)
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)
    index = 1
    for image_placement in absorber.image_placements:
        point1 = ap.Point(
            image_placement.rectangle.llx, image_placement.rectangle.lly
        )
        point2 = ap.Point(
            image_placement.rectangle.urx, image_placement.rectangle.urx
        )
        if rectangle.contains(point1, True) and rectangle.contains(point2, True):
            with FileIO(path_outfile.replace("index", str(index)), "w") as output_image:
                image_placement.image.save(output_image)
            index = index + 1
```

## 从 PDF 中提取图像信息

下面的示例演示如何分析嵌入在 PDF 页面中的图像并计算其有效分辨率。

1. 使用 'ap.Document' 打开 PDF。
1. 在读取页面内容时跟踪图形状态。
1. 处理操作符：
- 'GSave'/'GRestore' - 推/出矩阵。
- 'ConcatenateMatrix' - 更新变换。
- 'Do' - 如果是图像，获取大小并应用变换。
1. 计算有效 DPI。
1. 打印图像名称、缩放尺寸和 DPI。

```python

    import aspose.pdf as ap
    from io import FileIO
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
