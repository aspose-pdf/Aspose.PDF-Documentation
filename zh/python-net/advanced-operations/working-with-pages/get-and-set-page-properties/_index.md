---
title: 使用 Python 获取和设置页面属性
linktitle: 获取和设置页面属性
type: docs
weight: 90
url: /zh/python-net/get-and-set-page-properties/
description: 本节展示了如何获取 PDF 文件的页数，获取 PDF 页面属性（如颜色）信息以及设置页面属性。
lastmod: "2025-11-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 如何使用 Python 获取和设置页面属性
Abstract: 本文讨论了 Aspose.PDF for Python via .NET 的功能，重点在于使用 Python 读取和设置 PDF 文件的页面属性。文章涵盖了多种功能，包括确定 PDF 的页数、访问和修改页面属性以及处理颜色信息。为了获取页数，使用 `Document` 类和 `PageCollection` 集合，并提供代码片段演示如何检索页数，即使在未保存文档的情况下。文章解释了不同的页面属性，如 MediaBox、BleedBox、TrimBox、ArtBox 和 CropBox，并提供了访问这些属性的代码示例。此外，还介绍了如何从 PDF 中提取特定页面并将其保存为单独的文档，以及如何确定每页的颜色类型。全文示例均使用 Python 实现，展示了这些特性的实际应用。
---

Aspose.PDF for Python via .NET 让您在 Python 应用程序中读取和设置 PDF 文件页面的属性。本节展示了如何获取 PDF 文件的页数，获取 PDF 页面属性（如颜色）信息以及设置页面属性。示例使用 [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 和 [`PageCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) API，并以 Python 编写。

## 获取 PDF 文件的页数

在处理文档时，您通常想知道它们包含多少页。使用 Aspose.PDF 这只需两行代码即可实现。

获取 PDF 文件页数的方法如下：

1. 使用 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 类打开 PDF 文件。
1. 然后使用 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合的 Count 属性（来自 Document 对象），获取文档的总页数。

以下代码片段展示了如何获取 PDF 文件的页数。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count(input_file_name):
    """
    Get the total number of pages in a PDF document.
    Args:
        input_file_name (str): Path to the input PDF file.
    Returns:
        None: Prints the page count to console.
    Example:
        get_page_count("example.pdf")
        # Output: Page Count: 10
    """
    # Open document
    document = ap.Document(input_file_name)

    # Get page count
    print("Page Count:", str(len(document.pages)))
```

### 在未保存文档的情况下获取页数

有时我们即时生成 PDF 文件，在创建 PDF 文件的过程中，可能会遇到（创建目录等）需要在不将文件保存到系统或流中的情况下获取 PDF 的页数。因此，为满足此需求，Document 类引入了一个方法 [process_paragraphs()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)。请查看以下代码片段，了解在未保存文档的情况下获取页数的步骤。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_count_without_saving(input_file_name):
    """
    Get the page count of a PDF document after adding content without saving the file.

    This function opens an existing PDF document, adds a new page with 300 text fragments,
    processes the paragraphs to ensure accurate page counting, and prints the total number
    of pages in the document. The document is not saved to disk.

    Args:
        input_file_name (str): Path to the input PDF file to be processed.

    Returns:
        None: This function prints the page count but does not return a value.

    Example:
        >>> get_page_count_without_saving("sample.pdf")
        Number of pages in document = 2
    """
    # Instantiate Document instance
    document = ap.Document(input_file_name)
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

PDF 文件的每一页都有多个属性，例如宽度、高度、出血框、裁剪框和修剪框。Aspose.PDF 允许您访问这些属性。

### 理解页面属性：ArtBox、BleedBox、CropBox、MediaBox、TrimBox 和 Rect 属性之间的区别

- **Media box**：Media box 是最大的页面框。它对应于文档打印为 PostScript 或 PDF 时选择的页面尺寸（例如 A4、A5、美国信纸等）。换句话说，Media box 决定了 PDF 文档显示或打印时介质的物理尺寸。
- **Bleed box**：如果文档有出血，PDF 也会有出血框。出血是指超出页面边缘的颜色（或艺术作品）的面积。它用于确保在文档打印并裁切至尺寸（“修剪”）时，墨水能够覆盖到页面的边缘。即使页面裁剪不准确——稍微偏离修剪线——也不会在页面出现白边。
- **Trim box**：Trim box 表示文档打印并裁切后得到的最终尺寸。
- **Art box**：Art box 是围绕文档页面实际内容绘制的框。在其他应用程序导入 PDF 文档时会使用此页面框。
- **Crop box**：Crop box 是在 Adobe Acrobat 中显示 PDF 文档的“页面”尺寸。在普通视图下，仅显示 Crop box 的内容。
欲了解这些属性的详细描述，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页面边界章节。
-- **Page.Rect**：MediaBox 和 DropBox（`Page.rect`）的交集（通常可见的矩形）。请参阅 [`Rectangle`](https://reference.aspose.com/pdf/python-net/aspose.pdf/rectangle/) 类型了解矩形属性。下图演示了这些属性。

欲获取更多细节，请访问 [此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

### 访问页面属性

The [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类提供了特定 PDF 页面相关的所有属性。PDF 文件的所有页面都包含在 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象的 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中。

从中，您可以通过索引访问单个 `Page` 对象，或遍历集合获取所有页面。访问到单个页面后，就可以获取其属性。以下代码片段展示了如何获取页面属性（`Page` API）。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_properties(input_file_name):
    """
    Retrieves and displays various page properties for the first page of a PDF document.

    Args:
        input_file_name (str): Path to the PDF file to analyze.
    """
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
        "Rect": page.rect
    }

    # Print box properties
    for box_name, box in boxes.items():
        print(f"{box_name} : Height={box.height},Width={box.width},LLX={box.llx},LLY={box.lly},URX={box.urx},URY={box.ury}")

    # Print other page properties
    print(f"Page Number : {page.number}")
    print(f"Rotate : {page.rotate}")
```

## 确定页面颜色

[Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 类提供了 PDF 文档中特定页面的属性，包括页面使用的颜色类型——RGB、黑白、灰度或未定义。

PDF 文件的所有页面都包含在 [PageCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/pagecollection/) 集合中。[color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 属性指定页面上元素的颜色。要获取或确定特定 PDF 页面的颜色信息，请使用 [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) 对象的 [color_type](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) 属性。

以下代码片段展示了如何遍历 PDF 文件的各个页面以获取颜色信息。

```python

import os
import aspose.pdf as ap

# Global configuration
DATA_DIR = "your path here"

def get_page_color_type(input_file_name):
    """
    Analyzes and prints the color type information for each page in a PDF document.

    This function opens a PDF file and iterates through all pages to determine
    the color type of each page (black and white, grayscale, RGB, or undefined).
    The results are printed to the console with human-readable descriptions.

    Args:
        input_file_name (str): Path to the PDF file to analyze.

    Returns:
        None: This function prints results directly to console and doesn't return a value.

    Example:
        >>> get_page_color_type("sample.pdf")
        Page # 1 is RGB.
        Page # 2 is Gray Scale.
        Page # 3 is Black and white.

    Note:
        Requires the aspose.pdf library (imported as ap) to be installed and available.
        The PDF file must be accessible at the specified path.
    """
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
            ap.ColorType.UNDEFINED: "undefined"
        }
        color_description = color_type_map.get(page_color_type, "unknown")
        print(f"Page # {page_number} is {color_description}.")
```


