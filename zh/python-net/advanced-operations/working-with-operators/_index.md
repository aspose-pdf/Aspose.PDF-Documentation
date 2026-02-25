---
title: 使用 Python 进行运算符操作
linktitle: 运算符操作
type: docs
weight: 90
url: /zh/python-net/working-with-operators/
description: 本主题解释了如何在 .NET 环境下使用 Aspose.PDF for Python 的运算符。运算符类为 PDF 操作提供了强大的功能。
lastmod: "2025-05-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 .NET 环境下使用 Aspose.PDF for Python 对 PDF 进行运算符操作
Abstract: 本文深入探讨了 PDF 运算符及其在操作 PDF 内容流中的应用。运算符是 PDF 中的专用关键字，用于指示特定操作，例如在页面上渲染图形元素，仅在内容流内有效。本文详细说明了一种通过直接操作内容流并使用低层图形运算符来精确控制 PDF 中图像放置的方法。该方法适用于需要精确图像定位的任务，如添加水印、对齐叠加层以及创建自定义布局。文中强调了 GSave、ConcatenateMatrix、Do 和 GRestore 等特定运算符在管理图形状态和变换中的作用，确保准确渲染而不影响页面的其他内容。
---

## PDF 运算符及其使用介绍

运算符是 PDF 中指定应执行的某些操作的关键字，例如在页面上绘制图形形状。运算符关键字与已命名对象的区别在于其前面没有斜杠字符 (2Fh)。运算符仅在内容流内部有意义。

内容流是 PDF 流对象，其数据由描述在页面上绘制的图形元素的指令组成。关于 PDF 运算符的更多细节可在[PDF 规范](https://opensource.adobe.com/dc-acrobat-sdk-docs/)中找到。

### 实现细节

此方法通过直接使用低层图形运算符操作内容流，提供对 PDF 中图像放置的细粒度控制。当需要精确的图像定位和变换时，它特别有用，例如：

- 在特定位置添加水印或标志。

- 将图像叠加到现有内容上并实现精确对齐。

- 实现使用高级抽象无法实现的自定义布局。

通过使用 GSave、ConcatenateMatrix、Do 和 GRestore 等运算符，开发者可以确保图像精确渲染且不会对页面其他内容产生意外副作用。

- [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) 运算符保存 PDF 当前的图形状态。
- [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/)（拼接矩阵）运算符用于定义图像在 PDF 页面上的放置方式。
- [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) 运算符在页面上绘制图像。
- [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) 运算符恢复图形状态。

向 PDF 文件中添加图像：

1. 打开 PDF 文档
1. 定义图像放置坐标
1. 访问目标页面
1. 将图像加载到流中
1. 保存当前图形状态
1. 创建矩形和变换矩阵
1. 应用变换矩阵
1. 绘制图像
1. 恢复之前的图形状态
1. 保存修改后的 PDF 文档

以下代码片段展示了如何使用 PDF 运算符：

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## 使用运算符在页面上绘制 XForm

此示例利用 XForm 和图形运算符的强大功能，在 PDF 中高效地复用图形内容。通过将图像封装在 XForm 中，可以多次绘制而无需复制图像数据，从而减小文件大小并提升性能。这种方法在以下情况下尤为有益：

- 同一图像或图形需要在文档中出现多次。

- 需要对图形的放置和变换进行精确控制。

- 优化 PDF 的性能和大小是首要任务。

通过使用 GSave 和 GRestore 管理图形状态，并使用 ConcatenateMatrix 的变换矩阵，此技术确保每个图形都能正确且独立地渲染。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## 使用运算符类移除图形对象

以下代码片段展示了如何移除图形。请注意，如果 PDF 文件中包含图形的文本标签，使用此方法可能会导致这些标签仍然保留在 PDF 中。因此请搜索图形运算符，以寻找删除此类图像的替代方法。

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```


