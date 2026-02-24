---
title: 使用 Python 裁剪 PDF 页面
linktitle: 裁剪 PDF 页面
type: docs
weight: 70
url: /zh/python-net/crop-pages/
description: 您可以使用 Aspose.PDF for Python via .NET 更改页面属性，例如宽度、高度、出血框、裁剪框和修整框。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 访问和修改 PDF 的页面属性
Abstract: 本文概述了如何使用 Aspose.PDF for Python 访问和修改 PDF 文档的页面属性。它描述了多个页面属性，包括媒体框、出血框、修整框、艺术框和裁剪框，解释了它们在定义 PDF 页面打印和显示尺寸与边界方面的作用。媒体框代表最大的页面尺寸，而出血框确保在裁剪时墨水覆盖页面边缘以外的区域。修整框标记裁剪后最终文档的尺寸，艺术框包围实际的页面内容。裁剪框定义了 Adobe Acrobat 中可见的区域。文章包括一个 Python 代码示例，演示如何为 PDF 文档的特定页面设置新的裁剪框以及其他框。视觉示例展示了应用裁剪前后页面的外观，展示了修改这些属性的实际应用。
---

## 获取页面属性

PDF 文件中的每一页都有多个属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF for Python 允许您访问这些属性。

- **media_box**: 媒体框是最大的页面框。它对应于文档打印为 PostScript 或 PDF 时选择的页面尺寸（例如 A4、A5、美国信纸等）。换句话说，媒体框决定了 PDF 文档显示或打印时所使用介质的实际尺寸。
- **bleed_box**: 如果文档有出血，PDF 也会有出血框。出血是指颜色（或艺术作品）延伸到页面边缘之外的量。它用于确保在文档打印并裁剪（"trimmed"）时，墨水能够覆盖到页面的边缘。即使页面裁剪不准确——稍微偏离修整标记切割——页面上也不会出现白边。
- **trim_box**: 修整框指示文档在打印和裁剪后的最终尺寸。
- **art_box**: 艺术框是围绕文档页面实际内容绘制的框。在将 PDF 文档导入其他应用程序时会使用此页面框。
- **crop_box**: 裁剪框是 Adobe Acrobat 中显示 PDF 文档的“页面”尺寸。在普通视图中，Adobe Acrobat 只显示裁剪框内的内容。有关这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页面边界。

使用 Aspose.PDF for Python 将 PDF 的第一页 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 裁剪到特定的矩形区域。该函数会调整多个页面框——`crop_box`、`trim_box`、`art_box` 和 `bleed_box`——以确保视觉效果一致。裁剪可用于去除不需要的边距或聚焦于页面的特定区域。

1. 将 PDF 加载为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)（使用 `ap.Document()`）。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 定义裁剪矩形，并给出所需的坐标（单位为点）。
1. 将 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 的 `crop_box`、`trim_box`、`art_box` 和 `bleed_box` 设置为定义好的矩形。
1. 将修改后的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存为新的输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to a specified rectangular area.
    This function loads a PDF document, defines a new rectangular boundary,
    and applies this boundary to multiple box types (crop, trim, art, and bleed)
    of the first page. The modified document is then saved to a new file.
    Args:
        input_file_name (str): Path to the input PDF file to be cropped.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Note:
        The cropping rectangle is set to coordinates (200, 220, 2170, 1520)
        which defines the visible area of the page. All box types are set
        to the same dimensions to ensure consistent cropping behavior.
    """
    document = ap.Document(input_file_name)

    new_box = ap.Rectangle(200, 220, 2170, 1520, True)
    document.pages[1].crop_box = new_box
    document.pages[1].trim_box = new_box
    document.pages[1].art_box = new_box
    document.pages[1].bleed_box = new_box

    document.save(output_file_name)
```

在此示例中，我们使用了一个示例文件 [这里](crop_page.pdf)。最初我们的页面如图 1 所示。
![图 1. 裁剪页面](crop_page.png)

更改后，页面将显示为图 2。
![图 2. 裁剪页面](crop_page2.png)

## 基于首图内容裁剪 PDF 页面

动态地根据页面上找到的第一张图像的边界裁剪第一页 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/)。通过使用 [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/)，脚本识别第一张图像并将页面的 `crop_box` 调整为匹配该图像的尺寸。当您想关注特定的视觉内容而非预定义坐标时，这种方法非常有用。

1. 将 PDF 加载为 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)。
1. 使用 [`ImagePlacementAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf/imageplacementabsorber/) 在第一页定位图像。
1. 检查是否存在图像：
- 如果找到， 将 [`Page`](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 的 `crop_box` 设置为匹配第一张图像的 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/)。
- 如果没有，则保持页面不变并通知用户。
1. 将修改后的 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 保存到指定的输出文件。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def crop_page_by_content(input_file_name, output_file_name):
    """
    Crops the first page of a PDF document to the bounds of the first image found on that page.
    This function opens a PDF document, locates the first image on the first page,
    and sets the page's crop box to match the image's rectangle dimensions. If no
    images are found, the page remains unchanged.
    Args:
        input_file_name (str): Path to the input PDF file to be processed.
        output_file_name (str): Path where the cropped PDF will be saved.
    Returns:
        None
    Raises:
        Exception: May raise exceptions related to file I/O operations or PDF processing
                  if the input file is invalid, corrupted, or inaccessible.
    Note:
        - Only processes the first page of the document
        - Uses the first image found on the page for cropping dimensions
        - If no images are found, prints a message and saves the document unchanged
        - Requires the aspose.pdf library (imported as 'ap')
    """
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
