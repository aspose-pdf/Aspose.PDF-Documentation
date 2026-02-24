---
title: 使用 Python 进行矢量图形处理
linktitle: 矢量图形处理
type: docs
weight: 100
url: /zh/python-net/working-with-vector-graphics/
description: 本文描述了使用 Python 操作 GraphicsAbsorber 工具的功能。
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: 在 PDF 中使用 Python 的 GraphicsAbsorber 工具
Abstract: Aspose.PDF for Python via .NET 文档中的《使用矢量图形》文章提供了一个全面指南，帮助开发者使用 GraphicsAbsorber 类在 PDF 文档中操作矢量图形。该类支持在 PDF 页面之间提取、移动、删除和复制矢量图形元素。
---

在本章节中，我们将探讨如何使用强大的 `GraphicsAbsorber` 类与 PDF 文档中的矢量图形交互。无论是移动、删除还是添加图形，本指南都将展示如何有效完成这些任务。

## 介绍

矢量图形是许多 PDF 文档的重要组成部分，用于表示图像、形状和其他图形元素。Aspose.PDF 提供了 `GraphicsAbsorber` 类，允许开发者以编程方式访问和操作这些图形。通过使用 `GraphicsAbsorber` 的 `Visit` 方法，您可以从指定页面提取矢量图形并执行各种操作，例如移动、删除或复制到其他页面。

## 提取图形

处理矢量图形的第一步是从 PDF 文档中提取它们。以下是使用 `GraphicsAbsorber` 类的操作方法：

1. 打开 PDF 文档。
1. 初始化 GraphicsAbsorber。
1. 选择目标页面。
1. 从页面中提取图形。
1. 遍历并显示提取的元素。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

GraphicsAbsorber 类位于 aspose.pdf.vector 命名空间，专门用于与 PDF 文档中的矢量图形交互。

## 移动图形

提取图形后，您可以将它们移动到同一页面的其他位置。以下是实现方法：

1. 打开 PDF 文档。
1. 初始化 GraphicsAbsorber。
1. 选择目标页面。
1. 提取图形元素。
1. 暂停更新以提升性能。
1. 修改图形元素位置。
1. 恢复更新并应用更改。
1. 保存更新后的文档。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## 删除图形

在某些情况下，您可能需要从页面中删除特定图形。Aspose.PDF for Python 提供了两种方法来实现此操作：

### 方法 1：使用矩形边界

以下示例演示了如何使用 Aspose.PDF for Python via .NET 库删除位于 PDF 文档首页特定矩形区域内的矢量图形元素。此过程包括识别矩形内的图形元素并将其删除，以清理或修改 PDF 内容。

1. 打开 PDF 文档。
1. 初始化 GraphicsAbsorber。
1. 选择目标页面。
1. 提取图形元素。
1. 定义目标矩形。
1. 暂停更新以提升性能。
1. 删除矩形内的图形元素。
1. 恢复更新并应用更改。
1. 保存更新后的文档。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### 方法 2：使用已删除元素的集合

以下示例演示了如何使用 Aspose.PDF for Python via .NET 库删除位于 PDF 文档首页特定矩形区域内的矢量图形元素。此过程包括识别矩形内的图形元素并将其删除，以清理或修改 PDF 内容。

1. 打开 PDF 文档。
1. 初始化 GraphicsAbsorber。
1. 选择目标页面。
1. 定义目标矩形。
1. 提取图形元素。
1. 创建用于删除的集合。
1. 确认矩形内的元素。
1. 为提升性能暂停更新。
1. 删除图形元素。
1. 恢复更新并应用更改。
1. 保存更新后的文档。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## 将图形添加到另一页

从一页吸收的图形可以添加到同一文档的另一页。
以下是实现此目标的两种方法：

### 方法一：单独添加图形

下面的示例演示如何将 PDF 文档第一页的矢量图形元素复制并粘贴到第二页。此操作由 GraphicsAbsorber 类完成，该类可在 PDF 文档中提取和操作矢量图形。

1. 打开 PDF 文档。
1. 初始化 GraphicsAbsorber。
1. 选择目标页面。
1. 从第一页提取图形元素。
1. 为提升性能暂停第二页的更新。
1. 将提取的图形元素添加到第二页。
1. 恢复更新并应用更改。
1. 保存更新后的文档。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### 方法二：将图形作为集合添加

下面的示例演示如何复制 PDF 文档第一页的矢量图形元素并放置到第二页。此操作通过使用 GraphicsAbsorber 类实现，该类可在 PDF 文档中提取和操作矢量图形。

1. 打开 PDF 文档。
1. 初始化 GraphicsAbsorber。
1. 选择目标页面。
1. 从第一页提取图形元素。
1. 为提升性能暂停第二页的更新。
1. 将提取的图形元素添加到第二页。
1. 恢复更新并应用更改。
1. 保存更新后的文档。

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
