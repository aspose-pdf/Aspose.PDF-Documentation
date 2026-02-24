---
title: 使用 Python 向 PDF 添加图像
linktitle: 添加图像
type: docs
weight: 10
url: /zh/python-net/add-image-to-existing-pdf-file/
description: 本节描述如何使用 Python 库向现有 PDF 文件添加图像。
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: 如何使用 Python 向 PDF 添加图像
Abstract: 本文提供了使用 Python 结合 Aspose.PDF 库向现有 PDF 文件添加图像的指南。文中概述了两种实现方法。第一种方法使用 Aspose.PDF 的 `Document` 类，用户加载 PDF，指定页码，并使用 `Page` 类的 `add_image` 方法定位图像。随后使用 `save()` 方法保存文档。第二种方法利用 Aspose.PDF.Facades 命名空间下的 `PdfFileMend` 类，提供更简洁的接口。在此方法中调用 `add_image()` 将图像添加到指定页面和坐标，然后保存更新后的 PDF 并关闭 `PdfFileMend` 对象。文中提供了两种方法的代码片段以演示整个过程。
---

## 在现有 PDF 文件中添加图像

本示例演示如何使用 Aspose.PDF for Python via .NET 在 PDF 页面上的特定位置插入图像。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 选择目标页面 '(document.pages[1]' - 第第一页。
1. 使用 'page.add_image()' 放置图像：
- 图像的文件路径。
- 一个 'Rectangle' 对象，定义图像的坐标 (left=20, bottom=730, right=120, top=830)。
1. 保存更新后的 PDF。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]
    page.add_image(
        path.join(self.data_dir, image_file),
        ap.Rectangle(20, 730, 120, 830, True),
    )
    document.save(path_outfile)
```

## 使用操作符添加图像

下面的代码片段展示了一种低层次的方法，通过手动操作 PDF 操作符而非高级助手方法向 PDF 页面添加图像。

步骤：

1. 创建一个新的空白 'Document'。
1. 添加一页并设置其尺寸 (842 × 595 - 横向 A4)。
1. 访问页面的图像资源 (page.resources.images)。
1. 将图像文件加载到流中并添加到资源。
- 该方法返回一个 'image_id'。
- 从资源中检索新添加的图像对象。
1. 定义一个保持图像纵横比的矩形：
1. 构建操作符序列：
- 'GSave()' - 保存当前图形状态。
- 'ConcatenateMatrix(matrix)' - 应用变换（缩放并在页面上垂直居中图像）。
- 'Do(image_id)' - 渲染图像。
- 'GRestore()' - 恢复图形状态。
1. 将操作符序列添加到 'page.contents'。
1. 保存生成的 PDF。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_infile = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    # Get page resources
    resources_images = page.resources.images

    # Add image to resources
    image_stream = FileIO(path.join(self.data_dir, path_infile), "rb")
    image_id = resources_images.add(image_stream)

    x_image = list(resources_images)[-1]

    rectangle = ap.Rectangle(
        0,
        0,
        page.media_box.width,
        (page.media_box.width * x_image.height) / x_image.width,
        True,
    )

    # Create operator sequence for adding image
    operators = []

    # Save graphics state
    operators.append(ap.operators.GSave())

    # Set transformation matrix (position and size)
    matrix = ap.Matrix(
        rectangle.urx - rectangle.llx,
        0,
        0,
        rectangle.ury - rectangle.lly,
        rectangle.llx,
        rectangle.llx + (page.media_box.height - rectangle.height) / 2,
    )
    operators.append(ap.operators.ConcatenateMatrix(matrix))

    # Draw the image
    operators.append(ap.operators.Do(image_id))

    # Restore graphics state
    operators.append(ap.operators.GRestore())

    # Add operators to page contents
    page.contents.add(operators)

    document.save(path_outfile)
```

## 为图像添加备用文字

本示例展示如何向 PDF 页面添加图像并分配备用文字（alt text），以满足无障碍合规性（例如 PDF/UA）。

1. 创建一个新的 'Document' 并添加一页 (842 × 595, 横向 A4)。
1. 使用 'page.add_image()' 并使用跨越整页的矩形，将图像放置在页面上。
1. 访问页面的图像资源 ('page.resources.images')。
1. 定义一段备用文字字符串（例如，'Alternative text for image'）。
1. 从资源中检索第一个图像对象 ('x_image = resources_images[1]')。
1. 使用 'try_set_alternative_text(alt_text, page)' 为图像分配备用文字。
1. 保存生成的 PDF。

```python

    import aspose.pdf as ap
    from io import FileIO
    from os import path

    path_image_file = path.join(self.data_dir, image_file)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document()
    page = document.pages.add()
    page.set_page_size(842,595)

    page.add_image(
        path_image_file,
        ap.Rectangle(0, 0, 842, 595, True),
    )

    resources_images = page.resources.images
    alt_text = "Alternative text for image"
    x_image = resources_images[1]
    result = x_image.try_set_alternative_text(alt_text, page)

    # If set is successful, then get the alternative text for the image
    if (result):
        print ("Text has been added successfuly")
    document.save(path_outfile)
```
