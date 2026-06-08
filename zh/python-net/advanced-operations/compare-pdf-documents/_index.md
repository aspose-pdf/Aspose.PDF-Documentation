---
title: 在 Python 中比较 PDF 文档
linktitle: 比较 PDF
type: docs
weight: 130
url: /zh/python-net/compare-pdf-documents/
description: 了解如何在 Python 中使用 Aspose.PDF for Python via .NET 通过并排和图形差异输出比较 PDF 文档。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Python 中使用可视化差异输出比较 PDF 页面和完整文档
Abstract: 本文介绍了如何在 Aspose.PDF for Python via .NET 中比较 PDF 文档。了解如何比较特定页面或整个 PDF 文件，并以并排方式输出，以及如何使用图形比较方法生成基于图像或基于 PDF 的差异报告。
---

## 比较 PDF 文档的方法

在处理 PDF 文档时，有时需要比较两个文档的内容以识别差异。Aspose.PDF for Python via .NET 库为此提供了强大的工具集。在本文中，我们将通过几个简单的代码片段来探讨如何比较 PDF 文档。

当您希望得到一个在页面之间突出显示文本和布局更改的 PDF 输出时，请使用并排比较。当您需要基于图像的差异检测以用于可视化审查工作流、回归检查或 PDF 比较报告时，请使用图形比较。

Aspose.PDF 中的比较功能允许您逐页比较两个 PDF 文档。您可以选择比较特定页面或整个文档。生成的比较文档会突出显示差异，从而更容易识别两个文件之间的更改。

以下是使用 Aspose.PDF for Python via .NET 库比较 PDF 文档的可能方法列表：

1. **比较特定页面** - 比较两个 PDF 文档的第一页。
1. **比较整个文档** - 比较两个 PDF 文档的全部内容。
1. **以图形方式比较 PDF 文档**：

- 使用 'comparer.get_difference' 方法比较 PDF - 各个图像中标记了更改。
- 使用 'comparer.compare_documents_to_pdf' 方法比较 PDF - PDF 文档中包含标记了更改的图像。

## 比较特定页面

第一个代码片段演示了如何使用 SideBySidePdfComparer 类比较两个 PDF 文档的首页。

1. 文档初始化。
1. 创建一个函数来执行比较。
1. 比较过程：

- document1.pages[1] 和 document2.pages[1]： - 这些指定了每个文档用于比较的第一页。请注意，页面索引在 Aspose.PDF 中从 1 开始。
- SideBySideComparisonOptions - 此类允许自定义比较行为。
- additional_change_marks = True - 启用额外更改标记的显示，突出显示可能存在于其他页面的差异，即使这些差异不在当前比较的页面上。
- comparison_mode = ComparisonMode.IgnoreSpaces - 将比较模式设置为忽略文本中的空格，只关注单词内部的更改。

1. 比较的结果保存为一个新的 PDF 文件，名为 ComparingSpecificPages_out.pdf，放置在指定的 data_dir 中。

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## 比较整个文档

第二段代码扩展了范围，以比较两个 PDF 文档的全部内容。

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

提供的代码演示了使用 Aspose.PDF for Python via .NET 比较两个 PDF 文档。它利用 SideBySidePdfComparer 类逐页比较，生成一个显示差异并排的新 PDF。比较通过 SideBySideComparisonOptions 配置，其中 additional_change_marks 设置为 True，以便在当前页之外的其他页也突出显示更改，并且 comparison_mode 设置为 IgnoreSpaces，以通过忽略空白变化来关注有意义的内容差异。

## 使用 GraphicalPdfComparer 进行比较

在协作处理文档时，尤其是在专业环境中，你常常会得到同一文件的多个版本。
提供的代码演示了如何使用 Aspose.PDF for Python via .NET 对两个 PDF 文档的特定页面进行可视化比较。通过使用的 `GraphicalPdfComparer` 类，它突出显示两个 PDF 的首页之间的差异，并生成相应的图像来表示这些差异。

您可以设置以下类属性：

- Resolution - 输出图像的分辨率（以 DPI 为单位），以及比较过程中生成的图像的分辨率。
- Color - 更改标记的颜色。
- 阈值 - 以百分比更改阈值。默认值为零。将阈值设置为非零可以忽略对您而言不重要的图形更改。

使用 Aspose.PDF for Python via .NET，您可以比较文档和页面，并将比较结果输出为 PDF 文档或图像文件。

这 `GraphicalPdfComparer` 类有一个方法，允许您以适合进一步处理的形式获取页面图像差异： `get_difference(document1.pages[1], document2.pages[1])`.

此方法返回一个对象的 `images_difference` type，其中包含正在比较的第一页的图像以及差异数组。

这 `images_difference` 对象允许您生成不同的图像，并通过对原始图像应用差异数组来获取第二页的对比图像。要实现此目的，请使用 `difference_to_image` 和 `get_destination_image` 方法。

### 使用 Get Difference 方法比较 PDF

提供的代码定义了一个方法 `get_difference` 比较两个 PDF 文档并生成它们之间差异的可视化表示。

此方法比较两个 PDF 文件的第一页，并生成两张 PNG 图像：

- 一张图像以红色突出显示页面之间的差异。
- 另一张图像是目标（第二）PDF页面的可视化表示。

此过程可用于直观比较文档两个版本之间的更改或差异。

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### 使用 CompareDocumentsToPdf 方法比较 PDF

提供的代码片段使用了 `compare_documents_to_pdf` 方法，用于比较两个文档并生成比较结果的PDF报告。

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

此示例演示如何使用 Aspose.PDF for Python via .NET 对两个完整的 PDF 文档进行图形比较。通过利用 `GraphicalPdfComparer` 类，它会生成一个新的 PDF 文件，直观地突出显示文档之间的差异。

- 阈值属性设置为 3.0，这意味着在比较过程中，低于此百分比的细微差异将被忽略，关注更显著的变化。
- 差异通过将 color 属性设置为 ap.Color.blue 标记为蓝色，从而实现清晰的视觉区分。
- 通过设置分辨率属性，以 300 DPI 的分辨率执行比较，确保输出详尽清晰。

这 `compare_documents_to_pdf` 方法比较两个文档的所有页面，并将结果输出到一个新的 PDF 文件 compareDocumentsToPdf_out.pdf，差异以可视方式突出显示。

## 相关主题

- [Python中的高级PDF操作](/pdf/zh/python-net/advanced-operations/)
- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中处理 PDF 页面](/pdf/zh/python-net/working-with-pages/)
- [在Python中处理PDF文本](/pdf/zh/python-net/working-with-text/)
