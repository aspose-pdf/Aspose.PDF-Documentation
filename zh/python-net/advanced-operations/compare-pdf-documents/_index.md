---
title: 比较 PDF 文档
linktitle: 比较 PDF
type: docs
weight: 130
url: /zh/python-net/compare-pdf-documents/
description: 可以使用注释标记和并排输出比较 PDF 文档的内容。
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## 比较 PDF 文档的方法

在处理 PDF 文档时，有时需要比较两个文档的内容以找出差异。Aspose.PDF for Python via .NET 库提供了一套强大的工具来实现此目的。在本文中，我们将通过几个简单的代码片段来探索如何比较 PDF 文档。

Aspose.PDF 中的比较功能允许您逐页比较两个 PDF 文档。您可以选择比较特定页面或整个文档。生成的比较文档会突出显示差异，便于识别两个文件之间的更改。

以下是使用 Aspose.PDF for Python via .NET 库比较 PDF 文档的几种可能方式：

1. **比较特定页面** - 比较两个 PDF 文档的首页。
1. **比较整个文档** - 比较两个 PDF 文档的全部内容。
1. **图形化比较 PDF 文档**：

- 使用 'comparer.get_difference' 方法比较 PDF - 标记出更改的单独图像。
- 使用 'comparer.compare_documents_to_pdf' 方法比较 PDF - 包含标记更改图像的 PDF 文档。

## 比较特定页面

第一个代码片段演示如何使用 SideBySidePdfComparer 类比较两个 PDF 文档的首页。

1. 文档初始化。
1. 创建执行比较的函数。
1. 比较过程：

- document1.pages[1] 和 document2.pages[1]：- 指定每个文档的第一页进行比较。请注意，Aspose.PDF 中的页码从 1 开始。
- SideBySideComparisonOptions - 此类允许自定义比较行为。
- additional_change_marks = True - 启用额外更改标记的显示，突出显示其他页面可能存在的差异，即使这些差异不在当前比较的页面上。
- comparison_mode = ComparisonMode.IgnoreSpaces - 将比较模式设置为忽略文本中的空格，只关注单词内部的更改。

1. 比较结果保存为名为 ComparingSpecificPages_out.pdf 的新 PDF 文件，存放在指定的 data_dir 中。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## 比较整个文档

第二个代码片段将范围扩大到比较两个 PDF 文档的全部内容。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

提供的代码演示了使用 Aspose.PDF for Python via .NET 比较两个 PDF 文档。它利用 SideBySidePdfComparer 类执行逐页比较，生成一个并排显示差异的新 PDF。比较使用 SideBySideComparisonOptions 配置，其中 additional_change_marks 设置为 True，以突出显示不仅当前页面而且其他页面的更改；comparison_mode 设置为 IgnoreSpaces，通过忽略空白变化来关注有意义的内容差异。

## 使用 GraphicalPdfComparer 进行比较

在文档协作时，尤其是专业环境中，您常常会出现同一文件的多个版本。
提供的代码演示了如何使用 Aspose.PDF for Python via .NET 视觉比较两个 PDF 文档的特定页面。通过使用 `GraphicalPdfComparer` 类，它突出显示两个 PDF 首页之间的差异，并生成相应的图像来表示这些差异。

您可以设置以下类属性：

- Resolution - 输出图像的 DPI 分辨率，以及比较期间生成的图像的分辨率。
- Color - 更改标记的颜色。
- Threshold - 以百分比表示的更改阈值。默认值为零。设置非零值可让您忽略对您而言不重要的图形更改。

使用 Aspose.PDF for Python via .NET，可以比较文档和页面，并将比较结果输出为 PDF 文档或图像文件。

`GraphicalPdfComparer` 类具有一个方法，可让您获取适合进一步处理的页面图像差异：`get_difference(document1.pages[1], document2.pages[1])`。

此方法返回 `images_difference` 类型的对象，包含正在比较的第一页的图像以及差异数组。

`images_difference` 对象允许您通过将差异数组应用于原始图像来生成不同的图像，并获取第二页的图像。为此，请使用 `difference_to_image` 和 `get_destination_image` 方法。

### 使用 Get Difference 方法比较 PDF

提供的代码定义了一个 `get_difference` 方法，用于比较两个 PDF 文档并生成它们之间差异的可视化表示。

此方法比较两个 PDF 文件的首页，并生成两张 PNG 图像：

- 一张图像用红色突出显示页面之间的差异。
- 另一张图像是目标（第二）PDF 页面的可视化表示。

此过程可用于直观比较文档两个版本之间的更改或差异。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### 使用 CompareDocumentsToPdf 方法比较 PDF

提供的代码片段使用 `compare_documents_to_pdf` 方法，该方法比较两个文档并生成比较结果的 PDF 报告。

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

本示例演示如何使用 Aspose.PDF for Python via .NET 对两个完整的 PDF 文档进行图形比较。通过利用 `GraphicalPdfComparer` 类，它生成一个新的 PDF 文件，以可视方式突出显示文档之间的差异。

- 阈值属性设置为 3.0，这意味着在比较过程中低于该百分比的细微差异将被忽略，重点关注更显著的更改。
- 通过将颜色属性设置为 ap.Color.blue，将差异标记为蓝色，以实现清晰的视觉区分。
- 将分辨率属性设置为 300 DPI，进行比较，以确保输出细致清晰。

`compare_documents_to_pdf` 方法比较两个文档的所有页面，并将结果输出到新 PDF 文件 compareDocumentsToPdf_out.pdf，差异以可视方式突出显示。

