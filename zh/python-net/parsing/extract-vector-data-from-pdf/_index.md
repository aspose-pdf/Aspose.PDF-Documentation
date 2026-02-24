---
title: 使用 Python 从 PDF 文件中提取矢量数据
linktitle: 从 PDF 中提取矢量数据
type: docs
weight: 80
url: /zh/python-net/extract-vector-data-from-pdf/
description: Aspose.PDF 让从 PDF 文件中提取矢量数据变得简单。您可以获取矢量数据（路径、多边形、折线），例如位置、颜色、线宽等。
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## 访问 PDF 文档中的矢量数据

下面的代码片段使用 GraphicsAbsorber 类演示如何从 PDF 文档的特定页面提取矢量图形元素，并检查矩形边界、运算符和位置等属性。

1. 使用 'ap.Document' 加载 PDF 文档。
1. 初始化一个 'GraphicsAbsorber' 实例。
1. 调用 'gr_absorber.visit()' 检查第二页。
1. 通过 'gr_absorber.elements' 获取提取的元素。
1. 遍历每个元素并记录属性——矩形、位置和运算符数量。
1. 将信息写入文本输出文件。
1. 关闭文档以释放资源。

```python

import os
import aspose.pdf as ap

def extract_graphics_elements(infile, outfile):
    """
    Extract vector graphic elements from a specified page of a PDF and log basic element properties.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file for logging element info.
    """
    document = ap.Document(infile)
    try:
        gr_absorber = ap.vector.GraphicsAbsorber()
        # Visit page 2 (pages collection is 1-indexed; document.pages[1] is the second page)
        gr_absorber.visit(document.pages[1])
        
        elements = gr_absorber.elements
        with open(outfile, "w", encoding="utf-8") as f:
            for idx, elem in enumerate(elements, start=1):
                # Basic properties
                rect = elem.rectangle
                pos = elem.position
                ops_count = len(elem.operators)
                f.write(f"Element {idx}: Rectangle = {rect}, Position = {pos}, Operators = {ops_count}\n")
    finally:
        document.close()
```

## 将页面的矢量图形保存为 SVG 文件

将 PDF 页面中的矢量图形导出为 SVG 文件，保留矢量形状和路径：

1. 加载 PDF 文档。
1. 访问目标页面。
1. 调用 'page.try_save_vector_graphics()' 将页面的矢量路径导出为 SVG 文件。
1. 关闭文档。

```python

import os
import aspose.pdf as ap

def save_vector_graphics_to_svg(infile, svg_outfile):
    """
    Save vector graphics from a specified page of a PDF document into an SVG file.
    Args:
        infile (str): Path to input PDF file.
        svg_outfile (str): Path to output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        # Try to save vector graphics into SVG
        page.try_save_vector_graphics(svg_outfile)
    finally:
        document.close()
```

### 将每个子路径提取为单独的 SVG

使用提取选项对象将矢量图形的每个子路径（组件）提取为单独的 SVG 文件。

1. 加载 PDF。
1. 创建 'SvgExtractionOptions' 并设置 'extract_every_subpath_to_svg'。
1. 访问文档的第一页。
1. 使用该选项实例化 'SvgExtractor'。
1. 调用 'extractor.extract()' 为每个矢量子路径输出单独的 SVG 文件。
1. 关闭文档。

```python

import os
import aspose.pdf as ap

def extract_subpaths_to_svgs(infile, output_dir):
    """
    Extract each vector sub-path on a PDF page into separate SVG files using extraction options.
    Args:
        infile (str): Input PDF file path.
        output_dir (str): Directory path where SVG files will be saved.
    """
    document = ap.Document(infile)
    try:
        options = ap.vector.SvgExtractionOptions()
        options.extract_every_subpath_to_svg = True
        
        page = document.pages[1]
        extractor = ap.vector.SvgExtractor(options)
        extractor.extract(page, output_dir)
    finally:
        document.close()
```

### 将元素列表提取为单个图像

使用 Aspose.PDF for Python 从 PDF 页面提取多个矢量元素，并将它们保存为单个合并的 SVG 图像。
当您想要保留分组形状或绘图的视觉结构（如图表或 CAD 导出）时，这非常有用。

1. 使用 'Document' 打开 PDF。
1. 选择页面并准备矢量元素列表。
1. 使用 'SvgExtractor' 将这些元素合并为一个 SVG。
1. 保存输出文件。

```python

import os
import aspose.pdf as ap

def extract_list_of_elements_to_single_image(infile, outfile):
    """
    Extracts multiple vector graphic elements from a PDF page and saves them as a single SVG image.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[1]
        svg_extractor = ap.vector.SvgExtractor()
        elements = []  # Fill this list with specific graphic elements as needed
        svg_extractor.extract(elements, page, outfile)
    finally:
        document.close()
```

### 提取单个元素

从 PDF 中提取特定的单个矢量元素，并将其保存为独立的 SVG 文件。
这对于从复杂的基于矢量的 PDF 中隔离和导出徽标、图标或独立形状非常有帮助。

1. 创建一个 'GraphicsAbsorber' 来捕获矢量数据。
1. 访问特定页面以收集其矢量元素。
1. 选择目标元素（例如 'XFormPlacement'）。
1. 将该单个元素保存为 SVG 文件.

```python

import os
import aspose.pdf as ap

def extract_single_vector_element(infile, outfile):
    """
    Extracts a specific vector graphic element (e.g., an XFormPlacement) from a PDF page and saves it as an SVG file.
    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to the output SVG file.
    """
    document = ap.Document(infile)
    try:
        graphics_absorber = ap.vector.GraphicsAbsorber()
        page = document.pages[1]
        graphics_absorber.visit(page)
        xform_placement = graphics_absorber.elements[1]
        if isinstance(xform_placement, ap.vector.XFormPlacement):
            xform_placement.elements[2].save_to_svg(outfile)
    finally:
        document.close()
```
