---
title: 在 Python 中使用 PDF 操作符
linktitle: 使用操作符
type: docs
weight: 90
url: /zh/python-net/working-with-operators/
description: 了解如何在 Python 中使用低层 PDF 操作符，以实现精确的内容流处理和图形控制。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用低层 PDF 操作符进行内容流控制
Abstract: 本文解释了如何在 Aspose.PDF for Python via .NET 中使用低级 PDF 操作符。了解如何直接操作内容流，使用操作符类精确定位图形，以及在 Python 工作流中从 PDF 页面中删除绘制的对象。
---

## PDF 操作符及其用法简介

操作符是指定应执行的某种操作的 PDF 关键字，例如在页面上绘制图形形状。操作符关键字与具名对象的区别在于其前面没有斜线字符（2Fh）。操作符仅在内容流内部才有意义。

内容流是一个 PDF 流对象，其数据由描述在页面上绘制的图形元素的指令组成。关于 PDF 操作符的更多详细信息可在 [PDF 规范](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

当您需要在 Python 中直接控制 PDF 内容流时，请使用此页面，例如在精确坐标处放置图形、包装图形状态更改，或从页面中删除特定的绘图操作符。

## 使用运算符类添加图像

当您需要在 PDF 页面流中非常精确地放置图像内容且不依赖于更高级别的布局抽象时，请使用低层运算符类。

此方法通过直接使用低级图形操作符操控内容流，实现对 PDF 中图像放置的细粒度控制。当需要对图像进行精确定位和变换时，它特别有用，例如：

- 在特定位置添加水印或徽标。
- 将图像覆盖到已有内容上并实现精确对齐。
- 实现不能通过更高级抽象实现的自定义布局。

通过使用 GSave、ConcatenateMatrix、Do 和 GRestore 等运算符，开发人员可以确保图像准确渲染，并且不会对其他页面内容产生意外的副作用。

- 这 [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) 运算符保存 PDF 当前的图形状态。
- 这 [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) （concatenate matrix）运算符用于定义图像应如何放置在 PDF 页面上。
- 这 [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) 运算符在页面上绘制图像。
- 这 [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) 操作符恢复图形状态。

将图像添加到 PDF 文件中：

1. 打开 PDF 文档
1. 定义图像放置坐标
1. 访问目标页面
1. 将图像加载到流中
1. 保存当前图形状态
1. 创建矩形和变换矩阵
1. 应用变换矩阵
1. 绘制图像
1. 恢复先前的图形状态
1. 保存已修改的 PDF 文档

以下代码片段展示了如何使用 PDF 操作符：

```python
import sys
import aspose.pdf as ap
from os import path

def add_image_using_pdf_operators(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        page = document.pages[1]

        with open(imagefile, "rb") as image_stream:
            page.resources.images.add(image_stream)

        page.contents.append(ap.operators.GSave())

        rectangle = ap.Rectangle(
            lower_left_x, lower_left_y, upper_right_x, upper_right_y, True
        )
        matrix = ap.Matrix(
            [
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            ]
        )

        page.contents.append(ap.operators.ConcatenateMatrix(matrix))

        x_image = page.resources.images[len(page.resources.images)]

        page.contents.append(ap.operators.Do(x_image.name))

        page.contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## 使用运算符在页面上绘制 XForm

本示例利用 XForms 及图形运算符的强大功能，在 PDF 中高效地复用图形内容。通过将图像封装在 XForm 中，可以多次绘制而无需复制图像数据，从而减小文件大小并提升性能。此方法尤其在以下情况中受益：

- 同一图像或图形需要在文档中出现多次。

- 需要对图形的放置和变换进行精确控制。

- 优化 PDF 的性能和大小是首要任务。

通过使用 GSave 和 GRestore 管理图形状态，并使用 ConcatenateMatrix 进行变换矩阵操作，此技术确保每个图形都能正确且独立地渲染。

```python
import sys
import aspose.pdf as ap
from os import path

def draw_xform_on_page(infile, imagefile, outfile):
    with ap.Document(infile) as document:
        page_contents = document.pages[1].contents

        page_contents.insert(1, ap.operators.GSave())
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GSave())

        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.append(form)

        form.contents.append(ap.operators.GSave())
        form.contents.append(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        with open(imagefile, "rb") as image_stream:
            form.resources.images.add(image_stream)

        x_image = form.resources.images[len(form.resources.images)]
        form.contents.append(ap.operators.Do(x_image.name))
        form.contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 500)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        # Draw XForm at (100, 300)
        page_contents.append(ap.operators.GSave())
        page_contents.append(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.append(ap.operators.Do(form.name))
        page_contents.append(ap.operators.GRestore())

        page_contents.append(ap.operators.GRestore())

        document.save(outfile)
```

## 使用运算符类删除图形对象

下面的代码片段展示了如何删除图形。请注意，如果 PDF 文件包含图形的文本标签，使用此方法它们可能仍然保留在 PDF 文件中。因此，请搜索图形操作符，以寻找删除此类图像的备用方法。

```python
import sys
import aspose.pdf as ap
from os import path

def remove_graphics_objects(infile, outfile):
    with ap.Document(infile) as document:
        page = document.pages[1]
        # Collect operators to remove in single pass
        # Operator codes: S=Stroke, h=ClosePathStroke, f=Fill'
        graphics_operators = {"S", "h", "f"}
        operators_to_remove = [
            op for op in page.contents if str(op) in graphics_operators
        ]

        page.contents.delete(operators_to_remove)
        document.save(outfile)
```

## 相关主题

- [Python中的高级PDF操作](/pdf/zh/python-net/advanced-operations/)
- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [使用 Python 处理 PDF 中的图像](/pdf/zh/python-net/working-with-images/)
- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
