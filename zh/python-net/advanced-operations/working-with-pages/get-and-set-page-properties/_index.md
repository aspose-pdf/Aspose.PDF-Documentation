---
title: 在 Python 中获取和设置 PDF 页面属性
linktitle: 获取和设置页面属性
type: docs
weight: 90
url: /zh/python-net/get-and-set-page-properties/
description: 学习如何在 Python 中检查和更新 PDF 页面属性，如尺寸、页数和颜色信息。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 获取和设置页面属性的方法
Abstract: 本文讨论了 Aspose.PDF for Python via .NET 的功能，重点是使用 Python 读取和设置 PDF 文件的页面属性。文章涵盖了多种功能，包括确定 PDF 的页数、访问和修改页面属性以及处理颜色信息。要获取页数，使用 `Document` 类和 `PageCollection` 集合，并提供代码片段演示如何检索页数，即使不保存文档。文章解释了不同的页面属性，如 MediaBox、BleedBox、TrimBox、ArtBox 和 CropBox，并提供了访问这些属性的代码示例。此外，还介绍了从 PDF 中获取特定页面并将其另存为单独文档，以及确定每页的颜色类型。全文示例均使用 Python 实现，展示了这些功能的实际应用。
---

Aspose.PDF for Python via .NET 让您在 Python 应用程序中读取和设置 PDF 文件中页面的属性。本节展示如何获取 PDF 文件的页数，获取 PDF 页面属性（例如颜色）信息并设置页面属性。示例使用 the [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 和 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) APIs 并使用 Python 编写。

当您需要检查页面元数据、确定页面计数或更新页面级特征，以进行文档分析或标准化任务时，请使用本指南。

## 获取 PDF 文件的页数

在处理文档时，您通常想知道它们包含多少页。使用 Aspose.PDF，这只需不到两行代码。

获取 PDF 文件页数的方法如下：

1. 使用以下方式打开 PDF 文件 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类。
1. 然后使用 [页面集合](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合的 Count 属性（来自 Document 对象）来获取文档的总页数。

以下代码片段展示了如何获取 PDF 文件的页数。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count(input_file_name):
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### 获取页面计数而不保存文档

有时我们实时生成 PDF 文件，在 PDF 文件创建过程中，可能会遇到需求（例如创建目录等）需要在不将文件保存到系统或流中的情况下获取 PDF 文件的页面计数。为满足此需求，在 Document 类中引入了一个方法 [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 已在 Document 类中引入。请查看以下代码片段，展示了在不保存文档的情况下获取页面计数的步骤。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_count_without_saving(input_file_name):
    # Instantiate Document instance
    document = ap.Document()
    # Add page to pages collection of PDF file
    page = document.pages.add()
    # Create loop instance
    for _ in range(0, 300):
        # Add TextFragment to paragraphs collection of page object
        page.paragraphs.add(ap.text.TextFragment("Pages count test"))
    # Process the paragraphs in PDF file to get accurate page count
    document.process_paragraphs()
    # Print number of pages in document
    print("Number of pages in document =", str(len(document.pages)))
```

## 获取页面属性

PDF 文件中的每一页都有多个属性，例如宽度、高度、bleed-、crop- 和 trimbox。Aspose.PDF 允许您访问这些属性。

### 了解页面属性：Artbox、BleedBox、CropBox、MediaBox、TrimBox 和 Rect 属性之间的区别

- **Media box**: 媒体框是最大的页面框。它对应于文档在打印为 PostScript 或 PDF 时所选的页面尺寸（例如 A4、A5、US Letter 等）。换句话说，媒体框决定了显示或打印 PDF 文档的介质的实际尺寸。
- **Bleed box**: 如果文档有出血，PDF 也会有出血框。出血是指超出页面边缘的颜色（或艺术作品）的量。它用于确保在文档打印并裁剪到尺寸（“trimmed”）时，墨水能够一直覆盖到页面的边缘。即使页面裁剪不准确——稍微偏离裁切标记——也不会在页面出现白边。
- **Trim box**: 裁剪框表示文档打印并裁切后最终的尺寸。
- **Art box**: 艺术框是围绕文档页面实际内容绘制的框。该页面框在将 PDF 文档导入其他应用程序时使用。
- **Crop box**：Crop box 是在 Adobe Acrobat 中显示 PDF 文档时的“页面”尺寸。在普通视图中，只有 Crop box 的内容会在 Adobe Acrobat 中显示。
  有关这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 Page Boundaries。
-- **Page.Rect**：MediaBox 和 DropBox 的交集（通常可见的矩形）(`Page.rect`）。 查看 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 矩形属性的类型。下图说明了这些属性。

如需进一步了解，请访问 [此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### 访问页面属性

这 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类提供与特定 PDF 页面相关的所有属性。PDF 文件的所有页面都包含在的 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [页面集合](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合。

从那里，可以访问单个 `Page` 使用索引访问对象，或遍历集合以获取所有页面。访问单个页面后，我们可以获取其属性。以下代码片段展示了如何获取页面属性（ `Page` API).

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_properties(input_file_name):
    # Open document
    document = ap.Document(input_file_name)
    # Get particular page
    page = document.pages[1]

    # Get page properties
    boxes = {
        "ArtBox": page.art_box,
        "BleedBox": page.bleed_box,
        "CropBox": page.crop_box,
        "MediaBox": page.media_box,
        "TrimBox": page.trim_box,
        "Rect": page.rect,
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(
            f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}"
        )

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## 确定页面颜色

这 [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类提供与 PDF 文档中特定页面相关的属性，包括页面使用的颜色类型——RGB、黑白、灰度或未定义。

所有 PDF 文件的页面都包含在 [页面集合](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合。The [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property 指定页面上元素的颜色。要获取或确定特定 PDF 页面 的颜色信息，请使用 the [页面](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象的 [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) property.

以下代码片段展示了如何遍历 PDF 文件的各个页面以获取颜色信息。

```python
import sys
import aspose.pdf as ap
from os import path

def get_page_color_type(input_file_name):
    # Open source PDF file
    document = ap.Document(input_file_name)
    # Iterate through all the page of PDF file
    for page_number in range(1, len(document.pages) + 1):
        # Get the color type information for particular PDF page
        page_color_type = document.pages[page_number].color_type
        color_type_map = {
            ap.ColorType.BLACK_AND_WHITE: "Black and white",
            ap.ColorType.GRAYSCALE: "Gray Scale",
            ap.ColorType.RGB: "RGB",
            ap.ColorType.UNDEFINED: "undefined",
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```

## 相关页面主题

- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在 Python 中更改 PDF 页面大小](/pdf/zh/python-net/change-page-size/)
- [在 Python 中裁剪 PDF 页面](/pdf/zh/python-net/crop-pages/)
- [在 Python 中旋转 PDF 页面](/pdf/zh/python-net/rotate-pages/)