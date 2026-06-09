---
title: 使用 Python 处理 PDF 图层
linktitle: 处理 PDF 图层
type: docs
weight: 50
url: /zh/python-net/working-with-pdf-layers/
description: 了解如何在 Python 中添加、锁定、提取、扁平化和合并 PDF 图层。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 管理 PDF 图层。
Abstract: 本文介绍了如何使用 Aspose.PDF for Python via .NET 操作 PDF 图层（可选内容组）。了解如何添加图层、锁定图层可见性、提取图层内容、扁平化图层内容以及将多个图层合并为一个。
---

PDF 层，也称为可选内容组（OCG），允许您将内容组织成可在兼容的 PDF 查看器中显示或隐藏的独立视觉组。在 Aspose.PDF 中，层操作基于 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) API。

使用 Aspose.PDF for Python via .NET，您可以：

- 在页面上添加多个图层。
- 锁定和解锁图层以控制可见性行为。
- 将图层提取为单独的文件或流。
- 将分层内容展平到页面。
- 将多个图层合并为一个图层。

## 向 PDF 添加图层

此示例创建一个具有三个图层的 PDF。它使用一个 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)，添加 一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)，并追加 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 对象到该页面。

1. 创建一个新 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 并添加一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 创建并添加红色图层。
1. 创建并添加绿色图层。
1. 创建并添加蓝色层。
1. 保存 PDF 文档。

生成的 PDF 将包含三个独立的图层：一条红线、一条绿线和一条蓝线。每个图层都可以在支持分层内容的 PDF 阅读器中打开或关闭。

```python
import aspose.pdf as ap

def add_layers(outfile: str) -> None:
    document = ap.Document()
    page = document.pages.add()

    # Red layer
    layer = ap.Layer("oc1", "Red Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(1, 0, 0))
    layer.contents.append(ap.operators.MoveTo(500, 700))
    layer.contents.append(ap.operators.LineTo(400, 700))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Green layer
    layer = ap.Layer("oc2", "Green Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 1, 0))
    layer.contents.append(ap.operators.MoveTo(500, 750))
    layer.contents.append(ap.operators.LineTo(400, 750))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    # Blue layer
    layer = ap.Layer("oc3", "Blue Line")
    layer.contents.append(ap.operators.SetRGBColorStroke(0, 0, 1))
    layer.contents.append(ap.operators.MoveTo(500, 800))
    layer.contents.append(ap.operators.LineTo(400, 800))
    layer.contents.append(ap.operators.Stroke())
    page.layers.append(layer)

    document.save(outfile)
    print(f"Layers added successfully. File saved at {outfile}")
```

## 锁定 PDF 图层

此示例打开一个 PDF，在第一页锁定特定图层，并保存更新后的文件。

锁定图层可防止用户在支持的 PDF 查看器中更改该图层的可见性状态。图层从页面访问，并通过页面的图层集合进行管理。

可用的方法和属性：

- [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) 锁定该图层。
- [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) 解锁该层。
- [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties) 返回当前锁定状态。

1. 打开 PDF 文档。
1. 访问 PDF 的第一页。
1. 检查页面是否有图层。
1. 获取第一层并锁定它。
1. 保存更新后的 PDF。

如果 PDF 包含图层，第一层将被锁定，确保用户无法更改其可见性状态。如果未找到图层，则会打印一条消息。

```python
import aspose.pdf as ap

def lock_layer(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) > 0:
        layer = page.layers[0]
        layer.lock()
        document.save(outfile)
        print(f"Layer locked successfully. File saved at {outfile}")
    else:
        print("No layers found in the document.")
```

## 提取 PDF 图层元素

本示例使用 Aspose.PDF for Python via .NET 库，从 PDF 文档的首页提取各个图层，并通过使用将每个图层保存为单独的 PDF 文件 [`Layer.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

要从图层创建新的 PDF，您可以使用以下代码片段：

1. 加载 PDF [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 访问第1页的图层 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. 检查是否存在图层。
1. 遍历图层并保存每个图层。

```python
import aspose.pdf as ap

def extract_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    index = 1
    for layer in layers:
        output_file = outfile.replace(".pdf", f"{index}.pdf")
        layer.save(output_file)
        print(f"Layer {index} saved to {output_file}")
        index += 1
```

可以提取 PDF 图层元素并将其保存到新的 PDF 文件流中：

```python
from io import FileIO
import aspose.pdf as ap

def extract_layers_stream(infile: str, outfile: str) -> None:
    document = ap.Document(infile)

    if len(document.pages[1].layers) == 0:
        print("No layers found in the document.")
        return

    layer = document.pages[1].layers[0]

    with FileIO(outfile, "wb") as output_layer:
        layer.save(output_layer)
    print(f"Layer extracted to stream: {outfile}")
```

## 扁平化分层 PDF

此脚本使用 Aspose.PDF for Python via .NET 将 PDF 文档的首页的所有图层进行扁平化。扁平化将每个图层的可视内容合并为一个统一的图层，使得打印、共享或归档更为简便，同时不失去视觉保真度或图层特定的数据。该操作使用 [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods).

1. 加载 PDF 文档。
1. 访问第1页的图层。
1. 检查是否存在图层。
1. 使用以下方式扁平化每个图层 `layer.flatten(True)`.
1. 保存修改后的文档。

```python
import aspose.pdf as ap

def flatten_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    layers = document.pages[1].layers

    if len(layers) == 0:
        print("No layers found in the document.")
        return

    for layer in layers:
        layer.flatten(True)

    document.save(outfile)
    print(f"Layers flattened successfully. File saved at {outfile}")
```

## 将PDF中的所有图层合并为一个

此代码片段使用 Aspose.PDF 将 PDF 第一页的所有图层合并为一个具有自定义名称的统一图层，方法是使用 [`Page.merge_layers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods).

1. 加载 PDF 文档。
1. 访问第1页并检索其图层。
1. 检查是否存在图层。
1. 定义一个新图层名称。
1. 将图层合并为一个。
1. 保存文档。

```python
import aspose.pdf as ap

def merge_layers(infile: str, outfile: str) -> None:
    document = ap.Document(infile)
    page = document.pages[1]

    if len(page.layers) == 0:
        print("No layers found in the document.")
        return

    new_layer_name = "LayerNew"
    page.merge_layers(new_layer_name)
    document.save(outfile)
    print(f"Layers merged successfully. File saved at {outfile}")
```

## 相关图层主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [使用 Python 在 PDF 中处理表格](/pdf/zh/python-net/working-with-tables/)
- [在 Python 中添加 PDF 页面](/pdf/zh/python-net/add-pages/)
