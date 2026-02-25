---
title: 使用 Python 处理 PDF 图层
linktitle: 处理 PDF 图层
type: docs
weight: 50
url: /zh/python-net/work-with-pdf-layers/
description: 本文解释了如何锁定 PDF 图层、提取 PDF 图层元素、扁平化分层 PDF，以及将 PDF 中的所有图层合并为一个。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何在 Python 中管理、锁定、提取、扁平化和合并 PDF 图层
Abstract: 本文解释了如何使用 Aspose.PDF for .NET 在 Python 中处理 PDF 图层，包括锁定图层、提取图层元素、扁平化分层 PDF 和合并图层。
---

PDF 图层允许文档包含多个内容集合，可根据需要选择性显示或隐藏。每个图层可能包含文本、图像或图形，用户可以根据需要打开或关闭它们。图层在内容需要组织或分隔的复杂文档中尤其有用。下面的示例使用 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 和 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) API，并通过页面的 `layers` 集合操作 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 对象。

## 锁定 PDF 图层

使用 Aspose.PDF for Python via .NET，您可以打开 PDF（参见 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)），在第一页上锁定特定的 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)，并保存对文档所做的更改。

可用于 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 对象的方法和属性：

- `layer.lock()` – 锁定图层。（参见 [`Layer.lock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods)）
- `layer.unlock()` – 解锁图层。（参见 [`Layer.unlock()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods)）
- `layer.locked` – 返回当前的锁定状态。（参见 [`Layer.locked`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#properties)）

1. 打开 PDF 文档（参见 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)）。
1. 使用文档的 [`Pages`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) 集合获取第一页（参见 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)）。
1. 从 `page.layers` 中选择要锁定的 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)。
1. 调用 `layer.lock()` 以阻止用户切换图层的可见性。
1. 使用 [`Document.save()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 保存更新后的文档。

```python

import aspose.pdf as ap

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

Aspose.PDF 允许您从 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 中提取每个 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 并将其保存为单独的 PDF 文件。

要从图层创建新的 PDF，可使用以下代码片段（`layers` 集合通过 `Page.layers` 访问）：

```python

import aspose.pdf as ap

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF with a unique filename
        for i, layer in enumerate(layers):
            layer.save(f"{path_outfile}_layer_{i}.pdf")
```

您还可以将图层保存到流中：

```python

import aspose.pdf as ap
import io

def save_layers_to_stream(path_infile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        streams = []
        for layer in layers:
            layer_stream = io.BytesIO()
            layer.save(layer_stream)
            layer_stream.seek(0)
            streams.append(layer_stream)
        return streams
```

## 扁平化分层 PDF

扁平化会使页面上的 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/) 永久化，去除其切换功能。

```python

import aspose.pdf as ap

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

`cleanup_content_stream` 参数控制是否移除可选内容组标记（OCG 标记）。将其设置为 `False` 可以加快扁平化过程。详情请参见 [`Layer.flatten()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/#methods) 方法。

## 将 PDF 中的所有图层合并为一个

您可以将所有图层（或特定图层）合并为一个新的 [`Layer`](https://reference.aspose.com/pdf/python-net/aspose.pdf/layer/)（合并 API 位于 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象上）。

`Page` 对象的方法：

- `page.merge_layers(new_layer_name)` — 将所有图层合并为新的图层名称（参见 [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)）。
- `page.merge_layers(new_layer_name, new_optional_content_group_id)` — 使用自定义可选内容组 ID 进行合并（参见 [`Page.MergeLayers()`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods)）。

```python

import aspose.pdf as ap

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
