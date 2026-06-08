---
title: 在 Python 中裁剪 PDF 页面
linktitle: 裁剪 PDF 页面
type: docs
weight: 70
url: /zh/python-net/crop-pages/
description: 了解如何在 Python 中裁剪 PDF 页面并调整裁剪框、修剪框、出血框和媒体框。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 访问和修改 PDF 页面属性
Abstract: 本文概述了如何使用 Aspose.PDF for Python 访问和修改 PDF 文档中的页面属性。它描述了多种页面属性，包括 media box、bleed box、trim box、art box 和 crop box，并解释了它们在定义 PDF 页面用于打印和显示的尺寸和边界方面的作用。media box 表示最大的页面尺寸，而 bleed box 确保在页面边缘之外的墨水覆盖，以便裁剪。trim box 标记裁剪后最终文档的尺寸，art box 包含实际的页面内容。crop box 定义了在 Adobe Acrobat 中可见的区域。文章还包含了一个 Python 代码片段，演示如何为 PDF 文档中的特定页面设置新的 crop box 以及其他盒子。视觉示例展示了应用裁剪前后页面的外观，展示了修改这些属性的实际应用。
---

## 获取页面属性

PDF 文件中的每页都有多个属性，例如宽度、高度、bleed、crop 和 trimbox。Aspose.PDF for Python 允许您访问这些属性。

当您需要缩小可见页面区域、为印刷工作流准备文件或检查 PDF 文档中的页面框几何形状时，请使用此页面。

- **media_box**：媒体框是最大的页面框。它对应于文档打印成 PostScript 或 PDF 时所选的页面尺寸（例如 A4、A5、US Letter 等）。换句话说，媒体框决定了呈现或打印 PDF 文档的介质的物理尺寸。
- **bleed_box**：如果文档有出血，PDF 也会包含出血框。出血是指超出页面边缘的颜色（或艺术作品）的范围。它用于确保在文档打印并裁剪至尺寸（"trimmed"）时，墨水能够延伸至页面的边缘。即使页面裁剪不准确——略微偏离裁剪标记——页面上也不会出现白边。
- **trim_box**：修整框指示文档在打印和裁剪后的最终尺寸。
- **art_box**：艺术框是围绕文档页面实际内容绘制的框。在将 PDF 文档导入其他应用程序时会使用此页面框。
- **crop_box**：裁剪框是 Adobe Acrobat 中显示 PDF 文档的 “页” 大小。在普通视图中，Adobe Acrobat 只显示裁剪框的内容。有关这些属性的详细说明，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页面边界。

裁剪第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 使用 Aspose.PDF for Python 将 PDF 的内容定位到特定的矩形区域。该函数调整多个页面框—`crop_box`, `trim_box`, `art_box`，和 `bleed_box`—以确保视觉效果一致。裁剪对于去除不需要的边距或聚焦于页面的特定区域非常有用。

1. 将 PDF 加载为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) （使用 `ap.Document()`).
1. 使用以下方式定义裁剪矩形 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 使用所需的坐标（单位为点）。
1. 设置 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)的 `crop_box`, `trim_box`, `art_box`，和 `bleed_box` 到定义的矩形。
1. 保存已修改的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 到一个新的输出文件。

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

在此示例中我们使用了一个示例文件 [这里](crop_page.pdf). 最初我们的页面如图 1 所示。
![图 1. 裁剪页面](crop_page.png)

更改后，页面将如图 2 所示。
![图 2. 裁剪页面](crop_page2.png)

## 基于首个图像内容裁剪 PDF 页面

裁剪第一个 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 动态地基于页面上找到的第一个图像的边界。通过使用 [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)，脚本识别第一张图像并调整页面的 `crop_box` 以匹配图像的尺寸。当您想专注于特定的视觉内容而不是预先定义的坐标时，这种方法很有用。

1. 将 PDF 加载为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. 使用以下方法定位第一页上的图像 [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/).
1. 检查是否存在图像：
    - 如果找到，设置 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) `crop_box` 匹配第一张图像的 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/).
    - 如果不是，保持页面不变并通知用户。
1. 保存已修改的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 到指定的输出文件。

```python
import sys
import aspose.pdf as ap
from os import path

def crop_page_by_content(input_file_name, output_file_name):
    document = ap.Document(input_file_name)
    # Find first image on first page using ImagePlacementAbsorber
    absorber = ap.ImagePlacementAbsorber()
    document.pages[1].accept(absorber)

    if len(absorber.image_placements) > 0:
        first_image = absorber.image_placements[1]
        document.pages[1].crop_box = first_image.rectangle
    else:
        print("No images found on the first page")
    document.save(output_file_name)
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中更改 PDF 页面大小](/pdf/zh/python-net/change-page-size/)
- [在 Python 中获取和设置 PDF 页面属性](/pdf/zh/python-net/get-and-set-page-properties/)
- [在 Python 中旋转 PDF 页面](/pdf/zh/python-net/rotate-pages/)