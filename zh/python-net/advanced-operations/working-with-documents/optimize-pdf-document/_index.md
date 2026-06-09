---
title: 在 Python 中优化 PDF 文件
linktitle: 优化 PDF
type: docs
weight: 30
url: /zh/python-net/optimize-pdf/
description: 了解如何在 Python 中使用 Aspose.PDF 优化、压缩和减小 PDF 文件大小。
lastmod: "2026-06-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 压缩 PDF 页面。
Abstract: 本文提供了一份关于优化 PDF 文件以减小大小并提升在各种平台（如网页、电子邮件和存储系统）上的性能的全面指南。优化技术包括减小图像尺寸、移除未使用的资源以及解除嵌入字体。文中讨论了针对网络优化 PDF 以及整体减小文件大小的具体方法，使用 Aspose.PDF for Python 中的 `Optimize` 和 `OptimizeResources` 方法。通过 `OptimizationOptions` 可以自定义优化策略，针对性地执行压缩图像、移除未使用的对象和流、链接重复流以及解除嵌入字体等操作。其他策略还包括扁平化注释、移除表单字段以及将 PDF 文件从 RGB 转换为灰度，以进一步降低大小。文章还强调了使用 FlateDecode 压缩进行图像优化，确保在保持质量和功能的前提下有效管理 PDF 文件。
---

PDF 文档有时可能包含额外的数据。缩小 PDF 文件的大小有助于优化网络传输和存储。这在网页发布、社交网络分享、通过电子邮件发送或存档存储时尤为便利。我们可以使用多种技术来优化 PDF：

在需要减少 PDF 大小以用于网页传输、电子邮件共享、节省存储空间或打印友好输出且无需从头重新构建文档时，请使用此页面。

- 优化页面内容以便在线浏览
- 缩小或压缩所有图像
- 启用页面内容复用
- 合并重复的流
- 取消嵌入字体
- 删除未使用的对象
- 删除扁平化表单字段
- 删除或展平注释

{{% alert color="primary" %}}

 详细的优化方法说明可在“优化方法概览”页面中找到。

{{% /alert %}}

## 为网络优化 PDF 文档

优化（或称为 Web 线性化）是指将 PDF 文件处理成适合使用网页浏览器在线浏览的过程。要对文件进行 Web 显示优化：

1. 在一个中打开输入文档 [文档](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象。
1. 使用 [优化](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。
1. 使用以下方式保存已优化的文档 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。

以下代码片段展示了如何针对网页优化 PDF 文档。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## 压缩 PDF 大小

这 [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 该方法通过剔除不必要的信息来减小文档大小。默认情况下，该方法的工作方式如下：

- 未在文档页面上使用的资源会被移除
- 相等的资源被合并为一个对象
- 未使用的对象已被删除

下面的代码片段是一个示例。不过请注意，此方法不能保证文档的压缩。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## 优化策略管理

我们也可以自定义优化策略。目前， [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法使用了5种技术。这些技术可以通过 OptimizeResources() 方法与 [优化选项](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) 参数。

### 缩小或压缩所有图像

我们有两种处理图像的方法：降低图像质量和/或更改其分辨率。无论如何， [图像压缩选项](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) 应该应用。在以下示例中，我们通过将 ImageQuality 降至 50 来缩小图像。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 删除未使用的对象

PDF 文档有时会包含未被文档中任何其他对象引用的 PDF 对象。例如，当页面从文档页面树中被移除，但页面对象本身未被删除时，就可能出现这种情况。删除这些对象并不会使文档无效，而是会使文档体积变小。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 删除未使用的流

有时文档会包含未使用的资源流。这些流并不是“unused objects”，因为它们已在页面资源字典中被引用。因此，它们不会通过“remove unused objects”方法被移除。但这些流在页面内容中从未被使用。出现这种情况可能是因为图像已从页面中删除，但未从页面资源中删除。此外，当从文档中提取页面且文档页面具有“common”资源，也就是相同的 Resources 对象时，这种情况也经常出现。会分析页面内容，以确定资源流是否被使用。未使用的流会被删除。这有时会减小文档大小。使用此技术的方式类似于前一步：

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 链接重复的流

某些文档可能包含多个相同的资源流（例如图像）。这可能会在文档与自身拼接时发生。输出文档包含同一资源流的两个独立副本。我们会分析所有资源流并进行比较。如果流被重复，则将其合并，即只保留一个副本。相应地更改引用，并删除对象的副本。在某些情况下，这有助于减小文档大小。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 取消嵌入字体

如果文档使用嵌入式字体，这意味着所有字体数据都存储在文档中。好处是无论用户的机器上是否安装了该字体，文档都可以查看。但嵌入字体会使文档体积增大。取消嵌入字体的方法会移除所有嵌入的字体。于是，文档大小会减小，但如果没有安装正确的字体，文档本身可能会变得无法阅读。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

优化资源将这些方法应用于文档。如果应用了其中任何一种方法，文档大小很可能会减少。如果没有应用这些方法，文档大小将保持不变，这是显而易见的。

## 减少 PDF 文档大小的其他方法

### 删除或扁平化注释

当注释不必要时，可以将其删除。当注释是必需的但不需要进一步编辑时，可以将其展平。这两种技术都能减小文件大小。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### 删除表单字段

如果 PDF 文档包含 AcroForms，我们可以尝试通过扁平化表单字段来减小文件大小。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### 将 PDF 从 RGB 颜色空间转换为灰度

PDF 文件由 Text、Image、Attachment、Annotations、Graphs 和其他对象组成。您可能会遇到将 PDF 从 RGB 颜色空间转换为灰度的需求，以便在打印这些 PDF 文件时更快。此外，当文件转换为灰度后，文档大小也会减小，但这同样可能导致文档质量下降。此功能目前已由 Adobe Acrobat 的 Pre-Flight 功能支持，但在谈到 Office 自动化时，Aspose.PDF 是提供此类文档操作的终极解决方案。为了实现此需求，可使用以下代码片段。

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### FlateDecode 压缩

Aspose.PDF for Python via .NET 提供对 PDF 优化功能的 FlateDecode 压缩的支持。下面的代码片段展示了如何在 Optimization 中使用该选项将图像存储为 **FlateDecode** 压缩：

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## 相关文档主题

- [使用 Python 处理 PDF 文档](/pdf/zh/python-net/working-with-documents/)
- [在 Python 中合并 PDF 文件](/pdf/zh/python-net/merge-pdf-documents/)
- [在 Python 中拆分 PDF 文件](/pdf/zh/python-net/split-document/)
- [在 Python 中操作 PDF 文档](/pdf/zh/python-net/manipulate-pdf-document/)

