---
title: 在 Python 中优化、压缩或减小 PDF 大小
linktitle: 优化 PDF
type: docs
weight: 30
url: /zh/python-net/optimize-pdf/
description: 本文提供了关于优化 PDF 文件以减小其尺寸并提升在各种平台（如网页、电子邮件和存储系统）上的性能的全面指南。优化技术包括减小图像尺寸、删除未使用的资源以及取消嵌入字体。文章讨论了针对网络的 PDF 优化以及整体文件尺寸缩减的具体方法，使用 Aspose.PDF for Python 中的 `Optimize` 和 `OptimizeResources` 方法。通过 `OptimizationOptions` 可以自定义优化策略，执行如压缩图像、删除未使用的对象和流、链接重复流以及取消嵌入字体等针对性操作。额外的策略还包括扁平化注释、删除表单字段，以及将 PDF 文件从 RGB 转为灰度以进一步降低尺寸。文章还强调了使用 FlateDecode 压缩进行图像优化，确保在保持质量和功能的同时实现高效的 PDF 文件管理。
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Python 压缩 PDF 页面
Abstract: 本文提供了关于优化 PDF 文件以减小其尺寸并提升在各种平台（如网页、电子邮件和存储系统）上的性能的全面指南。优化技术包括减小图像尺寸、删除未使用的资源以及取消嵌入字体。文章讨论了针对网络的 PDF 优化以及整体文件尺寸缩减的具体方法，使用 Aspose.PDF for Python 中的 `Optimize` 和 `OptimizeResources` 方法。通过 `OptimizationOptions` 可以自定义优化策略，执行如压缩图像、删除未使用的对象和流、链接重复流以及取消嵌入字体等针对性操作。额外的策略还包括扁平化注释、删除表单字段，以及将 PDF 文件从 RGB 转为灰度以进一步降低尺寸。文章还强调了使用 FlateDecode 压缩进行图像优化，确保在保持质量和功能的同时实现高效的 PDF 文件管理。
---

PDF 文档有时会包含额外的数据。减小 PDF 文件的大小有助于优化网络传输和存储。这在网页发布、社交网络共享、电子邮件发送或存档存储时尤其便利。我们可以使用多种技术来优化 PDF：

- 为在线浏览优化页面内容
- 缩小或压缩所有图像
- 启用页面内容复用
- 合并重复的流
- 取消嵌入字体
- 删除未使用的对象
- 删除扁平化表单字段
- 删除或扁平化注释

{{% alert color="primary" %}}

有关优化方法的详细说明，请参阅优化方法概览页面。

{{% /alert %}}

## 为网页优化 PDF 文档

优化（或称网页线性化）是指使 PDF 文件适合在网页浏览器中在线浏览的过程。要将文件优化以进行网页显示：

1. 在 [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 对象中打开输入文档。
1. 使用 [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法。
1. 使用 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法保存优化后的文档。

下面的代码片段演示了如何为网页优化 PDF 文档。

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## 减小 PDF 大小

使用 [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法可以通过剔除不必要的信息来减小文档大小。默认情况下，该方法的工作方式如下：

- 删除文档页面上未使用的资源
- 将相同的资源合并为一个对象
- 删除未使用的对象

下面的代码片段是一个示例。但请注意，此方法不能保证文档一定会缩小。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## 优化策略管理

我们还可以自定义优化策略。目前，[OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) 方法使用 5 种技术。这些技术可以通过在 OptimizeResources() 方法中使用 [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) 参数来应用。

### 缩小或压缩所有图像

我们有两种处理图像的方式：降低图像质量和/或更改其分辨率。无论哪种情况，都应使用 [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/)。在下面的示例中，我们通过将 ImageQuality 降至 50 来压缩图像。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 删除未使用的对象

PDF 文档有时会包含在文档中未被其他对象引用的 PDF 对象。例如，当页面从文档页面树中被移除但页面对象本身未被删除时，就会出现这种情况。删除这些对象不会使文档无效，反而会使其体积减小。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 删除未使用的流

有时文档会包含未使用的资源流。这些流不是“未使用的对象”，因为它们在页面资源字典中被引用。因此，使用“删除未使用的对象”方法时不会被删除。但这些流在页面内容中从未被使用。这可能发生在图像已从页面中移除但未从页面资源中移除的情况。此外，当从文档中提取页面且文档页面具有“公共”资源（即相同的 Resources 对象）时，这种情况也经常出现。会分析页面内容以确定资源流是否被使用。未使用的流会被删除，这有时会减小文档大小。此技术的使用方式类似于前一步：

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 链接重复流

某些文档可能包含多个相同的资源流（例如图像）。这可能在文档与自身拼接时发生。输出文档包含两个独立的相同资源流副本。我们会分析所有资源流并进行比较。如果流是重复的，则将其合并，即只保留一份副本。引用会相应更改，对象的副本会被删除。在某些情况下，这有助于减小文档体积。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### 取消嵌入字体

如果文档使用了嵌入字体，这意味着所有字体数据都存储在文档中。这样即使用户机器上未安装该字体，文档也能正常查看。但嵌入字体会使文档体积增大。取消嵌入字体的方法会移除所有嵌入的字体，从而减小文档大小，但如果未安装正确的字体，文档可能无法正确显示。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

优化资源将这些方法应用于文档。如果应用了其中任何方法，文档大小很可能会减小。如果未应用任何方法，文档大小则不会改变，这一点不言自明。

## 额外的减小 PDF 文档大小的方法

### 删除或扁平化批注

当批注不必要时可以将其删除；当需要批注但不需要进一步编辑时，可以将其扁平化。这两种技术都能减小文件大小。

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### 删除表单字段

如果 PDF 文档包含 AcroForms，我们可以通过扁平化表单字段来尝试减小文件大小。

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### 将 PDF 从 RGB 色彩空间转换为灰度

PDF 文件包含文本、图像、附件、批注、图形等对象。您可能会遇到将 PDF 从 RGB 色彩空间转换为灰度的需求，以便在打印这些 PDF 文件时更快。同时，文件转换为灰度后，文档大小也会减小，但这同样可能导致文档质量下降。该功能目前由 Adobe Acrobat 的 Pre-Flight 功能支持，但在谈到 Office 自动化时，Aspose.PDF 是提供此类文档操作的终极解决方案。为了实现此需求，可以使用以下代码片段。

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### FlateDecode 压缩

下面的代码片段演示了如何在优化中使用该选项，以 **FlateDecode** 压缩存储图像：

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


