---
title: 使用 Python 处理 PDF 图层
linktitle: 处理 PDF 图层
type: docs
weight: 50
url: /zh/python-net/working-with-pdf-layers/
description: 接下来的任务解释如何锁定 PDF 图层、提取 PDF 图层元素、扁平化分层 PDF，以及将 PDF 中的所有图层合并为一个。
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 操作 PDF 图层
Abstract: 本指南提供了使用 Aspose.PDF for Python via .NET 库管理和操作 PDF 图层的全面概述。PDF 图层——也称为可选内容组 (OCG)——使内容能够组织成可在支持图层的查看器中打开或关闭的独立视觉组件。
---

PDF 图层是一种强大的方式，可在单个 PDF 文件中灵活组织和呈现内容，使用户能够根据需求显示或隐藏不同的部分。

使用 **Aspose.PDF for Python via .NET**，您可以：

- 锁定/解锁图层以控制可见性。
- 将图层提取为独立的文件或流。
- 扁平化图层，使其永久化。
- 将图层合并为单一统一的图层。

## 向 PDF 添加图层

本示例展示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中创建并添加多个图层。每个图层包含独立的图形内容，例如彩色线条，可在支持图层的 PDF 查看器中打开或关闭。

1. 创建一个新的 PDF 文档并添加一页。
1. 创建并添加红色图层。
1. 创建并添加绿色图层。
1. 创建并添加蓝色图层。
1. 保存 PDF 文档。

生成的 PDF 将包含三个独立的图层：红线、绿线和蓝线。每个图层都可以在支持分层内容的 PDF 阅读器中打开或关闭。

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## 锁定 PDF 图层

使用 Aspose.PDF for Python via .NET，您可以打开 PDF，在首页锁定特定图层，并保存带有更改的文档。

本示例展示了如何使用 Aspose.PDF for Python via .NET 在 PDF 文档中锁定图层（可选内容组，OCG）。锁定可防止用户在 PDF 查看器中更改该图层的可见性，确保内容始终按照文档定义保持可见（或隐藏）。

可用的方法和属性：

- layer.lock() – 锁定图层。
- layer.unlock() – 解锁图层。
- layer.locked – 返回当前锁定状态。

1. 打开 PDF 文档。
1. 访问 PDF 的首页。
1. 检查该页面是否有图层。
1. 获取第一个图层并锁定。
1. 保存更新后的 PDF。

如果 PDF 包含图层，首个图层将被锁定，确保其可见状态不能被用户更改。如果未找到图层，则会打印相应信息。

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## 提取 PDF 图层元素

本示例使用 Aspose.PDF for Python via .NET 库从 PDF 文档的首页提取各个图层，并将每个图层保存为单独的 PDF 文件。

要从图层创建新的 PDF，可使用以下代码片段：

1. 加载 PDF 文档。将输入的 PDF 加载到 Aspose.PDF.Document 对象中。
1. 访问第 1 页的图层。脚本使用 document.pages[1].layers 检索首页的所有图层。
1. 检查是否有图层。如果未找到图层，则打印信息并退出函数。
1. 遍历并保存每个图层。

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

可以提取 PDF 图层元素并将其保存到新的 PDF 文件流中：

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## 扁平化分层 PDF

此脚本使用 Aspose.PDF for Python via .NET 将 PDF 文档首页的所有图层扁平化。扁平化将每个图层的可视内容合并为一个统一的图层，使打印、共享或归档更为便利且不会失去视觉保真度或图层特定数据。

1. 加载 PDF 文档。输入的 PDF 被加载到 Aspose.PDF.Document 对象中。
1. 访问第 1 页的图层。脚本使用 document.pages[1].layers 获取第一页的所有图层。
1. 检查图层是否存在。如果未找到图层，打印消息并退出函数。
1. 扁平化每个图层。使用 layer.flatten(True) 扁平化每个图层，将其内容合并到页面中。
1. 保存修改后的文档。

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## 将 PDF 中的所有图层合并为一个

此代码片段使用 Aspose.PDF 将 PDF 首页的所有图层合并为一个具有自定义名称的统一图层。

1. 加载 PDF 文档。PDF 被加载到 Aspose.PDF.Document 对象中。
1. 访问页面及其图层。选择第一页，并检索其图层。
1. 检查图层。如果不存在图层，打印消息并退出过程。
1. 定义新图层名称。为合并结果指定新的图层名称（"LayerNew"）。
1. 合并图层。如果提供了可选内容组 ID，则在合并时使用它。否则，仅使用新名称合并图层。
1. 保存文档

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
