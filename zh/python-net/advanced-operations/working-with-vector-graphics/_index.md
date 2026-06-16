---
title: 在 Python 中使用矢量图形
linktitle: 使用矢量图形
type: docs
weight: 100
url: /zh/python-net/working-with-vector-graphics/
description: 学习如何使用 Python 中的 GraphicsAbsorber 在 PDF 页面之间提取、移动、删除和复制矢量图形。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用 GraphicsAbsorber 检查和操作 PDF 矢量图形。
Abstract: 本文解释了如何在 Aspose.PDF for Python via .NET 中使用 GraphicsAbsorber 类处理矢量图形。了解如何从 PDF 页面中提取矢量元素，移动或删除它们，以及在 Python 工作流中以低层控制在页面之间复制图形。
---

[Aspose.PDF for Python via .NET](/pdf/zh/python-net/) 提供 [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) 用于访问和操作已存在于 PDF 页面中的矢量图形的类。调用它的 `visit` 在任何页面上使用方法提取路径、形状和其他图形操作符，然后根据需要移动、删除或复制这些元素。

当您需要检查或修改嵌入在现有 PDF 中的矢量绘图元素，而不是从零开始绘制新形状时，请使用此页面。

## 提取图形

提取是所有矢量图形任务的起点。 `GraphicsAbsorber` 读取页面的内容流，并公开每个图形元素及其页面引用、位置和原始操作符。

1. 打开 PDF 文档。
1. 创建一个 [GraphicsAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicsabsorber/) 实例。
1. 调用 `visit` 在目标页面上填充 `elements`.
1. 遍历 `elements` 检查位置和运算符计数。

```python
import aspose.pdf as ap
import sys
from os import path

def using_graphics_absorber(infile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

`GraphicsAbsorber` 是...的一部分 `aspose.pdf.vector` 命名空间，专门用于与 PDF 内容流中的矢量图形交互。

## 动态图形

提取后，设置一个新的 `position` 对每个元素进行操作以将其重新定位到同一页面。将更新包装在 `suppress_update` / `resume_update` 调用将内容流写入批处理为单个操作，并避免冗余的重新绘制。

1. 打开 PDF 文档。
1. 创建一个 `GraphicsAbsorber` 并调用 `visit` 在目标页面上。
1. 调用 `suppress_update` 暂停内容流写入。
1. 更新 `position` 每个元素的
1. 调用 `resume_update` 一次性提交所有更改。
1. 保存修改后的文档。

```python
import aspose.pdf as ap
import sys
from os import path

def move_graphics(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                position = element.position
                element.position = ap.Point(position.x + 150, position.y - 10)
            graphics_absorber.resume_update()
        document.save(outfile)
```

## 删除图形

要从页面中删除特定的矢量元素，请按位置或边界矩形过滤，然后将其删除。Aspose.PDF for Python 提供了两种方法，取决于您是想内联删除元素还是先收集它们。

### 方法1：使用矩形边界删除内联

此方法检查每个元素相对于矩形的位置并调用 `element.remove()` 直接在循环内部使用。当你想要简洁的代码且不需要在之后检查已删除的集合时使用它。

1. 打开 PDF 文档。
1. 创建一个 `GraphicsAbsorber` 并调用 `visit` 在目标页面上。
1. 定义目标 [矩形](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
1. 调用 `suppress_update` 暂停内容流写入。
1. 迭代 `elements`，调用 `remove()` 对每个位置位于矩形内的元素。
1. 调用 `resume_update` 提交删除。
1. 保存修改后的文档。

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            graphics_absorber.visit(page)
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.suppress_update()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    element.remove()
            graphics_absorber.resume_update()
        document.save(outfile)
```

### 方法二：先收集元素，然后删除

此方法将匹配的元素收集到一个 [图形元素集合](https://reference.aspose.com/pdf/python-net/aspose.pdf.vector/graphicelementcollection/) 并将集合传递给 `page.delete_graphics`. 在提交删除之前，如果您需要审查或记录将要删除的内容，请使用它。

1. 打开 PDF 文档。
1. 创建一个 `GraphicsAbsorber` 并调用 `visit` 在目标页面上。
1. 定义目标矩形。
1. 迭代 `elements` 并将匹配的元素添加到 a `GraphicElementCollection`.
1. 调用 `page.contents.suppress_update` 暂停内容流写入。
1. 调用 `page.delete_graphics` 与集合一起。
1. 调用 `page.contents.resume_update` 提交删除。
1. 保存修改后的文档。

```python
import aspose.pdf as ap
import sys
from os import path

def remove_graphics_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page = document.pages[1]
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            graphics_absorber.visit(page)
            removed_elements_collection = ap.vector.GraphicElementCollection()
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position, False):
                    removed_elements_collection.add(element)
            page.contents.suppress_update()
            page.delete_graphics(removed_elements_collection)
            page.contents.resume_update()
        document.save(outfile)
```

## 在另一页上添加图形

从一个页面提取的矢量元素可以放置在同一文档的任何其他页面上。有两种方法可用：逐个添加元素，或在一次调用中传递整个集合。

### 方法 1：逐个添加元素

当您需要对每个元素进行控制时，例如在将它们放置到目标页面之前对单个元素进行过滤或转换，请使用此方法。

1. 打开 PDF 文档。
1. 创建一个 `GraphicsAbsorber` 并调用 `visit` 在源页面上。
1. 向文档添加一个新的目标页面。
1. 调用 `page_2.contents.suppress_update` 暂停内容流写入。
1. 调用 `element.add_on_page(page_2)` 对每个元素。
1. 调用 `page_2.contents.resume_update` 提交所有添加。
1. 保存修改后的文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_1(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            for element in graphics_absorber.elements:
                element.add_on_page(page_2)
            page_2.contents.resume_update()
        document.save(outfile)
```

### 方法 2：一次性添加整个集合

当您想一次性将所有提取的元素复制到页面，而无需手动遍历时，请使用此方法。

1. 打开 PDF 文档。
1. 创建一个 `GraphicsAbsorber` 并调用 `visit` 在源页面上。
1. 向文档添加一个新的目标页面。
1. 调用 `page_2.contents.suppress_update` 暂停内容流写入。
1. 调用 `page_2.add_graphics` 完整的 `elements` 集合。
1. 调用 `page_2.contents.resume_update` 提交所有添加。
1. 保存修改后的文档。

```python
import aspose.pdf as ap
import sys
from os import path

def add_to_another_page_method_2(infile: str, outfile: str):
    with ap.Document(infile) as document:
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            page_1 = document.pages[1]
            page_2 = document.pages.add()
            graphics_absorber.visit(page_1)
            page_2.contents.suppress_update()
            page_2.add_graphics(graphics_absorber.elements, None)
            page_2.contents.resume_update()
        document.save(outfile)
```

## 相关主题

- [Python中的高级PDF操作](/pdf/zh/python-net/advanced-operations/)
- [在 Python 中使用 PDF 图形](/pdf/zh/python-net/working-with-graphs/)
- [在 Python 中使用 PDF 操作符](/pdf/zh/python-net/working-with-operators/)
- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
