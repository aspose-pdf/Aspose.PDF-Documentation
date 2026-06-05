---
title: 在 Python 中向现有 PDF 添加图像
linktitle: 向 PDF 添加图像
type: docs
weight: 10
url: /zh/python-net/add-image-to-existing-pdf-file/
description: 了解如何在 Python 中向现有 PDF 文件添加图像、将其放置在固定坐标、设置替代文本并使用图像压缩。
lastmod: "2026-05-05"
TechArticle: true
AlternativeHeadline: 使用 Python 向现有 PDF 文件添加图像
Abstract: 本文展示了如何使用 Aspose.PDF for Python via .NET 向 PDF 文档添加图像。内容包括在固定坐标处放置图像、使用低级 PDF 操作符绘制图像、为可访问性分配替代文本以及使用 Flate compression 嵌入图像。
---

## 在 Python 中向现有 PDF 文件添加图像

此示例展示了如何使用 Aspose.PDF for Python via .NET 在现有 PDF 页面上的固定位置放置图像。

当您需要向现有 PDF 布局中添加徽标、照片、印章、图表或其他图形时，请使用这些示例。您可以使用页面坐标放置图像、使用操作符绘制图像、添加可访问性文本，或控制图像压缩。

1. 加载现有的 PDF `ap.Document(infile)`.
1. 选择目标页面（`document.pages[1]` 针对第一页)。
1. 呼叫 `page.add_image()` 使用：
    - 图像文件路径。
    - A `Rectangle` 定义放置坐标。
1. 保存更新后的 PDF。

```python
import aspose.pdf as ap


def add_image(infile, image_file, outfile):
    document = ap.Document(infile)
    page = document.pages[1]
    page.add_image(image_file, ap.Rectangle(20, 730, 120, 830, True))
    document.save(outfile)
```

## 使用运算符向 PDF 添加图像

此方法使用低级 PDF 运算符添加图像，而不是高级的 `add_image()` 帮助者。

1. 创建一个新 `Document` 并添加一页。
1. 将图像添加到页面资源（`page.resources.images`).
1. 创建转换运算符（`GSave`, `ConcatenateMatrix`, `Do`, `GRestore`).
1. 将操作符添加到页面内容。
1. 保存生成的 PDF。

```python
import aspose.pdf as ap
from io import FileIO


def add_image_using_operators(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream)

    rectangle = ap.Rectangle(0, 0, page.media_box.width, page.media_box.height, True)

    operators = [
        ap.operators.GSave(),
        ap.operators.ConcatenateMatrix(
            ap.Matrix(
                rectangle.urx - rectangle.llx,
                0,
                0,
                rectangle.ury - rectangle.lly,
                rectangle.llx,
                rectangle.lly,
            )
        ),
        ap.operators.Do(image_id),
        ap.operators.GRestore(),
    ]

    page.contents.add(operators)
    document.save(outfile)
```

## 向 PDF 添加带替代文本的图像

此示例添加了一张图像并为可访问性分配替代文本。

1. 创建一个新 `Document` 并添加一页。
1. 将图像添加到页面，使用 `page.add_image()`.
1. 获取图像资源来源 `page.resources.images`.
1. 使用设置替代文本 `try_set_alternative_text()`.
1. 保存生成的 PDF。

```python
import aspose.pdf as ap


def add_image_set_alternative_text(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842, 595)

    page.add_image(image_file, ap.Rectangle(0, 0, 842, 595, True))
    resources_images = page.resources.images
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text("Alternative text for image", page)

    if result:
        print("Alternative text has been added successfully")

    document.save(outfile)
```

## 向 PDF 添加使用 Flate 压缩的图像

此示例使用嵌入图像 `ImageFilterType.FLATE` 压缩。

1. 创建一个新 `Document` 并添加一页。
1. 将图像以 Flate 压缩方式添加到页面资源中。
1. 使用矩阵运算符放置并绘制图像。
1. 保存文档。

```python
import aspose.pdf as ap
from io import FileIO


def add_image_to_pdf_with_flate_compression(image_file, outfile):
    document = ap.Document()
    page = document.pages.add()
    resources_images = page.resources.images

    with FileIO(image_file, "rb") as image_stream:
        image_id = resources_images.add(image_stream, ap.ImageFilterType.FLATE)

    rectangle = ap.Rectangle(0, 0, 600, 600, True)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.lly,
    )

    page.contents.add([ap.operators.GSave()])
    page.contents.add([ap.operators.ConcatenateMatrix(matrix)])
    page.contents.add([ap.operators.Do(image_id)])
    page.contents.add([ap.operators.GRestore()])

    document.save(outfile)
```

## 相关图像主题

- [使用 Python 在 PDF 中处理图像](/pdf/zh/python-net/working-with-images/)
- [替换已有 PDF 文件中的图像](/pdf/zh/python-net/replace-image-in-existing-pdf-file/)
- [从 PDF 文件中删除图像](/pdf/zh/python-net/delete-images-from-pdf-file/)
- [从 PDF 文件中提取图像](/pdf/zh/python-net/extract-images-from-pdf-file/)
